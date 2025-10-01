
```bash
# Single image input just to see the features
uv run dinotool test/data/bird1.jpg -o out.jpg
# -> Outputs out.jpg

# Use DINOv3 (requires access to gated models)
uv run dinotool test/data/bird1.jpg -o out-v3.jpg -m dinov3-s

# Video input
uv run dinotool test/data/nasa.mp4 -o nasa.mp4 --batch-size 4
# -> Outputs nasa.mp4

# "I want see how RADIO local features look like"
uv run dinotool test/data/nasa.mp4 -o nasa-radio.mp4 --batch-size 4 --model-name radio-b
# -> Outputs nasa-siglip2.mp4
# CLIP/SigLIP inputs are resized based on the preprocessing pipeline of the model.

# "I want to use a specific OpenCLIP/timm model for extracting global features for video frames
uv run dinotool test/data/nasa.mp4 -o clip.mp4 --batch-size 4 --save-features 'frame' --model-name hf-hub:timm/vit_base_patch16_clip_224.openai

# "I want the local features of this image in a easily readable parquet format"
uv run dinotool test/data/bird1.jpg -o bird_features --save-features 'flat' --no-vis
# -> Produces bird_features.parquet

# I have a lot of images that are different sizes, and I want their local features in a format that preserves the locality
# I also want to save the PCA outputs for visual inspection
uv run dinotool test/data/imagefolder -o my_imagefolder --save-features 'full'
# -> Produces folder 'my_imagefolder', which contains visualizations and NetCDF files containing the local features

# I want also to get global feature vectors with SigLIP2 - no need for visualization
uv run dinotool test/data/imagefolder -o siglip2feats --save-features 'frame' --model-name siglip2
# -> Produces a file siglip2feats.parquet, with index determining the filename

# I have a folder of images but they can be all resized to the same size for faster batch processing. Use the DINOv3 remote sensing model (gated)
uv run dinotool test/data/drone_images -o drone --save-features 'full' --input-size 512 512 --batch-size 4 --no-vis -m dinov3-l-sat
# -> Produces drone.zarr with full local features with structure
# with --save features 'flat' this would produce a partitioned parquet directory

# I want also to get global feature vectors with SigLIP2 - no need for visualization
uv run dinotool test/data/imagefolder -o siglip2feats --save-features 'frame' --model-name siglip2
```