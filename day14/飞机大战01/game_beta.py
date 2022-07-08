# 作者: XWX
# 2022年06月15日17时27分11秒
import pygame

pygame.init()

# 初始化主窗口，创建一个屏幕数据对象screen
screen = pygame.display.set_mode((480, 700))

# 绘制背景图像
# 从指定的文件路径将图像数据从磁盘加载到内存,该图像的分辨率对应为480×700
bg = pygame.image.load("./images/background.png")
screen.blit(bg, (0, 0))     # blit 绘制图像
hero = pygame.image.load("./images/me1.png")
screen.blit(hero, (200, 500))

# 3> update 刷新屏幕显示
pygame.display.update()

# 初始化游戏时钟
clock = pygame.time.Clock()
# 定义hero_rect记录飞机的初始位置和大小等属性
hero_rect = pygame.Rect(150, 700, 102, 126)
# 游戏循环 -> 意味着游戏的正式开始！
while True:

    # 实际不能用进程挂起来实现游戏循环
    # 用游戏时钟来指定循环体内部的代码执行的频率
    # 这里直观上影响飞机运动的速度
    clock.tick(60)

    # 捕获事件,返回一个事件列表，用户可以同时触发多个事件
    event_list = pygame.event.get()

    # 处理时间
    for event in event_list:

        # 判断事件类型是否是退出事件
        if event.type == pygame.QUIT:
            print("游戏退出...")

            # quit 卸载所有的模块
            pygame.quit()

            # exit() 直接终止当前正在执行的程序
            exit()

    # 修改飞机的位置
    hero_rect.y -= 1
    if hero_rect.y==-hero_rect.height:
        # 当飞机刚好从上方完全飞出屏幕时，让其回到底部
        hero_rect.y=700
    # 调用blit方法绘制图像
    # 每次都要重绘背景图像
    screen.blit(bg, (0, 0))
    screen.blit(hero, hero_rect)

    # 调用update方法更新显示
    pygame.display.update()


pygame.quit()