from random import randrange

import pygame
import sys

# resolution
RES = 600
# size of tile
SIZE = 20

# setting default values to variables
x, y = RES // 2, RES // 2                                               # snake coordinates
apple = randrange(20, RES - 20, SIZE), randrange(20, RES - 20, SIZE)    # apple coordinates
bonus = -50, -50                                                        # bonus coordinates
directions = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': True}    # directions in which snake can move
length = 1                                                              # snake length
snake = [(x, y)]                                                        # snake
dir_x, dir_y = 0, 0                                                     # directions of snake movement (stand in one place on default)
score = 0                                                               # score
speed = 10                                                              # speed of snake
running = True
main_menu = True        # showing main menu window
play_game = False       # hiding play area window
game_over = False       # hiding game over menu window
walls_coordinates = []                                                  # list to store walls coordinates

walls = [           # background 30x30 tiles, 0 - empty space, 1 - wall
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# pygame initialization
pygame.init()
pygame.display.set_caption('Snake Game')                        # setting caption (upper left corner of the window)
screen = pygame.display.set_mode([RES, RES])                    # setting resolution of game window
clock = pygame.time.Clock()

# fonts
score_font = pygame.font.SysFont('times', 25, bold=True)        # "Score" font
game_over_font = pygame.font.SysFont('times', 80, bold=True)     # "GAME OVER" font
main_menu_font = pygame.font.SysFont('times', 80, bold=True)    # "MAIN MENU" font
start_font = pygame.font.SysFont('times', 30, bold=True)        # start font
quit_font = pygame.font.SysFont('times', 30, bold=True)         # quit font

# music initialization
pygame.mixer.init()
apple_sound = pygame.mixer.Sound("apple.wav")                   # apple sound
game_over_sound = pygame.mixer.Sound("game-over.wav")            # game over sound
bonus_sound = pygame.mixer.Sound("bonus.wav")                   # bonus sound
background_music = pygame.mixer.Sound("background.wav")         # background music


# function to write walls coordinates to a list
def save_walls():
    for i in range(len(walls)):
        for j in range(len(walls[i])):
            if walls[i][j] == 1:
                walls_coordinates.append([j * SIZE, i * SIZE])


# function to draw walls on correct position
def draw_walls():
    for i in range(len(walls_coordinates)):
        pygame.draw.rect(screen, 'gray', (walls_coordinates[i][0], walls_coordinates[i][1], SIZE, SIZE))    # drawing gray wall(square) in corresponding coordinates


# function to avoid drawing apple/bonus on the wall
def check_wall(target):
    for i in range(len(walls_coordinates)):
        if target[0] == walls_coordinates[i][0] and target[1] == walls_coordinates[i][1]:   # if apple/bonus position equal wall position
            target = randrange(80, RES - 80, SIZE), randrange(80, RES - 80, SIZE)           # then reducing zone of spawning apple/bonus
    return target[0], target[1]                                                             # returning new coordinates which can't be equal to wall coordinates


# starting game
while running:
    save_walls()                # saving walls when game starts
    apple = check_wall(apple)   # checking whether apple collides with wall

    # main menu window
    while main_menu:
        screen.fill('black')    # filling screen with black color

        # main menu text
        main_menu_render = main_menu_font.render('MAIN MENU', True, 'green')                # rendering MAIN MENU text
        screen.blit(main_menu_render, (RES // 2 - 250, 75))                                 # assigning MAIN MENU text to appropriate coordinates

        # start game text
        start_render = start_font.render('Press ENTER to start the game', True, 'white')    # rendering start text
        screen.blit(start_render, (RES // 2 - 210, RES // 2 - 50))                          # assigning start text to appropriate coordinates

        # quit game text
        quit_render = quit_font.render('Press ESCAPE to quit the game', True, 'white')      # rendering quit text
        screen.blit(quit_render, (RES // 2 - 210, RES // 2))                                # assigning quit text to appropriate coordinates

        # refreshing the screen and displaying every element which should be displayed (in this case it's text above)
        pygame.display.update()

        # event loop
        for event in pygame.event.get():                        # checking every occurring event in the game
            if event.type == pygame.QUIT:                       # if button EXIT clicked (upper right corner 'X')
                pygame.quit()                                   # then exiting the game
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:                # if button ESCAPE pressed
                    pygame.quit()                               # then exiting the game
                    sys.exit()
                if event.key == pygame.K_RETURN:                # if button ENTER pressed
                    main_menu = False                           # hiding main menu window
                    play_game = True                            # showing play area window
                    pygame.mixer.Sound.play(background_music)   # turning on background music

    # play area window
    while play_game:
        screen.fill('black')    # filling screen with black color
        draw_walls()            # drawing walls

        # drawing snake, apple and bonus
        for i in range(len(snake)):
            pygame.draw.rect(screen, (0, 200, 0), (snake[i][0], snake[i][1], SIZE, SIZE))       # green snake body as squares
        pygame.draw.rect(screen, (0, 255, 0), (snake[-1][0], snake[-1][1], SIZE, SIZE))         # light green snake head as square
        pygame.draw.circle(screen, 'red', (apple[0] + 10, apple[1] + 10), SIZE / 2)             # red apple as circle
        pygame.draw.circle(screen, 'yellow', (bonus[0] + 10, bonus[1] + 10), SIZE)              # yellow bonus as circle

        # score text
        score_render = score_font.render(f'Score: {score}', True, 'orange')     # rendering score text
        screen.blit(score_render, (4, 0))                                       # assigning score text to appropriate coordinates

        # event loop
        for event in pygame.event.get():                # checking every occurring event in the game
            if event.type == pygame.QUIT:               # if button EXIT clicked (upper right corner 'X')
                pygame.quit()                           # then exiting the game
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:        # if button ESCAPE pressed
                    pygame.quit()                       # then exiting the game
                    sys.exit()
                # control system
                if (event.key == pygame.K_w or event.key == pygame.K_UP) and directions['UP']:          # if button W or UP ARROW pressed and snake doesn't move DOWN
                    dir_x, dir_y = 0, -1                                                                # then changing move direction of the snake to UP
                    directions = {'UP': True, 'DOWN': False, 'LEFT': True, 'RIGHT': True}               # and snake can't move to the DOWN

                elif (event.key == pygame.K_s or event.key == pygame.K_DOWN) and directions['DOWN']:    # if button S or DOWN ARROW pressed and snake doesn't move UP
                    dir_x, dir_y = 0, 1                                                                 # then changing move direction of the snake to DOWN
                    directions = {'UP': False, 'DOWN': True, 'LEFT': True, 'RIGHT': True}               # and snake can't move to the UP

                elif (event.key == pygame.K_a or event.key == pygame.K_LEFT) and directions['LEFT']:    # if button A or LEFT ARROW pressed and snake doesn't move RIGHT
                    dir_x, dir_y = -1, 0                                                                # then changing move direction of the snake to LEFT
                    directions = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': False}               # and snake can't move to the RIGHT

                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT and directions['RIGHT']:    # if button D or RIGHT ARROW pressed and snake doesn't move LEFT
                    dir_x, dir_y = 1, 0                                                                 # then changing move direction of the snake to RIGHT
                    directions = {'UP': True, 'DOWN': True, 'LEFT': False, 'RIGHT': True}               # and snake can't move to the LEFT

        # snake movement logic
        # changing snake position depending on direction it moves
        x += dir_x * SIZE
        y += dir_y * SIZE
        snake.append((x, y))        # adding new coordinates to snake
        snake = snake[-length:]     # and deleting the previous coordinates depending on length of the snake

        # eating apple logic
        if snake[-1] == apple:      # if snake head position equals apple position
                                                                                            # then:
            apple = randrange(20, RES - 20, SIZE * 2), randrange(20, RES - 20, SIZE * 2)    # changing position of apple
            apple = check_wall(apple)                                                       # checking whether apple collides with wall
            pygame.mixer.Sound.play(apple_sound)                                            # turning on apple sound
            length += 1                                                                     # snake length increasing by 1
            score += 1                                                                      # score increasing by 1
            speed += 0.5                                                                    # snake speed increasing by 0.5

            # bonus appearing
            if score % 3 == 0 or score == 1:                                                # if modulus 3 of score equals 0 or score equals 1
                bonus = randrange(20, RES - 20, SIZE), randrange(20, RES - 20, SIZE)        # then setting new position to bonus
                bonus = check_wall(bonus)                                                   # checking whether bonus collides with wall
            else:                                                                           # else
                bonus = -50, -50                                                            # hiding bonus out of the screen

        # eating bonus logic
        if snake[-1] == (bonus[0], bonus[1] + SIZE) \
                or snake[-1] == (bonus[0] + SIZE, bonus[1]) \
                or snake[-1] == (bonus[0], bonus[1] - SIZE) \
                or snake[-1] == (bonus[0] - SIZE, bonus[1]):    # if snake head position equals bonus position
            pygame.mixer.Sound.play(bonus_sound)                # then turning on bonus sound
            bonus = -50, -50                                    # hiding bonus out of the screen
            score += 3                                          # score increasing by 3

        # conditions of game over, if snake goes out of the screen or snake goes into yourself
        if x < 0 or x > RES - SIZE or y < 0 or y > RES - SIZE or len(snake) != len(set(snake)):
            play_game = False                               # hiding play area window
            game_over = True                                # showing game over window
            pygame.mixer.Sound.stop(background_music)       # turning off background music
            pygame.mixer.Sound.play(game_over_sound)         # turning on  game over sound

        # conditions of game over, if snake bumps into the wall
        for i in range(len(walls_coordinates)):
            if x == walls_coordinates[i][0] and y == walls_coordinates[i][1]:
                play_game = False                           # hiding play area window
                game_over = True                            # showing game over window
                pygame.mixer.Sound.stop(background_music)   # turning off background music
                pygame.mixer.Sound.play(game_over_sound)     # turning on  game over sound

        # refreshing the screen and displaying every element which should be displayed (in this case it's snake, apple, bonus, score, walls)
        pygame.display.update()
        # frames per second the game passing depending on snake speed
        clock.tick(speed)

    # game over menu window
    while game_over:
        screen.fill('black')        # filling screen with black color

        # game over text
        game_over_render = game_over_font.render('GAME OVER', True, 'red')                        # rendering GAME OVER text
        screen.blit(game_over_render, (RES // 2 - 250, 75))                                      # assigning GAME OVER text to appropriate coordinates
        # score text
        score_render = score_font.render(f'Your score: {score}', True, 'orange')                # rendering score text
        screen.blit(score_render, (RES // 2 - 70, RES - 100))                                   # assigning score text to appropriate coordinates
        # restart text
        restart_render = start_font.render('Press ENTER to restart the game', True, 'white')    # rendering restart text
        screen.blit(restart_render, (RES // 2 - 210, RES // 2 - 50))                            # assigning restart text to appropriate coordinates
        # quit text
        quit_render = quit_font.render('Press ESCAPE to quit the game', True, 'white')          # rendering quit text
        screen.blit(quit_render, (RES // 2 - 210, RES // 2))                                    # assigning quit text to appropriate coordinates

        # refreshing the screen and displaying every element which should be displayed (in this case it's text above)
        pygame.display.update()

        # event loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:           # if button EXIT clicked (upper right corner 'X')
                pygame.quit()                       # then exiting the game
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:    # if button ESCAPE pressed
                    pygame.quit()                   # then exiting the game
                    sys.exit()
                if event.key == pygame.K_RETURN:    # if button ENTER pressed
                    # then setting default values to variables
                    x, y = RES // 2, RES // 2
                    apple = randrange(20, RES - 20, SIZE), randrange(20, RES - 20, SIZE)
                    apple = check_wall(apple)
                    bonus = -50, -50
                    directions = {'UP': True, 'DOWN': True, 'LEFT': True, 'RIGHT': True}
                    length = 1
                    dir_x, dir_y = 0, 0
                    score = 0
                    speed = 10

                    game_over = False                           # hiding game over menu window
                    play_game = True                            # showing play area window
                    pygame.mixer.Sound.play(background_music)   # turning on background music
