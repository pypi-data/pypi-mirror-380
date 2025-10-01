
from imagedatasetanalyzer.datasets.imagedataset import ImageDataset
from imagedatasetanalyzer.embeddings.medimageinsightembedding import MedImageInsightEmbedding

img_dir = r"C:\Users\joortif\Desktop\datasets\Completos\melanoma\full\subset"

dataset = ImageDataset(img_dir)
emb_model = MedImageInsightEmbedding(batch_size=2)

embeddings_dict = emb_model.generate_embeddings(dataset)

