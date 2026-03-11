import clip
import torch
from PIL import Image

device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

text_embeddings = torch.load("data/classes.pt")

def is_ragondin(path):
    img = Image.open(path)
    img = preprocess(img).unsqueeze(0).to(device)

    with torch.no_grad():
        image_features = model.encode_image(img)
        image_features = image_features / image_features.norm(dim=-1, keepdim=True)

        similarity = image_features @ text_embeddings.T
        pred = similarity.argmax(dim=-1).item()

    return pred == 0

print(is_ragondin("data/chat_ex.jpg"))