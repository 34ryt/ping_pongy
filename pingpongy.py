#Создай собственный Шутер!
# импорт модулей
from pygame import *
from random import randint
from time import time as tm
mixer.init()
# классы
class GameSprite(sprite.Sprite):
    def __init__(self, pl_image, pl_speed, pl_w, pl_h, pl_x, pl_y):
        super().__init__()
        self.image = transform.scale(image.load(pl_image), (pl_w, pl_h))
        self.speed = pl_speed
        self.rect = self.image.get_rect()
        self.rect.x = pl_x
        self.rect.y = pl_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 420:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 420:
            self.rect.y += self.speed
class Ball(GameSprite):
    def __init__(self, pl_image, pl_speed, pl_w, pl_h, pl_x, pl_y, speed_x, speed_y):
        super().__init__(pl_image, pl_speed, pl_w, pl_h, pl_x, pl_y)
        self.speed_x = speed_x
        self.speed_y = speed_y
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y < 0 or self.rect.y > 430:        
            self.speed_y *= -1
player1 = Player('canoe.png', 10, 65, 65, 50, 430)
player2 = Player('canoe.png', 10, 65, 65, 570, 10)
ball = Ball('tennis.png', 5, 65, 65, 50, 50, 5, 5)
# создание окна
window = display.set_mode((700, 500))
display.set_caption('Ping Pongy!')
# создание сцены
background = transform.scale(image.load('forest.jpg'), (700, 500))
# ИЦ
font.init()
font = font.Font(None, 70)
font1 = font.render('PLAYER 1 LOST ;(', True, (255, 0, 0))
font2 = font.render('PLAYER 2 LOST ;(', True, (255, 0, 0))
fps = 60
clock = time.Clock()
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        player1.update_l()
        player2.update_r()
        ball.update()
        window.blit(background, (0, 0))
        player1.reset()
        player2.reset()
        ball.reset()
        if sprite.collide_rect(ball, player1) or sprite.collide_rect(ball, player2):
            ball.speed_x *= -1
        if ball.rect.x <= 0:
            window.blit(font1, (170, 240))
        if ball.rect.x >= 700:
            window.blit(font2, (170, 240))
    display.update()
    clock.tick(fps)
