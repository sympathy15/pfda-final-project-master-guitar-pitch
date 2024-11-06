import pygame

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Master Guitar Pitch")
    screen = pygame.display.set_mode((800, 600))
    sound = pygame.mixer.Sound('test.wav')
    
    
    button_x, button_y = 400, 300
    button_wh = 200

    font = pygame.font.Font(None, 36)

    # sound.play()

    running = True
    while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        screen.fill(pygame.Color(0,0,0))
        mouse_x, mouse_y = pygame.mouse.get_pos()
        txt = font.render("Text", True, (255,255,255))
        screen.blit(txt, (50, 50))
        if button_x < mouse_x < button_x + button_wh and button_y < mouse_y < button_y + button_wh:
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, (255, 0, 0), (button_x, button_y, button_wh, button_wh))
        else:
            pygame.draw.rect(screen, (255, 255, 0), (button_x, button_y, button_wh, button_wh))
        
        pygame.display.flip()
    pygame.quit

if __name__ == "__main__":
    main()
