s_road = 109
v = int(input())
t = int(input())
s = v * t
if s > s_road:
	s -= s_road
print(s)
#Только я не понимаю, почему этот код не работает в командной строке?