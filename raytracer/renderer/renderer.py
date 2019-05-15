from PIL import Image, ImageDraw
from .world import World
from .camera import Camera
from objects import BlackHole

def render(world: World, camera: Camera, render_origin=(0, 0), render_size=None) -> Image.Image:
    image = Image.new('RGB', camera.resolution)

    if render_size is None:
        render_size = camera.resolution

    for i in range(render_size[0]):
        for j in range(render_size[1]):
            x = i + render_origin[0]
            y = j + render_origin[1]

            print(x, y)

            ray = camera.cast_ray((x, y))
            lum = ray.simulate_to_end(world.objects)
            image.putpixel((x, y), tuple(lum))

    return image



def test_render(dimensions=(800,600)) -> Image.Image:
    black_hole = BlackHole(None, None)
    color = black_hole.get_luminance(None)

    image = Image.new('RGB', dimensions)
    draw = ImageDraw.Draw(image)

    draw.rectangle((12, 12, 80, 32), fill=(255, 255, 255))
    draw.text((18, 18), 'Test', fill=tuple(color))

    return image
