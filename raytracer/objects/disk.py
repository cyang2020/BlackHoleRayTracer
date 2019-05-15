from utils import Spectrum, Ray
from math import cos, sin, radians
import numpy as np

BASENORMAL = np.array([0, 1, 1])

class Disk:
    def __init__(
        self,
        origin: np.array =  np.array([0.5, 0.5, 0.5]),
        normal: np.array = np.array([0, 1, 0]),
        inner_radius: float = 0,
        outer_radius: float = 0.1
    ):
        self.origin = origin
        self.normal = normal
        self.inner_radius = inner_radius
        self.outer_radius = outer_radius
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
        if self._intersects_plane(r, last_position):
            distance = np.linalg.norm(r.position - self.origin)
            return self.inner_radius <= distance <= self.outer_radius

    def get_luminance(self, out_position: np.array, out_direction: np.array) -> Spectrum:
        inner_spectrum = Spectrum(0, 0, 255)
        outer_spectrum = Spectrum(0, 0, 128)

        distance = np.linalg.norm(out_position - self.origin)
        ratio = (distance - self.inner_radius) / (self.outer_radius - self.inner_radius)

        spectrum = (1 - ratio) * inner_spectrum + ratio * outer_spectrum
        spectrum.r = int(spectrum.r)
        spectrum.g = int(spectrum.g)
        spectrum.b = int(spectrum.b)
        return spectrum
