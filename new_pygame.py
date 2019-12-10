import pygame
import images

#초기화
pygame.init()
width, height = 1280, 960
screen = pygame.display.set_mode((width, height))

#플레이어 위치 player location
keys = [False, False]
playpos = [220, 310]
#버튼 사전 button dictionary
button = images.button()
#플레이어 이미지 사전 plyaer dictionary
player = images.player()
pshoot = player['shoot']
#환영 이미지 사전 mirror dictionary
mirror = images.mirror()
mshoot = player['shoot']
#화살 이미지 사전 arrow images dictionary
arrow = images.arrow()
#현재 이미지 값 current image color
cur_color = 'red'

#
acc = [0,0]
#화살
arrows = []
#레벨 0 몬스터
Lv0 = images.Lv0_monster()
#레벨 1 몬스터
Lv1 = images.Lv1_monster()
#레벨 2 몬스터
Lv2 = images.Lv2_monster()
#레벨 3 몬스터
Lv3 = images.Lv3_monster()
#레벨 4 몬스터
Lv4 = images.Lv4_monster()
#레벨 5 몬스터
Lv5 = images.Lv5_monster()


#화면 띄우기
while True:
    #이미지 변경
    active_player = player[cur_color]
    active_mirror = mirror[cur_color]
    active_button = button[cur_color]
    active_arrow = arrow[cur_color]
    #화면을 깨끗하게 한다.
    screen.fill((255,255,255)) #RGB
    
    #모든 요소들을 다시 그린다.#blit은 다시 그리기
    for x in range(5):
            screen.blit(images.tent_road,(0,(x+1)*140-110))
            screen.blit(images.tent,(0,(x+1)*140-110))
            screen.blit(images.pave_road,(300,(x+1)*140-110))
    screen.blit(images.castle, (200,30))
    screen.blit(images.ball_room, (0,730))
    screen.blit(images.card_room, (230,730))
    screen.blit(active_player, playpos)
    screen.blit(Lv1['zombie'],(400,30))
    
    # screen.blit(images.zombie_barrier,(300,30))
    # screen.blit(images.nighthorror,(500,30))
    # screen.blit(images.ling,(600,30))
    # screen.blit(images.crawler,(700,30))
    # screen.blit(images.sting,(800,80))
    # screen.blit(images.cannon,(900,30))
    # screen.blit(images.ball,(900,40))
    # screen.blit(images.black,(500,310))
    # screen.blit(images.seer,(1200,30))
    # screen.blit(images.final,(600,30))
    # screen.blit(images.card_Red, (400,735))
    screen.blit(active_button,(15,750))
   

    #화면을 다시 그린다.
    pygame.display.flip() 

    #게임 이벤트
    for event in pygame.event.get(): 
        #게임 종료
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        #이동 관련 입력
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or  event.key == pygame.K_UP:
                keys[0] = True
            elif event.key == pygame.K_s or  event.key == pygame.K_DOWN:
                keys[1] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or  event.key == pygame.K_UP:
                keys[0] = False
            elif event.key == pygame.K_s or  event.key == pygame.K_DOWN:
                keys[1] = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                cur_color = 'red'
            elif event.key == pygame.K_2:
                cur_color = 'green'
            elif event.key == pygame.K_3:
                cur_color = 'blue'
            elif event.key == pygame.K_4:
                cur_color = 'yellow'
            elif event.key == pygame.K_5:
                cur_color = 'purple'
            elif event.key == pygame.K_6:
                cur_color = 'jade'
        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     position = pygame.mouse.get_pos()
        #     acc[1] = acc[1] + 1
        #     arrows.append()
    #플레이어 이동
    if keys[0] and playpos[1]>30:
        playpos[1] = playpos[1] - 140
    elif keys[1] and playpos[1]<590:
        playpos[1] = playpos[1] + 140
