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
    def shoot(self):
        pass
    def fire(self):
        bullet = Bullet('bullet.png', 10, 10, 30, self.rect.centerx, self.rect.top)
        bullets.add(bullet)
class Ball(GameSprite):
    def update(self):
        pass
player1 = Player('canoe.png', 10, 65, 65, 50, 420)
player2 = Player('canoe.png', 10, 65, 65, 570, 50)
# создание окна
window = display.set_mode((700, 500))
display.set_caption('Ping Pongy!')
# создание сцены
background = transform.scale(image.load('forest.jpg'), (700, 500))
# ИЦ
font.init()
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
        window.blit(background, (0, 0))
        player1.reset()
        player2.reset()
    display.update()
    clock.tick(fps)