from utils import *
from dataclasses import dataclass
import numpy as np
from numba import jit

_gravitational_constant = 6.674e-11
_speed_of_light = 2.9979e8


@dataclass
class Ray:
    position: np.array
    velocity: np.array

    depth: int = 0

    delta_t = 0.000001

    def __init__(self, position: np.array = np.array([0, 0, 0]), direction: np.array = np.array([1, 0, 0])):
        self.position = position
        self.velocity = direction * (_speed_of_light / np.linalg.norm(direction))

    @jit
    def simulate_to_end(self, gravity_objects=[]):
        max_timesteps = 1000000000000

        # print(self.velocity)
        # print(self.position)
        # print(np.linalg.norm(self.position - np.array([50000, 50000, 50000])))
        while np.linalg.norm(self.position - np.array(
                [50000, 50000, 50000])) < 85000:  # replace with better code for detecting exiting the worldbox
            # print(self.position.x, self.position.y, self.position.z)
            # print('-')
            # print(self.position)
            max_timesteps -= 1
            if max_timesteps < 0:
                break

            for object in gravity_objects:
                if object.mass == 0:
                    continue

                direction = object.origin - self.position
                distance = np.linalg.norm(direction)
                acceleration_scalar = 2 * _gravitational_constant * object.mass / (distance ** 2)

                acceleration = direction * (acceleration_scalar / distance)

                self.delta_t = 0.000001 * max(1, (distance / 60000) ** 2)
                # print(self.velocity)
                # print(acceleration)

                self.velocity += self.delta_t * acceleration

            self.velocity *= _speed_of_light / np.linalg.norm(self.velocity)

            # print(self.velocity)

            accleration = 0  # implement later

            new_position = self.position + self.velocity * self.delta_t
            # print(new_position)
            last_position = self.position
            self.position = new_position

            for object in gravity_objects:
                if object.hit_by_ray(self, last_position):
                    hit_position = self.position  # not accurate: e.g. move to surface of sphere
                    hit_direction = self.velocity / np.linalg.norm(self.velocity)

                    luminance = object.get_luminance(hit_position, hit_direction)  # maybe divide by distance travelled or sth?
                    print(str(luminance))
                    return luminance

            # print(gravity_objects[0].radius)
            # print(np.linalg.norm(self.position - np.array([0.5, 0.5, 0.5])))
            # exit()
        # exit()
        return Spectrum()

    # min_t: float = 0
    # max_t: float = float('inf')

    # inv_d: Vector = Vector(0,0,0)

    # def at_time(self, t) -> Vector:
    #     return self.o + t * self.d

    # may not be necessary but I'm putting this in here for the sake of completion later if necessary
    def transform_by(self, t):
        raise NotImplementedError()
