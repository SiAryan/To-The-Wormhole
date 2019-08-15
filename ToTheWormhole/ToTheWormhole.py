import math, random, pygame
from os.path import abspath, dirname
from pygame import *
basePath = abspath(dirname(__file__))
imagePath = basePath + '/images/ToTheWormhole/'
soundsPath = basePath + '/sounds/ToTheWormhole/'
fontsPath = basePath + '/fonts/ToTheWormhole/'
FONT = fontsPath + 'ToTheWormhole.ttf'

WHITE = (255, 255, 255)
GREEN = (78, 255, 87)
YELLOW = (241, 255, 0)
BLUE = (80, 255, 239)
PURPLE = (203, 0, 255)
RED = (237, 28, 36)

screenSize = (1000, 600)
screen = pygame.display.set_mode(screenSize)

bgOrigin = (-460, 0)
FPS = 60

class Asteroids(pygame.sprite.Sprite):
    def __init__(self):
        self.image = pygame.image.load(imagePath + 'asteroid.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (70, 70))
        self.rect = self.image.get_rect()
        self.num = 4
        self.asteroids = []
        self.asteroids_x = []
    def generate(self):
        for i in range(self.num):
            self.rect.x = random.randrange(700, 1100)
            self.rect.y = random.randrange(-300, 100)
            self.velocity = random.randrange(3,7)
            self.asteroids.append([self.rect.x, self.rect.y, self.velocity])

    def fall(self, screen):
        for i in self.asteroids:
            self.asteroids_x.append(i[0])
        for i in self.asteroids:
            i[0] -= i[2]
            i[1] += i[2]
            screen.blit(self.image, (i[0], i[1]))

            if i[0] <= 0 or i[1] >= 600:
                self.asteroids.remove(i)
                self.rect.x = random.randrange(700, 1100)
                self.rect.y = random.randrange(-300, 100)
                self.velocity = random.randrange(3, 7)
                self.asteroids.append([self.rect.x, self.rect.y, self.velocity])

    def destroy(self, i):
        self.asteroids.remove(i)
        self.rect.x = random.randrange(700, 1100)
        self.rect.y = random.randrange(-300, 100)
        self.velocity = random.randrange(3, 7)
        self.asteroids.append([self.rect.x, self.rect.y, self.velocity])

class score(object):
    def __init__(self):
        self.counter = 0
        self.playerScore = 0
        self.showOver = True
        self.livesImage = pygame.image.load(imagePath + 'ship1.png').convert_alpha()
        self.livesImage = pygame.transform.scale(self.livesImage, (30,30))
        self.livesRect = self.livesImage.get_rect(topleft=(50, 5))
        self.playerLives = 3
        self.scoreText = Text(FONT, 25, 'Score: ' + str(self.playerScore), WHITE, 820, 10)
        self.livesText = Text(FONT, 25, 'Lives: ', WHITE, 5, 10)
    def displayScore(self, screen):
        self.scoreText = Text(FONT, 25, 'Score: ' + str(self.playerScore), WHITE, 820, 10)
        self.scoreText.draw(screen)
        #pygame.display.update()

    def displayLives(self, screen):
        self.livesText.draw(screen)
        self.livesRect = self.livesImage.get_rect(topleft=(100, 5))
        for i in range(self.playerLives):
            screen.blit(self.livesImage, self.livesRect)
            self.livesRect.x += 31
    def gameOver(self, game):
        self.scoreText = Text(FONT, 50, 'Score: ' + str(self.playerScore), WHITE, 380, 200)
        game.screen.blit(game.background, bgOrigin)
        self.scoreText.draw(game.screen)
        pygame.display.flip()
        while self.showOver:
            print(self.counter)
            self.counter+=1
            if self.counter >= 200000:
                for event in pygame.event.get():
                    if event.type == KEYDOWN:
                        self.counter = 0
                        self.showOver = False
                        return True

                    elif event.type == pygame.QUIT:
                        self.counter = 0
                        game.run1 = False
                        self.showOver = False
                        return False

class player(pygame.sprite.Sprite):
    def __init__(self):
        self.image1 = pygame.image.load(imagePath + 'ship1.png').convert_alpha()
        self.image2 = pygame.image.load(imagePath + 'ship2.png').convert_alpha()
        self.Bimage1 = pygame.image.load(imagePath + 'Bship1.png').convert_alpha()
        self.Bimage2 = pygame.image.load(imagePath + 'Bship2.png').convert_alpha()
        self.rect = self.image1.get_rect(topleft=(474, 515))
        self.speed = 5
        self.flash = False
        self.counter = 0
        self.counter2 = 0

    def move(self, keys):
        if self.rect.x <= screenSize[0]-self.rect.width-5:
            if keys[pygame.K_RIGHT]:
                self.rect.x += self.speed

        if self.rect.x >= 5:
            if keys[pygame.K_LEFT]:
                self.rect.x -= self.speed

        if self.rect.y >= 150:
            if keys[pygame.K_UP]:
                self.rect.y -= self.speed

        if self.rect.y <= 540:
            if keys[pygame.K_DOWN]:
                self.rect.y += self.speed

        position = [self.rect.x + self.rect.width/2 - 2, self.rect.y - 15]
        return position

    def draw(self, screen ,cond, keys):
        if not self.flash:
            self.counter = 0
            if (keys[pygame.K_UP]):
                if cond:
                    screen.blit(self.Bimage1, self.rect)
                if not cond:
                    screen.blit(self.Bimage2, self.rect)

            if not (keys[pygame.K_UP]):
                if cond:
                    screen.blit(self.image1, self.rect)
                if not cond:
                    screen.blit(self.image2, self.rect)
        if self.flash:
            self.counter +=1
            if self.counter > 15 and self.counter <= 30 or self.counter > 45 and self.counter <=60 :
                if (keys[pygame.K_UP]):
                    if cond:
                        screen.blit(self.Bimage1, self.rect)
                    if not cond:
                        screen.blit(self.Bimage2, self.rect)

                if not (keys[pygame.K_UP]):
                    if cond:
                        screen.blit(self.image1, self.rect)
                    if not cond:
                        screen.blit(self.image2, self.rect)

            if self.counter > 60:
                self.flash = False

    def kill(self, Game, score):
        Game.run2 = score.gameOver(Game)
        Game.run1 = False

class particle(pygame.sprite.Sprite):
    def __init__(self):
        self.image1 = pygame.image.load(imagePath + 'particle3.png').convert_alpha()
        self.image2 = pygame.image.load(imagePath + 'particle1.png').convert_alpha()
        self.image3 = pygame.image.load(imagePath + 'particle2.png').convert_alpha()
        self.images = [self.image1, self.image2, self.image3]
        self.num = 30
        self.speed = 1
        self.particles1 = []
        self.particles2 = []
        self.particles3 = []

    def generate(self):
        for i in range(self.num):
            self.x = random.randrange(0, screenSize[0])
            self.y = random.randrange(0, screenSize[1])
            self.particles1.append([self.x, self.y])

        for i in range(self.num):
            self.x = random.randrange(0, screenSize[0])
            self.y = random.randrange(0, screenSize[1])
            self.particles2.append([self.x, self.y])

        for i in range(self.num):
            self.x = random.randrange(0, screenSize[0])
            self.y = random.randrange(0, screenSize[1])
            self.particles3.append([self.x, self.y])

    def fall(self, screen):
        for i in self.particles1:
            i[1] += self.speed

            screen.blit(self.image1, i)
            if i[1] > screenSize[1]:
                i[1] = random.randrange(-50, -5)

        for i in self.particles2:
            i[1] += self.speed

            screen.blit(self.image2, i)
            if i[1] > screenSize[1]:
                i[1] = random.randrange(-50, -5)

        for i in self.particles3:
            i[1] += self.speed

            screen.blit(self.image3, i)
            if i[1] > screenSize[1]:
                i[1] = random.randrange(-50, -5)

class Bullets(pygame.sprite.Sprite):
    def __init__(self, player):
        self.image1 = pygame.image.load(imagePath + 'laser.png').convert_alpha()
        self.image2 = pygame.image.load(imagePath + 'enemylaser.png').convert_alpha()
        self.Beam = []
        self.velocity = 9
        self.playerRect = self.image1.get_rect(topleft=(player.rect.x +
                                                    player.rect.width / 2 - 2, player.rect.y - 15))

    def Fire(self, screen, keys, run, position):
        if keys[pygame.K_SPACE] and run == False:
            run = True
            self.playerRect.x = position[0]
            self.playerRect.y = position[1]

        if run:
            screen.blit(self.image1, self.playerRect)
            self.playerRect.y -= self.velocity
            if self.playerRect.y < 0:
                run = False

        return run, self.playerRect

    def Quickfire(self, screen, keys, position, refresh, player):
        if keys[pygame.K_SPACE] and refresh > 1 and not player.flash:

            self.Beam.append(position)
            refresh = 0


        for i in self.Beam:
            screen.blit(self.image1, i)
            i[1] -= self.velocity
            if i[1] < 0:
                self.Beam.remove(i)

        return refresh

    def kill(self, i):
        self.Beam.remove(i)

class enemies(pygame.sprite.Sprite):
    def __init__(self):
        self.velocity = 7
        self.image1 = pygame.image.load(imagePath + 'enemy1_1.png').convert_alpha()
        self.image1 = pygame.transform.scale(self.image1, (50, 50))
        self.image2 = pygame.image.load(imagePath + 'enemy2_1.png')
        self.image2 = pygame.transform.scale(self.image2, (50, 50))
        self.image3 = pygame.image.load(imagePath + 'enemy3_1.png')
        self.image3 = pygame.transform.scale(self.image3, (50, 50))
        self.rect = self.image1.get_rect()
        self.oneNum = 5
        self.Enemies = []
        self.Enemies_x = []
        self.images = [self.image1, self.image2, self.image3]
        self.rightEdge = False
        self.generated = False

    def randomGen(self):
        width = 0
        if len(self.Enemies) != self.oneNum:
            for i in range(self.oneNum):
                self.x = random.randrange(0 + width, 200 + width - 50)
                self.y = random.randrange(-100, -15)
                if self.x not in self.Enemies_x:
                    self.Enemies.append([self.x, self.y])
                    self.Enemies_x.append(self.x)
                width += 200

    def randomFall(self, screen):

        for j in self.Enemies:
            self.Enemies_x.append(j[0])
        for i in self.Enemies:
            screen.blit(self.image1, i)
            if i[1] < screenSize[1]:
                i[1] += self.velocity

            if i[1] >= screenSize[1]:
                i[1] = random.randrange(-100, -15)
                i[0] = random.randrange(0, screenSize[0])


    def Begin(self, screen):
        self.randomFall(screen)



    def kill(self, i):
        if i in self.Enemies:
            self.Enemies.remove(i)

        if len(self.Enemies) <= self.oneNum:
            self.x = random.randrange(0 , screenSize[0] - 55)
            self.y = random.randrange(-100, -15)
            self.Enemies.append([self.x, self.y])

class explode(pygame.sprite.Sprite):
    def __init__(self):
        self.image1 = pygame.image.load(imagePath + 'explosionpurple.png').convert_alpha()
        self.image1 = pygame.transform.scale(self.image1, (50, 50))
        self.image2 = pygame.image.load(imagePath + 'explosionblue.png').convert_alpha()
        self.image2 = pygame.transform.scale(self.image2, (50, 50))
        self.image3 = pygame.image.load(imagePath + 'explosiongreen.png').convert_alpha()
        self.image3 = pygame.transform.scale(self.image3, (50, 50))
        self.rect = self.image1.get_rect()
        self.refresh = 0
        self.explode = False

    def showExplosion(self, screen, i):
        if self.explode:
            if self.refresh <= 10:
                screen.blit(self.image1, i)
            if self.refresh <= 20 and self.refresh >= 10:
                screen.blit(pygame.transform.scale(self.image1, (64, 64)), (i.x - 7, i.y - 7))

            if self.refresh > 20:
                self.explode = False
        self.refresh += 1

    def hit(self, enemy, bullets, player, screen, game, score, asteroids):
        for i in asteroids.asteroids:
            for j in bullets.Beam:
                if (j[0] >= i[0]-5 and j[0] <= i[0] + 70) and (j[1] >= i[1] and j[1] <= i[1] + 70):
                    self.rect.x = i[0]
                    self.rect.y = i[1]
                    self.explode = True
                    self.refresh = 0
                    asteroids.destroy(i)
                    bullets.kill(j)

        for i in enemy.Enemies:
            for j in bullets.Beam:
                if (j[0] >= i[0]-5 and j[0] <= i[0] + 50) and (j[1] >= i[1] and j[1] <= i[1] + 50):
                    self.rect.x = i[0]
                    self.rect.y = i[1]
                    self.explode = True
                    self.refresh = 0
                    enemy.kill(i)
                    bullets.kill(j)
                    score.playerScore += 1
        for i in enemy.Enemies:
            if (player.rect.x >= i[0]-50 and player.rect.x <= i[0] + 50) and \
                    (player.rect.y >= i[1] and  player.rect.y <= i[1] + 50):
                score.playerLives -= 1
                player.flash = True
                if score.playerLives <= 0:
                    player.kill(game, score)
                self.rect.x = i[0]
                self.rect.y = i[1]
                self.explode = True
                self.refresh = 0
                enemy.kill(i)
        for i in asteroids.asteroids:
            if (player.rect.x >= i[0]-70 and player.rect.x <= i[0] + 70) and \
                    (player.rect.y >= i[1] and  player.rect.y <= i[1] + 70):

                score.playerLives -= 1
                player.flash = True
                if score.playerLives <= 0:
                    player.kill(game, score)
                self.rect.x = i[0]
                self.rect.y = i[1]
                self.explode = True
                self.refresh = 0
                asteroids.asteroids.remove(i)

        self.showExplosion(screen, self.rect)

class Text(object):
    def __init__(self, textFont, size, message, color, xpos, ypos):
        self.font = font.Font(textFont, size)
        self.surface = self.font.render(message, True, color)
        self.rect = self.surface.get_rect(topleft=(xpos, ypos))

    def draw(self, surface):
        surface.blit(self.surface, self.rect)

class ToTheWormhole(object):
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.time = pygame.time.get_ticks()
        self.caption = pygame.display.set_caption("To The Wormhole")
        self.screen = screen
        self.background = pygame.image.load(imagePath + 'bg.png').convert_alpha()
        self.cond = True
        self.titleText = Text(FONT, 50, 'To The Wormhole', WHITE, 240, 155)
        self.titleText2 = Text(FONT, 25, 'Press any key to continue', WHITE,
                               290, 225)
        self.framerate = self.clock.get_fps()
        self.run1 = True
        self.run2 = True
        self.gameOver = False
        self.frameText = Text(FONT, 25, str(self.time), WHITE, 20, 200)
        ship = player()
        Score = score()
        asteroids = Asteroids()
        asteroids.generate()
        dust = particle()
        enemy = enemies()
        enemy.randomGen()
        bullet = Bullets(ship)
        dust.generate()
        hit = explode()
        refreshes = 0
        refresh = 1000

    def startScreen(self):

        self.run2 = True
        particles = particle()
        particles.generate()
        ship = player()
        while self.run2:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run2 = False
                if event.type == KEYDOWN:
                    self.run1 = True
                    self.runGame()

            screen.blit(self.background, bgOrigin)
            particles.fall(self.screen)
            screen.blit(pygame.transform.scale(ship.image1, (65, 59)), (460, 340))

            self.titleText.draw(self.screen)
            self.titleText2.draw(self.screen)

            pygame.display.flip()
            print(self.framerate)

    def runGame(self):

        ship = player()
        Score = score()
        asteroids = Asteroids()
        asteroids.generate()
        dust = particle()
        enemy = enemies()
        enemy.randomGen()
        bullet = Bullets(ship)
        dust.generate()
        hit = explode()
        refreshes = 0
        refresh = 1000
        run2 = False
        while self.run1:
            refreshes += 1
            self.clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run1 = False
                    self.run2 = False


            keys = pygame.key.get_pressed()

            self.screen.blit(self.background, bgOrigin)
            dust.fall(self.screen)
            asteroids.fall(self.screen)
            enemy.Begin(self.screen)
            position = ship.move(keys)
            ship.draw(self.screen, self.cond, keys)
            # run2, bullet = bullet.Fire(self.screen, keys, run2,
            #                            (ship.rect.x + ship.rect.width / 2 - 2, ship.rect.y - 15))

            if refreshes == 10:
                self.cond = not self.cond
                refreshes = 0
                refresh += 1

            hit.hit(enemy, bullet, ship, self.screen, self, Score, asteroids)
            refresh = bullet.Quickfire(self.screen, keys, position, refresh, ship)
            Score.displayScore(self.screen)
            Score.displayLives(self.screen)
            pygame.display.flip()
            print(ship.counter)


    def main(self):
        self.startScreen()

if __name__ == '__main__':
    game = ToTheWormhole()
    game.main()


"""
 TRASHCAN FOR OLD CODE :(
 
 
 1. some methods for the enemy class, I was playing around with
    to get the enemies to a certain altitude and move around till 
    they are taken out. They would also shoot laser towards the player.
    Perhaps some other time. 
    
     
     def generate(self):
        width = 0
        if len(self.Enemies) != self.oneNum:
            for i in range(self.oneNum):
                self.x = random.randrange(0 + width, 200 + width - 50)
                self.y = random.randrange(-25, -15)
                if self.x not in self.Enemies_x:
                    self.Enemies.append([self.x, self.y])
                    self.Enemies_x.append(self.x)
                width += 200

    def levelOne(self, screen):
        for j in self.Enemies:
            self.Enemies_x.append(j[0])
        for i in self.Enemies:
            screen.blit(self.image1, i)
            if i[0] == max(self.Enemies_x):
                self.element1 = i
            if i[0] == min(self.Enemies_x):
                self.element2 = i

            if i[1] < 150:
                i[1] += self.velocity

            if i[1] >= 150:

                if self.element1[0] <= screenSize[0]-50 and self.rightEdge == False:
                    i[0] += self.velocity
                elif self.element2[0] >= 0 and self.rightEdge == True:
                    i[0] -= self.velocity
                if self.element1[0] >= screenSize[0] - 50:
                    self.rightEdge = True
                if self.element2[0] <= 0:
                    self.rightEdge = False

    def levelTwo(self, screen):
        for j in self.Enemies:
            self.Enemies_x.append(j[0])
        for i in self.Enemies:
            screen.blit(self.image2, i)
            if i[0] == max(self.Enemies_x):
                self.element1 = i
            if i[0] == min(self.Enemies_x):
                self.element2 = i

            if i[1] < 200:
                i[1] += self.velocity

            if i[1] >= 200:

                if self.element1[0] <= screenSize[0]-45 and self.rightEdge == False:
                    i[0] += self.velocity
                elif self.element2[0] >= 5 and self.rightEdge == True:
                    i[0] -= self.velocity
                if self.element1[0] >= screenSize[0] - 45:
                    self.rightEdge = True
                if self.element2[0] <= 5:
                    self.rightEdge = False

    def levelThree(self, screen):
        for j in self.Enemies:
            self.Enemies_x.append(j[0])
        for i in self.Enemies:
            screen.blit(self.image3, i)
            if i[0] == max(self.Enemies_x):
                self.element1 = i
            if i[0] == min(self.Enemies_x):
                self.element2 = i

            if i[1] < 300:
                i[1] += self.velocity

            if i[1] >= 300:

                if self.element1[0] <= screenSize[0] - 45 and self.rightEdge == False:
                    i[0] += self.velocity
                elif self.element2[0] >= 5 and self.rightEdge == True:
                    i[0] -= self.velocity
                if self.element1[0] >= screenSize[0] - 45:
                    self.rightEdge = True
                if self.element2[0] <= 5:
                    self.rightEdge = False
 2. 

"""