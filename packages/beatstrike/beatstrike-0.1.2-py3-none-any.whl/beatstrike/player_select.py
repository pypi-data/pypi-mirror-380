import pygame
import importlib.resources
from beatstrike.button import BackButton

class PlayerSelect():
    def __init__(self, screen, background):
        # Preparação
        self.screen = screen
        self.bg = background
        self.options = ['voltar', 'solo', 'versus']
        self.selected_index = 1
        self.mouse_pos = (0, 0)

        # Carregar fonts
        with importlib.resources.path('beatstrike.assets.fonts', 'PressStart2P-Regular.ttf') as f:
            self.font_title = pygame.font.Font(str(f), 48)
        with importlib.resources.path('beatstrike.assets.fonts', 'Stencilia-A.ttf') as f:
            self.font_x = pygame.font.Font(str(f), 90)

        def load_image(package, filename, scale=None, rotate=0, flip=False):
            with importlib.resources.path(package, filename) as path:
                img = pygame.image.load(str(path)).convert_alpha()
            if scale:
                img = pygame.transform.scale(img, scale)
            if flip:
                img = pygame.transform.flip(img, True, False)
            if rotate != 0:
                img = pygame.transform.rotate(img, rotate)
            return img

        self.img_solo = load_image('beatstrike.assets.menu.player_select', 'Echo_player_select.png', (256, 320))
        self.img_vs1 = load_image('beatstrike.assets.menu.player_select', 'Beat_player_select.png', (256, 320), -25)
        self.img_vs2 = load_image('beatstrike.assets.menu.player_select', 'Pulse_player_select.png', (256, 320), -30, flip=True)
        self.img_vs0_no_light = load_image('beatstrike.assets.menu.player_select', 'vs_img_no_light.png', (100, 100))
        self.img_vs0_light = load_image('beatstrike.assets.menu.player_select', 'vs_img_light.png', (100, 100))

        # Calcula posições e Rects
        card_width, card_height = 450, 600
        self.hitbox_solo = pygame.Rect(435, 240, card_width, card_height)
        self.hitbox_vs = pygame.Rect(1035, 240, card_width, card_height)

        self.overlay_size = (1170, 720)
        self.overlay = pygame.Surface(self.overlay_size, pygame.SRCALPHA)
        self.overlay_rect = self.overlay.get_rect(topleft=(375, 180))
        pygame.draw.rect(
            surface=self.overlay,
            color=(0, 0, 0, 180),
            rect=pygame.Rect(0, 0, self.overlay_size[0], self.overlay_size[1]),
            border_radius=15
        )

        self.img_solo_rect = self.img_solo.get_rect(center=(660, 520))
        self.img_vs1_rect = self.img_vs1.get_rect(center=(1160, 480))
        self.img_vs2_rect = self.img_vs2.get_rect(center=(1340, 680))
        self.img_vs0_rect = self.img_vs0_light.get_rect(center=(1260, 580))

        # Texto
        self.color_normal = (150, 150, 150)
        self.color_selected = (255, 255, 255)

        self.text_solo_normal = self.font_title.render("Solo", True, self.color_normal)
        self.text_solo_selected = self.font_title.render("Solo", True, self.color_selected)
        self.text_solo_rect = self.text_solo_normal.get_rect(centerx=self.hitbox_solo.centerx, top=self.hitbox_solo.top + 30)

        self.text_vs_normal = self.font_title.render("Versus", True, self.color_normal)
        self.text_vs_selected = self.font_title.render("Versus", True, self.color_selected)
        self.text_vs_rect = self.text_vs_normal.get_rect(centerx=self.hitbox_vs.centerx, top=self.hitbox_vs.top + 30)

        # Botão de voltar
        self.back_button = BackButton(400, 195)

        self.clickable_elements = {
            'voltar': self.back_button.rect,
            'solo': self.hitbox_solo,
            'versus': self.hitbox_vs
        }

    def run(self, events, dt):
        self.mouse_pos = pygame.mouse.get_pos()

        for i, option_name in enumerate(self.options):
            if self.clickable_elements[option_name].collidepoint(self.mouse_pos):
                self.selected_index = i

        for event in events:
            if event.type == pygame.QUIT:
                return 'quit'

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: return 'menu'
                if event.key in (pygame.K_RIGHT, pygame.K_DOWN):
                    self.selected_index = (self.selected_index + 1) % len(self.options)
                if event.key in (pygame.K_LEFT, pygame.K_UP):
                    self.selected_index = (self.selected_index - 1) % len(self.options)
                if event.key == pygame.K_RETURN:
                    player_mode = self.options[self.selected_index]
                    if player_mode == "voltar": return 'menu'
                    if player_mode == "solo": return 'char_select', 1
                    if player_mode == "versus": return 'char_select', 2

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.back_button.check_click(event): return 'menu'
                if self.hitbox_solo.collidepoint(self.mouse_pos): return 'char_select', 1
                if self.hitbox_vs.collidepoint(self.mouse_pos): return 'char_select', 2

        self.bg.update(dt)
        self.bg.draw(self.screen, (0, 0))
        self.screen.blit(self.overlay, self.overlay_rect)
        pygame.draw.rect(self.screen, (234, 0, 255), self.overlay_rect, 3, border_radius=15)

        self.screen.blit(self.img_solo, self.img_solo_rect)
        if self.selected_index == 0:
            self.back_button.image = self.back_button.img_on
            self.back_button.draw(self.screen)
            pygame.draw.rect(self.screen, self.color_selected, self.back_button, 3, border_radius=15)
        else:
            self.back_button.image = self.back_button.img_off
            self.back_button.draw(self.screen)

        if self.selected_index == 1:
            pygame.draw.rect(self.screen, self.color_selected, self.hitbox_solo, 3, border_radius=15)
            self.screen.blit(self.text_solo_selected, self.text_solo_rect)
        else:
            self.screen.blit(self.text_solo_normal, self.text_solo_rect)

        self.screen.blit(self.img_vs1, self.img_vs1_rect)
        self.screen.blit(self.img_vs2, self.img_vs2_rect)

        if self.selected_index == 2:
            pygame.draw.rect(self.screen, self.color_selected, self.hitbox_vs, 3, border_radius=15)
            self.screen.blit(self.text_vs_selected, self.text_vs_rect)
            self.screen.blit(self.img_vs0_light, self.img_vs0_rect)
        else:
            self.screen.blit(self.text_vs_normal, self.text_vs_rect)
            self.screen.blit(self.img_vs0_no_light, self.img_vs0_rect)

        pygame.display.update()
        return 'player_select'
