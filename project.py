from pygame import *

display.set_caption("Shooter")
window = display.set_mode((700, 500))
background = transform.scale(image.load("3.jpg"), (700, 500))
clock = time.Clock()
FPS = 60

PLAYER_WALKSPEED = 5


def move(model, x, y):
    if x != None:
        model.x += x
        model.rect.x += x
    if y != None:
        model.y += y
        model.rect.y += y

class GameSprite(sprite.Sprite):
    def __init__(self, image_name, x, y, width, height):
        super().__init__()
        self.x = x
        self.y = y
        self.image_name = image_name
        self.width = width
        self.height = height
        self.image = transform.scale(
            image.load(image_name),
            (width, height)
        ) 
        self.rect = self.image.get_rect()
    def reset(self):
        window.blit(self.image, (self.x, self.y))

class Player(GameSprite):
    def __init__(self, name, x, y, width, height):
        super().__init__(name, x, y, width, height)

    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w]:
            move(self, None, -PLAYER_WALKSPEED)
        if keys_pressed[K_d]:
            move(self, None, PLAYER_WALKSPEED)
        if keys_pressed[K_a]:
            move(self, -PLAYER_WALKSPEED, None)
        if keys_pressed[K_d]:
            move(self, PLAYER_WALKSPEED, None)
        self.reset()

class Wall(GameSprite):
    def __init__(self, name, x, y, width, height):
        super().__init__(name, x, y, width, height)

    def update(self):
        if sprite.collide_rect(self.rect, ''):
            if ''.x + ''.width - self.x <= PLAYER_WALKSPEED:
                while ''.x + ''.width - self.x <= 0
                    move('', -1, None)
            if self.x + self.width - ''.x <= PLAYER_WALKSPEED:
                while self.x + self.width - ''.x <= 0
                    move('', 1, None)
            if ''.y + ''.height - self.y <= PLAYER_WALKSPEED:
                while ''.y + ''.height - self.y <= 0
                    move('', None, -1)
            if self.y + self.height - ''.y <= PLAYER_WALKSPEED:
                while self.y + self.height - ''.y <= 0
                    move('', None, 1)
        self.reset()

class Enemy(GameSprite):
    def __init__(self, image_name, x, y, width, height):
        super().__init__()
        



game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()