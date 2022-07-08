# 作者: XWX
# 2022年06月15日22时26分33秒

import pygame

# 定义屏幕大小和尺寸
SCREEN_RECT = pygame.Rect(0, 0, 480, 700)

# 定义刷新频率为60
FRAME_PER_SEC= 60

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
    pass


class Hero(GameSprite):
    def __init__(self):
        super().__init__("./images/me1.png", 10)

        # 确定飞机开始时的坐标
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120
        self.move_operate=None  # 定义当前操作类型（上下左右）

    def update(self):
        # 通过键盘事件实现上下左右的移动
        if self.move_operate=='up':
            self.rect.y-=self.speed
        elif self.move_operate=='down':
            self.rect.y+=self.speed
        elif self.move_operate=='left':
            self.rect.x-=self.speed
        elif self.move_operate=='right':
            self.rect.x+=self.speed
        self.move_operate=None


        # 控制英雄不能离开屏幕
        if self.rect.x<0:
            self.rect.x=0
        elif self.rect.right>SCREEN_RECT.right:
            self.rect.right = SCREEN_RECT.right
        if self.rect.y<0:
            self.rect.y=0
        elif self.rect.bottom>SCREEN_RECT.bottom:
            self.rect.bottom=SCREEN_RECT.bottom

class Bullet(GameSprite):
    pass



