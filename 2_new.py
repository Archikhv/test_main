s_road = 109
v = int(input('Скорость '))
t = int(input('Время '))
s = v * t
if s > s_road:
    s %= s_road
print(s)