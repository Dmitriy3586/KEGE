'''from turtle import*

screensize(10_000,10_000)
tracer(0)
m=10

for i in range(9):
    fd(22*m)
    rt(90)
    fd(6*m)
    rt(90)
up()
fd(1*m)
rt(90)
fd(5*m)
lt(90)
down()
for i in range(9):
    fd(53*m)
    rt(90)
    fd(75*m)
    rt(90)

for x in range(0,22):
    for y in range(-1,1):
        teleport(x*m,y*m)
        dot(3,'red')


print()



update()
done()'''



ans=[]
for N in range(3,10_000):
    R =f'{N:b}'
    if N%2==0:
        R = R+(R[:3])
    else:
        R = '1'+R+'01'
    R = int(R,2)
    if R > 600:
        ans.append(R)

print(min(ans))

