import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from datetime import datetime, timedelta

today = datetime.today().strftime('%Y-%m-%d')
i = 0
while i < 100:
    try:
        today = datetime.today() - timedelta(days=i)
        today = today.strftime('%Y-%m-%d')
        print(today)
        i += 1
    except KeyError:
        i += 1
        pass




style.use('default')

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data = open('bitcoin1.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            xs.append(float(x))
            ys.append(float(y))
    ax1.clear()
    ax1.plot(xs, ys)

ani = animation.FuncAnimation(fig, animate, interval=500)
plt.show()

import datetime

with open("bitcoin1.txt", "r") as f:
    lines = f.readlines()
with open("bitcoin1.txt", "w") as f:
    i = 0
    l = []
    for line in lines:
        line = line.strip("\n")
        l.append(line.split(","))
        l[0][0] = datetime.datetime.fromtimestamp(l[0][0]).isoformat()

        if l[0][1].isdigit():
            f.write(line +"\n")
        l = []


        
        if line.strip("\n").isdigit():
            f.write(line)