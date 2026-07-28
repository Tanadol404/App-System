from math import sqrt
from kivy.uix.button import Button

class RoundedButton(Button):
    def __init__(self, corner_radius=30, **kwargs):
        self.corner_radius = corner_radius
        super().__init__(**kwargs)

    def collide_point(self, x, y):
        inside_box = super().collide_point(x, y)
        if not inside_box:
            return False

        r = self.corner_radius
        bx, by = self.pos
        bw, bh = self.size

        if x < bx + r and y > by + bh - r:
            return sqrt((x - (bx + r)) ** 2 + (y - (by + bh - r)) ** 2) <= r

        if x > bx + bw - r and y > by + bh - r:
            return sqrt((x - (bx + bw - r)) ** 2 + (y - (by + bh - r)) ** 2) <= r

        if x < bx + r and y < by + r:
            return sqrt((x - (bx + r)) ** 2 + (y - (by + r)) ** 2) <= r

        if x > bx + bw - r and y < by + r:
            return sqrt((x - (bx + bw - r)) ** 2 + (y - (by + r)) ** 2) <= r

        return True