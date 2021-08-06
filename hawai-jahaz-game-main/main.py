import pygame
from pygame.locals import \
    (K_UP,
     K_DOWN,
     K_LEFT,
     K_RIGHT,
     QUIT,
     K_ESCAPE,
     KEYDOWN)

#   screen - player - left to right (left,right,up and down)
#   object - left to right
#   player don't move out of the screen
#   game end - quit / player hit by obstacle


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

running = True


# Player class which represent 2d character
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surface = pygame.Surface((75, 25))
        self.surface.fill((255, 255, 255))
        self.rect = self.surface.get_rect()

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)


pygame.init()

running = True
player = Player()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.type == K_ESCAPE:
                running = False
        elif event.type == QUIT:
            running = False

        screen.blit(player.surface, player.rect)

        pressed_keys = pygame.key.get_pressed()

        player.update(pressed_keys)

        screen.fill((0, 0, 0))
        pygame.display.flip()
        # pygame.display.update()
