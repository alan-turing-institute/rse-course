
import numpy as np
from io import BytesIO
import imageio as img
import requests

class Map(object):
    def __init__(self, lat, long, satellite=True, zoom=10,
                 size=(400, 400), sensor=False):
        base = "https://static-maps.yandex.ru/1.x/?"

        params = dict(
            z=zoom,
            size=str(size[0]) + "," + str(size[1]),
            ll=str(long) + "," + str(lat),
            l="sat" if satellite else "map",
            lang="en_US"
        )

        self.image = requests.get(
            base, params=params).content  # Fetch our PNG image data
        content = BytesIO(self.image)
        self.pixels = img.imread(content) # Parse our PNG image as a numpy array
        
    def green(self, threshold):
        # Use NumPy to build an element-by-element logical array
        greener_than_red = self.pixels[:, :, 1] > threshold * self.pixels[:, :, 0]
        greener_than_blue = self.pixels[:, :, 1] > threshold * self.pixels[:, :, 2]
        green = np.logical_and(greener_than_red, greener_than_blue)
        return green

    def count_green(self, threshold=1.1):
        return np.sum(self.green(threshold))

    def show_green(data, threshold=1.1):
        green = self.green(threshold)
        out = green[:, :, np.newaxis] * array([0, 1, 0])[np.newaxis, np.newaxis, :]
        buffer = BytesIO()
        result = img.imwrite(buffer, out, format='png')
        return buffer.getvalue()
