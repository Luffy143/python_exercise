# 作者: XWX
# 2022年06月15日22时20分27秒
import time
from plane_sprites import *

class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):

        # 初始化游戏时钟、主屏幕、
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()

        # 初始化精灵和精灵组
        self.__create_sprites()

        # 初始化定时器事件，用于触发敌人的产生
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000) # 每隔1000毫秒触发一次

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

        # 创建背景的精灵组
        back1=Background()
        back2=Background(True)
        # 此处若忘记传入True，则两张背景图重合，飞机在移动时会有重影
        '''
        实现背景滚动需要设置两张背景图片，第一张与屏幕完全贴合，第二张则位于屏幕上方，
        两张图片同时向下移动，当任意一张图片的y坐标大于屏幕的高度height时说明完全离开屏幕下方，
        此时将其y修改为-height,即重新回到上方
        '''
        self.back_group = pygame.sprite.Group(back1,back2)

        # 创建英雄
        self.hero = Hero()
        self.hero_group = pygame.sprite.Group(self.hero)

        # 创建敌机的精灵组
        self.enemy_group = pygame.sprite.Group()

    def __event_handler(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                # 检测鼠标退出事件
                PlaneGame.__game_over()
            elif event.type==CREATE_ENEMY_EVENT:
                # 检测敌机出现事件
                if self.enemy_group.__len__()<5:
                    # 控制屏幕中敌人的数量
                    new_enemy=Enemy()
                    self.enemy_group.add(new_enemy)

        # 检测键盘输入事件
        # 返回所有按键元组(元素值为0或1）
        keys_pressed = pygame.key.get_pressed()
        # 判断元组中对应的按键是否被按下
        # 同时长按两个键，按右左上下的顺序选择靠前的执行
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.move_operate='right'
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.move_operate = 'left'
        elif keys_pressed[pygame.K_UP]:
            self.hero.move_operate = 'up'
        elif keys_pressed[pygame.K_DOWN]:
            self.hero.move_operate = 'down'
        else:
            self.hero.move_operate = None

    def __check_collide(self):
        # 碰撞检测：敌机撞毁英雄时游戏结束
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            # 让英雄牺牲
            self.hero.kill()
            time.sleep(2)
            PlaneGame.__game_over()

    def __update_sprites(self):
        # 覆盖顺序：背景<敌机<英雄

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

    @staticmethod
    def __game_over():
        """静态方法，退出游戏"""
        print("游戏结束")
        pygame.quit()
        exit()  # 进程结束


if __name__=='__main__':
    pygame.init()
    # 初始化游戏
    game = PlaneGame()
    # 开启游戏循环
    game.start_game()
    pygame.quit()
