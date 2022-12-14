from PIL import Image, ImageOps
from kcu import kpath
import os

def _invert(
    path_in: str,
    path_out: str
) -> None:
    image = Image.open(path_in)

    if image.mode != 'RGBA':
        image = image.convert('RGBA')

    r,g,b,a = image.split()
    rgb_image = Image.merge('RGB', (r,g,b))
    inverted_image = ImageOps.invert(rgb_image)
    r2,g2,b2 = inverted_image.split()
    final_transparent_image = Image.merge('RGBA', (r2,g2,b2,a))
    final_transparent_image.save(path_out)
    # elif image.mode == 'RGB':
    #     inverted_image = ImageOps.invert(image)
    #     inverted_image.save(path_out)
    # else:
    #     print(path_in, image.mode)

def invert(path_in: str) -> None:
    img_ext = path_in.split('.')[-1]
    _invert(path_in, path_in) # path_in.replace('.' + img_ext, '-dark.' + img_ext))



for img_path in kpath.file_paths_from_folder(kpath.folder_path_of_file(), allowed_extensions=['.png']):
    # if img_path.endswith('-dark.' + img_path.split('.')[-1]):
    if img_path.endswith('background-org.png'):
        # os.remove(img_path)
        continue

    invert(img_path)
