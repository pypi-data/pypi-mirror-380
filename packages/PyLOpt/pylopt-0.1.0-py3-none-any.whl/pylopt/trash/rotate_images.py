import os
import cv2
import shutil

# path_bsd68 = '/home/florianthaler/Documents/trash/denoising_datasets/CBSD68'
# image_path = '/home/florianthaler/Documents/data/image_data/BSDS300/images/test'
# target_path = '/home/florianthaler/Documents/data/image_data/BSDS68'

path_src = '/home/florianthaler/Documents/data/image_data/BSDS68'
path_target = '/home/florianthaler/Documents/data/image_data/BSDS68_rotated'


for item in os.listdir(path_src):

    # base = os.path.splitext(item)[0]
    # shutil.copy2(os.path.join(image_path, '{:s}.jpg'.format(base)), target_path)
    img = cv2.imread(os.path.join(path_src, item))
    h, w, c = img.shape
    if h < w:
        img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
    cv2.imwrite(os.path.join(path_target, item), img)
