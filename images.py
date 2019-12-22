import pygame
#이미지를 가져온다. 나중에 클래스로 묶도록 한다. Load images
#나중에 몬스터들은 체력(전체, 현재), 이동속도, 이미지, 레벨을 포함하는 객체로 다시 만들도록 한다.
def Lv0_monster():
    ling = pygame.image.load("resources/my_resources/nighthorror_ling.png")
    sting = pygame.image.load("resources/my_resources/sting.png")
    ball = pygame.image.load("resources/my_resources/cannon_ball.png")
    return {'ling' : ling, 'sting' : sting, 'ball' : ball}
def Lv1_monster():
    zombie = pygame.image.load("resources/my_resources/zombie.png")
    zombie_barrier = pygame.image.load("resources/my_resources/zombie_barrier.png")
    return {'zombie' : zombie, 'zombie_barrier' : zombie_barrier}
def Lv2_monster():
    nighthorror = pygame.image.load("resources/my_resources/nighthorror.png")
    crawler = pygame.image.load("resources/my_resources/crawler.png")
    return {'nighthorror' : nighthorror, 'crawler' : crawler}
def Lv3_monster():
    cannon = pygame.image.load("resources/my_resources/cannon.png")
    seer = pygame.image.load("resources/my_resources/overseer.png")
    return {'cannon' : cannon, 'seer' : seer}
def Lv4_monster():
    black = pygame.image.load("resources/my_resources/Black_lord.png")
    return {'black' : black}
def Lv5_monster():
    final = pygame.image.load("resources/my_resources/Final_lord.png")
    return {'final' : final}

#플레이어, 환영 그리고 화살 players, mirrors and arrows
def player():
    red = pygame.image.load("resources/my_resources/player_ready_Red.png")
    green = pygame.image.load("resources/my_resources/player_ready_Green.png")
    blue = pygame.image.load("resources/my_resources/player_ready_Blue.png")
    yellow = pygame.image.load("resources/my_resources/player_ready_Yellow.png")
    purple = pygame.image.load("resources/my_resources/player_ready_Purple.png")
    jade = pygame.image.load("resources/my_resources/player_ready_Jade.png")
    fin = pygame.image.load("resources/my_resources/player_shoot.png")
    return {'red' : red, 'green' : green, 'blue' : blue, 'yellow' : yellow, \
        'purple' : purple, 'jade' : jade, 'shoot' : fin} 
def mirror():
    red = pygame.image.load("resources/my_resources/mirror_ready_Red.png")
    green = pygame.image.load("resources/my_resources/mirror_ready_Green.png")
    blue = pygame.image.load("resources/my_resources/mirror_ready_Blue.png")
    yellow = pygame.image.load("resources/my_resources/mirror_ready_Yellow.png")
    purple = pygame.image.load("resources/my_resources/mirror_ready_Purple.png")
    jade = pygame.image.load("resources/my_resources/mirror_ready_Jade.png")
    fin = pygame.image.load("resources/my_resources/mirror_shoot.png")
    return {'red' : red, 'green' : green, 'blue' : blue, 'yellow' : yellow, \
    'purple' : purple, 'jade' : jade, 'shoot' : fin}
def arrow():
    red = pygame.image.load("resources/my_resources/arrow_Red.png")
    green = pygame.image.load("resources/my_resources/arrow_Green.png")
    blue = pygame.image.load("resources/my_resources/arrow_Blue.png")
    yellow = pygame.image.load("resources/my_resources/arrow_Yellow.png")
    purple = pygame.image.load("resources/my_resources/arrow_Purple.png")
    jade = pygame.image.load("resources/my_resources/arrow_Jade.png")
    return {'red' : red, 'green' : green, 'blue' : blue, 'yellow' : yellow, \
        'purple' : purple, 'jade' : jade}

#배경 backgrounds
ball_room = pygame.image.load("resources/my_resources/ball_room.png")
card_room = pygame.image.load("resources/my_resources/card_room.png")
pave_road = pygame.image.load("resources/my_resources/pave_road.png")
tent = pygame.image.load("resources/my_resources/tent.png")
tent_road = pygame.image.load("resources/my_resources/tent_road.png")
castle = pygame.image.load("resources/my_resources/castle_wall.png")
score = pygame.image.load("resources/my_resources/score.png")
corpse = pygame.image.load("resources/my_resources/corpse.png")
Ehealth = pygame.image.load("resources/my_resources/entire_health.png")
health0 = pygame.image.load("resources/my_resources/lv0.png")
health1 = pygame.image.load("resources/my_resources/lv1.png")
health2 = pygame.image.load("resources/my_resources/lv2.png")
health3 = pygame.image.load("resources/my_resources/lv3.png")
health4 = pygame.image.load("resources/my_resources/lv4.png")
health5 = pygame.image.load("resources/my_resources/lv5.png")


#버튼 buttons 
def button():
    Red_button = pygame.image.load("resources/my_resources/Red_button.png")
    Green_button = pygame.image.load("resources/my_resources/Green_button.png")
    Blue_button = pygame.image.load("resources/my_resources/Blue_button.png")
    Yellow_button = pygame.image.load("resources/my_resources/Yellow_button.png")
    Purple_button = pygame.image.load("resources/my_resources/Purple_button.png")
    Jade_button = pygame.image.load("resources/my_resources/Jade_button.png")
    return {'red' : Red_button, 'green' : Green_button, 'blue' : Blue_button, 'yellow' : Yellow_button, \
        'purple' : Purple_button, 'jade' : Jade_button}

#이펙트 effects

def red_effect():
    return pygame.image.load("resources/my_resources/larva_road.png")
def green_effect():
    return pygame.image.load("resources/my_resources/revenge.png")
def blue_effect():
    return pygame.image.load("resources/my_resources/theworld.png")
def yellow_effect():
    return pygame.image.load("resources/my_resources/protected.png")
def purple_effect():
    return pygame.image.load("resources/my_resources/bloodfeast.png")
def effect():
    red = red_effect()
    green = green_effect()
    blue = blue_effect()
    yellow = yellow_effect()
    purple = purple_effect()
    return {'red' : red, 'green' : green, 'blue' : blue, 'yellow' : yellow, \
        'purple' : purple}



#승리, 패배 win, lose
def result():
    win = pygame.image.load("resources/my_resources/win.png")
    lose = pygame.image.load("resources/my_resources/lose.png")
    return (lose, win)
    





