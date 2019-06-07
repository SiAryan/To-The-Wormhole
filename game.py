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

isJump = False
jumpCount = 10
run = True
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
        if keys[pygame.K_UP] and y > vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < screen_height - vel - height:
            y += vel
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




