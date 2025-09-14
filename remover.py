from rembg import remove, new_session
from PIL import Image

SESSION = new_session("u2net")  # auto-download, no manual weights

def remove_bg(input_path: str, output_path: str) -> None:
    with Image.open(input_path) as im:
        im = im.convert("RGBA")
        out = remove(im, session=SESSION)
        out.save(output_path)
