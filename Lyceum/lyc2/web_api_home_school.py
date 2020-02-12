import distance

points = ['36.309855,54.571470', '36.285527,54.554340']

dist = int(distance.lonlat_distance(map(float, points[0].split(',')), map(float, points[1].split(','))))

print('Координаты дома: ' + points[0])
print('Координаты школы: ' + points[1])

print(f'Расстояние от дома до школы: {dist} метров')

