from utils import Ray
import numpy as np
class Camera:
    def __init__(self, position=np.array([0.5, 0.5, 0]), fov=(0.5, 0.33), resolution=(800, 600), render_portion=None, render_origin=(0, 0)):
        self.position = position
        self.fov = fov
        self.resolution = resolution

    def cast_ray(self, pixel):
        ray_direction = np.array([
            (pixel[0] / self.resolution[0] - 0.5) * self.fov[0],
            (pixel[1] / self.resolution[1] - 0.5) * self.fov[1],
            1
        ])

        ray = Ray(position=self.position, direction=ray_direction)
        return ray
