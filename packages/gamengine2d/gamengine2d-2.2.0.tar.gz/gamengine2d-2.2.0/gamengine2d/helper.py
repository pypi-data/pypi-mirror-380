import os
import importlib.util
import sys
import math
import time


# -----------------------------
# Vector 2D
# -----------------------------
class vector2d:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    @property
    def magnitude(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)

    @property
    def sqr_magnitude(self):
        return self.x ** 2 + self.y ** 2

    def __add__(self, other):
        if isinstance(other, vector2d):
            return vector2d(self.x + other.x, self.y + other.y)
        else:
            return vector2d(self.x + other, self.y + other)

    def __sub__(self, other):
        if isinstance(other, vector2d):
            return vector2d(self.x - other.x, self.y - other.y)
        else:
            return vector2d(self.x - other, self.y - other)

    def __mul__(self, other):
        if isinstance(other, vector2d):
            return vector2d(self.x * other.x, self.y * other.y)
        else:
            return vector2d(self.x * other, self.y * other)

    def __truediv__(self, other):
        if isinstance(other, vector2d):
            return vector2d(self.x / other.x, self.y / other.y)
        else:
            return vector2d(self.x / other, self.y / other)

    def totuple(self):
        return (self.x, self.y)

    @classmethod
    def fromtuple(cls, tuple):
        cls.x, cls.y = tuple
        return vector2d(cls.x, cls.y)

    def __repr__(self):
        return f"vector2d({self.x}, {self.y})"

    def copy(self):
        return vector2d(self.x, self.y)

    def __neg__(self):
        return vector2d(-self.x, -self.y)

vector2d.up = vector2d(0, 1)
vector2d.down = vector2d(0, -1)
vector2d.right = vector2d(1, 0)
vector2d.left = vector2d(-1, 0)
vector2d.one = vector2d(1, 1)
vector2d.zero = vector2d(0, 0)

def rotate(pos: vector2d, angle):
    rad = math.radians(angle)
    cos_a = math.cos(rad)
    sin_a = math.sin(rad)

    x = pos.x * cos_a - pos.y * sin_a
    y = pos.x * sin_a + pos.y * cos_a
    return vector2d(x, y)

# -----------------------------
# Color
# -----------------------------
class Color:
    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    @staticmethod
    def RGB(r, g, b): return Color(r, g, b)
    @staticmethod
    def hex(hex_string):
        if not hex_string.startswith("#"): raise Exception("String must start with #")
        if not len(hex_string) == 7: raise Exception("String must contain 7 characters")
        r = int(hex_string[1:3], 16)
        g = int(hex_string[3:5], 16)
        b = int(hex_string[5:7], 16)
        return Color(r, g, b)
    @staticmethod
    def black(): return Color(0, 0, 0)
    @staticmethod
    def red(): return Color(255, 0, 0)
    @staticmethod
    def green(): return Color(0, 255, 0)
    @staticmethod
    def blue(): return Color(0, 0, 255)
    @staticmethod
    def yellow(): return Color(255, 255, 0)
    @staticmethod
    def cyan(): return Color(0, 255, 255)
    @staticmethod
    def magenta(): return Color(255, 0, 255)
    @staticmethod
    def white(): return Color(255, 255, 255)

    def to_hex(self):
        if not all(0 <= x <= 255 for x in (self.r, self.g, self.b)):
            raise ValueError("RGB values must be in the range 0-255")
        return "#{:02X}{:02X}{:02X}".format(self.r, self.g, self.b)

    def to_rgb(self):
        return self.r, self.g, self.b

class Delay:
    def __init__(self, delay, start_time, callback):
        self.delay = delay
        self.start_time = start_time
        self.callback = callback
        self.finished = False

    def update(self):
        if time.monotonic() - self.start_time > self.delay:
            self.callback()
            self.finished = True
            return

# -----------------------------
# Context / Functions
# -----------------------------
class Functions:
    def __init__(self):
        self.draw_circle = None
        self.is_colliding = None
        self.draw_text = None
        self.draw_rect = None
        self.get_objects_with_prefix = None
        self.add_sound = None
        self.create_sound = None
        self.is_colliding_pos = None

class Context:
    def __init__(self):
        self.functions = Functions()
        self.screen_size = vector2d(0, 0)  # <-- added
        self.settings = []
        self.pause = False
        self.hide_all = False
        self.start_time = None
        self.runtime_vars = {}
        self.game_objects = []
        self.delays = []
        self.sounds = {}

    def get(self, name):
        for obj in self.game_objects:
            if obj.name == name:
                return obj
        else:
            raise EngineError(f"Error, name '{name}' not found")

    def remove_object(self, obj):
        self.game_objects.remove(obj)

    def add_delay(self, delay, callback):
        self.delays.append(Delay(delay, time.monotonic(), callback))

# -----------------------------
# Script
# -----------------------------
class Script:
    def __init__(self, obj, script_path, context):
        self.obj = obj
        self.context = context
        self.script_path = script_path
        self.module = None
        self.cls = None
        self.instance = None
        self.load(script_path)

    def load(self, path):
        if not os.path.exists(path):
            print(f"[Script] File not found: {path}")
            return
        module_name = os.path.splitext(os.path.basename(path))[0]
        spec = importlib.util.spec_from_file_location(module_name, path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        try:
            spec.loader.exec_module(module)
        except Exception as e:
            print(f"[Script] Error loading module {path}: {e}")
            return
        self.module = module

        # Class is PascalCase version of file name
        class_name = ''.join(word.capitalize() for word in module_name.split('_'))
        if hasattr(module, class_name):
            self.cls = getattr(module, class_name)
        else:
            print(f"[Script] No class '{class_name}' found in {path}")

    def init_instance(self):
        """Instantiate the class, passing the owner object and context."""
        if self.cls is None or self.instance is not None:
            return
        try:
            self.instance = self.cls(self.obj, self.context)
        except Exception as e:
            print(f"[Script] Failed to instantiate script for {self.obj.name}: {e}")
            self.instance = None

        if self.instance and hasattr(self.instance, "start"):
            try:
                self.instance.start()
            except Exception:
                pass

    def update(self, dt):
        if self.instance is None:
            return
        self.instance.update(dt)
# -----------------------------
# Camera
# -----------------------------
class Camera:
    def __init__(self, pos=None, zoom=1, screen_size=None):
        self.pos = pos or vector2d(0, 0)
        self.zoom = zoom
        self.screen_size = screen_size or vector2d(800, 600)
        self.min_zoom = 0.1
        self.max_zoom = 10

    def world_to_screen(self, world_pos: vector2d):
        screen_pos = vector2d(
            (world_pos.x - self.pos.x) * self.zoom,
            (-world_pos.y + self.pos.y) * self.zoom  # invert Y
        )
        screen_pos += vector2d(self.screen_size.x / 2, self.screen_size.y / 2)
        return screen_pos

    def screen_to_world(self, screen_pos: vector2d):
        world_pos = screen_pos - vector2d(self.screen_size.x / 2, self.screen_size.y / 2)
        world_pos = world_pos * (1 / self.zoom) + self.pos
        return world_pos

    def zoom_at(self, zoom_factor, pivot: vector2d):
        old_zoom = self.zoom
        self.zoom *= zoom_factor
        self.zoom = max(self.min_zoom, min(self.max_zoom, self.zoom))
        self.pos += (pivot - self.pos) * (1 - old_zoom / self.zoom)

class EngineError(Exception):
    pass

def project_polygon(axis, vertices):
    dots = [v.x * axis.x + v.y * axis.y for v in vertices]
    return min(dots), max(dots)

def overlap(p1, p2):
    return p1[0] <= p2[1] and p2[0] <= p1[1]

def is_colliding(poly1, poly2):
    # poly1, poly2 = lists of vector2d
    for polygon in (poly1, poly2):
        for i in range(len(polygon)):
            # get edge
            p1, p2 = polygon[i], polygon[(i + 1) % len(polygon)]
            edge = vector2d(p2.x - p1.x, p2.y - p1.y)
            # perpendicular axis
            axis = vector2d(-edge.y, edge.x)
            # project both polygons
            proj1 = project_polygon(axis, poly1)
            proj2 = project_polygon(axis, poly2)
            # check overlap
            if not overlap(proj1, proj2):
                return False
    return True
