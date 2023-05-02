#создай игру "Лабиринт"!
from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y =player_y
    def reset(self):
        window.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x >5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x <620:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y >5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y <420:
            self.rect.y += self.speed
         
class Enemy(GameSprite):
    direction = 'left'
    def update(self):
        if self.rect.x <=510:
            self.direction = 'right'
        if self.rect.x >= 630:
            self.direction = 'left'
        if self.direction == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Wall (sprite.Sprite):
    def __init__(self,c1,c2,c3,x,y,w,h):
        super().__init__()
        self.c1 = c1
        self.c2 = c2
        self.c3 = c3
        self.width = w
        self.height = h
        self.image = Surface((self.width,self.height))
        self.image.fill((c1,c2,c3))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw_wall(self):
        window.blit(self.image,(self.rect.x, self.rect.y))
    


window = display.set_mode((700,500))
display.set_caption("Лабиринт")
background = transform.scale(image.load("background.jpg"),(700,500))
game = True
finish = False
clock = time.Clock()
FPS = 120
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
kick = mixer.Sound('kick.ogg')
money = mixer.Sound('money.ogg')

player = Player('hero.png',30,400,5)
monster = Enemy('cyborg.png',640,300,3)
gold = GameSprite('treasure.png',580,420,0)

font.init()
font = font.Font(None,70)
lose = font.render('GAME OVER!', True,(0,0,0))
win = font.render('VICTORY', True,(0,255,0))

w1 = Wall(255,0,0,0,20,700,10)
w2 = Wall(255,0,0,100, 20,10,350)
w3 = Wall(255,0,0,10,480,510,10)
w4 = Wall(255,0,0,210,120,10,360)
w5 = Wall(255,0,0,315,20,10,370)
w6 = Wall(255,0,0,405,120,10,360)
w7 = Wall(255,0,0,510,120,10,360)

while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish != True:
       
        window.blit(background,(0,0))
        player.reset()
        player.update()
        monster.reset()
        monster.update()
        gold.reset()


    w1.draw_wall()
    w2.draw_wall()
    w3.draw_wall()
    w4.draw_wall()
    w5.draw_wall()
    w6.draw_wall()
    w7.draw_wall()

    if sprite.collide_rect(player,monster) or sprite.collide_rect(player,w1) or sprite.collide_rect(player,w2) or sprite.collide_rect(player,w3) or \
        sprite.collide_rect(player,w4) or sprite.collide_rect(player,w5) or sprite.collide_rect(player,w6) or sprite.collide_rect(player,w7):
        finish = True
        window.blit(lose,(200,200))
        kick.play()
    if sprite.collide_rect(player,gold):
        finish = True
        window.blit(win,(200,200))
        money.play()


    display.update()
    clock.tick(FPS)
