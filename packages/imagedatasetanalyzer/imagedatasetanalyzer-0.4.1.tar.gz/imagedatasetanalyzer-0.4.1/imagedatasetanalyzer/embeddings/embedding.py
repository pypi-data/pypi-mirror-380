import numpy as np
import torch

from imagedatasetanalyzer.datasets.imagedataset import ImageDataset

class Embedding:
    """
    Represents an embedding generator for image datasets.

    Methods:
        generate_embeddings(dataset: ImageDataset) -> dict:
            Generates embeddings for a given image dataset.

        _transform_image(batch) -> torch.Tensor:
            Transforms a batch of images into a format suitable for embedding generation.
    """
    def generate_embeddings(self, dataset: ImageDataset) -> dict:
        raise NotImplementedError("Subclasses must implement this method")

    def _transform_image(self, batch) -> torch.Tensor:
        raise NotImplementedError("Subclasses must implement this method")