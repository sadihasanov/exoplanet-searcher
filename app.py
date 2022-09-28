import numpy as np
from PIL import Image

sample_image = Image.open('sample_image.jpg')

converted_np = np.asarray(sample_image)

def detect_anomalies(arrays = []):
    pass

class Analysis:
    def __init__(self):
        self.default = 0
        self.image_idx = 0
        self.data = {}
        self.average_data = {}

    def set_default(self, value):
        self.default = value

    def add_data(self, path):
        new_image = Image.open(path)
        converted_image = np.asarray(new_image)
        average_value = np.average(converted_image)

        self.data[self.image_idx] = converted_image
        self.average_data[self.image_idx] = average_value

        self.image_idx += 1

    def get_graph(self):
        pass

    def remove_data_point(self, idx):
        try:
            del self.data[idx]
            del self.average_data[idx]
        except KeyError as ex:
            print("No such element: '%s'" % ex.message)

    