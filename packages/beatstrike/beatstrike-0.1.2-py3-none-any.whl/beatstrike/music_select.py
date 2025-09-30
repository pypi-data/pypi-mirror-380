import pygame
import importlib.resources
import json
from beatstrike.button import BackButton

class MusicSelect:
    def __init__(self, screen, background):
        self.screen = screen
        self.bg = background
        self.music = ['All The Things She Said', 'Amiga da Minha Mulher', 'Beat It', 'Enemy',
                      'Hohoemi no Bakudan', 'Ichirin no Hana', 'Rebel Yell', 'Runaway (U & I)', 'Pompeii']
        self.options = [self.music, 'voltar', 'selecionar']
        self.music_info = {}
        self.mouse_pos = (0, 0)

        self.selected_index_menu = 0
        self.selected_index_music = 0

        # Cores
        self.color_green_normal = (90, 100, 90)
        self.color_green_selected = (35, 254, 37)
        self.color_white = (255, 255, 255)
        self.color_red = (255, 10, 50)
        self.color_blue = (0, 150, 255)
        self.color_normal = (200, 200, 200)
        self.color_selected = (255, 255, 0)

        with importlib.resources.path("beatstrike.assets.fonts", "PressStart2P-Regular.ttf") as p:
            self.font_music = pygame.font.Font(str(p), 28)
        with importlib.resources.path("beatstrike.assets.fonts", "Determination.ttf") as p:
            self.font_select = pygame.font.Font(str(p), 84)
        with importlib.resources.path("beatstrike.assets.fonts", "BebasNeue-Regular.ttf") as p:
            self.font_info = pygame.font.Font(str(p), 64)
            self.font_artist = pygame.font.Font(str(p), 52)
            self.font_year = pygame.font.Font(str(p), 32)

        # Botão SELECIONAR
        self.select_button_normal = self.font_select.render("SELECIONAR", True, self.color_green_normal)
        self.select_button_selected = self.font_select.render("SELECIONAR", True, self.color_green_selected)
        self.select_button_rect = self.select_button_normal.get_rect(center=(1440, 530))

        # Overlay
        self.overlay_music_size = (700, 800)
        self.overlay_music = pygame.Surface(self.overlay_music_size, pygame.SRCALPHA)
        self.overlay_music_rect = self.overlay_music.get_rect(topleft=(100, 140))
        self.overlay_details_size = (920, 290)
        self.overlay_details = pygame.Surface(self.overlay_details_size, pygame.SRCALPHA)
        self.overlay_details_rect = self.overlay_details.get_rect(topleft=(900, 140))
        pygame.draw.rect(self.overlay_music, (0, 0, 0, 180), self.overlay_music.get_rect(), border_radius=15)
        pygame.draw.rect(self.overlay_details, (0, 0, 0, 180), self.overlay_details.get_rect(), border_radius=15)

        with importlib.resources.path("beatstrike.assets.menu.music_select", "star.png") as p:
            self.star_img = pygame.image.load(str(p)).convert_alpha()
            self.star_img = pygame.transform.scale(self.star_img, (100, 100))
        with importlib.resources.path("beatstrike.assets.menu.music_select", "star_empty.png") as p:
            self.star_empty_img = pygame.image.load(str(p)).convert_alpha()
            self.star_empty_img = pygame.transform.scale(self.star_empty_img, (100, 100))

        # JSON de música
        with importlib.resources.open_text("beatstrike.assets.menu.music_select", "music_info.json", encoding="utf-8") as f:
            self.music_info_bruto = json.load(f)
        self._load_music_info()

        # Back button
        self.back_button = BackButton(1120, 530, True)
    def _load_music_info(self):
        y_music = 160
        for music, info in self.music_info_bruto.items():
            self.music_info[music] = info.copy()

            img_name = f"{music}.png"
            with importlib.resources.path("beatstrike.assets.menu.music_select", img_name) as img_path:
                self.music_info[music]['image_path'] = str(img_path)

            self.music_info[music]['text_info'] = self.font_info.render(music, True, self.color_white)
            self.music_info[music]['text_normal'] = self.font_music.render(music, True, self.color_normal)
            self.music_info[music]['text_selected'] = self.font_music.render(music, True, self.color_selected)
            self.music_info[music]['artist'] = self.font_artist.render(info['artist'], True, self.color_normal)
            self.music_info[music]['year'] = self.font_year.render(f"Ano: {info['year']}", True, self.color_blue)
            self.music_info[music]['time'] = self.font_year.render(f"Duração: {info['time']}", True, self.color_red)

            rect = self.music_info[music]['text_selected'].get_rect()
            rect.topleft = (120, y_music)
            self.music_info[music]['rect'] = rect
            y_music += 60

    def _draw_info_music(self, music):
        info = self.music_info[music]

        if info['image_path']:
            img = pygame.image.load(info['image_path']).convert_alpha()
            img = pygame.transform.scale(img, (250, 250))
            self.screen.blit(img, (920, 160))

        self.screen.blit(info['text_info'], (1190, 150))
        self.screen.blit(info['artist'], (1190, 205))
        self.screen.blit(info['year'], (1190, 260))
        self.screen.blit(info['time'], (1190, 295))

        difficulty = info['difficulty']
        max_difficulty = 3
        x_star = 1180
        y_star = 320
        for _ in range(difficulty):
            self.screen.blit(self.star_img, (x_star, y_star))
            x_star += 120
        for _ in range(max_difficulty - difficulty):
            self.screen.blit(self.star_empty_img, (x_star, y_star))
            x_star += 120

    def run(self, events, dt):
        self.mouse_pos = pygame.mouse.get_pos()

        for i, music in enumerate(self.music):
            if self.music_info[music]['rect'].collidepoint(self.mouse_pos):
                self.selected_index_music = i

        for event in events:
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: return 'char_select'
                if event.key == pygame.K_UP and self.selected_index_menu == 0:
                    self.selected_index_music = (self.selected_index_music - 1) % len(self.music)
                if event.key == pygame.K_DOWN and self.selected_index_menu == 0:
                    self.selected_index_music = (self.selected_index_music + 1) % len(self.music)
                if event.key == pygame.K_RIGHT:
                    self.selected_index_menu = (self.selected_index_menu + 1) % len(self.options)
                if event.key == pygame.K_LEFT:
                    self.selected_index_menu = (self.selected_index_menu - 1) % len(self.options)
                if event.key == pygame.K_RETURN:
                    if self.selected_index_menu == 1: return 'char_select'
                    elif self.selected_index_menu == 2: return 'bg_select', self.music[self.selected_index_music]

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.back_button.check_click(event): return 'char_select'
                if self.select_button_rect.collidepoint(self.mouse_pos):
                    return 'bg_select', self.music[self.selected_index_music]

            if self.back_button.check_hover(self.mouse_pos): self.selected_index_menu = 1
            if self.select_button_rect.collidepoint(self.mouse_pos): self.selected_index_menu = 2

        self.bg.update(dt)
        self.bg.draw(self.screen, (0, 0))
        self.screen.blit(self.overlay_music, self.overlay_music_rect)
        self.screen.blit(self.overlay_details, self.overlay_details_rect)

        pygame.draw.rect(self.screen, (255, 240, 31), self.overlay_music_rect, 2, border_radius=15)
        pygame.draw.rect(self.screen, (255, 49, 49), self.overlay_details_rect, 3, border_radius=15)

        for i, music in enumerate(self.music):
            info = self.music_info[music]
            text = info['text_selected'] if i == self.selected_index_music and self.selected_index_menu == 0 else info['text_normal']
            self.screen.blit(text, info['rect'])
            if info['rect'].collidepoint(self.mouse_pos):
                self.selected_index_music = i
                self.selected_index_menu = 0

        self._draw_info_music(self.music[self.selected_index_music])

        if self.selected_index_menu == 1:
            pygame.draw.rect(self.screen, self.color_white, self.back_button, 3, border_radius=15)
            self.back_button.image = self.back_button.img_on
            self.back_button.draw(self.screen)
            self.screen.blit(self.select_button_normal, self.select_button_rect)
        elif self.selected_index_menu == 2:
            self.back_button.image = self.back_button.img_off
            self.back_button.draw(self.screen)
            self.screen.blit(self.select_button_selected, self.select_button_rect)
        else:
            self.back_button.image = self.back_button.img_off
            self.back_button.draw(self.screen)
            self.screen.blit(self.select_button_normal, self.select_button_rect)

        pygame.display.update()
        return 'music_select'
