import pygame
import random
import time

def main():
    pygame.init()
    pygame.mixer.init()
    pygame.display.set_caption("Master Guitar Pitch")
    screen = pygame.display.set_mode((800, 600))
    
    white = 255, 255, 255
    a_color = 255, 190, 0
    ab_color = 127, 0, 255
    b_color = 0, 0, 255
    c_color = 255, 0, 0
    cd_color = 0, 204, 102
    d_color = 255, 128, 0
    de_color = 0, 0, 255
    e_color = 255, 255, 0
    f_color = 153, 0, 153
    fg_color = 0, 153, 0
    g_color = 255, 85, 0
    ga_color = 0, 128, 255

    padding = 27
    button_wh = 100
    a_button_x, a_button_y = padding, 300
    ab_button_x, ab_button_y = a_button_x + button_wh + padding, 300
    b_button_x, b_button_y = ab_button_x + button_wh + padding, 300
    c_button_x, c_button_y = b_button_x + button_wh + padding, 300
    cd_button_x, cd_button_y = c_button_x + button_wh + padding, 300
    d_button_x, d_button_y = cd_button_x + button_wh + padding, 300

    de_button_x, de_button_y = padding, + 430
    e_button_x, e_button_y = de_button_x + button_wh + padding, 430
    f_button_x, f_button_y = e_button_x + button_wh + padding, 430
    fg_button_x, fg_button_y = f_button_x + button_wh + padding, 430
    g_button_x, g_button_y = fg_button_x + button_wh + padding, 430
    ga_button_x, ga_button_y = g_button_x + button_wh + padding, 430
    
    answer = random.randrange(0,13)
    shuffle = False

    EE = pygame.mixer.Sound('guitar-notes/EE.mp3')
    EF = pygame.mixer.Sound('guitar-notes/EF.mp3')
    EGb = pygame.mixer.Sound('guitar-notes/EGb.mp3')
    EG = pygame.mixer.Sound('guitar-notes/EG.mp3')
    EAb = pygame.mixer.Sound('guitar-notes/EAb.mp3')
    EA = pygame.mixer.Sound('guitar-notes/EA.mp3')
    EBb = pygame.mixer.Sound('guitar-notes/EBb.mp3')
    EB = pygame.mixer.Sound('guitar-notes/EB.mp3')
    EC = pygame.mixer.Sound('guitar-notes/EC.mp3')
    EDb = pygame.mixer.Sound('guitar-notes/EDb.mp3')
    ED = pygame.mixer.Sound('guitar-notes/ED.mp3')
    EEb = pygame.mixer.Sound('guitar-notes/EEb.mp3')

    if answer == 0:
        EA.play()
    elif answer == 1:
        EBb.play()
    elif answer == 2:
        EB.play()
    elif answer == 3:
        EC.play()
    elif answer == 4:
        EDb.play()
    elif answer == 5:
        ED.play()
    elif answer == 6:
        EEb.play()
    elif answer == 7:
        EE.play()
    elif answer == 8:
        EF.play()
    elif answer == 9:
        EGb.play()
    elif answer == 10:
        EG.play()
    elif answer == 11:
        EAb.play()

    running = True
    while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        screen.fill(pygame.Color(0,0,0))
        mouse_x, mouse_y = pygame.mouse.get_pos()

        if shuffle == True:
            answer = random.randrange(0,13)
            shuffle = False
        
        shuffle = shuffle or check_mouse(a_button_x, a_button_y, mouse_x, mouse_y, button_wh, event, screen, a_color, white, 0, answer)
        shuffle = shuffle or check_mouse(ab_button_x, ab_button_y, mouse_x, mouse_y, button_wh, event, screen, ab_color, white, 1, answer)
        shuffle = shuffle or check_mouse(b_button_x, b_button_y, mouse_x, mouse_y, button_wh, event, screen, b_color, white, 2, answer)
        shuffle = shuffle or check_mouse(c_button_x, c_button_y, mouse_x, mouse_y, button_wh, event, screen, c_color, white, 3, answer)
        shuffle = shuffle or check_mouse(cd_button_x, cd_button_y, mouse_x, mouse_y, button_wh, event, screen, cd_color, white, 4, answer)
        shuffle = shuffle or check_mouse(d_button_x, d_button_y, mouse_x, mouse_y, button_wh, event, screen, d_color, white, 5, answer)
        shuffle = shuffle or check_mouse(de_button_x, de_button_y, mouse_x, mouse_y, button_wh, event, screen, de_color, white, 6, answer)
        shuffle = shuffle or check_mouse(e_button_x, e_button_y, mouse_x, mouse_y, button_wh, event, screen, e_color, white, 7, answer)
        shuffle = shuffle or check_mouse(f_button_x, f_button_y, mouse_x, mouse_y, button_wh, event, screen, f_color, white, 8, answer)
        shuffle = shuffle or check_mouse(fg_button_x, fg_button_y, mouse_x, mouse_y, button_wh, event, screen, fg_color, white, 9, answer)
        shuffle = shuffle or check_mouse(g_button_x, g_button_y, mouse_x, mouse_y, button_wh, event, screen, g_color, white, 10, answer)
        shuffle = shuffle or check_mouse(ga_button_x, ga_button_y, mouse_x, mouse_y, button_wh, event, screen, ga_color, white, 11, answer)
        
        pygame.display.flip()
    pygame.quit()

def check_mouse(button_x, button_y, mouse_x, mouse_y, button_wh, event, screen, color, white, num, answer):
    text = ["A", "A#/Bb", "B", "C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab"]
    shuffle = False

    if button_x < mouse_x < button_x + button_wh and button_y < mouse_y < button_y + button_wh:
        if event.type == pygame.MOUSEBUTTONDOWN:
            make_button(screen, color, button_x, button_y, button_wh, text[num])
            if answer == num:
                print("correct")
                time.sleep(3)
                shuffle = True
            else:
                print("incorrect")
        else:
            make_button(screen, white, button_x, button_y, button_wh, text[num])
    else:
        make_button(screen, color, button_x, button_y, button_wh, text[num])
    return shuffle

def make_button(screen, color, button_x, button_y, button_wh, text):
    large_txt = ["A", "B", "C", "D", "E", "F", "G"]
    if text in large_txt:
        font = pygame.font.Font(None, 100)
    else: 
        font = pygame.font.Font(None, 40)
    pygame.draw.rect(screen, color, (button_x, button_y, button_wh, button_wh))
    txt = font.render(text, True, (0,0,0))
    if text in large_txt:
        screen.blit(txt, (button_x + 26, button_y + 20))
    else: 
        screen.blit(txt, (button_x + 12, button_y + 35))

if __name__ == "__main__":
    main()
