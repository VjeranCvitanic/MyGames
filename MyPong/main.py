from settings import *
from modes import mode
import sys

#check collision


def main_menu():
    screen = pygame.display.set_mode((screen_width, screen_height))

    pygame.display.set_caption('MyPong')

    background_color = 'light yellow'
    mode_image = pygame.transform.scale(light_mode_image, (90, 80))

    while True:
        mouse_position = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                if int(screen_width / 2) - 80 <= mouse_position[0] <= int(screen_width / 2) + 80 and int(screen_height / 2) - 5 <= mouse_position[1] <= int(screen_height / 2) + 25:
                    mode('normal', background_color)
                    screen = pygame.display.set_mode((screen_width, screen_height))
                if int(screen_width / 2) - 80 <= mouse_position[0] <= int(screen_width / 2) + 80 and int(screen_height / 2) + 35 <= mouse_position[1] <= int(screen_height / 2) + 65:
                    mode('survival', background_color)
                    screen = pygame.display.set_mode((screen_width, screen_height))
                if int(screen_width / 2) - 80 <= mouse_position[0] <= int(screen_width / 2) + 80 and int(screen_height / 2) + 75 <= mouse_position[1] <= int(screen_height / 2) + 105:
                    mode('random', background_color)
                    screen = pygame.display.set_mode((screen_width, screen_height))
                if screen_width - 110 <= mouse_position[0] <= screen_width - 20 and screen_height - 110 <= mouse_position[1] <= screen_height - 30:
                    if background_color == background_color_light_mode:
                        mode_image = dark_mode_image
                        background_color = background_color_dark_mode
                    else:
                        mode_image = light_mode_image
                        background_color = background_color_light_mode

        screen.fill(background_color)
        pygame.draw.rect(screen, button_color, pygame.Rect(int(screen_width / 2) - 80, int(screen_height / 2) - 5, 160, 30))
        pygame.draw.rect(screen, button_color, pygame.Rect(int(screen_width / 2) - 80, int(screen_height / 2) + 35, 160, 30))
        pygame.draw.rect(screen, button_color, pygame.Rect(int(screen_width / 2) - 80, int(screen_height / 2) + 75, 160, 30))
        pygame.draw.rect(screen, button_color, pygame.Rect(screen_width - 110, screen_height - 110, 90, 80))

        screen.blit(mode_image, (screen_width - 110, screen_height - 110))

        if int(screen_width / 2) - 80 <= mouse_position[0] <= int(screen_width / 2) + 80 and int(screen_height / 2) - 5 <= mouse_position[1] <= int(screen_height / 2) + 25:
            pygame.draw.rect(screen, dark_button_color, pygame.Rect(int(screen_width / 2) - 80, int(screen_height / 2) - 5, 160, 30))
        elif int(screen_width / 2) - 80 <= mouse_position[0] <= int(screen_width / 2) + 80 and int(screen_height / 2) + 35 <= mouse_position[1] <= int(screen_height / 2) + 65:
            pygame.draw.rect(screen, dark_button_color, pygame.Rect(int(screen_width / 2) - 80, int(screen_height / 2) + 35, 160, 30))
        elif int(screen_width / 2) - 80 <= mouse_position[0] <= int(screen_width / 2) + 80 and int(screen_height / 2) + 75 <= mouse_position[1] <= int(screen_height / 2) + 105:
            pygame.draw.rect(screen, dark_button_color, pygame.Rect(int(screen_width / 2) - 80, int(screen_height / 2) + 75, 160, 30))
        elif screen_width - 110 <= mouse_position[0] <= screen_width - 20 and screen_height - 110 <= mouse_position[1] <= screen_height - 30:
            pygame.draw.rect(screen, dark_button_color, pygame.Rect(screen_width - 110, screen_height - 110, 90, 80), 1)

        main_text = font.render('MyPong', True, 'blue', background_color)
        main_text = pygame.transform.scale(main_text, (120, 30))
        screen.blit(main_text, (int(screen_width / 2) - 59, 40))

        text_normal_mode = font.render('Normal Mode', True, 'blue', button_color)
        screen.blit(text_normal_mode, (int(screen_width / 2) - 65, int(screen_height / 2)))

        text_survival_mode = font.render('Survival Mode', True, 'blue', button_color)
        screen.blit(text_survival_mode, (int(screen_width / 2) - 70, int(screen_height / 2) + 40))

        text_random_mode = font.render('Random Mode', True, 'blue', button_color)
        screen.blit(text_random_mode, (int(screen_width / 2) - 70, int(screen_height / 2) + 80))

        pygame.display.flip()

main_menu()


