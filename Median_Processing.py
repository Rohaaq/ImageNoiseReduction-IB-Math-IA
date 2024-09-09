# Code for running various OpenCV related filters

import cv2
import os
import numpy as np

original = cv2.imread('snow_noise_crop.jpg')
full_original = cv2.imread("snow_noise.JPG")

processed_a = cv2.medianBlur(original, 5)
processed_b = cv2.medianBlur(original, 9)
processed_c = cv2.medianBlur(original, 15)
processed_d = cv2.medianBlur(original, 19)
processed_e = cv2.medianBlur(original, 25)

processed_best = cv2.medianBlur(full_original, 11)

# Create a canvas to hold both images side by side
canvas_width = original.shape[1] + processed_a.shape[1] + processed_b.shape[1] + processed_c.shape[1] + processed_d.shape[1] + processed_e.shape[1]
canvas_height = original.shape[0]
canvas = np.zeros((canvas_height, canvas_width, 3), dtype=np.uint8)

# Place the images on the canvas
canvas[:original.shape[0], :original.shape[1]] = original
canvas[:processed_a.shape[0], original.shape[1]:2*original.shape[1]] = processed_a
canvas[:processed_b.shape[0], 2*original.shape[1]:3*original.shape[1]] = processed_b
canvas[:processed_c.shape[0], 3*original.shape[1]:4*original.shape[1]] = processed_c
canvas[:processed_d.shape[0], 4*original.shape[1]:5*original.shape[1]] = processed_d
canvas[:processed_e.shape[0], 5*original.shape[1]:] = processed_e

# Display the combined image
os.chdir("G:\My Drive\High School\Grade 12\Math Stats\Math IA\Code and resources\Median_Processed") 
cv2.imwrite("median_strip.png", canvas)
cv2.imwrite("best_kernel.png", processed_best)

