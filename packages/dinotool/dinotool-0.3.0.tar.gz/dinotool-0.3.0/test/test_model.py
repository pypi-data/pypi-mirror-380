import pytest
from dinotool.data import Video, VideoDataset
import torch
from torch.utils.data import DataLoader
from torchvision import transforms
from dinotool.cli import DinoToolModel
from dinotool.model import load_model, PCAModule, DinoFeatureExtractor
from dinotool.data import InputProcessor
from dinotool.utils import BatchHandler
import numpy as np

from .utils import setup_model_and_batch


def test_feature_extractor_basic():

    d = setup_model_and_batch()
    model = d["model"]
    batch = d["batch"]

    device = "cuda" if torch.cuda.is_available() else "cpu"
    extractor = DinoFeatureExtractor(model, device=device)

    out = extractor(batch["img"]).tensor
    assert out.shape == torch.Size([1, 256, 384])
    assert torch.allclose(out[0, 0, :].norm().cpu(), torch.tensor([1.0]), atol=1e-5)

    # # not flattened, normalized
    # out2 = extractor(batch["img"], flattened=False)
    # assert isinstance(out, torch.Tensor)
    # assert out2.shape == torch.Size([1, 16, 16, 384])
    # assert torch.allclose(out2[0, 0, 0, :].norm().cpu(), torch.tensor([1.0]), atol=1e-5)

    # # flattened, not normalized
    # out3 = extractor(batch["img"], flattened=True, normalized=False)
    # assert out3.shape == torch.Size([1, 256, 384])
    # assert not torch.allclose(
    #     out3[0, 0, :].norm().cpu(), torch.tensor([1.0]), atol=1e-5
    # )


@pytest.mark.parametrize("model_name,features,normalized", [
    ("vit-s", "full", True),
    ("vit-s", "full", False),
    ("vit-s", "flat", True),
    ("vit-s", "flat", False),
    ("vit-s", "frame", True),
    ("vit-s", "frame", False),
    ("dinov3-s", "full", True),
    ("dinov3-s", "full", False),
    ("dinov3-s", "flat", True),
    ("dinov3-s", "flat", False),
    ("dinov3-s", "frame", True),
    ("dinov3-s", "frame", False),
    ("radio-b", "full", True),
    ("radio-b", "full", False),
    ("radio-b", "flat", True),
    ("radio-b", "flat", False),
    ("radio-b", "frame", True),
    ("radio-b", "frame", False),
])
def test_dinotoolmodel(model_name, features, normalized):
    model = DinoToolModel(model_name=model_name)
    batch = torch.rand(1, 3, 224, 224)
    features = model(batch, features=features, normalized=normalized)
    print(features.shape)

    if features == "frame":
        assert len(features.shape) == 2
    elif features == "flat":
        assert len(features.shape) == 3
    elif features == "full":
        assert len(features.shape) == 4

    if normalized:
        if features == "frame":
            assert torch.allclose(features[0, :].norm().cpu(), torch.tensor([1.0]), atol=1e-5)
        elif features == "flat":
            assert torch.allclose(features[0, 0, :].norm().cpu(), torch.tensor([1.0]), atol=1e-5)
        elif features == "full":
            assert torch.allclose(features[0, 0, 0, :].norm().cpu(), torch.tensor([1.0]), atol=1e-5)

# def test_feature_extractor_flattened():
#     from dinotool.model import DinoFeatureExtractor

#     d = setup_model_and_batch()
#     model = d["model"]
#     batch = d["batch"]
#     # input size not set
#     extractor = DinoFeatureExtractor(model, device='cuda')
#     with pytest.raises(ValueError):
#         _ = extractor(batch["img"], flattened=False)


def test_pca_module():

    d = setup_model_and_batch()
    model = d["model"]
    batch = d["batch"]

    device = "cuda" if torch.cuda.is_available() else "cpu"
    extractor = DinoFeatureExtractor(model, device=device)
    features = extractor(batch["img"])

    pca = PCAModule(n_components=3)
    pca.fit(features.flat().tensor)
    assert pca.pca.mean_.shape == (384,)
    assert pca.pca.components_.shape == (3, 384)
    pca_features = pca.transform(features.flat().tensor)
    assert pca_features.shape == (1, 256, 3)

@pytest.mark.parametrize("n_components", [1, 3, 9])
def test_pca_module_dinotoolmodel(n_components):
    model = DinoToolModel("vit-s")
    batch = torch.rand(1, 3, 224, 224)
    features = model(batch, features="flat")
    pca_features = model.pca(features, n_components=n_components)
    assert pca_features.shape == (16,16, n_components)
    assert np.allclose(pca_features.min(), 0.0)
    assert np.allclose(pca_features.max(), 1.0)

def test_pca_module_nonflat():

    d = setup_model_and_batch()
    model = d["model"]
    batch = d["batch"]

    device = "cuda" if torch.cuda.is_available() else "cpu"
    extractor = DinoFeatureExtractor(model, device=device)
    features = extractor(batch["img"])

    pca = PCAModule(n_components=3, feature_map_size=(16, 16))
    pca.fit(features.flat().tensor)
    pca_features = pca.transform(features.flat().tensor, flattened=False)
    assert pca_features.shape == (1, 16, 16, 3)


def test_batch_handler():

    model = load_model("dinov2_vits14_reg")

    input_processor = InputProcessor(
        "dinov2_vits14_reg",
        "test/data/nasa.mp4",
        patch_size=model.patch_size,
        batch_size=1,
    )
    input_data = input_processor.process()
    batch = next(iter(input_data.data))

    device = "cuda" if torch.cuda.is_available() else "cpu"
    extractor = DinoFeatureExtractor(model, device=device)
    features = extractor(batch["img"])

    pca = PCAModule(n_components=3, feature_map_size=input_data.feature_map_size)
    pca.fit(features.flat().tensor)

    batch_handler = BatchHandler(input_data.source, extractor, pca)

    batch_frames = batch_handler(batch)
    assert batch_frames[0].img.size == (480, 270)
    assert batch_frames[0].features.shape == torch.Size([1, 19, 34, 384])
    assert batch_frames[0].pca.shape == (19, 34, 3)


def test_feature_saving():
    from dinotool.model import load_model, PCAModule, DinoFeatureExtractor
    from dinotool.data import InputProcessor, create_xarray_from_batch_frames
    from dinotool.utils import BatchHandler

    model = load_model("dinov2_vits14_reg")

    input_processor = InputProcessor(
        "dinov2_vits14_reg",
        "test/data/nasa.mp4",
        patch_size=model.patch_size,
        batch_size=2,
    )
    input_data = input_processor.process()
    batch = next(iter(input_data.data))

    device = "cuda" if torch.cuda.is_available() else "cpu"
    extractor = DinoFeatureExtractor(model, device=device)
    features = extractor(batch["img"])
    pca = PCAModule(n_components=3, feature_map_size=input_data.feature_map_size)
    pca.fit(features.flat().tensor)

    batch_handler = BatchHandler(input_data.source, extractor, pca)
    i = 0
    for batch in input_data.data:
        batch_frames = batch_handler(batch)
        f_data = create_xarray_from_batch_frames(batch_frames, identifier="frame_idx")
        i += 1
        if i == 2:
            break
    assert f_data.shape == (2, 19, 34, 384)
    assert all(f_data.frame_idx.values == [2, 3])
