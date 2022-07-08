# 作者: XWX
# 2022年06月15日22时26分33秒

import pygame
import random

# 定义屏幕大小和尺寸
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

# 定义刷新频率为60
FRAME_PER_SEC= 60

# 创建敌机的定时器常量，为事件定义不同名字的常量，从而能够区分，从24算起
CREATE_ENEMY_EVENT = pygame.USEREVENT

# 英雄发射子弹事件，为事件定义不同名字的常量，从而能够区分
HERO_FIRE_EVENT = pygame.USEREVENT + 1

class GameSprite(pygame.sprite.Sprite):
    """定义精灵基类（精灵指一切需要显示给用户的对象），包含图像名和图像大小两个属性"""
    def __init__(self,image_name,speed=0):
        # 在重写初始化方法时，一定要先super()一下父类的__init__ 方法
        super().__init__()

        self.image = pygame.image.load(image_name)
        # 获取图像的尺寸属性,默认(x,y)=(0,0)
        self.rect = self.image.get_rect()
        self.speed = speed      # speed确定每种对象的移动速度,默认不移动，为0
    def update(self):
        # 精灵基类中默认向上图像向下移动，子类可根据需要来重写
        self.rect.y+=self.speed


class Background(GameSprite):
    def __init__(self, is_top=False):
        # 1. 调用父类方法实现精灵的创建(image/rect/speed)
        super().__init__("./images/background.png",speed=2)

        if is_top:
            self.rect.y=-self.rect.height

    def update(self):
        super().update()
        # 当图片完全离开屏幕下方时，将其重新置于屏幕上方
        if self.rect.y>self.rect.height:
            self.rect.y=-self.rect.height

class Enemy(GameSprite):
    def __init__(self):
        super().__init__("./images/enemy1.png")

        # 指定敌机的初始速度
        self.speed = 3

        # 3. 指定敌机的初始随机位置
        self.rect.bottom = 0
        # 屏幕宽度减去飞机宽度得到有效的初始x的最大值
        max_x = SCREEN_RECT.width - self.rect.width
        self.rect.x = random.randint(0, max_x)

    def update(self):
        super().update()    # 保持敌机一直向下运动
        '''敌机在水平方向随机移动
        x_increment=random.randint(-1,1)
        self.rect.x += x_increment*10'''

        # 判断是否飞出屏幕，如果是，需要从精灵组删除敌机
        # kill方法可以将精灵从所有精灵组中移出，精灵就会被自动销毁
        if self.rect.y >= SCREEN_RECT.height:
            # 飞机从下方离开屏幕
            self.kill()
        if self.rect.right<0 or self.rect.x>SCREEN_RECT.width:
            # 飞机从水平方向离开屏幕
            self.kill()

class Hero(GameSprite):
    def __init__(self):
        super().__init__("./images/me1.png", 10)

        # 确定飞机开始时的坐标
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.operate=None  # 定义当前移动操作（上下左右）
        # 定义该英雄所发出的子弹精灵组
        self.bullets = pygame.sprite.Group()

    def update(self):
        # 通过键盘事件实现上下左右的移动
        if self.operate=='up':
            self.rect.y-=self.speed
        elif self.operate=='down':
            self.rect.y+=self.speed
        elif self.operate=='left':
            self.rect.x-=self.speed
        elif self.operate=='right':
            self.rect.x+=self.speed
        self.operate=None

        # 控制英雄不能离开屏幕
        if self.rect.x<0:
            self.rect.x=0
        elif self.rect.right>SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        if self.rect.y<0:
            self.rect.y=0
        elif self.rect.bottom>SCREEN_RECT.bottom:
            self.rect.bottom=SCREEN_RECT.bottom

    def hero_file(self):
        """开火初始化一发子弹"""

        # 1. 创建子弹精灵
        bullet = Bullet()

        # 2. 设置精灵的位置
        bullet.rect.bottom = self.rect.y
        bullet.rect.centerx = self.rect.centerx

        # 3. 将精灵添加到精灵组
        self.bullets.add(bullet)

class Bullet(GameSprite):
    def __init__(self):
        # 调用父类方法，设置子弹图片，设置初始速度
        super().__init__("./images/bullet1.png", -5)

    def update(self):
        # 发出的子弹会一直向上移动
        # 调用父类方法，让子弹沿垂直方向飞行
        super().update()

        # 判断子弹是否飞出屏幕
        if self.rect.bottom < 0:
            self.kill()



