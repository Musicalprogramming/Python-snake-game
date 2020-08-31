import pygame
import copy
import random

pygame.init()


myfont = pygame.font.SysFont('Comic Sans MS', 30)




width = 720
height = 360

screen = pygame.display.set_mode((width, height))

WHITE = (255, 255, 255)
BLACK = (0,0,0)

#Game loop
running = True
clock = pygame.time.Clock()
x = 0
y = 0

speed = 12
score = 0

xSpeed = speed;
ySpeed = 0;

length = 4
distance = speed

position = [[x, y],[x - distance, 0],[x - 2*distance, 0],[x - 3*distance, 0]]
newBlock = [x - 4*distance, 0]
gameOver = False

token = [random.randint(1, 59)*12, random.randint(1, 29)*12]
playCrash = 0

while running:

    clock.tick(15)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False;

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if ySpeed != speed:
                    xSpeed = 0
                    ySpeed = -speed
            elif event.key == pygame.K_DOWN:
                if ySpeed != -speed:
                    xSpeed = 0
                    ySpeed = speed
            elif event.key == pygame.K_LEFT:
                if xSpeed != speed:
                    xSpeed = -speed
                    ySpeed = 0
            elif event.key == pygame.K_RIGHT:
                if xSpeed != -speed:
                    xSpeed = speed
                    ySpeed = 0

            if event.key == pygame.K_SPACE:
                if(gameOver):
                    x = 0
                    y = 0
                    playCrash = 0
                    position = [[x, y],[x - distance, 0],[x - 2*distance, 0],[x - 3*distance, 0]]
                    newBlock[0] = x - 4*distance
                    newBlock[1] = 0

                    gameOver = False
                    score = 0
                    xSpeed = speed
                    token[0] = random.randint(1, 59)*12
                    token[1] = random.randint(1, 29)*12

    screen.fill(BLACK)

    textsurface = myfont.render(str(score), False, (255, 255, 255))
    screen.blit(textsurface,(width / 2, height - 50))

    if(gameOver):
        playCrash += 1
        textsurface = myfont.render("Game over, press space to restart!", False, (255, 255, 255))
        screen.blit(textsurface,(width / 2 - (textsurface.get_width()/2), height / 2 - (textsurface.get_height()/2)))
        xSpeed = 0
        ySpeed = 0

    if playCrash == 1:
        pygame.mixer.music.set_volume(0.15)
        token_sound = pygame.mixer.music.load("Crash.mp3")
        pygame.mixer.music.play(loops=0, start=0)


    pygame.draw.rect(screen, WHITE, [token[0], token[1], 10, 10], 2)

    for i in range(1, len(position)):
        if(position[0][0] == position[i][0] and position[0][1] == position[i][1]):
            gameOver = True;

    for i in range(0, len(position)):
        pygame.draw.rect(screen, WHITE, [position[i][0], position[i][1], 10, 10], 2)

    if(position[0][0] == token[0] and position[0][1] == token[1]):
        pygame.mixer.music.set_volume(1)
        token_sound = pygame.mixer.music.load("Magic_Chime.mp3")
        pygame.mixer.music.play(loops=0, start=1.2)
        position.append(copy.deepcopy(newBlock))
        token[0] = random.randint(1, 59)*12
        token[1] = random.randint(1, 29)*12
        score = score + 1


    newBlock[0] = position[len(position) - 1][0]
    newBlock[0] = position[len(position) - 1][1]

    for i in range(len(position) -1, 0, -1):
        position[i][0] = position[i - 1][0]
        position[i][1] = position[i - 1][1]


    position[0][0] = position[0][0] + xSpeed
    position[0][1] = position[0][1] + ySpeed

    if(position[0][0] > width -1):
        position[0][0] = 0
    elif(position[0][0] < 0):
        position[0][0] = width
    elif(position[0][1] > height - 1):
        position[0][1] = 0
    elif(position[0][1] < 0):
        position[0][1] = height


    pygame.display.flip()
