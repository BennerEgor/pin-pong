from pygame import*

back = (200, 255, 255)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

game = True
finish = False
clock = time.Clock()
FPS = 60

#  часть другой программы


back = transform.scale(image.load('dinosaurs-seamless-pattern-for-kids--creative-vector-childish-background-v_1781425jpg_bw700-removebg-preview.png'), (win_width, win_height))

Player = True
run = True
racket1 = Player('png-clipart-cartoon-dinosaur-dracula-baby-mammal-cat-like-mammal-thumbnail-removebg-preview.png', 520,200,4,50,150)
racket2 = Player('pngtree-cartoon-style-of-a-female-triceratops-dinosaur-png-image_3587883-removebg-preview.png', 300,100,2,50,150)
ball = GameSprite('picture_of_the_day_16_psyche_1-removebg-preview.png', 200, 200, 4,ball_width,ball_height)


speed_x = 3
speed_y = 3

   
while run:
    for e in event.get():
        if e.type == QUIT :
                run = False
    

      

        if not finish:
            window.blit(back,(0,0))
            racket1.update_1()
            racket2.update_2()
            ball.rect.x += speed_x
            ball.rect.y += speed_y

            if sprite.collide_rect(racket1, ball) or (sprite.collide_rect(racket2, ball)):
                speed *= -1
            
        

            display.update()
            clock.tick(60)




class GameSprite(sprite.Sprite):
    def __init__(self, picture, x, y,width, height,  speed):
        super().__init__()
        self.image = transform.scale(image.load(picture), (width,height))
        self.speed = speed
        self.height = height
        self.width = width
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        main_win.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed






