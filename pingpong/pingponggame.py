from pygame import*

#CLASSES
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        sprite.Sprite.__init__(self)
        #Properties
        self.image = transform.scale(image.load(player_image), (size_x, size_y))    
        self.speed = player_speed
        #Rectangle
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        
    def reset(self):
        #draw the character on the window
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win-height - 80:
            self.rect.y += self.speed

    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win-height - 80:
            self.rect.y += self.speed

#game scene
back = (200, 213, 222)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

#Game loop
game = True
finish = False
clock = time.Clock()
FPS = 60

racket1 = Player("racket.png", 30, 200,4, 50,150)
racket2 = Player("racket.png", 30, 200,4, 50,150)
ball = GameSprite("tennis_ball.png", 200, 200, 4, 50, 50)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()