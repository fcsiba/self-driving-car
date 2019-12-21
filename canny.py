import cv2
import numpy as np
import matplotlib.pyplot as plt
import os


def canny(img):
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny_img = cv2.Canny(blur, 20, 190)
    return canny_img


def region_of_interest(img):
    # height = img.shape[0]
    polygons = np.array([
        [(0, 1300), (1250, 450), (2550, 1300)]
    ])
    mask = np.zeros_like(img)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(img, mask)
    return masked_image


def display_lines(img, lines):
    line_img = np.zeros_like(img)
    if lines is not None:
        for line in lines:
            x1, y1, x2, y2 = line.reshape(4)
            cv2.line(line_img, (x1, y1), (x2, y2), (255, 0, 0), 10)
    return line_img


for file in os.listdir('camera'):
    if file.endswith('.jpg'):
        input_path = os.path.join('camera', file)
        append_path = os.path.join('camera', 'lanes')
        print(os.path.join('camera', file))
        image = cv2.imread(input_path)
        lane_image = np.copy(image)
        canny_image = canny(lane_image)
        cropped_image = region_of_interest(canny_image)
        lane_lines = cv2.HoughLinesP(cropped_image, 2, np.pi / 180, 100, np.array([]), minLineLength=40, maxLineGap=5)
        line_image = display_lines(lane_image, lane_lines)
        combo_image = cv2.addWeighted(lane_image, 0.8, line_image, 1, 1)
        save_path = os.path.join(append_path, file)
        cv2.imwrite(save_path, combo_image)
        print('saved: ' + file)
# cv2.imshow("result", combo_image)
# cv2.waitKey(0)
# plt.imshow(lane_image)
# plt.show()
