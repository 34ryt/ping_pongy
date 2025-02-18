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
        if keys_pressed[K_DOWN] and self.rect.y < 920:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 920:
            self.rect.y += self.speed
class Ball(GameSprite):
    def __init__(self, pl_image, pl_speed, pl_w, pl_h, pl_x, pl_y, speed_x, speed_y):
        super().__init__(pl_image, pl_speed, pl_w, pl_h, pl_x, pl_y)
        self.speed_x = speed_x
        self.speed_y = speed_y
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.y < 0 or self.rect.y > 930:        
            self.speed_y *= -1
    def push(self, paddle):
        height = paddle.rect.bottom-paddle.rect.top
        if self.rect.centery <= paddle.rect.top + height*2/5:
            self.speed_y = -5
        elif self.rect.centery <= paddle.rect.top + height*3/5:
            self.speed_y = -3
        elif self.rect.centery <= paddle.rect.top + height*4/5:
            self.speed_y = 0
        elif self.rect.centery <= paddle.rect.top + height*5/5:
            self.speed_y = 3
        else:
            self.speed_y = 5
player1 = Player('bat.png', 10, 65, 65, 60, 430)
player2 = Player('bat.png', 10, 65, 65, 870, 10)
ball = Ball('tennis.png', 5, 65, 65, 500, 500, 5, 5)
player1_win = 0
player2_win = 0
# создание окна
window = display.set_mode((1000, 1000))
display.set_caption('Ping Pongy!')
# создание сцены
background = transform.scale(image.load('forest.jpg'), (1000, 1000))
# ИЦ
font.init()
font = font.Font(None, 70)
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
        font1 = font.render(str(player1_win), True, (255, 0, 0))
        font2 = font.render(str(player2_win), True, (0, 255, 0))
        font3 = font.render('YOU LOSE ;(', True, (255, 0, 0))
        font4 = font.render('YOU LOSE ;(', True, (0, 255, 0))
        window.blit(font1, (10, 10))
        window.blit(font2, (960, 10))
        player1.reset()
        player2.reset()
        ball.reset()
        if sprite.collide_rect(ball, player1):
            ball.speed_x *= -1
            ball.push(player1)
        if sprite.collide_rect(ball, player2):
            ball.speed_x *= -1
            ball.push(player2)
        if ball.rect.x <= 0:
            player1_win += 1
            ball.speed_x *= -1
            ball.rect.x = 500
            ball.rect.y = 500
        if ball.rect.x >= 1000:
            player2_win += 1
            ball.speed_x *= -1
            ball.rect.x = 500
            ball.rect.y = 500
        if player1_win >= 10:
            finish = True
            ball.kill()
            window.blit(font4, (400, 500))
        if player2_win >= 10:
            finish = True
            ball.kill()
            window.blit(font3, (400, 500))
    display.update()
    clock.tick(fps)
