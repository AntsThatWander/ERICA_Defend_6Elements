import images
import random 

class monster:
    lv = 0
    hp = 0
    mv = 0
    ad = 1
    height = 0
    shield = 0
    def __init__(self, image, lv, mv, shield):
        self.weight = 1280
        self.image = image
        self.lv = lv
        self.ad = 1 * (lv+1)
        self.mv = mv
        hl = [30, 170, 310, 450, 590]
        self.height = random.choice(hl)
        self.shield = shield
    def getlv(self):
        return self.lv
    def gethp(self):
        return self.hp
    def sethp(self, hp):
        if hp - self.shield > 0 :
            self.hp -= (hp-self.shield)
    def getmv(self):
        return self.mv
    def setmv(self,mv):
        self.mv -= mv
    def getad(self):
        return self.ad
    def setad(self):
        self.ad -= ad
    def move(self):
        self.weight = self.weight - self.mv
    def getpos(self):
        return [self.weight, self.height]
    def is_spawn(self):
        return False
    def is_ranged(self):
        return False

class ling(monster):
    def __init__(self, hp):
        super().__init__(images.Lv0_monster()['ling'], 0, 5, 0)
        self.hp = hp

class sting(monster):
    def __init__(self, hp, weight, height):
        super().__init__(images.Lv0_monster()['sting'], 0, 3, 0)
        self.hp = hp
        self.weight = weight
        self.height = height
    

class ball(monster):
    def __init__(self, hp, weight, height):
        super().__init__(images.Lv0_monster()['ball'], 0, 3, 0)
        self.hp = hp
        self.weight = weight
        self.height = height

class zombie(monster):
    def __init__(self, hp):
        super().__init__(images.Lv1_monster()['zombie'], 1, 7, 0)
        self.hp = hp

class zombie_b(monster):
    def __init__(self, hp):
        super().__init__(images.Lv1_monster()['zombie_barrier'], 1, 7, 1)
        self.hp = hp


class horror(monster):
    def __init__(self, hp):
        super().__init__(images.Lv2_monster()['nighthorror'], 2, 10, 0)
        self.hp = hp
    def spawn(self,ls):
        if self.hp<0:
            l1 = ling(1)
            l2 = ling(1)
            ls.append(l1,l2)
    def is_spawn(self):
        return True

class crawler(monster):
    def __init__(self, hp):
        super().__init__(images.Lv2_monster()['crawler'], 2, 3, 0)
        self.hp = hp
    def move(self):
        if self.weight>580:
            self.weight = self.weight - self.mv
    def is_ranged(self):
        return True
    def ranged(self,ls):
        if self.weight<=780:
            st = sting(1)
            ls.append(st)

class cannon(monster):
    def __init__(self, hp):
        super().__init__(images.Lv3_monster()['cannon'], 3, 1, 5)
        self.hp = hp
    def move(self):
        if self.weight>1080:
            self.weight = self.weight - self.mv
    def is_ranged(self):
        return True
    def ranged(self,ls):
        if self.weight<=580:
            st = sting(1)
            ls.append(st)

class seer(monster):
    def __init__(self, hp):
        super().__init__(images.Lv3_monster()['seer'], 3, 10, 0)
        self.hp = hp

class black(monster):
    def __init__(self, hp, height):
        super().__init__(images.Lv4_monster()['black'], 4, 5, 5)
        self.hp = hp
        self.height = height

class final(monster):
    def __init__(self, hp):
        super().__init__(images.Lv5_monster()['final'], 200, 3, 10)
        self.hp = hp
        self.height = 30

    
    
        


