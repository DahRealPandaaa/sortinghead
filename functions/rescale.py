# import numpy as np
# from PIL import Image as Image_pil, ImageDraw


def rescale(image_webcam):
    base = 350
    box = ((image_webcam.width / 2) - (base / 3 * 2), (image_webcam.height / 2 - (base / 3 * 2)),
           (image_webcam.width / 2) + (base / 3 * 2), image_webcam.height / 2 + (base / 3 * 2))
    image_webcam = image_webcam.resize(box=box, size=(base, base))

    # Open the input image as numpy array, convert to RGB
    # img = image_webcam.convert("RGB")
    # npImage = np.array(img)

    # Make circle
    # alpha = Image_pil.new('L', img.size, 0)
    # draw2 = ImageDraw.Draw(alpha)
    # draw2.pieslice([0, 0, base, base], 0, 360, fill=255)
    # npAlpha = np.array(alpha)
    # npImage = np.dstack((npImage, npAlpha))

    # image_webcam = Image_pil.fromarray(npImage)

    return image_webcam

