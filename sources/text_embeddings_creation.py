import clip
import torch
from PIL import Image


class Prompts:
    def __init__(self, prompts, model, device):
        tokens = clip.tokenize(prompts).to(device)

        text_features = model.encode_text(tokens)
        text_features /= text_features.norm(dim=-1, keepdim=True)

