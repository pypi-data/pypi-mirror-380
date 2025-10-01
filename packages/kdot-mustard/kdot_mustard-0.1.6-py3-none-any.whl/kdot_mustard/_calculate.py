import numpy as np
from numpy import asarray
from PIL import Image
from tqdm import trange

def _get_frames(src_img: Image.Image, target_img: Image.Image, frames: int = 100) -> list:
    src_np = asarray(src_img)
    target_np = asarray(target_img)
    delta = (target_np - src_np) / (frames - 1)
    res = [src_img,]
    for i in trange(1, frames, desc="Processing frames", leave=True):
        res.append(Image.fromarray((src_np + delta * i).astype(np.uint8)))
    
    return res