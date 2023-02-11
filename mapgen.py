from classes import *
def genMap(ground, wall):
    walls.clear()
    grounds.clear()
    x = 0
    y= 0
    map_elements = ["#", "_"]
    map1 = []
    map_row = ""
    for i in range(12):
        if (i == 0) or (i == 11):
            for j in range(12): map_row += map_elements[0]
        else:
            for j in range(12):
                if (j == 0) or (j == 11): map_row += map_elements[0]
                elif (j == 11) : map_row += map_elements[1]
                elif map_row.find("#_"): map_row += "_"
                else : map_row += map_elements[random.randint(0, 1)]
        map1.append(map_row)
        map_row = ""
    for i in range(len(map1)):
        for j in range(len(map1[i])):
            if map1[i][j] == '_':
                Floor(ground, x, y)
            elif map1[i][j] == '#':
                Block(wall, x, y)
            x += 32
        y += 32
        x = 0
    
