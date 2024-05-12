import pygame
import random
import sys
class SoundManager:
    def __init__(self):
        self.sound_on = True
        pygame.mixer.music.load('sounds/background.mp3')
        pygame.mixer.music.play(-1)
    def toggle_sound(self):
        self.sound_on = not self.sound_on
        if self.sound_on:
            pygame.mixer.unpause()
        else:
            pygame.mixer.pause()
class GameOver:
    def __init__(self):
        self.game_over_sound = pygame.mixer.Sound('sounds/game_over.mp3')
    def play_sound(self):
        self.game_over_sound.play()
class Menu:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        self.main_menu_background = pygame.image.load('images/background.png').convert()
        self.main_menu_background = pygame.transform.scale(self.main_menu_background, (self.width, self.height))
        self.start_button_image = pygame.image.load('images/start.png')
        self.start_button_image = pygame.transform.scale(self.start_button_image, (200, 100))
        self.start_button_rect = self.start_button_image.get_rect(center=(self.width // 2, self.height // 2 - 75))
        self.about_button_image = pygame.image.load('images/about.png')
        self.about_button_image = pygame.transform.scale(self.about_button_image, (200, 100))
        self.about_button_rect = self.about_button_image.get_rect(center=(self.width // 2, self.height // 2 + 75))
        self.shop_button_image = pygame.image.load('images/shop.png')
        self.shop_button_image = pygame.transform.scale(self.shop_button_image, (200, 100))
        self.shop_button_rect = self.shop_button_image.get_rect(center=(self.width // 2, self.height // 2 + 225))
    def draw_menu(self):
        self.screen.blit(self.main_menu_background, (0, 0))
        self.screen.blit(self.start_button_image, self.start_button_rect)
        self.screen.blit(self.about_button_image, self.about_button_rect)
        self.screen.blit(self.shop_button_image, self.shop_button_rect)
class PlayGame:
    def __init__(self, screen, width, height):
        self.screen = screen
        self.width = width
        self.height = height
        # Add other game initialization code here
    def update_game(self):
        # Add game update logic here
        pass
class Swimmer:
    def __init__(self, image_path, width, height):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
    def move(self, dx, dy):
        self.rect.x += dx
        self.rect.y += dy
class Shark:
    def __init__(self, image_paths, width, height):
        self.images = [pygame.image.load(path) for path in image_paths]
        self.images = [pygame.transform.scale(image, (width, height)) for image in self.images]
        self.rect = self.images[0].get_rect()
    def move(self, dy):
        self.rect.y += dy
class Coin:
    def __init__(self, image_path, width, height):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
    def move(self, dy):
        self.rect.y += dy
class Potion:
    def __init__(self, image_path, width, height):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = self.image.get_rect()
    def move(self, dy):
        self.rect.y += dy
class Game:
    def __init__(self):
        # Initialize Pygame
        pygame.init()
        # Screen size
        self.width = 800
        self.height = 600
        self.screen_size = (self.width, self.height)
        self.screen = pygame.display.set_mode(self.screen_size)
        pygame.display.set_caption('Defying Shark')
        # Initialize sound manager
        self.sound_manager = SoundManager()
        # Initialize game over handler
        self.game_over_handler = GameOver()
        # Initialize menu
        self.menu = Menu(self.screen, self.width, self.height)
        # Initialize game objects
        self.play_game = PlayGame(self.screen, self.width, self.height)
        self.swimmer = Swimmer('images/perenang.png', self.width // 5, self.height // 5)
        self.shark = Shark(['images/hiu1.png', 'images/hiu2.png', 'images/hiu3.png'], self.width // 2, self.height // 2)
        self.coin = Coin('images/koin.png', self.width // 4, self.height // 4)
        self.potion = Potion('images/ramuan.png', self.width // 12, self.height // 12)
        # Game variables
        self.game_over = False
        self.menu_active = True
        self.about_active = False
    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            if self.play_game.game_over:
                self.game_over.draw_game_over_screen()
            elif self.play_game.menu_active:
                self.menu.draw_menu()
            else:
                self.play_game.update_game()
            pygame.display.flip()
            pygame.time.Clock().tick(60)
        pygame.quit()
        sys.exit()
if __name__ == "__main__":
    game = Game()
    game.run()

