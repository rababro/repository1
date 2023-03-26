from pygame import *
from random import randint

img_back = 'back.jpg'
ball = 'ball.png'
rocket = 'rocket.bmp'

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 90:
            self.rect.x += self.speed

win_width = 700
win_height = 500
display.set_caption('Ping-Pong')
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_back), (win_width, win_height))

finish = False
run = True

clock = time.Clock()
FPS = 60



while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    
    if not finish:
        window.blit(background, (0,0))
        rocket.draw(window)

    else:
        finish = False

   
    display.update()
    clock.tick(FPS)