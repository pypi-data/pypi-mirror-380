from PIL import Image

def _load_image(path: str) -> Image.Image:
    try: 
        img = Image.open(path)
        return img
    except FileNotFoundError:
        print(f"Error: Image file not found at {path}")
    except Exception as e:
        print(f"{e}")
    return None

def _crop_image(src_img: Image.Image, dim: tuple) -> Image.Image:
    src_size = src_img.size
    center = tuple(map(lambda x: x // 2, src_size))
    box = (center[0] - dim[0] // 2, center[1] - dim[1] // 2, 
           center[0] + dim[0] // 2, center[1] + dim[1] // 2)
    return src_img.crop(box)

def _save_anim(frames: list, path: str, loop: int | None = 1, duration: int = 5) -> None:
    frames[0].save(path, save_all=True, 
                   append_images=frames[1:], duration=duration, 
                   loop=loop, optimize=True, subrectangles=True)