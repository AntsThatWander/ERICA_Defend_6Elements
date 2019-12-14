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

#카드와 이펙트 cards and cards' effects
def red_card():
    burning_1 = pygame.image.load("resources/my_resources/Red_burning_1.png")
    burning_2 = pygame.image.load("resources/my_resources/Red_burning_2.png")
    burning_3 = pygame.image.load("resources/my_resources/Red_burning_3.png")
    burning_effect = pygame.image.load("resources/my_resources/larva_road.png")
    dragon_1 = pygame.image.load("resources/my_resources/Red_dragon_1.png")
    dragon_2 = pygame.image.load("resources/my_resources/Red_dragon_2.png")
    dragon_3 = pygame.image.load("resources/my_resources/Red_dragon_3.png")
    dragon_effect = pygame.image.load("resources/my_resources/fire.png")
    burning = [[burning_1, burning_2, burning_3], burning_effect]
    dragon = [[dragon_1, dragon_2, dragon_3], dragon_effect]
    return {'burning' : burning, 'dragon' : dragon}
def green_card():
    lifec_1 = pygame.image.load("resources/my_resources/Green_lifeconsume_1.png")
    lifec_2 = pygame.image.load("resources/my_resources/Green_lifeconsume_2.png")
    lifec_3 = pygame.image.load("resources/my_resources/Green_lifeconsume_3.png")
    revng_1 = pygame.image.load("resources/my_resources/Green_revenge_1.png")
    revng_2 = pygame.image.load("resources/my_resources/Green_revenge_2.png")
    revng_3 = pygame.image.load("resources/my_resources/Green_revenge_3.png")
    revng_effect = pygame.image.load("resources/my_resources/revenge.png")
    lifec = [lifec_1, lifec_2, lifec_3]
    revng = [[revng_1, revng_2, revng_3], revng_effect]
    return {'lifec' : lifec, 'revng' : revng}
def blue_card():
    again_1 = pygame.image.load("resources/my_resources/Blue_firstagain_1.png")
    again_2 = pygame.image.load("resources/my_resources/Blue_firstagain_2.png")
    again_3 = pygame.image.load("resources/my_resources/Blue_firstagain_3.png")
    world_1 = pygame.image.load("resources/my_resources/Blue_theworld_1.png")
    world_2 = pygame.image.load("resources/my_resources/Blue_theworld_2.png")
    world_3 = pygame.image.load("resources/my_resources/Blue_theworld_3.png")
    world_effect = pygame.image.load("resources/my_resources/theworld.png")
    again = [again_1, again_2, again_3]
    world = [[world_1, world_2, world_3], world_effect]
    return {'again' : again, 'world' : world}
def yellow_card():
    wrath_1 = pygame.image.load("resources/my_resources/Yellow_protect_1.png")
    wrath_2 = pygame.image.load("resources/my_resources/Yellow_protect_2.png")
    wrath_3 = pygame.image.load("resources/my_resources/Yellow_protect_3.png")
    wrath_effect = pygame.image.load("resources/my_resources/wrath.png")
    protect_1 = pygame.image.load("resources/my_resources/Yellow_wrath_1.png")
    protect_2 = pygame.image.load("resources/my_resources/Yellow_wrath_2.png")
    protect_3 = pygame.image.load("resources/my_resources/Yellow_wrath_3.png")
    protect_effect = pygame.image.load("resources/my_resources/protected.png")
    wrath = [[wrath_1, wrath_2, wrath_3], wrath_effect]
    protect = [[protect_1, protect_2, protect_3], protect_effect]
    return {'wrath' : wrath, 'protect' : protect}
def purple_card():
    blood_1 = pygame.image.load("resources/my_resources/Purple_bloodfeast_1.png")
    blood_2 = pygame.image.load("resources/my_resources/Purple_bloodfeast_2.png")
    blood_3 = pygame.image.load("resources/my_resources/Purple_bloodfeast_3.png")
    blood_effect = pygame.image.load("resources/my_resources/bloodfeast.png")
    corplosion_1 = pygame.image.load("resources/my_resources/Purple_corplosion_1.png")
    corplosion_2 = pygame.image.load("resources/my_resources/Purple_corplosion_2.png")
    corplosion_3 = pygame.image.load("resources/my_resources/Purple_corplosion_3.png")
    blood = [[blood_1, blood_2, blood_3], blood_effect]
    corplosion = [corplosion_1, corplosion_2, corplosion_3]
    return {'blood' : blood, 'corplosion' : corplosion}
def jade_card():
    cloudance_1 = pygame.image.load("resources/my_resources/Jade_clouddance_1.png")
    cloudance_2 = pygame.image.load("resources/my_resources/Jade_clouddance_2.png")
    cloudance_3 = pygame.image.load("resources/my_resources/Jade_clouddance_3.png")
    mirror_1 = pygame.image.load("resources/my_resources/Jade_mirror_1.png")
    mirror_2 = pygame.image.load("resources/my_resources/Jade_mirror_2.png")
    mirror_3 = pygame.image.load("resources/my_resources/Jade_mirror_3.png")
    cloudance = [cloudance_1, cloudance_2, cloudance_3]
    mirror = [mirror_1, mirror_2, mirror_3]
    return {'cloudance' : cloudance, 'mirror' : mirror}




#승리, 패배 win, lose
def result():
    win = pygame.image.load("resources/my_resources/win.png")
    lose = pygame.image.load("resources/my_resources/lose.png")
    return (lose, win)
    





