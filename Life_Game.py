"""
Игра "Жизнь", написанная с помощью библиотеки pygame.

Если вы хотите, чтобы в клатке появилась или исчезла жизнь - 
нажмите на неё левой кнопкой мыши.

Если вы хотите посмотреть, как будет выглядеть следующее поколение - 
нажмите правой кнопкой мыши в любое место игрового поля.

Если вы хотите очистить экран -
нажмите на колёсико мыши.
"""

import pygame as pg
import sys

#координаты начала поля
x = 5
y = 5

#высота и ширина всех клеток поля
weight = 20
height = 20

#задаётся размер дисплея
sc = pg.display.set_mode((486, 486))


class Make_Array(object):
    """
    В данном классе создаётся массив mas 20*20 из чисел 255.
    Каждый элемент массива соответствует одной кла=етке поля.
    В будущем он понадобится для определения цвета клеток поля.
    """


    def __init__(self, mas):
        self.mas = mas


    def make(self):
        """
        Создаём массив 20*20 из чисел 255
        """
        for r in range(20):
            self.mas.append([])
            for j in range(20):
                self.mas[r].append([])
                self.mas[r][j] = 255

        return self.mas


class Left_Mouse_Button(object):
    """
    В данном классе происходят изменения после нажатия левой кнопки мыши.
    """


    def __init__(self, mas, pos, x, y):
        """pos - координаты нахождения мыши во время нажатия на поле"""
        self.mas = mas
        self.pos = pos
        self.x = x
        self.y = y


    def click_1(self):
        """
        С помощью координат pos находим в какой клетке поля находилась мышка 
        и меняем цвет данной клатке, 
        заменив соответствующий ей элемент в массиве mas.
        Т.е. если элемент имел значение 255, то меняем его на 0 (и наоборот).
        Таким образом цвет клетки становится светлее или темнее.
        """
        color_of_cell = self.mas[(self.pos[0]-self.x)//24][(self.pos[1]-self.y)//24]

        if color_of_cell == 255:
            self.mas[(self.pos[0]-self.x)//24][(self.pos[1]-self.y)//24] = 0
        else:
            self.mas[(self.pos[0]-self.x)//24][(self.pos[1]-self.y)//24] = 255

        return self.mas


class Right_Mouse_Button(object):
    """
    В данном классе происходят изменения после нажатия правой кнопки мыши.
    """


    def __init__(self, mas):
        self.mas = mas


    def click_2(self):
        """
        Создаём новый массив mas_2.
        Проверяем цвета всех соседей каждой клетки.
        Если клетка жива, то добавляем 1 в счётчик num_of_bl.
        Затем, в зависимости от того, сколько живых соседей есть у клетки, 
        мы меняем или не меняем цвет клетки.
        """
        mas_2 = []
        for r in range(20):
            mas_2.append([])
            for j in range(20):
                mas_2[r].append([])
                mas_2[r][j] = 255
        for r in range(1, 19):
            for j in range(1, 19):
                num_of_bl = 0
                if self.mas[r-1][j] == 0:
                    num_of_bl+=1
                if self.mas[r+1][j] == 0:
                    num_of_bl+=1
                if self.mas[r][j-1] == 0:
                    num_of_bl+=1
                if self.mas[r][j+1] == 0:
                    num_of_bl+=1
                if self.mas[r-1][j-1] == 0:
                    num_of_bl+=1
                if self.mas[r+1][j+1] == 0:
                    num_of_bl+=1
                if self.mas[r-1][j+1] == 0:
                    num_of_bl+=1
                if self.mas[r+1][j-1] == 0:
                    num_of_bl+=1

                if (num_of_bl == 2 or num_of_bl == 3) and self.mas[r][j] == 0:
                    mas_2[r][j] = 0

                elif num_of_bl == 3 and self.mas[r][j] == 255:
                    mas_2[r][j] = 0

                else:
                    mas_2[r][j] = 255

        return mas_2


class Central_Mouse_Button(object):
    """
    В данном классе происходят изменения после нажатия центральной кнопки мыши.
    """


    def __init__(self, mas):
        self.mas = mas


    def click_3(self):
        """
        Здесь очищается поле => все клетки становятся светлыми => все элементы mas вновь становятся 255.
        """
        for r in range(20):
            self.mas.append([])
            for j in range(20):
                self.mas[r].append([])
                self.mas[r][j] = 255

        return self.mas

mas = []
mas = Make_Array(mas).make()

while 1:
    for i in pg.event.get():
        if i.type == pg.QUIT:
            #Если нажат крестик, то закрываем программу.
            sys.exit()

        for r in range(20):
            for j in range(20):
                """
                Рисует 400 клеток на поле. 
                Испльзует массив mas для создания цветов клеток
                """
                pg.draw.rect(sc, (abs(mas[r][j]-100), abs(mas[r][j]-80), abs(mas[r][j]-10)), (x+r*24, y+j*24, weight, height))

        #обновляет экран игры, добавив все изменения
        pg.display.update()

        if i.type == pg.MOUSEBUTTONDOWN:

            if i.button == 1:
                #Если пользователь нажал левую кнопку мыши
                mas = Left_Mouse_Button(mas, i.pos, x, y).click_1()

                #обновляет экран игры, добавив все изменения
                pg.display.update()

            elif i.button == 3:
                #Если пользователь нажал правую кнопку мыши
                mas = Right_Mouse_Button(mas).click_2()

                #обновляет экран игры, добавив все изменения
                pg.display.update()

            elif i.button == 2:
                #Если пользователь нажал среднюю кнопку мыши
                mas = Central_Mouse_Button(mas).click_3()

                #обновляет экран игры, добавив все изменения
                pg.display.update()
 
    pg.time.delay(0)
