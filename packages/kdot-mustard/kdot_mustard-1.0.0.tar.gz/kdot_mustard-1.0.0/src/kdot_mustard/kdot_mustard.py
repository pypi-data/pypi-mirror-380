from kdot_mustard._calculate import _get_frames
from kdot_mustard._visual import _load_image, _save_anim, _crop_image
from importlib.resources import files

KENDRICK = files('kdot_mustard').joinpath('img', 'kendrick.jpeg')
TEST = files('kdot_mustard').joinpath('img', 'test.jpg')

def kdot(src_path: str, target_path: str = "bossman.gif", 
         loop: int | None = None, frames: int = 100, duration: int = 50) -> None:
    kendrick = _load_image(KENDRICK)
    src_img = _crop_image(_load_image(src_path), kendrick.size)
    print("Images locked and loaded...")
    frames = _get_frames(src_img, kendrick, frames = 100)
    print("Frames made and moulded...")
    print("Stitching the man that's goated...")
    _save_anim(frames, target_path, loop, duration)
    print("On the beat, Mustarddddddd!")

def kdot_simple(src_path: str) -> None:
    kdot(src_path)

def kdot_example() -> None:
    kdot(TEST)

if __name__ == "__main__":
    kdot_example()