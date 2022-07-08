# 作者: XWX
# 2022年06月15日22时20分27秒
import time
from plane_sprites import *

# 载入游戏音乐!!
pygame.init()
pygame.mixer.init()

pygame.mixer.music.load("./sound/game_music.ogg")
pygame.mixer.music.set_volume(0.2)
bullet_sound = pygame.mixer.Sound("./sound/bullet.wav")
bullet_sound.set_volume(0.2)
bomb_sound = pygame.mixer.Sound ("sound/use_bomb.wav")
bomb_sound.set_volume (0.2)

class PlaneGame(object):
    """飞机大战主游戏"""

    def __init__(self):

        # 初始化游戏时钟、主屏幕
        self.screen = pygame.display.set_mode(SCREEN_RECT.size)
        self.clock = pygame.time.Clock()

        # 初始化精灵和精灵组
        self.__create_sprites()

        # 初始化定时器事件，用于触发敌人的产生
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 1000) # 每隔1000毫秒触发一次

        # 初始化子弹的发射频率
        pygame.time.set_timer(HERO_FIRE_EVENT, 100)



    def start_game(self):
        """开始游戏循环"""
        # 播放背景音乐
        pygame.mixer.music.play(-1)
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

        # 检测键盘输入事件
        # 返回所有按键元组(元素值为0或1）
        keys_pressed = pygame.key.get_pressed()
        # 判断元组中对应的按键是否被按下
        # 同时长按两个键，按右左上下的顺序选择靠前的执行
        if keys_pressed[pygame.K_RIGHT]:
            self.hero.operate = 'right'
        elif keys_pressed[pygame.K_LEFT]:
            self.hero.operate = 'left'
        elif keys_pressed[pygame.K_UP]:
            self.hero.operate = 'up'
        elif keys_pressed[pygame.K_DOWN]:
            self.hero.operate = 'down'
        else:
            self.hero.operate = None

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
            elif event.type==HERO_FIRE_EVENT and keys_pressed[pygame.K_SPACE]:
                # 设置子弹的发射频率上限，避免长按空格键时射出一条线状的子弹轨迹
                self.hero.hero_file()
                bullet_sound.play() # 播放子弹发射音效！！！

    def __check_collide(self):

        # 碰撞检测：子弹摧毁敌机
        pygame.sprite.groupcollide(self.hero.bullets, self.enemy_group, True, True)

        # 碰撞检测：敌机撞毁英雄时游戏结束
        enemies = pygame.sprite.spritecollide(self.hero, self.enemy_group, True)
        if len(enemies) > 0:
            # 让英雄牺牲
            self.hero.kill()
            bomb_sound.play()
            time.sleep(1)
            PlaneGame.__game_over()

    def __update_sprites(self):
        # 覆盖顺序：背景<敌机<英雄<子弹

        self.back_group.update()
        self.back_group.draw(self.screen)

        self.enemy_group.update()
        self.enemy_group.draw(self.screen)

        self.hero_group.update()
        self.hero_group.draw(self.screen)

        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

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
