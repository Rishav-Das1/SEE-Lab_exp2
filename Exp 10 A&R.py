import eyes17.eyes
p = eyes17.eyes.open()

from pylab import *
p.select_range('A1',4)
x1,y1,u1,v1 = p.capture2(1000,1000)
x2,y2,u2,v2 = p.capture2(1000,1000)
x3,y3,u3,v3 = p.capture2(1000,1000)
x4,y4,u4,v4 = p.capture2(1000,1000)
x2=x2+1000
x3=x3+2000
x4=x4+3000
u2=u2+1000
u3=u3+2000
u4=u4+3000
x=list(x1)
u=list(u1)
u.extend(list(u2))
u.extend(list(u3))
u.extend(list(u4))
x.extend(list(x2))
x.extend(list(x3))
x.extend(list(x4))
y=list(y1)
v=list(v1)
v.extend(list(v2))
v.extend(list(v3))
v.extend(list(v4))
y.extend(list(y2))
y.extend(list(y3))
y.extend(list(y4))
plot(x,y,color='b')
plot(u,v,color='r')

show()
quit()
