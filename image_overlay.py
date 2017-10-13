# -*- coding: utf-8 -*-
"""image_overlay.py module.

Project: garage.smartanalytics.sva
Created: 10/2017 - u.maurer@enbw.com

(c) Copyright EnBW AG 2017.
"""

import cv2
import numpy as np


def overlay_image(target, overlay, row, col, new_image=True):

    orows, ocols, _ = overlay.shape
    trows, tcols, _ = target.shape

    # if overlay is out of bounds return target unchanged:
    if row+orows <= 0 or col+ocols <= 0 or row >= trows or col >= tcols:
        return target

    if row < 0 or col < 0:
        # Left side of overlay will be clipped
        overlay = overlay[-(row+orows):,-(col+ocols):]
        row = col = 0
    elif row+orows > trows or col+ocols > tcols:
        # Right side of overlay will be clipped
        overlay = overlay[:orows-(row+orows-trows), :ocols-(col+ocols-tcols)]

    orows, ocols, _ = overlay.shape
    print(orows,ocols)

    # create a ROI
    y1 = row
    x1 = col
    y2 = row + orows
    x2 = col + ocols
    roi = target[y1:y2, x1:x2]
    print(roi.shape)

    # Now create a mask of overlay and create its inverse mask
    img2gray = cv2.cvtColor(overlay, cv2.COLOR_BGR2GRAY)

    # add a threshold
    ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)

    # Now black-out the area of overlay in ROI
    mask_inv = cv2.bitwise_not(mask)
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

    # Take only region of overlay from overlay image.
    img2_fg = cv2.bitwise_and(overlay, overlay, mask=mask)

    # Insert overlay into target roi
    dst = cv2.add(img1_bg, img2_fg)

    if new_image:
        result = target.copy()
    else:
        result = target

    # Paste roi in target image:
    result[y1:orows + y1, x1:ocols + x1] = dst
    return result


# Load two images
target = cv2.imread('3D-Matplotlib.png')
overlay = cv2.imread('mainlogo.png')

result = overlay_image(target, overlay, 200, 400)

cv2.imshow('target',target)
cv2.imshow('overlay',overlay)
cv2.imshow('result',result)
cv2.waitKey(0)
cv2.destroyAllWindows()