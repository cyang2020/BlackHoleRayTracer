from utils import Spectrum, Ray
import numpy as np

class Background:
    def __init__(
        self,
        origin: np.array =  np.array([50000, 50000, 80000]),
        normal: np.array = np.array([0, 0, 1])
    ):
        self.origin = origin
        self.normal = normal
        self.mass = 0


    def _intersects_plane(self, r: Ray, last_position: np.array) -> bool:
        relative_direction = np.dot(r.position - self.origin, self.normal)
        relative_last_direction = np.dot(last_position - self.origin, self.normal)

        if relative_direction == 0:
            return True

        if relative_direction > 0:
            return relative_last_direction < 0

        # relative_direction < 0:
        return relative_last_direction > 0

    def hit_by_ray(self, r: Ray, last_position: np.array) -> bool:
        return self._intersects_plane(r, last_position)

    def get_luminance(self, out_position: np.array, out_direction: np.array) -> Spectrum:
        relative_direction = out_position - self.origin
        # print(relative_direction)
        if np.floor(np.floor(relative_direction[0]/5000) + np.floor(relative_direction[1]/5000)) % 2 == 0:
            return Spectrum(0, 255, 0)

        return Spectrum(255, 255, 0)
