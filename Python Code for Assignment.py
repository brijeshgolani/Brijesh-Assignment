import cv2
import numpy as np
import time


class Robot:
    def __init__(self, center):
        self.center = center

class DataTest:
    def __init__(self):
        self.end_time = None
        self.data = {}

class Result:
    def __init__(self, success, description):
        self.success = success
        self.description = description


def count_leds(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


    _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)


    lit_pixels = cv2.countNonZero(binary)

   
    threshold = 500  

    lit_segments = lit_pixels > threshold

    return lit_segments


def task_example(robot, image, dataTest):
    if dataTest.end_time is None:
        dataTest.end_time = time.time() + 10


    lit_segments = count_leds(image)


    num_lit_segments = sum(lit_segments)


    result = Result(True, f"{num_lit_segments} segments are lit")


    text = f"{num_lit_segments} segments are lit on the LED strip."

    return dataTest, text, result
