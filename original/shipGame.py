import pygame

pygame.init()
win_dimensions = (1000, 600)
bg_origin = (-460, -480)
win = pygame.display.set_mode(win_dimensions)
pygame.display.set_caption("Space Shuttle")
bg = pygame.image.load('bg.png')
char = pygame.image.load('shuttle2.png')
clock = pygame.time.Clock()



class player(object):
    def __init__(self, x, y, width, height, speed):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = speed

    def move(self, keys):
        if self.y >= win_dimensions[1] - 500:
            if keys[pygame.K_UP]:
                self.y -= self.speed
        if  self.y < win_dimensions[1] - 52:
            if keys[pygame.K_DOWN]:
                self.y += self.speed
        if self.x <= win_dimensions[0] - self.width - 10:
            if keys[pygame.K_RIGHT]:
                self.x += self.speed
        if self.x >= 10:
            if keys[pygame.K_LEFT]:
                self.x -= self.speed


    def draw(self, win):
        win.blit(char, (self.x, self.y))


def drawGamewindow(player):
    #win.blit(bg, bg_origin)  # Fills the screen with black
    win.fill((0,0,0))
    player.draw(win)
    #pygame.draw.rect(win, (255, 0, 0), (player.x, player.y, player.width, player.height))
    pygame.display.update()
    #pygame.display.flip()


run = True

ship = player(474, 500, 52, 52, 10)

while run:
    clock.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    ship.move(pygame.key.get_pressed())


    drawGamewindow(ship)



