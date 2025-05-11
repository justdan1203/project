from pygame import *

display.set_caption("Shooter")
window = display.set_mode((700, 500))
clock = time.Clock()
FPS = 60

PLAYER_WALKSPEED = 1

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
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image, (self.x, self.y))

class Player(GameSprite):
    def __init__(self, image_name, x, y, width, height):
        super().__init__(image_name, x, y, width, height)

    def update(self):
        self.reset()
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w]:
            move(self, None, -PLAYER_WALKSPEED)
        if keys_pressed[K_s]:
            move(self, None, PLAYER_WALKSPEED)
        if keys_pressed[K_a]:
            move(self, -PLAYER_WALKSPEED, None)
        if keys_pressed[K_d]:
            move(self, PLAYER_WALKSPEED, None)
        

class WallHitbox(GameSprite):
    def __init__(self, image_name, x, y, width, height):
        super().__init__(image_name, x, y, width, height)

    def update(self):
        if sprite.collide_rect(self, Player):
            if Player.x + Player.width - self.x <= PLAYER_WALKSPEED:
                while Player.x + Player.width - self.x > 0:
                    move(Player, -1, None)
            if self.x + self.width - Player.x <= PLAYER_WALKSPEED:
                while self.x + self.width - Player.x > 0:
                    move(Player, 1, None)
            if Player.y + Player.height - self.y <= PLAYER_WALKSPEED:
                while Player.y + Player.height - self.y > 0:
                    move(Player, None, -1)
            if self.y + self.height - Player.y <= PLAYER_WALKSPEED:
                while self.y + self.height - Player.y > 0:
                    move(Player, None, 1)

class Enemy(GameSprite):
    def __init__(self, image_name, x, y, width, height):
        super().__init__(image_name, x, y, width, height)

#class Wall(GameSprite)

class Floor(GameSprite):
    def __init__(self, image_name, x, y, width, height):
        super().__init__(image_name, x, y, width, height)

    def update(self):
        self.reset()    

def InitiateBasicClass(ClassName, Objects):
    InitiatedObjects = []
    for i in range(len(Objects)):
        Object = ClassName(Objects[i][0], Objects[i][1], Objects[i][2], Objects[i][3], Objects[i][4])
        InitiatedObjects.append(Object)
    return InitiatedObjects
    
def MassUpdate(UpdateList):
    for i in UpdateList:
        i.update()

WallHitboxes = [
    ["wall.png", 100, 100, 50, 100],
    ["wall.png", 100, 200, 100, 50]
]

Floors = [
    ["floor.png", 150, 100, 50, 100]
]

Walls = []

background = GameSprite("background.png", 0, 0, 700, 500)  
Player = Player("player.png", 0, 0, 50, 50)

WallHitboxes = InitiateBasicClass(WallHitbox, WallHitboxes)
Floors = InitiateBasicClass(Floor, Floors)   



game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    
    
    background.reset()
    MassUpdate(Floors)
    Player.update()
    

    MassUpdate(WallHitboxes)
    

    display.update()