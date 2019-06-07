import pygame
import objects
pygame.init()


screen_width = 1400
screen_height = 700
screen = pygame.display.set_mode([screen_width,screen_height])
pygame.display.set_caption("Asteroid belt")

x = 50
y = 50
width = 20
height = 30
vel = 15

screen_color = (255,255,255)
screen.fill(screen_color)
pygame.display.update()

left = False
right = False
walkCount = 0
isJump = False
jumpCount = 10
run = True

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')





while run:
    pygame.time.delay(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT] and x < screen_width- vel - width:
        x += vel
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel


    if not(isJump):
        #if keys[pygame.K_UP] and y > vel:
        #    y -= vel
        #if keys[pygame.K_DOWN] and y < screen_height - vel - height:
        #   y += vel
        if keys[pygame.K_SPACE]:
            isJump = True

    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg

            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10



    screen.fill([0,0,0])
    pygame.draw.rect(screen, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()




