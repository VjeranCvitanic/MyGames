from settings import *

def print_score(screen, p1, p2):
    text = font.render(str(p1.score) + ':' + str(p2.score), True, 'blue', background_color)
    screen.blit(text, (int(game_screen_width / 2) - 10, 20))