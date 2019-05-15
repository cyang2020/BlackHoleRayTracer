from utils import Ray, Spectrum
import numpy as np

G = 6.674e-11
C = 2.9979e8

class BlackHole:
    def __init__(
        self,
        origin: np.array = np.array([0.5, 0.5, 0.5]),
        mass: float = 7.5e+24
    ):
        self.origin = origin
        self.mass = mass
        self.radius = 2 * G * mass / (C ** 2)

    def hit_by_ray(self, r: Ray, last_position: np.array) -> bool:
        # if np.linalg.norm(r.position - self.origin) <= (2.5 * self.radius):  # photon sphere
        return np.linalg.norm(r.position - self.origin) <= self.radius

    def get_luminance(self, out_position: np.array, out_direction: np.array) -> Spectrum:
        relative_direction = out_position - self.origin
        if sum(1 if i > 0 else 0 for i in relative_direction) % 2 == 0:
            return Spectrum(255, 0, 0)

        return Spectrum(128, 0, 0)
