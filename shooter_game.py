#Создай собственный Шутер!

from pygame import *
from random import randint

window = display.set_mode((700, 500))
display.set_caption('Шутер')
clock = time.Clock()
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
bullets_counter = 30
bullets = sprite.Group()
FPS = 60
background = transform.scale(image.load('galaxy.jpg'), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, lenght):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(width, lenght))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.width = width
        self.lenght = lenght
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed,width,lenght):
        super().__init__(player_image, player_x, player_y, player_speed, width,lenght)
    def update(self):
        if self.rect.y <= 5:
            self.kill()
        else:
            self.rect.y -= self.speed
class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, lenght):
        super().__init__(player_image, player_x, player_y, player_speed,width,lenght)
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_LEFT] and self.rect.x > 10:
            self.rect.x -= self.speed

        if keys_pressed[K_RIGHT] and self.rect.x < 610:
            self.rect.x += self.speed
lost = 0
class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, lenght):
        super().__init__(player_image, player_x, player_y, player_speed, width,lenght)
    def update(self):

        global lost

        if self.rect.y <= 450:
            self.rect.y += self.speed
        else:
            self.rect.x = randint(50, 610)
            self.speed = randint(1, 5)
            self.rect.y = 0
            lost = lost + 1



player = Player(('rocket.png'), 50, 420, 3, 75, 75)
enemy_group = sprite.Group()
for i in range(5):
    ufo = Enemy(('ufo.png'), randint(50, 610), 0, randint(1, 5), 75, 75)
    enemy_group.add(ufo)


game = True
finish = False
while game:
    
    for e in event.get():   
        if e.type == QUIT:
            game = False

    if finish != True:

        window.blit(background, (0, 0))
    
        clock.tick(FPS)

        player.reset()
        player.update()

        keys_pressed = key.get_pressed()
        

        enemy_group.draw(window)
        enemy_group.update()
        display.update()
