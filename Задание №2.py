import os
from time import sleep
class robot:
    def __init__(self,x,y) -> None:
        self.matrix = [['.' for x in range(101)] for y in range(101)]
        self.first_position = self.matrix
        self.second_position = self.matrix
        self.a = {y:[x]}
        for m in self.a:
            for n in self.a[m]:
                if n in range(0, 101):
                    self.first_position[m][n] = '█'
        self.location = [x, y]
        self.d = {
            'n':lambda x, y: [x,0] if y-1<0 else [x,100] if y-1>100 else [x,y-1],
            's':lambda x, y: [x,0] if y+1<0 else [x,100] if y+1>100 else [x,y+1],
            'e':lambda x, y: [0,y] if x+1<0 else [100,y] if x+1>100 else [x+1,y],
            'w':lambda x, y: [0,y] if x-1<0 else [100,x] if x-1>100 else [x-1,y]
        }
        
    def move(self, movements):
        for move in movements: self.location = self.d[move](self.location[0],self.location[1])
        for m in self.a:
            for n in self.a[m]:
                if n in range(0, 101):
                    self.second_position[m][n] = '█'
        return self.first_position,self.second_position,[str(x) for x in self.location]
        
antoha = robot(10,10)
res = antoha.move('sssssssss')
for y in res[0]: print(''.join(y))
sleep(3)
os.system('clear')
for y in res[1]: print(''.join(y))
sleep(3)
os.system('clear')
print(f'Текущие координаты: x = {res[2][0]}, y = {res[2][1]}')