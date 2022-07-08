# 作者: XWX
# 2022年06月15日22时20分27秒
import pygame
from plane_sprites import *

class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):
        """
        初始化游戏时钟、主屏幕、
        """
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()

        # 初始化精灵和精灵组
        self.__create_sprites()

    def start_game(self):
        """开始游戏循环"""
        while True:
            # 1. 设置刷新帧率
            self.clock.tick(FRAME_PER_SEC)  # 刷新频率用常量表示
            # 2. 事件监听
            self.__event_handler()
            # 3. 碰撞检测
            self.__check_collide()
            # 4. 更新/绘制精灵组
            self.__update_sprites()
            # 5. 更新显示
            pygame.display.update()

    def __create_sprites(self):
        """作用是创建精灵对象和精灵组"""

        back1=Background()
        self.back_group = pygame.sprite.Group(back1)

        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)


    def __event_handler(self):
        pass

    def __check_collide(self):
        pass

    def __update_sprites(self):

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)


if __name__=='__main__':
    pygame.init()
    # 初始化游戏
    game = PlaneGame()
    # 开启游戏循环
    game.start_game()
    pygame.quit()
