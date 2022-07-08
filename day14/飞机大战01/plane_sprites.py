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
        self.rect = self.image.get_rect()  # 获取图像的尺寸属性
        self.speed = speed      # speed确定每种对象的移动速度,默认不移动，为0
    def update(self):
        # 精灵基类中默认向上图像向下移动，子类可根据需要来重写
        self.rect.y+=self.speed


class Background(GameSprite):
    def __init__(self, is_alt=False):
        # 1. 调用父类方法实现精灵的创建(image/rect/speed)
        super().__init__("./images/background.png")

    def update(self):
        super().update()


class Enemy(GameSprite):
    pass


class Hero(GameSprite):
    def __init__(self):
        super().__init__("./images/me1.png", 0)     # 初始化时默认飞机不移动

        # 确定飞机开始时的坐标
        self.rect.centerx = SCREEN_RECT.centerx
        self.rect.bottom = SCREEN_RECT.bottom - 120

    def update(self):

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



