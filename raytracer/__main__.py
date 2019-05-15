# import your favorite argument parser here
import random

from renderer.renderer import render
from renderer import Camera, World
from objects import BlackHole, Disk, Background
from numba import jit

import numpy as np

from objects.disk import Disk



def normalize_vector(v: np.array) -> np.array:
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm


# def generate_stars(num: int, world_radius: int) -> [Star]:
#     stars = []
#     spacing = 5000
#
#     for i in range(num):
#         x = world_radius + random.randint(-30000, 30000)
#         y = world_radius + random.randint(-30000, 30000)
#         stars.append(Star(origin=np.array([x, y, world_radius+40000])))
#     return stars

# import plac
# @plac.annotation
@jit
def main():
    disk_direction = normalize_vector(np.array([,1,0]))
    disk2_direction = normalize_vector(np.array([0,1,0]))

    world_radius = 50000

    objects_list = []

    black_hole = BlackHole(mass=1.989e30, origin=np.array([world_radius - 10000, world_radius, world_radius]))
    disk = Disk(
        origin=np.array([world_radius - 10000, world_radius, world_radius]),
        normal=disk_direction,
        inner_radius=black_hole.radius * 2.6,
        outer_radius=black_hole.radius * 6
    )
    # black_hole2 = BlackHole(mass=1.989e30, origin=np.array([world_radius + 10000, world_radius, world_radius]))
    # disk2 = Disk(
    #     origin=np.array([world_radius + 10000, world_radius, world_radius]),
    #     normal=disk_direction,
    #     inner_radius=black_hole.radius * 2.6,
    #     outer_radius=black_hole.radius * 6
    # )
    bg = Background()

    objects_list.append(black_hole)
    # objects_list.append(black_hole2)
    objects_list.append(disk)
    # objects_list.append(disk2)
    # objects_list.extend(generate_stars(10, world_radius))
    objects_list.append(bg)
    # disk = Disk()
    world = World(objects=objects_list, size=np.array([world_radius * 2] * 3))
    camera = Camera(resolution=(300, 200), fov=(1, 0.66), position=np.array([world_radius, world_radius, 0]))
    image = render(world, camera)
    image.save('test_render_binary_disks.png')


if __name__ == '__main__':
    main()
