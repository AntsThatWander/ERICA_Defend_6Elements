import images
import random 

class monster:
    lv = 0
    hp = 0
    mv = 0
    ad = 1
    height = 0
    def __init__(self, image, lv, mv):
        self.weight = 1280
        self.image = image
        self.lv = lv
        self.ad = 1 * (lv+1)
        self.mv = mv
        hl = [30, 170, 310, 450, 590]
        self.height = random.choice(hl)
    def getlv(self):
        return self.lv
    def gethp(self):
        return self.hp
    def sethp(self, hp):
        self.hp -= hp
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
        super().__init__(images.Lv0_monster()['ling'], 0, 30)
        self.hp = hp

class sting(monster):
    def __init__(self, hp):
        super().__init__(images.Lv0_monster()['sting'], 0, 10)
        self.hp = hp
    def spawn(self, list):
        ling1 = ling(1,)

class ball(monster):
    def __init__(self, hp):
        super().__init__(images.Lv0_monster()['ball'], 0, 10)
        self.hp = hp

class zombie(monster):
    def __init__(self, hp):
        super().__init__(images.Lv1_monster()['zombie'], 1, 30)
        self.hp = hp

class zombie_b(monster):
    def __init__(self, hp):
        super().__init__(images.Lv1_monster()['zombie_barrier'], 1, 30)
        self.hp = hp
    def sethp(self, hp):
        self.hp -= (hp-2)

class horror(monster):
    def __init__(self, hp):
        super().__init__(images.Lv2_monster()['nighthorror'], 2, 40)
        self.hp = hp
    def spawn(self,ls):
        if(self.hp<0):
            l1 = ling(1)
            l2 = ling(1)
            ls.append(l1,l2)
    def is_spawn(self):
        return True

class crawler(monster):
    def __init__(self, hp):
        super().__init__(images.Lv2_monster()['crawler'], 2, 10)
        self.hp = hp
    def move(self):
        if(self.weight>580):
            self.weight = self.weight - self.mv
    def is_ranged(self):
        return True
    def ranged(self,ls):
        if(self.weight<=580):
            st = sting(1)
            ls.append(st)

class cannon(monster):
    def __init__(self, hp):
        super().__init__(images.Lv3_monster()['cannon'], 3, 10)
        self.hp = hp
    def move(self):
        if(self.weight>1080):
            self.weight = self.weight - self.mv
    def is_ranged(self):
        return True
    def ranged(self,ls):
        if(self.weight<=580):
            st = sting(1)
            ls.append(st)

class seer(monster):
    def __init__(self, hp):
        super().__init__(images.Lv3_monster()['seer'], 3, 20)
        self.hp = hp

class black(monster):
    def __init__(self, hp, height):
        super().__init__(images.Lv4_monster()['black'], 4, 20)
        self.hp = hp
        self.height = height

class final(monster):
    def __init__(self, hp):
        super().__init__(images.Lv5_monster()['final'], 5, 10)
        self.hp = hp
    
    
        


