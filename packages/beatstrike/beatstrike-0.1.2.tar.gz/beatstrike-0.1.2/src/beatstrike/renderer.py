import pygame
from importlib import resources

class Template(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        with resources.path("beatstrike.assets.game", "template.png") as path:
            self.img = pygame.image.load(str(path))
        with resources.path("beatstrike.assets.game", "template_light.png") as path:
            self.img_hit = pygame.image.load(str(path))

        self.img = pygame.transform.scale(self.img, (120, 115))
        self.img_hit = pygame.transform.scale(self.img_hit, (120, 115))
        self.image = self.img
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]
        self.x = x

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update_visuals(self, key_is_pressed):
        self.image = self.img_hit if key_is_pressed else self.img


class Note(pygame.sprite.Sprite):
    def __init__(self, x, lane, duration=0, speed=1100):
        super().__init__()
        y = 1080
        self.lane = lane
        self.speed = speed
        self.duration = duration

        arrow_files = ["arrow_left.png", "arrow_down.png", "arrow_up.png", "arrow_right.png"]
        with resources.path("beatstrike.assets.game", arrow_files[lane]) as path:
            img = pygame.image.load(str(path))

        self.image = pygame.transform.scale(img, (120, 115))
        self.rect = self.image.get_rect()
        self.rect.topleft = [x, y]

        self.missed = False
        self.hold_time = 0
        self.is_holding = False
        self.hold_locked = False
        self.hold_failed = False

        if self.duration > 0:
            self.current_tail_height = self.speed * self.duration
            self.lane_colors = [
                (163, 172, 3),
                (163, 10, 10),
                (6, 127, 171),
                (4, 171, 9)
            ]

            self.holding_colors = [
                (219, 232, 0),
                (255, 43, 43),
                (62, 204, 255),
                (0, 240, 7)
            ]

            self.color_normal = self.lane_colors[lane]
            self.color_hold = self.holding_colors[lane]

    def start_hold(self):
        if self.duration > 0 and not self.hold_failed:
            self.is_holding = True
            self.hold_locked = True
            self.rect.y = 70

    def stop_hold(self):
        if self.hold_locked:
            self.is_holding = False
            self.hold_locked = False
            self.hold_failed = True

    def draw(self, screen):
        if self.duration > 0 and self.current_tail_height > 0:
            tail_rect = pygame.Rect(
                self.rect.centerx - 15,
                self.rect.bottom,
                30,
                self.current_tail_height
            )
            tail_color = self.color_hold if self.is_holding else self.color_normal
            pygame.draw.rect(screen, tail_color, tail_rect, border_radius=10)

        screen.blit(self.image, self.rect)

    def update(self, dt):
        if not self.hold_locked:
            mov = self.speed * (dt / 1000.0)
            self.rect.y -= mov

        if self.duration > 0 and self.is_holding:
            self.hold_time += dt / 1000.0
            remaining_time = max(self.duration - self.hold_time, 0)
            self.current_tail_height = self.speed * remaining_time
            if self.hold_time >= self.duration:
                self.is_holding = False
                self.hold_locked = False
                self.hold_time = self.duration
