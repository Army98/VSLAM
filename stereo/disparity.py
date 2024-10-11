import cv2
import numpy as np


def calc_disparity(left_image, right_image):
    fx = 718.856
    fy = 718.856
    cx = 607.1928
    cy = 185.2157
    b = 0.573

    left_image = cv2.imread(left_image, cv2.IMREAD_GRAYSCALE)
    right_image = cv2.imread(right_image, cv2.IMREAD_GRAYSCALE)

    sgbm_ptr = cv2.StereoSGBM_create(
        minDisparity=0,
        numDisparities=96,
        blockSize=8,
        P1=9 * 3 * 8,
        P2=32 * 3 * 8,
        disp12MaxDiff=1,
        preFilterCap=63,
        uniquenessRatio=10,
        speckleWindowSize=100,
        speckleRange=32
    )

    disparity = sgbm_ptr.compute(left_image, right_image)
    disparity_norm = np.float32(disparity) / 16.0

    point_cloud = [None] * 4

    for v in range(left_image.shape[0]):
        for u in range(left_image.shape[1]):
            if 10.0 <= disparity[v, u] < 96:
                depth = fx * b / disparity[v, u]
                X = (u - cx) * depth / fx
                Y = (v - cy) * depth / fy
                point_cloud.append([X, Y, depth])


    cv2.imshow('disparity', disparity_norm)
    cv2.waitKey(0)


calc_disparity('left.png', 'right.png')
