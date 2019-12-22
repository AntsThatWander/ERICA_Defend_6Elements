import pygame
import images
import random
import monster






#초기화
pygame.init()
width, height = 1280, 960
screen = pygame.display.set_mode((width, height))

#폰트
font = pygame.font.Font(None,30)


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
#현재 이미지 값 current image color
cur_color = 'red'
#화살 생성 주기
arrow_rate = 10
arrow_count = arrow_rate - 1
#이펙트 effects
effect = images.effect()
#화살
arrows = []
#몬스터 등장 시간
bad_rate = 10
bad_count = 0
#몬스터 리스트
badguys = []
#출력 몬스터 리스트
seebadguys = []
#몬스터 탄환
monarrow = []

#성 체력
healthvalue = 200
#wave
wave = [[],[],[],[]]
zombie = [20,0]
zombie_b = [20,0]
horror = [10,1]
crawler = [10,1]
seer = [10,2]
cannon = [5,2]
final = [1,3]
height = [30, 170, 310, 450, 590]
for x in range(0,4):
    if x == zombie[1] :
        zombie[1] += 1
        for y in range(0,zombie[0]):
            m = monster.zombie(20)
            wave[x].append(m)
    if x == zombie_b[1] :
        zombie_b[1] += 1
        for y in range(0,zombie_b[0]):
            m = monster.zombie_b(20)
            wave[x].append(m)
    if x == horror[1] :
        horror[1] += 1
        for y in range(0,horror[0]):
            m = monster.horror(20)
            wave[x].append(m)
    if x == crawler[1] :
        crawler[1] += 1
        for y in range(0,crawler[0]):
            m = monster.crawler(40)
            wave[x].append(m)
    if x == seer[1] :
        seer[1] += 1
        for y in range(0,seer[0]):
            m = monster.seer(40)
            wave[x].append(m)
    if x == cannon[1] :
        cannon[1] += 1
        for y in range(0,cannon[0]):
            m = monster.cannon(50)
            wave[x].append(m)
    if x == 3 :
            m = monster.final(100)
            wave[x].append(m)
for x in range(0,4):
    random.shuffle(wave[x])
    for y in range(0,5):
        if y != 0 and y != 4:
            lord = monster.black(50,30+140*y)
            wave[x].append(lord)
badguys = wave[0]
left = len(wave[0]) + len(wave[1]) + len(wave[2]) + len(wave[3]) 

#FPS
clock = pygame.time.Clock()


running = 1
excitcode = 0

#화면 띄우기
while running:
    clock.tick(60)
    bad_count += 1
    #색깔 관리
    active_player = player[cur_color]
    active_mirror = mirror[cur_color]
    active_button = button[cur_color]

    #화면을 깨끗하게 한다.
    screen.fill((255,255,255)) #RGB
    
    #모든 요소들을 다시 그린다.#blit은 다시 그리기
    for x in range(5):
            screen.blit(images.tent_road,(0,(x+1)*140-110))
            screen.blit(images.tent,(0,(x+1)*140-110))
            if(cur_color == 'red' or cur_color == 'blue' or cur_color == 'purple') :
                screen.blit(effect[cur_color],(300,(x+1)*140-110))
            else:
                screen.blit(images.pave_road,(300,(x+1)*140-110))

    if(cur_color == 'yellow') :
        screen.blit(effect['yellow'], (200,30))
    else:
        screen.blit(images.castle, (200,30))
    if(cur_color == 'green'):
        screen.blit(effect['green'], (200,30))
    screen.blit(images.ball_room, (0,730))
    screen.blit(images.card_room, (230,730))
    screen.blit(images.score,(0,0))
    screen.blit(images.Ehealth,(0,0))
    screen.blit(active_button,(15,750))
   
    #화살 리스트와 플레이어 이미지 관리
    arrow_count += 1
    if arrow_count==arrow_rate :
        arrows.append([[playpos[0], playpos[1]+32], images.arrow()[cur_color]])
        arrow_count = 0
        screen.blit(pshoot, playpos)
    else :
        screen.blit(active_player, playpos)
    #화살 이미지 관리
    for bullet in arrows:
        bullet[0][0] += 30
        if(bullet[0][0]>1280) :
            arrows.pop(0)
        else:
            screen.blit(bullet[1], bullet[0])

    #나쁜 놈들 리스트 정렬
    if(not wave[0]):
        badguys = wave[1]
 
    if(not wave[1]):
        badguys = wave[2]
 
    if(not wave[2]):
        badguys = wave[3]

    #나쁜 놈들 소환
    if(bad_count == bad_rate and badguys):
        bad_count = 0
        seebadguys.append(badguys[0])
        badguys.pop(0)
    #나쁜 놈들 충돌 크기 조정
    windex = 0
    for badguy in seebadguys:
        badrect = pygame.Rect(badguy.image.get_rect())
        badrect.top = badguy.height
        badrect.left = badguy.weight
        #성 공격
        if badrect.left < 300:
            healthvalue -= badguy.getad()
            seebadguys.pop(windex)
        else :
            badguy.move()
            if(badguy.is_ranged()):
                badguy.ranged(monarrow)
                monarrow_count = 0
        #화살과의 충돌
        bindex = 0
        for bullet in arrows:
            bullrect = pygame.Rect(bullet[1].get_rect())
            bullrect.left = bullet[0][0]
            bullrect.top = bullet[0][1]
            if badrect.colliderect(bullrect):
                badguy.sethp(20)
                if(badguy.gethp()<=0):
                    seebadguys.pop(windex)
                    left -= 1
                arrows.pop(bindex)
            bindex += 1
        windex += 1
    for badguy in seebadguys:
        screen.blit(badguy.image, badguy.getpos())
    bindex = 0
    #몬스터 탄환
    for bullet in monarrow:
        bullrect = pygame.Rect(bullet.image.get_rect())
        bullrect.top = bullet.height
        bullrect.left = bullet.weight
        if bullrect.left < 300:
            healthvalue -= bullet.getad()
            monarrow.pop(bindex)
        else :
            bullet.move()
    for bullet in monarrow:
        screen.blit(bullet.image, bullet.getpos())

    #체력 감소
    for health in range((200-healthvalue)//2):
        screen.blit(images.health0, (200-(health+1)*2,0))
    
    #남은 수
    text = font.render("left : "+str(left), True, (255,255,255))
    screen.blit(text, [1000,0])

    #화면을 다시 그린다.
    pygame.display.flip() 

    #게임 이벤트
    for event in pygame.event.get(): 
        #게임 종료
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)
        #이동 moving
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w or  event.key == pygame.K_UP:
                keys[0] = True
            elif event.key == pygame.K_s or  event.key == pygame.K_DOWN:
                keys[1] = True
        #색깔 바꾸기 changing color
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
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or  event.key == pygame.K_UP:
                keys[0] = False
            elif event.key == pygame.K_s or  event.key == pygame.K_DOWN:
                keys[1] = False


    #플레이어 이동 범위 제한 player movement range limits
    if keys[0] and playpos[1]>30:
        playpos[1] = playpos[1] - 140
    elif keys[1] and playpos[1]<590:
        playpos[1] = playpos[1] + 140
    
    #이겼는가?
    if not wave[0] and not wave[1] and not wave[2] and not wave[3] and not seebadguys:
        running = 0
        exitcode = 1
    if healthvalue <= 0:
        running = 0
        exitcode = 0
    
#승리와 패배 처리
screen.blit(images.result()[exitcode], (0,0))
while True :
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            pygame.quit()
            exit(0)
    pygame.display.flip()
    

