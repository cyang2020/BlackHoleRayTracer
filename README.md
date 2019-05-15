# BlackholeRaytracerCS184
Final project for CS184 at UC Berkeley


# Requirements
- Python 3.7
- Pillow


# Running
`python3 raytracer [args...]`


# Notes about Python
- a folder with a file named `__init__.py` is considered a "module". So we have a module named `raytracer`, with 3 submodules named `renderer`, `objects`, and `utils`.
- to import from a file in the same module, do `from .camera import Camera`.
- to import from a file within another module do `from utils.vector import Vector` or `import utils.vector [as uv]`.
- the file `__init__.py` is used to define stuff accessible via a simple `import module`. This is what allows us to do `from utils import Vector`.
- the file `__main__.py` is run when a module is "run". Which is what allows us to run the program using `python3 raytracer`.
