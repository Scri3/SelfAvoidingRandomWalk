""" Self Avoiding Random Walk Visualization implementation in python
Please enter lattice size and screen size (for both, enter N for NxN), seperated by space in command line """

import pygame
import sys
import time
from random import choice


check = True
print("\"Self Avoiding Random Walk Visualization\"")

# validate inputs
try:
    lat_size = int(sys.argv[1])
    sc_size = int(sys.argv[2])
    ratio = sc_size / lat_size
except (ValueError, IndexError, ZeroDivisionError):
    print("""ERROR: Lattice size or screen size is invalid.
HINT: You need to enter lattice size and screen size (for both, enter N for NxN),
seperated by space in command line.""")
    check = False

if check and ((lat_size < 10) or (lat_size > 150) or (sc_size < 100) or (sc_size > 1000)):
    print("""ERROR: Lattice or screen size is too small or too large.
HINT:
Lattice size should be between 10 and 150
Screen Size should be between 100 and 1000
""")
    check = False

if check and (sc_size/lat_size == 2):
    print("Please enter larger screen size for better visualization.")
    check = False

if check:
    if ratio.is_integer() and (lat_size % 2 == 0):

        # initialize pygame
        pygame.init()
        pygame.font.init()

        # create a screen:
        main_screen = pygame.display.set_mode((sc_size, sc_size))
        main_screen.fill((255, 255, 255))
        pygame.display.set_caption("Random Walk")

        # main vars
        font_size = int(sc_size/15)
        text_font = pygame.font.SysFont("Arial", font_size)
        size = main_screen.get_size()
        height = size[0]
        width = size[1]
        x, y = (height / 2, width / 2)
        avoid_list = [(x, y)]
        # color in (red,green,blue)
        gridcolor = (200, 200, 200)
        linecolor = (0, 0, 0)

        # function that draws grid
        def draw_grid(screen, lattice_size, grid_color):
            screen_size = screen.get_size()
            for x in range(0, screen_size[0], int(screen_size[0] / lattice_size)):
                for y in range(0, screen_size[1], int(screen_size[1] / lattice_size)):
                    rect = pygame.Rect(x, y, screen_size[0] / lattice_size, screen_size[1] / lattice_size)
                    pygame.draw.rect(screen, grid_color, rect, 1)

        draw_grid(main_screen, lat_size, gridcolor)

        # main loop
        while True:
            # manage user exit
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # self avoid random walk
            z, k = choice([(x + (height / lat_size), y), (x - (height / lat_size), y),
                           (x, y + (width / lat_size)), (x, y - (width / lat_size))])
            if not (z, k) in avoid_list:
                pygame.draw.line(main_screen, linecolor, (x, y), (z, k))
                right = ((z + (height / lat_size)), k)
                left = ((z - (height / lat_size)), k)
                up = (z, (k + (width / lat_size)))
                down = (z, (k - (width / lat_size)))
                # check for dead end
                if (right in avoid_list) and (left in avoid_list) and (up in avoid_list) and (down in avoid_list):
                    text_surface = text_font.render("DEAD END!", True, (255, 0, 0))
                    main_screen.blit(text_surface, ((height/2)-(2*font_size), width-(2*font_size)))
                    pygame.display.update()
                    print("Result: DEAD END!")
                    break
                avoid_list.append((z, k))
                (x, y) = (z, k)
                pygame.display.update()
                time.sleep(0.1)

            # check for escape
            if (z >= height) or (k >= width) or (z <= 0) or (k <= 0):
                text_surface = text_font.render("ESCAPE!", True, (0, 128, 0))
                main_screen.blit(text_surface, ((height/2)-(2*font_size), width-(2*font_size)))
                pygame.display.update()
                print("Result: ESCAPE!")
                break

        # manage user exit
        while True:
            time.sleep(0.05)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    else:
        print("""ERROR: Lattice size is not Even or Lattice/Screen ratio is not an integer.
HINT: You need to enter lattice size and screen size (for both, enter N for NxN),
seperated by space in command line.""")
