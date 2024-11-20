import pygame
import random
import time

attempts = 3
score = 0

def main():
    global attempts, score
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
    dot_changed = False
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
    AA = pygame.mixer.Sound('guitar-notes/AA.mp3')
    ABb = pygame.mixer.Sound('guitar-notes/ABb.mp3')
    AB = pygame.mixer.Sound('guitar-notes/AB.mp3')
    AC = pygame.mixer.Sound('guitar-notes/AC.mp3')
    ADb = pygame.mixer.Sound('guitar-notes/ADb.mp3')
    AD = pygame.mixer.Sound('guitar-notes/AD.mp3')
    AEb = pygame.mixer.Sound('guitar-notes/AEb.mp3')
    AE = pygame.mixer.Sound('guitar-notes/AE.mp3')
    AF = pygame.mixer.Sound('guitar-notes/AF.mp3')
    AGb = pygame.mixer.Sound('guitar-notes/AGb.mp3')
    AG = pygame.mixer.Sound('guitar-notes/AG.mp3')
    AAb = pygame.mixer.Sound('guitar-notes/AAb.mp3')
    DD = pygame.mixer.Sound('guitar-notes/DD.mp3')
    DEb= pygame.mixer.Sound('guitar-notes/DEb.mp3')
    DE = pygame.mixer.Sound('guitar-notes/DE.mp3')
    DF = pygame.mixer.Sound('guitar-notes/DF.mp3')
    DGb = pygame.mixer.Sound('guitar-notes/DGb.mp3')
    DG = pygame.mixer.Sound('guitar-notes/DG.mp3')
    DAb = pygame.mixer.Sound('guitar-notes/DAb.mp3')
    DA = pygame.mixer.Sound('guitar-notes/DA.mp3')
    DBb = pygame.mixer.Sound('guitar-notes/DBb.mp3')
    DB = pygame.mixer.Sound('guitar-notes/DB.mp3')
    DC = pygame.mixer.Sound('guitar-notes/DC.mp3')
    DDb = pygame.mixer.Sound('guitar-notes/DDb.mp3')
    GG = pygame.mixer.Sound('guitar-notes/GG.mp3')
    GAb = pygame.mixer.Sound('guitar-notes/GAb.mp3')
    GA = pygame.mixer.Sound('guitar-notes/GA.mp3')
    GBb = pygame.mixer.Sound('guitar-notes/GBb.mp3')
    GB = pygame.mixer.Sound('guitar-notes/GB.mp3')
    GC = pygame.mixer.Sound('guitar-notes/GC.mp3')
    GDb = pygame.mixer.Sound('guitar-notes/GDb.mp3')
    GD = pygame.mixer.Sound('guitar-notes/GD.mp3')
    GEb = pygame.mixer.Sound('guitar-notes/GEb.mp3')
    GE = pygame.mixer.Sound('guitar-notes/GE.mp3')
    GF = pygame.mixer.Sound('guitar-notes/GF.mp3')
    GGb = pygame.mixer.Sound('guitar-notes/GGb.mp3')
    BB = pygame.mixer.Sound('guitar-notes/BB.mp3')
    BC = pygame.mixer.Sound('guitar-notes/BC.mp3')
    BDb = pygame.mixer.Sound('guitar-notes/BDb.mp3')
    BD = pygame.mixer.Sound('guitar-notes/BD.mp3')
    BEb = pygame.mixer.Sound('guitar-notes/BEb.mp3')
    BE = pygame.mixer.Sound('guitar-notes/BE.mp3')
    BF = pygame.mixer.Sound('guitar-notes/BF.mp3')
    BGb = pygame.mixer.Sound('guitar-notes/BGb.mp3')
    BG = pygame.mixer.Sound('guitar-notes/BG.mp3')
    BAb = pygame.mixer.Sound('guitar-notes/BAb.mp3')
    BA = pygame.mixer.Sound('guitar-notes/BA.mp3')
    BBb = pygame.mixer.Sound('guitar-notes/BBb.mp3')
    HEE = pygame.mixer.Sound('guitar-notes/HEE.mp3')
    HEF = pygame.mixer.Sound('guitar-notes/HEF.mp3')
    HEGb = pygame.mixer.Sound('guitar-notes/HEGb.mp3')
    HEG = pygame.mixer.Sound('guitar-notes/HEG.mp3')
    HEAb = pygame.mixer.Sound('guitar-notes/HEAb.mp3')
    HEA = pygame.mixer.Sound('guitar-notes/HEA.mp3')
    HEBb = pygame.mixer.Sound('guitar-notes/HEBb.mp3')
    HEB = pygame.mixer.Sound('guitar-notes/HEB.mp3')
    HEC = pygame.mixer.Sound('guitar-notes/HEC.mp3')
    HEDb = pygame.mixer.Sound('guitar-notes/HEDb.mp3')
    HED = pygame.mixer.Sound('guitar-notes/HED.mp3')
    HEEb = pygame.mixer.Sound('guitar-notes/HEEb.mp3')
    

    E_string = [EE, EF, EGb, EG, EAb, EA, EBb, EB, EC, EDb, ED, EEb]
    A_string = [AA, ABb, AB, AC, ADb, AD, AEb, AE, AF, AGb, AG, AAb]
    D_string = [DD, DEb, DE, DF, DGb, DG, DAb, DA, DBb, DB, DC, DDb]
    G_string = [GG, GAb, GA, GBb, GB, GC, GDb, GD, GEb, GE, GF, GGb]
    B_string = [BB, BC, BDb, BD, BEb, BE, BF, BGb, BG, BAb, BA, BBb]
    high_E_string = [HEE, HEF, HEGb, HEG, HEAb, HEA, HEBb, HEB, HEC, HEDb, HED, HEEb]

    sounds = [E_string, A_string, D_string, G_string, B_string, high_E_string]
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
            string_i = random.randint(0,5)
            fret_i = random.randint(0,11)
            answer_sound = (string_i, fret_i)
            if answer_sound == (0,5) or answer_sound == (1,0) or answer_sound == (2,7) or answer_sound == (3,2) or answer_sound == (4,10) or answer_sound == (5,5):
                answer = 0
            elif answer_sound == (0,6) or answer_sound == (1,1) or answer_sound == (2,8) or answer_sound == (3,3) or answer_sound == (4,11) or answer_sound == (5,6):
                answer = 1
            elif answer_sound == (0,7) or answer_sound == (1,2) or answer_sound == (2,9) or answer_sound == (3,4) or answer_sound == (4,0) or answer_sound == (5,7):
                answer = 2
            elif answer_sound == (0,8) or answer_sound == (1,3) or answer_sound == (2,10) or answer_sound == (3,5) or answer_sound == (4,1) or answer_sound == (5,8):
                answer = 3
            elif answer_sound == (0,9) or answer_sound == (1,4) or answer_sound == (2,11) or answer_sound == (3,6) or answer_sound == (4,2) or answer_sound == (5,9):
                answer = 4
            elif answer_sound == (0,10) or answer_sound == (1,5) or answer_sound == (2,0) or answer_sound == (3,7) or answer_sound == (4,3) or answer_sound == (5,10):
                answer = 5
            elif answer_sound == (0,11) or answer_sound == (1,6) or answer_sound == (2,1) or answer_sound == (3,8) or answer_sound == (4,4) or answer_sound == (5,11):
                answer = 6
            elif answer_sound == (0,0) or answer_sound == (1,7) or answer_sound == (2,2) or answer_sound == (3,9) or answer_sound == (4,5) or answer_sound == (5,0):
                answer = 7
            elif answer_sound == (0,1) or answer_sound == (1,8) or answer_sound == (2,3) or answer_sound == (3,10) or answer_sound == (4,6) or answer_sound == (5,1):
                answer = 8
            elif answer_sound == (0,2) or answer_sound == (1,9) or answer_sound == (2,4) or answer_sound == (3,11) or answer_sound == (4,7) or answer_sound == (5,2):
                answer = 9
            elif answer_sound == (0,3) or answer_sound == (1,10) or answer_sound == (2,5) or answer_sound == (3,0) or answer_sound == (4,8) or answer_sound == (5,3):
                answer = 10
            elif answer_sound == (0,4) or answer_sound == (1,11) or answer_sound == (2,6) or answer_sound == (3,1) or answer_sound == (4,9) or answer_sound == (5,4):
                answer = 11
            sound_played = False
            shuffle = False
    
        if sound_played == False:
            sounds[answer_sound[0]][answer_sound[1]].play()
            sound_played = True
        
        if dot_changed == False:
            place_dot(screen, answer_sound)
        
        font = pygame.font.Font(None, 50)
        text = f"score: {score}"
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

def place_dot(screen, answer_sound):
    note_dot_answer = 0

    if answer_sound == (0,5):
        note_dot_answer = 5
    if answer_sound == (0,6):
        note_dot_answer = 6
    if answer_sound == (0,7):
        note_dot_answer = 7
    if answer_sound == (0,8):
        note_dot_answer = 8
    if answer_sound == (0,9):
        note_dot_answer = 9
    if answer_sound == (0,10):
        note_dot_answer = 10
    if answer_sound == (0,11):
        note_dot_answer = 11
    if answer_sound == (0,0):
        note_dot_answer = 0
    if answer_sound == (0,1):
        note_dot_answer = 1
    if answer_sound == (0,2):
        note_dot_answer = 2
    if answer_sound == (0,3):
        note_dot_answer = 3
    if answer_sound == (0,4):
        note_dot_answer = 4
    
    if answer_sound == (1,0):
        note_dot_answer = 12
    if answer_sound == (1,1):
        note_dot_answer = 13
    if answer_sound == (1,2):
        note_dot_answer = 14
    if answer_sound == (1,3):
        note_dot_answer = 15
    if answer_sound == (1,4):
        note_dot_answer = 16
    if answer_sound == (1,5):
        note_dot_answer = 17
    if answer_sound == (1,6):
        note_dot_answer = 18
    if answer_sound == (1,7):
        note_dot_answer = 19
    if answer_sound == (1,8):
        note_dot_answer = 20
    if answer_sound == (1,9):
        note_dot_answer = 21
    if answer_sound == (1,10):
        note_dot_answer = 22
    if answer_sound == (1,11):
        note_dot_answer = 23

    if answer_sound == (2,0):
        note_dot_answer = 24
    if answer_sound == (2,1):
        note_dot_answer = 25
    if answer_sound == (2,2):
        note_dot_answer = 26
    if answer_sound == (2,3):
        note_dot_answer = 27
    if answer_sound == (2,4):
        note_dot_answer = 28
    if answer_sound == (2,5):
        note_dot_answer = 29
    if answer_sound == (2,6):
        note_dot_answer = 30
    if answer_sound == (2,7):
        note_dot_answer = 31
    if answer_sound == (2,8):
        note_dot_answer = 32
    if answer_sound == (2,9):
        note_dot_answer = 33
    if answer_sound == (2,10):
        note_dot_answer = 34
    if answer_sound == (2,11):
        note_dot_answer = 35

    if answer_sound == (3,0):
        note_dot_answer = 36
    if answer_sound == (3,1):
        note_dot_answer = 37
    if answer_sound == (3,2):
        note_dot_answer = 38
    if answer_sound == (3,3):
        note_dot_answer = 39
    if answer_sound == (3,4):
        note_dot_answer = 40
    if answer_sound == (3,5):
        note_dot_answer = 41
    if answer_sound == (3,6):
        note_dot_answer = 42
    if answer_sound == (3,7):
        note_dot_answer = 43
    if answer_sound == (3,8):
        note_dot_answer = 44
    if answer_sound == (3,9):
        note_dot_answer = 45
    if answer_sound == (3,10):
        note_dot_answer = 46
    if answer_sound == (3,11):
        note_dot_answer = 47

    if answer_sound == (4,0):
        note_dot_answer = 48
    if answer_sound == (4,1):
        note_dot_answer = 49
    if answer_sound == (4,2):
        note_dot_answer = 50
    if answer_sound == (4,3):
        note_dot_answer = 51
    if answer_sound == (4,4):
        note_dot_answer = 52
    if answer_sound == (4,5):
        note_dot_answer = 53
    if answer_sound == (4,6):
        note_dot_answer = 54
    if answer_sound == (4,7):
        note_dot_answer = 55
    if answer_sound == (4,8):
        note_dot_answer = 56
    if answer_sound == (4,9):
        note_dot_answer = 57
    if answer_sound == (4,10):
        note_dot_answer = 58
    if answer_sound == (4,11):
        note_dot_answer = 59
    
    if answer_sound == (5,0):
        note_dot_answer = 60
    if answer_sound == (5,1):
        note_dot_answer = 61
    if answer_sound == (5,2):
        note_dot_answer = 62
    if answer_sound == (5,3):
        note_dot_answer = 63
    if answer_sound == (5,4):
        note_dot_answer = 64
    if answer_sound == (5,5):
        note_dot_answer = 65
    if answer_sound == (5,6):
        note_dot_answer = 66
    if answer_sound == (5,7):
        note_dot_answer = 67
    if answer_sound == (5,8):
        note_dot_answer = 68
    if answer_sound == (5,9):
        note_dot_answer = 69
    if answer_sound == (5,10):
        note_dot_answer = 70
    if answer_sound == (5,11):
        note_dot_answer = 71

    fret_0 = 263
    fret_1 = 302
    fret_2 = 350
    fret_3 = 394
    fret_4 = 435
    fret_5 = 475
    fret_6 = 512
    fret_7 = 548
    fret_8 = 580
    fret_9 = 611
    fret_10 = 640
    fret_11 = 668
    low_e_row = 217
    a_row = 205
    d_row = 195
    g_row = 185 
    b_row = 173
    high_e_row = 162
    
    if note_dot_answer == 0:
        dot_x = fret_0
        dot_y = low_e_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 1:
        dot_x = fret_1
        dot_y = low_e_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 2:
        dot_x = fret_2
        dot_y = low_e_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 3:
        dot_x = fret_3
        dot_y = low_e_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 4:
        dot_x = fret_4
        dot_y = low_e_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 5:
        dot_x = fret_5
        dot_y = low_e_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 6:
        dot_x = fret_6
        dot_y = low_e_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 7:
        dot_x = fret_7
        dot_y = low_e_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 8:
        dot_x = fret_8
        dot_y = low_e_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 9:
        dot_x = fret_9
        dot_y = low_e_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 10:
        dot_x = fret_10
        dot_y = low_e_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 11:
        dot_x = fret_11
        dot_y = low_e_row
        make_dot(screen, dot_x, dot_y)

    if note_dot_answer == 12:
        dot_x = fret_0
        dot_y = a_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 13:
        dot_x = fret_1
        dot_y = a_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 14:
        dot_x = fret_2
        dot_y = a_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 15:
        dot_x = fret_3
        dot_y = a_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 16:
        dot_x = fret_4
        dot_y = a_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 17:
        dot_x = fret_5
        dot_y = a_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 18:
        dot_x = fret_6
        dot_y = a_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 19:
        dot_x = fret_7
        dot_y = a_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 20:
        dot_x = fret_8
        dot_y = a_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 21:
        dot_x = fret_9
        dot_y = a_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 22:
        dot_x = fret_10
        dot_y = a_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 23:
        dot_x = fret_11
        dot_y = a_row
        make_dot(screen, dot_x, dot_y)

    if note_dot_answer == 24:
        dot_x = fret_0
        dot_y = d_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 25:
        dot_x = fret_1
        dot_y = d_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 26:
        dot_x = fret_2
        dot_y = d_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 27:
        dot_x = fret_3
        dot_y = d_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 28:
        dot_x = fret_4
        dot_y = d_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 29:
        dot_x = fret_5
        dot_y = d_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 30:
        dot_x = fret_6
        dot_y = d_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 31:
        dot_x = fret_7
        dot_y = d_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 32:
        dot_x = fret_8
        dot_y = d_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 33:
        dot_x = fret_9
        dot_y = d_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 34:
        dot_x = fret_10
        dot_y = d_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 35:
        dot_x = fret_11
        dot_y = d_row
        make_dot(screen, dot_x, dot_y)

    if note_dot_answer == 36:
        dot_x = fret_0
        dot_y = g_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 37:
        dot_x = fret_1
        dot_y = g_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 38:
        dot_x = fret_2
        dot_y = g_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 39:
        dot_x = fret_3
        dot_y = g_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 40:
        dot_x = fret_4
        dot_y = g_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 41:
        dot_x = fret_5
        dot_y = g_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 42:
        dot_x = fret_6
        dot_y = g_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 43:
        dot_x = fret_7
        dot_y = g_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 44:
        dot_x = fret_8
        dot_y = g_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 45:
        dot_x = fret_9
        dot_y = g_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 46:
        dot_x = fret_10
        dot_y = g_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 47:
        dot_x = fret_11
        dot_y = g_row
        make_dot(screen, dot_x, dot_y)

    if note_dot_answer == 48:
        dot_x = fret_0
        dot_y = b_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 49:
        dot_x = fret_1
        dot_y = b_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 50:
        dot_x = fret_2
        dot_y = b_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 51:
        dot_x = fret_3
        dot_y = b_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 52:
        dot_x = fret_4
        dot_y = b_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 53:
        dot_x = fret_5
        dot_y = b_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 54:
        dot_x = fret_6
        dot_y = b_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 55:
        dot_x = fret_7
        dot_y = b_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 56:
        dot_x = fret_8
        dot_y = b_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 57:
        dot_x = fret_9
        dot_y = b_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 58:
        dot_x = fret_10
        dot_y = b_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 59:
        dot_x = fret_11
        dot_y = b_row
        make_dot(screen, dot_x, dot_y)

    if note_dot_answer == 60:
        dot_x = fret_0
        dot_y = high_e_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 61:
        dot_x = fret_1
        dot_y = high_e_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 62:
        dot_x = fret_2
        dot_y = high_e_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 63:
        dot_x = fret_3
        dot_y = high_e_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 64:
        dot_x = fret_4
        dot_y = high_e_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 65:
        dot_x = fret_5
        dot_y = high_e_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 66:
        dot_x = fret_6
        dot_y = high_e_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 67:
        dot_x = fret_7
        dot_y = high_e_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 68:
        dot_x = fret_8
        dot_y = high_e_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 69:
        dot_x = fret_9
        dot_y = high_e_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 70:
        dot_x = fret_10
        dot_y = high_e_row
        make_dot(screen, dot_x, dot_y)
    if note_dot_answer == 71:
        dot_x = fret_11
        dot_y = high_e_row
        make_dot(screen, dot_x, dot_y)


def make_dot(screen, dot_x, dot_y):
    dot = pygame.Surface((10,10))
    dot.fill((0,255,0))
    screen.blit(dot, (dot_x,dot_y))

def check_mouse(button_x, button_y, mouse_x, mouse_y, button_wh, event, screen, color, white, num, answer):
    text = ["A", "A#/Bb", "B", "C", "C#/Db", "D", "D#/Eb", "E", "F", "F#/Gb", "G", "G#/Ab"]
    shuffle = False
    global attempts, score

    if button_x < mouse_x < button_x + button_wh and button_y < mouse_y < button_y + button_wh:
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            make_button(screen, color, button_x, button_y, button_wh, text[num])
            if answer == num:
                make_checkmark(screen)
                pygame.display.flip()
                pygame.time.delay(1000)
                time.sleep(1)
                shuffle = True
                attempts = 3
                score += 1
            else:
                attempts -= 1
                make_x(screen)
                pygame.display.flip()
                pygame.time.delay(1000)
                time.sleep(1)
                if attempts == 0:
                    shuffle = True 
                    attempts = 3
                    score = 0
        else:
            make_button(screen, white, button_x, button_y, button_wh, text[num])
    else:
        make_button(screen, color, button_x, button_y, button_wh, text[num])
    
    return shuffle

def make_lives(screen, attempts):
    
    if attempts == 3:
        heart1 = pygame.Surface((50,50))
        heart2 = pygame.Surface((50, 50))
        heart3 = pygame.Surface((50, 50))
        heart1.fill((255,49,49))
        heart2.fill((255,49,49))
        heart3.fill((255,49,49))
        screen.blit(heart1, (550,10))
        screen.blit(heart2, (610,10))
        screen.blit(heart3, (670,10))
    if attempts == 2:
        heart1 = pygame.Surface((50,50))
        heart2 = pygame.Surface((50, 50))
        heart3 = pygame.Surface((50, 50))
        heart1.fill((255,49,49))
        heart2.fill((255,49,49))
        heart3.fill((0,0,0))
        screen.blit(heart1, (550,10))
        screen.blit(heart2, (610,10))
        screen.blit(heart3, (670,10))
    if attempts == 1:
        heart1 = pygame.Surface((50,50))
        heart2 = pygame.Surface((50, 50))
        heart3 = pygame.Surface((50, 50))
        heart1.fill((255,49,49))
        heart2.fill((0,0,0))
        heart3.fill((0,0,0))
        screen.blit(heart1, (550,10))
        screen.blit(heart2, (610,10))
        screen.blit(heart3, (670,10))
    if attempts == 0:
        heart1 = pygame.Surface((50,50))
        heart2 = pygame.Surface((50, 50))
        heart3 = pygame.Surface((50, 50))
        heart1.fill((0,0,0))
        heart2.fill((0,0,0))
        heart3.fill((0,0,0))
        screen.blit(heart1, (550,10))
        screen.blit(heart2, (610,10))
        screen.blit(heart3, (670,10))

    screen.blit(heart1, (550,10))
    screen.blit(heart2, (610,10))
    screen.blit(heart3, (670,10))

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
