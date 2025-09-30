from gamengine2d import Engine, Circle, Color, vector2d, Rectangle


def run():
    engine = Engine(1200, 800, resizable=True)
    circle = Circle(radius=30, color=Color.red())
    rectangle = Rectangle(size=vector2d(100, 400), color=Color.blue(), pos=vector2d(100, 40), rotation=90)

    engine.add_object(circle)
    engine.add_object(rectangle)

    engine.run()
