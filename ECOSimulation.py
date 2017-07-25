import matplotlib
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


def addGrass(_num):
    for i in range(_num):
        x = np.random.randint(0, size)
        y = np.random.randint(0, size)
        while grid[x][y] != 0:
            x = np.random.randint(0, size)
            y = np.random.randint(0, size)

        grid[x][y] = 1  # 1代表草


def addGrassEater(_num):
    for i in range(_num):
        x = np.random.randint(0, size)
        y = np.random.randint(0, size)
        while grid[x][y] != 0:
            x = np.random.randint(0, size)
            y = np.random.randint(0, size)

        grid[x][y] = 2  # 2代表食草动物


def addMeatEater(_num):
    for i in range(_num):
        x = np.random.randint(0, size)
        y = np.random.randint(0, size)
        while grid[x][y] != 0 or growAround(x, y, 2) == [-1, -1]:
            x = np.random.randint(0, size)
            y = np.random.randint(0, size)

        grid[x][y] = 3  # 3代表食肉动物


def growAround(_x, _y, _id):
    field = []
    if _x-1 < 0:
        x_begin = 0
    else:
        x_begin = _x-1
    if _y-1 < 0:
        y_begin = 0
    else:
        y_begin = _y-1
    if _x+1 > size-1:
        x_end = size-1
    else:
        x_end = _x+1
    if _y+1 > size-1:
        y_end = size-1
    else:
        y_end = _y+1

    for i in range(x_begin, x_end+1):
        for j in range(y_begin, y_end+1):
            if grid[i][j] == _id or grid[i][j] == _id*10:  # 2代表食草动物，1代表草，0代表空地
                field += [[i, j]]

    if len(field) == 0:  # 没有食物或者空地
        return [-1, -1]
    else:
        count = np.random.randint(0, len(field))
        return field[count]


def fieldUpdate():
    for i in range(size):
        for j in range(size):
            if grid[i][j] == 30:
                grid[i][j] = 3
            elif grid[i][j] == 20:
                grid[i][j] = 2
            elif grid[i][j] == 10:
                grid[i][j] = 1


def data_gen():
    for count in range(times):
        timesText.set_text('times: %d' % (count+1))
        for i in range(size):
            for j in range(size):
                if grid[i][j] == 3:
                    place = growAround(i, j, 2)
                    if place == [-1, -1]:
                        grid[i][j] = 0  # 食肉动物死亡
                    else:
                        grid[i][j] = 0
                        grid[place[0]][place[1]] = 30  # 食肉动物进食并移动
                        growth = growAround(i, j, 0)
                        if growth != [-1, -1]:
                            grid[growth[0]][growth[1]] = 30  # 食肉动物繁殖

                if grid[i][j] == 2:
                    place = growAround(i, j, 1)
                    if place == [-1, -1]:
                        grid[i][j] = 0  # 食草动物死亡
                    else:
                        grid[i][j] = 0
                        grid[place[0]][place[1]] = 20  # 食草动物进食并移动
                        growth = growAround(i, j, 0)
                        if growth != [-1, -1]:
                            grid[growth[0]][growth[1]] = 20  # 食草动物繁殖

                elif grid[i][j] == 1:
                    growth = growAround(i, j, 0)
                    if growth != [-1, -1]:
                        grid[growth[0]][growth[1]] = 10  # 草生长

        fieldUpdate()
        yield grid


def update(_data):
    ax.imshow(_data, interpolation='nearest', cmap='Set3', norm=norm)
    return ax

times = 100  # 迭代次数
size = 40
grid = np.zeros((size, size))  # 0代表空地
addGrass(1200)
addGrassEater(150)
addMeatEater(30)

fig = plt.figure()
ax = plt.subplot(111)
norm = matplotlib.colors.Normalize(vmin=0, vmax=3)  # 固定数值对应的颜色映射
gci = ax.imshow(grid, interpolation='nearest', cmap='Set3', norm=norm)
ax.set_xticks([])
ax.set_yticks([])
cbar = plt.colorbar(gci)  # 显示colorbar
cbar.set_ticks(np.linspace(0, 3, 4))
cbar.set_ticklabels(('Space', 'Grass', 'GrassEater', 'MeatEater'))
timesText = plt.text(-2, -2, 'times: 0')  # 左上角显示迭代次数

ani = animation.FuncAnimation(fig, update, data_gen, interval=1000, repeat=False)

plt.show()
