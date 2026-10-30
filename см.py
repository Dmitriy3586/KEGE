from turtle import*

screensize(10_000,10_000)
tracer(0)
m=10
for i in range(5):
    fd(13*m)
    rt(90)
    fd(5*m)
up()
rt(90)
fd(10*m)
lt(90)
fd(7*m)
down()
for i in range(2):
    fd(8*m)
    rt(90)
    fd(11*m)
    rt(90)

for x in range(-5,4):
    for y in range(-18,-11):
        teleport(x*m,y*m)
        dot(3,'red')

print(13*5+8*11-6*8)


update()
done()