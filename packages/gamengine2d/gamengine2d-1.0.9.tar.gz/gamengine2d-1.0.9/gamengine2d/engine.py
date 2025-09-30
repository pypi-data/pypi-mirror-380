import pygame
from .helper import vector2d, Context, Color, Camera, EngineError, is_colliding
from .objects import GameObject
import tkinter as tk
from tkinter import ttk

# -----------------------------
# Number / String Input Objects
# -----------------------------
class NumberInputObj:
    def __init__(self, var: tk.DoubleVar, default=0):
        self.var = var
        self.default = default

    @property
    def value(self):
        try:
            # Try converting to float; fallback to default if empty or invalid
            val = self.var.get()
            if val == "":
                return self.default
            return float(val)
        except Exception:
            return self.default

    @value.setter
    def value(self, v):
        self.var.set(v)


class StringInputObj:
    def __init__(self, var: tk.StringVar, default=""):
        self.var = var
        self.default = default

    @property
    def value(self):
        val = self.var.get()
        if val == "":
            return self.default
        return val

    @value.setter
    def value(self, v):
        self.var.set(v)


# -----------------------------
# Settings Window
# -----------------------------
class SettingsWindow:
    _root = None  # single hidden root

    def __init__(self, title="Settings"):
        if SettingsWindow._root is None:
            SettingsWindow._root = tk.Tk()
            SettingsWindow._root.withdraw()  # hide main root

        self.root = tk.Toplevel(SettingsWindow._root)
        self.root.title(title)
        self.inputs = {}

        self.container = ttk.Frame(self.root, padding=20)
        self.container.pack(fill="both", expand=True)

    def add_number_input(self, label, default=0):
        var = tk.StringVar(master=self.root, value=str(default))
        frame = ttk.Frame(self.container)
        frame.pack(fill="x", pady=2)
        ttk.Label(frame, text=label).pack(side="left")
        ttk.Entry(frame, textvariable=var).pack(side="right")
        input_obj = NumberInputObj(var, default)
        self.inputs[label] = input_obj
        return input_obj

    def add_string_input(self, label, default=""):
        var = tk.StringVar(master=self.root, value=default)
        frame = ttk.Frame(self.container)
        frame.pack(fill="x", pady=2)
        ttk.Label(frame, text=label).pack(side="left")
        ttk.Entry(frame, textvariable=var).pack(side="right")
        input_obj = StringInputObj(var, default)
        self.inputs[label] = input_obj
        return input_obj

    def update(self):
        self.root.update()

# -----------------------------
# Engine
# -----------------------------
class Engine:
    def __init__(self, width=500, height=500, name="GamEngine2D", resizable=True, background_color=Color.black()):
        if not pygame.get_init():
            pygame.init()
        flags = pygame.RESIZABLE if resizable else 0
        self.screen = pygame.display.set_mode((width, height), flags)
        pygame.display.set_caption(name)

        self.clock = pygame.time.Clock()
        self.camera = Camera(screen_size=vector2d(width, height))
        self.objects = []
        self.background_color = background_color

        # Context setup
        self.context = Context()
        self.context.functions.draw_circle = self.draw_circle
        self.context.functions.draw_text = self.draw_text
        self.context.functions.is_colliding = self.is_colliding
        self.context.screen_size = vector2d(width, height)

    def draw_circle(self, pos: vector2d, radius: int, color: Color):
        screen_pos = self.camera.world_to_screen(pos).totuple()
        pygame.draw.circle(self.screen, color.to_rgb(), screen_pos, int(radius * self.camera.zoom))

    def is_colliding(self, obj1, obj2_name):
        try:
            obj2 = [obj for obj in self.objects if obj.name == obj2_name][0]
        except IndexError:
            raise EngineError(f"Error, game object with name '{obj2_name}' not found")

        if not isinstance(obj1, GameObject):
            raise EngineError(f"Error, {obj1.name} is not the name of a game object")

        if not isinstance(obj2, GameObject):
            raise EngineError(f"Error, {obj2.name} is not the name of a game object")

        if not hasattr(obj1, "get_corners"):
            raise EngineError(f"Error, game object with name '{obj1.name}' has no get_corners method")

        if not hasattr(obj2, "get_corners"):
            raise EngineError(f"Error, game object with name '{obj2.name}' has no get_corners method")

        return is_colliding(obj1.get_corners(), obj2.get_corners())

    def draw_text(self, text: str, pos: vector2d, color: Color, font_size=18, center=False):
        """Draw text at world position (pos)."""
        font = pygame.font.SysFont("Arial", font_size)
        text_surface = font.render(text, True, color.to_rgb())
        screen_pos = self.camera.world_to_screen(pos).totuple()

        if center:
            rect = text_surface.get_rect(center=(int(screen_pos[0]), int(screen_pos[1])))
        else:
            rect = text_surface.get_rect(topleft=(int(screen_pos[0]), int(screen_pos[1])))

        self.screen.blit(text_surface, rect)

    def add_object(self, obj: GameObject):
        self.objects.append(obj)

    def init_all_scripts(self):
        for obj in self.objects:
            obj.init_scripts()

    def run(self, fps=60, dynamic_view=True):
        self.init_all_scripts()
        running = True

        dragging = False
        last_mouse_pos = None

        while running:
            dt = self.clock.get_time() / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if dynamic_view:
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            dragging = True
                            last_mouse_pos = vector2d(*event.pos)
                    elif event.type == pygame.MOUSEBUTTONUP:
                        if event.button == 1:
                            dragging = False
                    elif event.type == pygame.MOUSEMOTION and dragging:
                        mouse_pos = vector2d(*event.pos)
                        delta = mouse_pos - last_mouse_pos
                        delta.y = -delta.y
                        self.camera.pos -= delta * (1 / self.camera.zoom)
                        last_mouse_pos = mouse_pos
                    elif event.type == pygame.MOUSEWHEEL:
                        zoom_factor = 1.1 if event.y > 0 else 0.9
                        mouse_world = self.camera.screen_to_world(vector2d(*pygame.mouse.get_pos()))
                        self.camera.zoom_at(zoom_factor, mouse_world)

            w, h = self.screen.get_size()
            self.context.screen_size = vector2d(w, h)
            self.camera.screen_size = vector2d(w, h)

            self.screen.fill(self.background_color.to_rgb())

            if not self.context.pause:
                for obj in self.objects:
                    obj.update(dt)

            if not self.context.hide_all:
                for obj in self.objects:
                    obj.draw(self.screen, self.camera)

            for setting in self.context.settings:
                setting.update()

            pygame.display.flip()
            self.clock.tick(fps)

        pygame.quit()
