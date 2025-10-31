hour = int(input('what hour ?'))
min =int(input('what minute ?'))
hour= hour % 12
hour_degree = hour * 30 + min*0.5
min_degree = min * 6
degree = abs(hour_degree - min_degree)
if degree > 180 :
    degree = degree-180
    print(degree)
else :
    print(degree)