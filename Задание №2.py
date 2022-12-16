# Задание №2

import os
from time import sleep
class robot:
    def __init__(self,x,y) -> None:
        self.first_position = [['.' for x in range(101)] for y in range(101)]
        self.second_position = [['.' for x in range(101)] for y in range(101)]
        self.first_position[y][x] = '█'
        self.location = [x, y]
        self.d = {
            'n':lambda x, y: [x,0] if y-1<0 else [x,100] if y-1>100 else [x,y-1],
            's':lambda x, y: [x,0] if y+1<0 else [x,100] if y+1>100 else [x,y+1],
            'e':lambda x, y: [0,y] if x+1<0 else [100,y] if x+1>100 else [x+1,y],
            'w':lambda x, y: [0,y] if x-1<0 else [100,x] if x-1>100 else [x-1,y]
        }
        
    def move(self, movements):
        for move in movements: self.location = self.d[move](self.location[0],self.location[1])
        self.second_position[self.location[1]][self.location[0]] = '█'
        return [self.first_position,self.second_position,[str(x) for x in self.location]]
        
antoha = robot(50,50)
res = antoha.move('sssssssss')
os.system('clear')
for i in res[0]: print(''.join(i))
sleep(3)
os.system('clear')
for i in res[1]: print(''.join(i))
sleep(3)
os.system('clear')
print(f'Текущие координаты: x = {res[2][0]}, y = {res[2][1]}')