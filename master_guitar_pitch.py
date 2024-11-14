import pygame
import random
import time

attempts = 5

def main():
    global attempts
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
    height_a = 350
    height_b = 480
    a_button_x, a_button_y = padding, height_a
    ab_button_x, ab_button_y = a_button_x + button_wh + padding, height_a
    b_button_x, b_button_y = ab_button_x + button_wh + padding, height_a
    c_button_x, c_button_y = b_button_x + button_wh + padding, height_a
    cd_button_x, cd_button_y = c_button_x + button_wh + padding, height_a
    d_button_x, d_button_y = cd_button_x + button_wh + padding, height_a

    de_button_x, de_button_y = padding, + height_b
    e_button_x, e_button_y = de_button_x + button_wh + padding, height_b
    f_button_x, f_button_y = e_button_x + button_wh + padding, height_b
    fg_button_x, fg_button_y = f_button_x + button_wh + padding, height_b
    g_button_x, g_button_y = fg_button_x + button_wh + padding, height_b
    ga_button_x, ga_button_y = g_button_x + button_wh + padding, height_b
    
    answer = random.randrange(0,12)
    shuffle = True
    sound_played = False

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

    sounds = [EA, EBb, EB, EC, EDb, ED, EEb, EE, EF, EGb, EG, EAb]
    guitar = pygame.image.load("guitar_PNG3361.png").convert_alpha()
    lives = 3

    running = True
    while running:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
        
        screen.fill(pygame.Color(0,0,0))
        mouse_x, mouse_y = pygame.mouse.get_pos()
        screen.blit(pygame.transform.scale(guitar, (2048//1.5, 993//1.5)),(0,-100))

        if shuffle == True:
            answer = random.randrange(0,12)
            sound_played = False
            shuffle = False
    
        if sound_played == False:
            sounds[answer].play()
            sound_played = True
        
        font = pygame.font.Font(None, 50)
        text = f"attempts: {attempts}/5"
        txt = font.render(text, True, (255,255,255))
        screen.blit(txt, (10, 10))
        
        make_lives(screen, attempts)
        
        make_button(screen, a_color, a_button_x, a_button_y, button_wh, "A")
        make_button(screen, ab_color, ab_button_x, ab_button_y, button_wh, "A#/Bb")
        make_button(screen, b_color, b_button_x, b_button_y, button_wh, "B")
        make_button(screen, c_color, c_button_x, c_button_y, button_wh, "C")
        make_button(screen, cd_color, cd_button_x, cd_button_y, button_wh, "C#/Db")
        make_button(screen, d_color, d_button_x, d_button_y, button_wh, "D")
        make_button(screen, de_color, de_button_x, de_button_y, button_wh, "D#/Eb")
        make_button(screen, e_color, e_button_x, e_button_y, button_wh, "E")
        make_button(screen, f_color, f_button_x, f_button_y, button_wh, "F")
        make_button(screen, fg_color, fg_button_x, fg_button_y, button_wh, "F#/Gb")
        make_button(screen, g_color, g_button_x, g_button_y, button_wh, "G")
        make_button(screen, ga_color, ga_button_x, ga_button_y, button_wh, "G#/Ab")

        shuffle = shuffle or check_mouse(a_button_x, a_button_y, mouse_x, mouse_y, button_wh, event, screen, a_color, white, 0, answer)
        shuffle = shuffle or check_mouse(ab_button_x, ab_button_y, mouse_x, mouse_y, button_wh, event, screen, ab_color, white, 1, answer)
        shuffle = shuffle or check_mouse(b_button_x, b_button_y, mouse_x, mouse_y, button_wh, event, screen, b_color, white, 2, answer)
        shuffle = shuffle or check_mouse(c_button_x, c_button_y, mouse_x, mouse_y, button_wh, event, screen, c_color, white, 3, answer)
        shuffle = shuffle or check_mouse(d_button_x, d_button_y, mouse_x, mouse_y, button_wh, event, screen, d_color, white, 5, answer)
        shuffle = shuffle or check_mouse(cd_button_x, cd_button_y, mouse_x, mouse_y, button_wh, event, screen, cd_color, white, 4, answer)
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
    global attempts

    if button_x < mouse_x < button_x + button_wh and button_y < mouse_y < button_y + button_wh:
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            make_button(screen, color, button_x, button_y, button_wh, text[num])
            if answer == num:
                print("correct")
                make_checkmark(screen)
                pygame.display.flip()
                pygame.time.delay(1000)
                time.sleep(1)
                shuffle = True
                attempts = 5
            else:
                print("incorrect")
                attempts -= 1
                make_x(screen)
                pygame.display.flip()
                pygame.time.delay(1000)
                time.sleep(1)
                if attempts == 0:
                    shuffle = True 
                    attempts = 5
        else:
            make_button(screen, white, button_x, button_y, button_wh, text[num])
    else:
        make_button(screen, color, button_x, button_y, button_wh, text[num])
    
    return shuffle

def make_lives(screen, attempts):
    
    if attempts == 5:
        heart1 = pygame.Surface((50,50))
        heart2 = pygame.Surface((50, 50))
        heart3 = pygame.Surface((50, 50))
        heart4 = pygame.Surface((50, 50))
        heart5 = pygame.Surface((50, 50))
        heart1.fill((255,49,49))
        heart2.fill((255,49,49))
        heart3.fill((255,49,49))
        heart4.fill((255,49,49))
        heart5.fill((255,49,49))
        screen.blit(heart1, (430,10))
        screen.blit(heart2, (490,10))
        screen.blit(heart3, (550,10))
        screen.blit(heart4, (610,10))
        screen.blit(heart5, (670,10))
    if attempts == 4:
        heart1 = pygame.Surface((50,50))
        heart2 = pygame.Surface((50, 50))
        heart3 = pygame.Surface((50, 50))
        heart4 = pygame.Surface((50, 50))
        heart5 = pygame.Surface((50, 50))
        heart1.fill((255,49,49))
        heart2.fill((255,49,49))
        heart3.fill((255,49,49))
        heart4.fill((255,49,49))
        heart5.fill((0,0,0))
        screen.blit(heart1, (430,10))
        screen.blit(heart2, (490,10))
        screen.blit(heart3, (550,10))
        screen.blit(heart4, (610,10))
        screen.blit(heart5, (670,10))
    if attempts == 3:
        heart1 = pygame.Surface((50,50))
        heart2 = pygame.Surface((50, 50))
        heart3 = pygame.Surface((50, 50))
        heart4 = pygame.Surface((50, 50))
        heart5 = pygame.Surface((50, 50))
        heart1.fill((255,49,49))
        heart2.fill((255,49,49))
        heart3.fill((255,49,49))
        heart4.fill((0,0,0))
        heart5.fill((0,0,0))
        screen.blit(heart1, (430,10))
        screen.blit(heart2, (490,10))
        screen.blit(heart3, (550,10))
        screen.blit(heart4, (610,10))
        screen.blit(heart5, (670,10))
    if attempts == 2:
        heart1 = pygame.Surface((50,50))
        heart2 = pygame.Surface((50, 50))
        heart3 = pygame.Surface((50, 50))
        heart4 = pygame.Surface((50, 50))
        heart5 = pygame.Surface((50, 50))
        heart1.fill((255,49,49))
        heart2.fill((255,49,49))
        heart3.fill((0,0,0))
        heart4.fill((0,0,0))
        heart5.fill((0,0,0))
        screen.blit(heart1, (430,10))
        screen.blit(heart2, (490,10))
        screen.blit(heart3, (550,10))
        screen.blit(heart4, (610,10))
        screen.blit(heart5, (670,10))
    if attempts == 1:
        heart1 = pygame.Surface((50,50))
        heart2 = pygame.Surface((50, 50))
        heart3 = pygame.Surface((50, 50))
        heart4 = pygame.Surface((50, 50))
        heart5 = pygame.Surface((50, 50))
        heart1.fill((255,49,49))
        heart2.fill((0,0,0))
        heart3.fill((0,0,0))
        heart4.fill((0,0,0))
        heart5.fill((0,0,0))
        screen.blit(heart1, (430,10))
        screen.blit(heart2, (490,10))
        screen.blit(heart3, (550,10))
        screen.blit(heart4, (610,10))
        screen.blit(heart5, (670,10))
    if attempts == 0:
        heart1 = pygame.Surface((50,50))
        heart2 = pygame.Surface((50, 50))
        heart3 = pygame.Surface((50, 50))
        heart4 = pygame.Surface((50, 50))
        heart5 = pygame.Surface((50, 50))
        heart1.fill((0,0,0))
        heart2.fill((0,0,0))
        heart3.fill((0,0,0))
        heart4.fill((0,0,0))
        heart5.fill((0,0,0))
        screen.blit(heart1, (430,10))
        screen.blit(heart2, (490,10))
        screen.blit(heart3, (550,10))
        screen.blit(heart4, (610,10))
        screen.blit(heart5, (670,10))

    screen.blit(heart1, (430,10))
    screen.blit(heart2, (490,10))
    screen.blit(heart3, (550,10))
    screen.blit(heart4, (610,10))
    screen.blit(heart5, (670,10))

def make_checkmark(screen):
    check = pygame.Surface((50,50))
    check.fill((0,255,0))
    screen.blit(check, (368,200))

def make_x(screen):
    x = pygame.Surface((50,50))
    x.fill((255,49,49))
    screen.blit(x, (368,200))

def make_button(screen, color, button_x, button_y, button_wh, text):
    large_txt = ["A", "B", "C", "D", "E", "F", "G"]
    if text in large_txt:
        font = pygame.font.Font(None, 100)
    else: 
        font = pygame.font.Font(None, 40)
    pygame.draw.rect(screen, color, (button_x, button_y, button_wh, button_wh))
    txt = font.render(text, True, (0,0,0))
    if text in large_txt:
        screen.blit(txt, (button_x + 24, button_y + 20))
    else: 
        screen.blit(txt, (button_x + 12, button_y + 35))

if __name__ == "__main__":
    main()
