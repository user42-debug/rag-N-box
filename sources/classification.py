import clip
import torch
from PIL import Image

class Classifier:
    def __init__(self, prompts):

        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model, self.preprocess = clip.load("ViT-B/32", device=self.device)

        tokens = clip.tokenize(prompts).to(self.device)

        self.text_embeddings = self.model.encode_text(tokens)
        self.text_embeddings /= self.text_embeddings.norm(dim=-1, keepdim=True)


    def predict(self, picture):
        img = picture.img
        img = self.preprocess(img).unsqueeze(0).to(self.device)

        with torch.no_grad():
            image_features = self.model.encode_image(img)
            image_features = image_features / image_features.norm(dim=-1, keepdim=True)

            similarity = image_features @ self.text_embeddings.T
            pred = similarity.argmax(dim=-1).item()

        return pred == 0
