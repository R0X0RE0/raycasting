from classes import *
from defaults import *

map_elements = ["#", "_"]
maze_elements = ["-","+","|","."]
replace_dict = {"-":"#","+":"#","|":"#",".":"_"}

def generate_map(maze):
    map = []
    for i in range(len(maze)):
        map.append(''.join(idx if idx not in replace_dict else replace_dict[idx] for idx in maze[i]))
    return map

def genMap(ground, wall):
    grounds.clear()
    walls.clear()
    x = 0
    y= 0
   
    maze_map1 = ["+-+-+-+-+-+",
                 "|.........|",
                 "+--.--|.|.|",
                 "|.....|.|.|",
                 "|.+---+.|.|",
                 "|.|.....|.|",
                 "|.|.|.----+",
                 "|...|.....|",
                 "+-+-+-+-+-+"
                 ]
    map1 = generate_map(maze_map1)

    # map_row = ""
    # for i in range(MAP_SIZE):
    #     if (i == 0) or (i == MAP_SIZE - 1):
    #         for j in range(MAP_SIZE): map_row += map_elements[0]
    #     else:
    #         for j in range(MAP_SIZE):
    #             if (j == 0) or (j == MAP_SIZE - 1): map_row += map_elements[0]
    #             elif (j == 1) and (i == 1): map_row += map_elements[1]
    #             elif (i > 1) and (map1[i-1][j]==map_elements[0]) : map_row += map_elements[1]
    #             elif (len(map1) == MAP_SIZE) and (j > 1) and (map1[i][j-1]==map_elements[1]) : map_row += map_elements[0]
    #             else : map_row += map_elements[random.randint(0, 1)]
    #     map1.append(map_row)
    #     map_row = ""
    for i in range(len(map1)):
        for j in range(len(map1[i])):
            if map1[i][j] == '_':
                Floor(ground, x, y)
            elif map1[i][j] == '#':
                Block(wall, x, y)
            x += 32
        y += 32
        x = 0
    
