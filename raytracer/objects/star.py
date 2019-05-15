# stars in the background. mass doesn't matter here since they're just visual.
import numpy as np
from utils import Spectrum, Ray

G = 6.674e-11
C = 2.9979e8

class Star:
    def __init__(
            self,
            origin: np.array = np.array([0.5, 0.5, 0.5]),
            mass: float = 0,
            radius: float = 2949
    ):
        self.origin = origin
        self.mass = mass
        self.radius = 2 * G * 0.75e30 / (C ** 2)

    def hit_by_ray(self, r: Ray, last_position: np.array) -> bool:
        # if np.linalg.norm(r.position - self.origin) <= (2.5 * self.radius):  # photon sphere
        if np.linalg.norm(r.position - self.origin) <= self.radius:  # using event horizon for testing purposes
            return True

        return False

    def get_luminance(self, out_position: np.array, out_direction: np.array) -> Spectrum:
        return Spectrum(255, 255, 255)
