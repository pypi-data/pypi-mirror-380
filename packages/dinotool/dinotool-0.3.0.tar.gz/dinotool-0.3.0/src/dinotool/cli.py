"""
DINOtool CLI: Extract and visualize DINO features from images and videos.
"""

import argparse
import os
import shutil
import subprocess
import uuid
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Literal, Optional, Tuple, Union

import numpy as np
import pandas as pd
import torch
import xarray as xr
from tqdm import tqdm

import dinotool
from dinotool import data
from dinotool.model import (
    DinoFeatureExtractor,
    DinoV3FeatureExtractor,
    OpenCLIPFeatureExtractor,
    RADIOFeatureExtractor,
    PCAModule,
    load_model,
)
from dinotool.utils import BatchHandler, frame_visualizer


# Configuration
MODEL_SHORTCUTS = {
    "vit-s": "dinov2_vits14_reg",
    "vit-b": "dinov2_vitb14_reg",
    "vit-l": "dinov2_vitl14_reg",
    "vit-g": "dinov2_vitg14_reg",

    "dinov2-s": "dinov2_vits14_reg",
    "dinov2-b": "dinov2_vitb14_reg",
    "dinov2-l": "dinov2_vitl14_reg",
    "dinov2-g": "dinov2_vitg14_reg",

    "siglip1": "hf-hub:timm/ViT-B-16-SigLIP-i18n-256",

    "siglip2": "hf-hub:timm/ViT-B-16-SigLIP2-512",
    "siglip2-so400m-384": "hf-hub:timm/ViT-SO400M-16-SigLIP2-384",
    "siglip2-so400m-512": "hf-hub:timm/ViT-SO400M-16-SigLIP2-512",
    "siglip2-b16-256": "hf-hub:timm/ViT-B-16-SigLIP2-256",
    "siglip2-b16-512": "hf-hub:timm/ViT-B-16-SigLIP2-512",
    "siglip2-b32-256": "hf-hub:timm/ViT-B-32-SigLIP2-256",

    "clip": "hf-hub:timm/vit_base_patch16_clip_224.openai",

    "dinov3-s": "facebook/dinov3-vits16-pretrain-lvd1689m",
    "dinov3-splus": "facebook/dinov3-vits16plus-pretrain-lvd1689m",
    "dinov3-b": "facebook/dinov3-vitb16-pretrain-lvd1689m",
    "dinov3-l": "facebook/dinov3-vitl16-pretrain-lvd1689m",
    "dinov3-hplus": "facebook/dinov3-vith16plus-pretrain-lvd1689m",
    "dinov3-7b": "facebook/dinov3-vit7b16-pretrain-lvd1689m",
    "dinov3-l-sat": "facebook/dinov3-vitl16-pretrain-sat493m",
    "dinov3-7b-sat": "facebook/dinov3-vit7b16-pretrain-sat493m",

    "radio-b": "NVlabs/RADIO/c-radio_v3-b",
    "radio-l": "NVlabs/RADIO/c-radio_v3-l",
    "radio-h": "NVlabs/RADIO/c-radio_v3-h",
    "radio-g": "NVlabs/RADIO/c-radio_v3-g",

}

class PrintModelsAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        print("Available model shortcuts:")
        for shortcut, model in MODEL_SHORTCUTS.items():
            print(f"  {shortcut} \t->\t{model}")
        print("\nMost timm models from Huggingface Hub should work with the prefix 'hf-hub:timm/<model>'",
              "\nMore information:",
              "\n - DINOv2: https://github.com/facebookresearch/dinov2",
              "\n - DINOv3: https://github.com/facebookresearch/dinov3",
              "\n - RADIO: https://github.com/NVlabs/RADIO")
        parser.exit()

VALID_IMAGE_EXTENSIONS = (".jpg", ".png")
VALID_VIDEO_EXTENSIONS = (".mp4", ".avi")
VALID_OUTPUT_EXTENSIONS = VALID_IMAGE_EXTENSIONS + VALID_VIDEO_EXTENSIONS


@dataclass
class DinotoolConfig:
    """Configuration for DINOtool processing."""

    input: str
    output: str
    model_name: str = "dinov2_vits14_reg"
    input_size: Optional[Tuple[int, int]] = None
    batch_size: int = 1
    only_pca: bool = False
    save_features: Optional[str] = None
    no_vis: bool = False


class ArgumentValidator:
    """Validates command-line arguments."""

    @staticmethod
    def validate_input_path(input_path: str) -> None:
        """Validate that input path exists."""
        if not os.path.exists(input_path):
            raise argparse.ArgumentTypeError(
                f"Input path '{input_path}' does not exist."
            )

    @staticmethod
    def validate_output_path(output_path: str, force: bool) -> None:
        """Validate output path doesn't exist unless force is used."""
        if os.path.exists(output_path) and not force:
            raise argparse.ArgumentTypeError(
                f"Output path '{output_path}' already exists. Use --force to overwrite."
            )

    @staticmethod
    def validate_feature_files(output_path: str, save_features: str) -> None:
        """Validate feature output files."""
        if save_features == "full":
            nc_file = f"{output_path}.nc"
            zarr_dir = f"{output_path}.zarr"

            if os.path.exists(nc_file):
                print(
                    f"Warning: Output file '{nc_file}' already exists and will be overwritten."
                )

            if os.path.exists(zarr_dir):
                raise argparse.ArgumentTypeError(
                    f"Output directory '{zarr_dir}' already exists. Please remove it first."
                )

    @staticmethod
    def validate_output_extension(
        input_type: str, output_path: str, no_vis: bool
    ) -> None:
        """Validate output file extension."""
        if (
            not no_vis
            and not output_path.endswith(VALID_OUTPUT_EXTENSIONS)
            and input_type != "image_directory"
        ):
            raise argparse.ArgumentTypeError(
                f"Output file must have a valid extension {VALID_OUTPUT_EXTENSIONS}. "
                "Use --no-vis to skip visualization."
            )

    @staticmethod
    def validate_vis_and_features(no_vis: bool, save_features: Optional[str]) -> None:
        """Validate that either visualization or feature saving is enabled."""
        if no_vis and not save_features:
            raise argparse.ArgumentTypeError(
                "If --no-vis is set, you must also set --save-features to save features."
            )

    @staticmethod
    def validate_input_type_and_vis_and_batch(
        input_type: str, input_size, no_vis: bool, input_path: str, batch_size: int
    ) -> None:
        if input_type == "image_directory" and batch_size > 1:
            if not no_vis:
                raise argparse.ArgumentTypeError(
                    "Visualization of image directories with batch size > 1 is not supported. "
                    "Set --no-vis or set --batch-size to 1."
                )
            if input_size is None:
                raise argparse.ArgumentTypeError(
                    "Batch size > 1 is not (currently) supported for image directories. "
                    "with varying input sizes. "
                    "Do not set --batch-size or set it to 1, or set --input-size to a fixed size."
                )


class ArgumentParser:
    """Handles command-line argument parsing."""

    def __init__(self):
        self.parser = self._create_parser()

    def _create_parser(self) -> argparse.ArgumentParser:
        """Create the argument parser."""
        parser = argparse.ArgumentParser(
            description="🦕 DINOtool: Extract and visualize ViT features from images and videos."
        )

        # Required arguments
        parser.add_argument(
            "input", type=str, help="Path to an image, video file, or folder of images."
        )
        parser.add_argument(
            "--output",
            "-o",
            type=str,
            required=True,
            help="Path to output file or directory where features and visualizations will be saved.",
        )

        # Model arguments
        parser.add_argument(
            "--model-name",
            "-m",
            type=str,
            default="dinov2_vits14_reg",
            help="Model to use (default: dinov2_vits14_reg). OpenCLIP/timm models can be used with 'hf-hub:timm/<model_name>' format.",
        )
        parser.add_argument(
            "--input-size",
            type=int,
            nargs=2,
            default=None,
            help="Resizes input to this size before passing it to the model. Mandatory for image directories with batch size > 1. ",
        )

        # Processing arguments
        parser.add_argument(
            "--batch-size",
            "-b",
            type=int,
            default=1,
            help="Batch size for processing (default: 1).",
        )

        # Feature arguments
        parser.add_argument(
            "--only-pca",
            action="store_true",
            help="Only visualize PCA features (default: False).",
        )
        parser.add_argument(
            "--save-features",
            "-s",
            type=str,
            default=None,
            choices=["full", "flat", "frame"],
            help="Save features to file (netCDF for images, zarr for videos)."
            " 'full' saves local features with spatial information, 'flat' saves local flattened features, 'frame' saves global frame-level features.",
        )

        # Output arguments
        parser.add_argument(
            "--no-vis",
            action="store_true",
            help="Do not visualize features, only save them (default: False).",
        )
        parser.add_argument(
            "--force",
            "-f",
            action="store_true",
            help="Force overwrite output file if it exists (default: False).",
        )
        parser.add_argument(
            "--models",
            action=PrintModelsAction,
            nargs=0,
            help="List available model shortcuts and exit.",
        )

        # Version
        parser.add_argument(
            "--version",
            action="version",
            version=dinotool.__version__,
            help="Show the version of DINOtool.",
        )

        return parser

    def parse(self) -> DinotoolConfig:
        """Parse arguments and return configuration."""
        args = self.parser.parse_args()

        # Validate arguments
        try:
            _, input_type = data.InputProcessor.find_source(args.input)
            print(f"Input type: {input_type}")
            ArgumentValidator.validate_input_path(args.input)
            ArgumentValidator.validate_output_path(args.output, args.force)
            ArgumentValidator.validate_output_extension(
                input_type, args.output, args.no_vis
            )
            ArgumentValidator.validate_vis_and_features(args.no_vis, args.save_features)
            ArgumentValidator.validate_input_type_and_vis_and_batch(
                input_type, args.input_size, args.no_vis, args.input, args.batch_size
            )

            if args.save_features:
                ArgumentValidator.validate_feature_files(
                    args.output, args.save_features
                )

        except argparse.ArgumentTypeError as e:
            self.parser.error(str(e))

        # Handle model shortcuts
        model_name = args.model_name
        if model_name in MODEL_SHORTCUTS:
            print(
                f"Using model shortcut: {model_name} -> {MODEL_SHORTCUTS[model_name]}"
            )
            model_name = MODEL_SHORTCUTS[model_name]

        return DinotoolConfig(
            input=args.input,
            output=args.output,
            model_name=model_name,
            input_size=tuple(args.input_size) if args.input_size else None,
            batch_size=args.batch_size,
            only_pca=args.only_pca,
            save_features=args.save_features,
            no_vis=args.no_vis,
        )


class FeatureSaver:
    """Handles saving features in different formats."""

    @staticmethod
    def save_batch_features(
        batch_frames: List[data.FrameData], method: Literal["full", "flat"], output: str
    ) -> None:
        """Save features from a batch of frames to a file."""
        if batch_frames[0].filename is not None:
            identifier = "filename"
        else:
            identifier = "frame_idx"

        if method == "full":
            f_data = data.create_xarray_from_batch_frames(
                batch_frames, identifier=identifier
            )
            f_data.to_netcdf(f"{output}.nc")
        elif method == "flat":
            f_data = data.create_dataframe_from_batch_frames(
                batch_frames, identifier=identifier
            )
            f_data.to_parquet(f"{output}.parquet")

    @staticmethod
    def combine_frame_features(
        method: Literal["full", "flat"], tmpdir: str, feature_out_name: str
    ) -> None:
        """Combine features from temporary files into a single output."""
        if method == "full":
            FeatureSaver._combine_netcdf_files(tmpdir, feature_out_name)
        elif method == "flat":
            FeatureSaver._combine_parquet_files(tmpdir, feature_out_name)

        print(f"Saved features to {feature_out_name}")

    @staticmethod
    def _combine_netcdf_files(tmpdir: str, output_name: str) -> None:
        """Combine netCDF files into a zarr directory."""
        nc_files = sorted(Path(tmpdir).glob("*.nc"))

        def load_dataset(path):
            with xr.open_dataset(path) as ds:
                ds.load()
                return ds

        if "filename" in xr.open_dataset(nc_files[0]).dims:
            identifier = "filename"
        else:
            identifier = "frame_idx"

        xr_data = xr.concat([load_dataset(path) for path in nc_files], dim=identifier)
        xr_data.to_zarr(output_name)

    @staticmethod
    def _combine_parquet_files(tmpdir: str, output_name: str) -> None:
        """Combine parquet files into a partitioned directory."""
        Path(output_name).mkdir(parents=True, exist_ok=True)
        parquet_files = sorted(Path(tmpdir).glob("*.parquet"))

        for idx, file in enumerate(parquet_files):
            file.rename(Path(output_name) / f"part.{idx}.parquet")


class FrameLevelProcessor:
    """Handles frame-level feature extraction."""

    def __init__(self, extractor: DinoFeatureExtractor):
        self.extractor = extractor

    def process(self, input_data: data.InputData, output_path_base: str) -> None:
        """
        Handle frame-level/global feature extraction and saving for various input types.
        output_path_base will be used to construct the final output file(s).
        """
        input_type = input_data.input_type
        data = input_data.data

        if input_type == "single_image":
            tensor = data
            global_features = self.extractor(tensor, return_clstoken=True).cpu().numpy()
            np.savetxt(f"{output_path_base}.txt", global_features, delimiter=",")
            print(f"Saved frame features to {output_path_base}.txt")

        elif input_type in ["video_file", "video_dir"]:
            print(
                "Extracting frame-level features from video. This does not produce a video output."
            )
            tmpdir = Path(f"temp_dinotool_frames-{uuid.uuid4()}")
            tmpdir.mkdir()

            try:
                self._extract_frame_features_from_iterable(data, tmpdir)
                FeatureSaver._combine_parquet_files(
                    tmpdir, f"{output_path_base}.parquet"
                )
            finally:
                self._cleanup_temp_dir(tmpdir)
            print(f"Saved frame features to {output_path_base}.parquet")

        elif input_type == "image_directory":
            print(
                "Extracting frame-level features from image directory for single parquet output."
            )

            all_features_dfs = []
            progbar = tqdm(total=len(input_data.source))
            for batch in data:
                filename = batch["filename"]

                global_features = (
                    self.extractor(batch["img"], return_clstoken=True).cpu().numpy()
                )

                columns = [f"feature_{i}" for i in range(global_features.shape[1])]
                # Create DataFrame for current image's features, using filename_stem as index
                df = pd.DataFrame(global_features, index=[filename], columns=columns)

                df.index.set_names(["filename"], inplace=True)
                all_features_dfs.append(df)

                progbar.set_description(f"Processed {filename}")
                progbar.update(len(batch["img"]))
            progbar.close()

            # Concatenate all DataFrames and save to a single parquet file
            if all_features_dfs:
                combined_df = pd.concat(all_features_dfs, axis=0)

                final_output_path = Path(output_path_base).with_suffix(".parquet")
                combined_df.to_parquet(final_output_path)
                print(f"Saved combined frame features to {final_output_path}")
            else:
                print(
                    "No images found or processed in the directory to save frame features."
                )
        else:
            raise ValueError(
                f"Unsupported input type for frame-level features: {input_type}"
            )

    def _extract_frame_features_from_iterable(
        self, data_iterable: object, tmpdir: Path
    ) -> None:
        """Extract features from an iterable (e.g., video loader) into temporary files."""
        progbar = tqdm(total=len(data_iterable))

        try:
            for idx, batch in enumerate(data_iterable):
                global_features = (
                    self.extractor(batch["img"], return_clstoken=True).cpu().numpy()
                )
                frame_idx = batch["frame_idx"].cpu().numpy()

                columns = [f"feature_{i}" for i in range(global_features.shape[1])]
                df = pd.DataFrame(global_features, index=frame_idx, columns=columns)
                df.to_parquet(tmpdir / f"{idx:05d}.parquet")

                progbar.update(1)
        except KeyboardInterrupt:
            print("Keyboard interrupt detected. Cleaning up...")
            progbar.close()
            raise

    @staticmethod
    def _cleanup_temp_dir(tmpdir: Path) -> None:
        """Clean up temporary directory."""
        shutil.rmtree(tmpdir, ignore_errors=True)


class ExtractorFactory:
    """Factory for creating feature extractors."""

    @staticmethod
    def create_extractor(
        model_name: str,
        model: torch.nn.Module,
        device: str = "cuda",
    ) -> DinoFeatureExtractor:
        """Create appropriate feature extractor based on model name."""
        if model_name.startswith("hf-hub:timm"):
            return OpenCLIPFeatureExtractor(model, device=device)
        
        elif model_name.startswith("facebook/dinov3"):
            return DinoV3FeatureExtractor(model, device=device)
        elif model_name.startswith("NVlabs/RADIO/"):
            return RADIOFeatureExtractor(model, device=device)
        else:
            return DinoFeatureExtractor(model, device=device)


def create_video_from_frames(
    tmpdir: str, output_path: str, framerate: float = 30
) -> None:
    """Create video from frame images using ffmpeg."""
    output_path = Path(output_path)
    if not output_path.parent.exists():
        output_path.parent.mkdir(parents=True, exist_ok=True)
    try:
        subprocess.run(
            [
                "ffmpeg",
                "-y",
                "-framerate",
                str(framerate),
                "-i",
                f"{tmpdir}/%05d.jpg",
                "-c:v",
                "libx264",
                "-pix_fmt",
                "yuv420p",
                str(output_path),
            ],
            check=True,
        )

        print(f"Saved visualization to {output_path}")
    except FileNotFoundError:
        raise FileNotFoundError(
            "ffmpeg is not installed. Please install ffmpeg to create video outputs."
        )
    except subprocess.CalledProcessError as e:
        raise RuntimeError(
            f"Failed to create video from frames: {e}. "
        )
    except Exception as e:
        raise RuntimeError(
            f"An unexpected error occurred while creating video: {e}"
        ) from e
    


class DinotoolProcessor:
    """Main processor for DINOtool operations."""

    def __init__(self, config: DinotoolConfig):
        self.config = config
        self.device = "cuda" if torch.cuda.is_available() else "cpu"

    def run(self) -> None:
        """Run the main processing pipeline."""
        # Load model and setup
        model: torch.nn.Module = load_model(self.config.model_name)
        print(f"Using model: {self.config.model_name}")
        print(f"Model patch size: {model.patch_size}")
        print(f"Using device: {self.device}")

        # Setup input pipeline
        input_processor = data.InputProcessor(
            model_name=self.config.model_name,
            input_path=self.config.input,
            patch_size=model.patch_size,
            batch_size=self.config.batch_size,
            resize_size=self.config.input_size,
        )
        input_data: data.InputData = input_processor.process()

        # Create extractor
        extractor = ExtractorFactory.create_extractor(
            model_name=self.config.model_name,
            model=model,
            device=self.device,
        )

        # Handle frame-level features
        if self.config.save_features == "frame":
            processor = FrameLevelProcessor(extractor)
            output_path = Path(self.config.output).with_suffix("")
            processor.process(input_data, str(output_path))
            return

        if input_data.input_type in ["video_dir", "video_file"]:
            self._process_video(input_data, extractor)
        elif input_data.input_type == "single_image":
            self._process_image(input_data, extractor)
        elif (
            input_data.input_type == "image_directory"
            and self.config.input_size is not None
        ):
            # process image directory with specified input size
            self._process_video(input_data, extractor)
        elif input_data.input_type == "image_directory":
            self._process_image_directory(input_data, extractor)
        else:
            raise ValueError(f"Unsupported input type: {input_data.input_type}")

    def _process_image(
        self, input_data: data.InputData, extractor: DinoFeatureExtractor
    ) -> None:
        """Process a single image."""
        batch = {"img": input_data.data}
        features = extractor(batch["img"])

        Path(self.config.output).parent.mkdir(parents=True, exist_ok=True)

        # Setup PCA
        if not self.config.no_vis:
            pca = PCAModule(
                n_components=3, feature_map_size=input_data.feature_map_size
            )
            pca.fit(features.flat().tensor)
            pca_array = pca.transform(features.flat().tensor, flattened=False)[0]
        else:
            pca_array = None

        # Create frame data
        frame = data.FrameData(
            img=input_data.source,
            features=features,
            pca=pca_array,  # PCA features if visualization is enabled
            frame_idx=0,
        )

        # Save visualization
        if not self.config.no_vis:
            out_img = frame_visualizer(
                frame, output_size=input_data.input_size, only_pca=self.config.only_pca
            )
            out_img.save(self.config.output)
            print(f"Saved visualization to {self.config.output}")

        # Save features
        if self.config.save_features:
            output_stem = Path(self.config.output).with_suffix("")
            FeatureSaver.save_batch_features(
                [frame], method=self.config.save_features, output=str(output_stem)
            )

            extension = ".nc" if self.config.save_features == "full" else ".parquet"
            print(f"Saved features to {output_stem}{extension}")

    def _process_video(
        self, input_data: data.InputData, extractor: DinoFeatureExtractor
    ) -> None:
        """Process a video."""
        # Setup PCA
        if not self.config.no_vis:
            first_batch = next(iter(input_data.data))
            pca = PCAModule(
                n_components=3, feature_map_size=input_data.feature_map_size
            )
            first_features = extractor(first_batch["img"])
            pca.fit(first_features.flat().tensor)
        else:
            pca = None

        # Setup output paths
        feature_out_name = None
        if self.config.save_features:
            extension = ".zarr" if self.config.save_features == "full" else ".parquet"
            feature_out_name = Path(self.config.output).with_suffix(extension)

        # Process video
        progbar = tqdm(total=len(input_data.source))
        batch_handler = BatchHandler(
            input_data.source, extractor, pca, progress_bar=progbar
        )
        tmpdir = f"temp_dinotool_frames-{uuid.uuid4()}"
        os.mkdir(tmpdir)

        try:
            self._process_video_batches(
                input_data, batch_handler, tmpdir, feature_out_name
            )

            # Create output video
            if not self.config.no_vis:
                try:
                    framerate = input_data.source.framerate
                except (ValueError, AttributeError):
                    framerate = 30

                create_video_from_frames(tmpdir, self.config.output, framerate)

            # Combine features
            if self.config.save_features:
                FeatureSaver.combine_frame_features(
                    method=self.config.save_features,
                    tmpdir=tmpdir,
                    feature_out_name=str(feature_out_name),
                )

        finally:
            # Cleanup
            shutil.rmtree(tmpdir, ignore_errors=True)

    def _process_video_batches(
        self,
        input_data: data.InputData,
        batch_handler: BatchHandler,
        tmpdir: str,
        feature_out_name: Optional[Path],
    ) -> None:
        """Process video batches."""
        try:
            idx = 0
            for batch in input_data.data:
                batch_frames = batch_handler(batch)

                # Save visualization frames
                if not self.config.no_vis:
                    for frame in batch_frames:
                        out_img = frame_visualizer(
                            frame,
                            output_size=input_data.input_size,
                            only_pca=self.config.only_pca,
                        )
                        out_img.save(f"{tmpdir}/{frame.frame_idx:05d}.jpg")

                # Save features
                if self.config.save_features:
                    output_path = f"{tmpdir}/{idx:05d}"
                    FeatureSaver.save_batch_features(
                        batch_frames,
                        method=self.config.save_features,
                        output=output_path,
                    )
                idx += 1

        except KeyboardInterrupt:
            print("Keyboard interrupt detected. Cleaning up...")
            raise

    def _process_image_directory(
        self, input_data: data.InputData, extractor: DinoFeatureExtractor
    ) -> None:
        """Process a directory of images. Supports only batch size of 1."""
        out_dir = Path(self.config.output)
        out_dir.mkdir(parents=True, exist_ok=True)

        progbar = tqdm(total=len(input_data.source))
        for batch in input_data.data:
            filename = batch["filename"][0]
            filename_stem = Path(filename).stem

            # Adapt extractor input size dynamically for each image in the directory
            feature_map_size = tuple(x.item() for x in batch["feature_map_size"])
            input_size = extractor.patch_size * np.array(feature_map_size)
            progbar.set_description(f"Processing {filename}. Input size: {input_size}")

            features = extractor(batch["img"])
            if not self.config.no_vis:
                pca = PCAModule(n_components=3, feature_map_size=feature_map_size)
                pca.fit(features.flat().tensor, verbose=False)
                pca_array = pca.transform(features.flat().tensor, flattened=False)[0]
            else:
                pca = None
                pca_array = None

            frame = data.FrameData(
                img=input_data.source.get_by_name(filename),
                features=features.full()[0],
                frame_idx=0,
                pca=pca_array,  # PCA features if visualization is enabled
            )

            # Save visualization
            if not self.config.no_vis:
                out_img = frame_visualizer(
                    frame, output_size=input_size, only_pca=self.config.only_pca
                )
                out_img_path = os.path.join(self.config.output, f"{filename_stem}.jpg")
                out_img.save(out_img_path)

            # Save features
            if self.config.save_features:
                output_stem = Path(self.config.output).with_suffix("")
                out_path = os.path.join(str(output_stem), f"{filename_stem}")
                FeatureSaver.save_batch_features(
                    [frame], method=self.config.save_features, output=out_path
                )

                extension = ".nc" if self.config.save_features == "full" else ".parquet"
                print(f"Saved features to {out_path}{extension}")
            progbar.update(1)



# public API classes
class DinoToolModel:
    """A high-level interface for feature extraction and visualization with DINOtool
    
    Args:
        model_name (str): Model name or shortcut to use. Default is "dinov2_vits14_reg".
        device (str, optional): Device to use ("cuda" or "cpu"). Defaults to None, which selects "cuda" if available.
        verbose (bool): Whether to print model and device information. Default is True.
    Attributes:
        model_name (str): The full model name being used.
        device (str): The device being used.
        model (torch.nn.Module): The loaded model.
        extractor (DinoFeatureExtractor): The feature extractor.
        transform_factory (data.TransformFactory): Factory for input transformations.
    Methods:
        __call__(input, features="full", normalized=True): Extract features from input tensor.
        get_transform(input_size): Get the appropriate input transformation for a given size.
        pca(features, n_components=3): Apply PCA to local features and return the transformed array.    
    Example:
    """
    def __init__(self, model_name: str = "dinov2_vits14_reg", device: Optional[str] = None, verbose: bool = True):
        """Initialize DinoToolModel with specified model and device.
        
        Args:
            model_name (str): Model name or shortcut to use. Default is "dinov2_vits14_reg".
            device (str, optional): Device to use ("cuda" or "cpu"). Defaults to None, which selects "cuda" if available.
            verbose (bool): Whether to print model and device information. Default is True.
        """
        if model_name in MODEL_SHORTCUTS:
            self.model_name_shortcut = model_name
            if verbose:
                print(
                    f"Using model shortcut: {model_name} -> {MODEL_SHORTCUTS[model_name]}"
                )
            model_name = MODEL_SHORTCUTS[model_name]
        else:
            self.model_name_shortcut = None
        self.model_name = model_name

        if device is None:
            self.device = "cuda" if torch.cuda.is_available() else "cpu"
        else:
            self.device = device

        self.model = load_model(self.model_name).to(self.device)

        if verbose:
            print(f"Using model: {self.model_name} on device: {self.device}")
        
        self.extractor = ExtractorFactory.create_extractor(
            model_name=self.model_name,
            model=self.model,
            device=self.device,
        )

        self.transform_factory = data.TransformFactory(model_name=self.model_name, patch_size=self.model.patch_size)
    
    def __repr__(self) -> str:
        return f"DinoToolModel(model_name='{self.model_name}', device='{self.device}')"
    
    def __call__(self, input: torch.Tensor, features: Literal["full", "flat", "frame"] = "full", normalized: bool = True) -> data.LocalFeatures:
        """Extract features from input tensor.
        Args:
            input (torch.Tensor): Input tensor of shape (B, C, H, W).
            features (str): Type of features to extract ("full", "flat", or "frame
). Default is "full".
            normalized (bool): Whether to return normalized features. Default is True.
        Returns:
            data.LocalFeatures: Extracted features.
        Example:
            >>> from dinotool import DinoToolModel
            >>> from PIL import Image
            >>> model = DinoToolModel("dinov2_vits14_reg")
            >>> transform = model.get_transform((224, 224))
            >>> img = transform(Image.open("path/to/image.jpg")).unsqueeze(0)
            >>> features = model(img, features="full")
        """
        if features == "frame":
            return self.extractor(input, return_clstoken=True, normalized=normalized)
        if features == "flat":
            flattened = True
        else:
            flattened = False
        return self.extractor(input, flattened=flattened, normalized=normalized)
    
    def get_transform(self, input_size: Tuple[int, int]) -> torch.nn.Module:
        """Get the appropriate input transformation for a given size.
        Args:
            input_size (Tuple[int, int]): Desired input size (W, H).
        Returns:
            torch.nn.Module: Transformation module.
        Example:
            >>> from dinotool import DinoToolModel
            >>> from PIL import Image
            >>> model = DinoToolModel("dinov2_vits14_reg")
            >>> transform = model.get_transform((224, 224))
        """
        return self.transform_factory.get_transform(input_size)
    
    def pca(self, features: data.LocalFeatures, n_components: int = 3) -> np.ndarray:
        """Apply PCA to local features and return the transformed array.
        Args:
            features (dinotool.data.LocalFeatures): Local features to apply PCA on.
            n_components (int): Number of PCA components to retain. Default is 3.
        Returns:
            np.ndarray: PCA transformed features.
        Example:
            >>> from dinotool import DinoToolModel
            >>> from PIL import Image
            >>> model = DinoToolModel("dinov2_vits14_reg")
            >>> transform = model.get_transform((224, 224))
            >>> img = transform(Image.open("path/to/image.jpg")).unsqueeze(0)
            >>> features = model(img)
            >>> pca_features = model.pca(features, n_components=3)
        """
        pca = PCAModule(n_components=n_components,
                        feature_map_size=(features.w, features.h))
        pca.fit(features.flat().tensor, verbose=False)
        pca_array = pca.transform(features.flat().tensor, flattened=False)
        if pca_array.shape[0] == 1:
            pca_array = pca_array[0]
        return pca_array
    
    @classmethod
    def available_models(cls) -> Dict[str, str]:
        """Get available model shortcuts.
        Returns:
            Dict[str, str]: Dictionary of model shortcuts and their full names.
        Example:
            >>> from dinotool import DinoToolModel
            >>> model = DinoToolModel()
            >>> print(model.available_models)
        """
        return MODEL_SHORTCUTS

def main() -> None:
    """Main entry point."""
    try:
        parser = ArgumentParser()
        config = parser.parse()
        processor = DinotoolProcessor(config)
        processor.run()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
    except Exception as e:
        print(f"Error: {e}")
        raise


def cli() -> None:
    """CLI entry point."""
    main()


if __name__ == "__main__":
    main()
