import pydicom
from pydicom.data import get_testdata_files
import glob
import numpy as np
import cv2

def convert_to_png(nodules):
    for i, nodule in enumerate(nodules):
        name = nodule.split('.')[0]
        if i % 100 == 0:
            print(f'\r{i}')
        img = cv2.normalize(pydicom.dcmread(nodule).pixel_array, None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX)
        cv2.imwrite(f'/Volumes/Macintosh HD - Data/LIDC/All Extracted Images/nodules/nodules_png/{name}.png', img)
if __name__=='__main__':
    nodules = glob.glob('*.dcm')
    convert_to_png(nodules)