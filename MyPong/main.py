from settings import *
from modes import mode
import sys

#check collision


def main_menu():
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption('MyPong')

    background_color = 'light yellow'

    against_bot = False
    mode_image = pygame.transform.scale(light_mode_image, (90, 80))

    while True:
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if int(screen_width / 2) - 80 <= mouse_position[0] <= int(screen_width / 2) + 80 and int(screen_height / 2) - 25 <= mouse_position[1] <= int(screen_height / 2) + 5:
                    mode('normal', background_color, against_bot)
                    screen = pygame.display.set_mode((screen_width, screen_height))
                elif int(screen_width / 2) - 80 <= mouse_position[0] <= int(screen_width / 2) + 80 and int(screen_height / 2) + 15 <= mouse_position[1] <= int(screen_height / 2) + 45:
                    mode('survival', background_color, against_bot)
                    screen = pygame.display.set_mode((screen_width, screen_height))
                elif int(screen_width / 2) - 80 <= mouse_position[0] <= int(screen_width / 2) + 80 and int(screen_height / 2) + 55 <= mouse_position[1] <= int(screen_height / 2) + 85:
                    mode('random', background_color, against_bot)
                    screen = pygame.display.set_mode((screen_width, screen_height))
                elif int(screen_width / 2) - 80 <= mouse_position[0] <= int(screen_width / 2) + 80 and int(screen_height / 2) + 95 <= mouse_position[1] <= int(screen_height / 2) + 125:
                    mode('double', background_color, against_bot)
                    screen = pygame.display.set_mode((screen_width, screen_height))
                elif screen_width - 110 <= mouse_position[0] <= screen_width - 20 and screen_height - 110 <= mouse_position[1] <= screen_height - 30:
                    if background_color == background_color_light_mode:
                        mode_image = dark_mode_image
                        background_color = background_color_dark_mode
                    else:
                        mode_image = light_mode_image
                        background_color = background_color_light_mode
                elif 30 <= mouse_position[0] <= 141 and screen_height - 90 <= mouse_position[1] <= screen_height - 70:
                    against_bot = not against_bot

        screen.fill(background_color)
        pygame.draw.rect(screen, button_color, pygame.Rect(int(screen_width / 2) - 80, int(screen_height / 2) - 25, 160, 30))
        pygame.draw.rect(screen, button_color, pygame.Rect(int(screen_width / 2) - 80, int(screen_height / 2) + 15, 160, 30))
        pygame.draw.rect(screen, button_color, pygame.Rect(int(screen_width / 2) - 80, int(screen_height / 2) + 55, 160, 30))
        pygame.draw.rect(screen, button_color, pygame.Rect(int(screen_width / 2) - 80, int(screen_height / 2) + 95, 160, 30))
        pygame.draw.rect(screen, button_color, pygame.Rect(screen_width - 110, screen_height - 110, 90, 80))

        screen.blit(mode_image, (screen_width - 110, screen_height - 110))

        if int(screen_width / 2) - 80 <= mouse_position[0] <= int(screen_width / 2) + 80 and int(screen_height / 2) - 25 <= mouse_position[1] <= int(screen_height / 2) + 5:
            pygame.draw.rect(screen, dark_button_color, pygame.Rect(int(screen_width / 2) - 80, int(screen_height / 2) - 25, 160, 30))
        elif int(screen_width / 2) - 80 <= mouse_position[0] <= int(screen_width / 2) + 80 and int(screen_height / 2) + 15 <= mouse_position[1] <= int(screen_height / 2) + 45:
            pygame.draw.rect(screen, dark_button_color, pygame.Rect(int(screen_width / 2) - 80, int(screen_height / 2) + 15, 160, 30))
        elif int(screen_width / 2) - 80 <= mouse_position[0] <= int(screen_width / 2) + 80 and int(screen_height / 2) + 55 <= mouse_position[1] <= int(screen_height / 2) + 85:
            pygame.draw.rect(screen, dark_button_color, pygame.Rect(int(screen_width / 2) - 80, int(screen_height / 2) + 55, 160, 30))
        elif int(screen_width / 2) - 80 <= mouse_position[0] <= int(screen_width / 2) + 80 and int(screen_height / 2) + 95 <= mouse_position[1] <= int(screen_height / 2) + 125:
            pygame.draw.rect(screen, dark_button_color, pygame.Rect(int(screen_width / 2) - 80, int(screen_height / 2) + 95, 160, 30))
        elif screen_width - 110 <= mouse_position[0] <= screen_width - 20 and screen_height - 110 <= mouse_position[1] <= screen_height - 30:
            pygame.draw.rect(screen, dark_button_color, pygame.Rect(screen_width - 110, screen_height - 110, 90, 80), 1)

        main_text = font.render('MyPong', True, 'blue', background_color)
        main_text = pygame.transform.scale(main_text, (120, 30))
        screen.blit(main_text, (int(screen_width / 2) - 59, 30))

        text_normal_mode = font.render('Normal Mode', True, 'blue', button_color)
        screen.blit(text_normal_mode, (int(screen_width / 2) - 65, int(screen_height / 2) - 20))

        text_survival_mode = font.render('Survival Mode', True, 'blue', button_color)
        screen.blit(text_survival_mode, (int(screen_width / 2) - 70, int(screen_height / 2) + 20))

        text_random_mode = font.render('Random Mode', True, 'blue', button_color)
        screen.blit(text_random_mode, (int(screen_width / 2) - 70, int(screen_height / 2) + 60))

        text_double_mode = font.render('Double Mode  ', True, 'blue', button_color)
        screen.blit(text_double_mode, (int(screen_width / 2) - 70, int(screen_height / 2) + 100))

        if not against_bot:
            text_bot = font.render('Turn Bot on', True, 'blue', button_color)

        else:
            text_bot = font.render('Turn Bot off', True, 'blue', button_color)


        screen.blit(text_bot, (30, screen_height - 90))
        pygame.display.flip()

main_menu()


