import particle as prt
import numpy as np
import matplotlib.pyplot as plt

p1 = prt.Particle()

p1.init(100, 45, 0, 0)
print("Za v={0} i kut {1} domet je {2:.2f} m.".format(100, 45, p1.range()))
p1.plot_trajectory()
p1.reset()

p1.init(10,60,0,0)
print("Za v={0} i kut {1} domet je {2:.2f} m.".format(10, 60, p1.range()))
p1.plot_trajectory()
p1.reset()

time = []
error = []
analitical = 8.83

for dt in np.arange(0.00005, 0.1, 0.00005):
    p1.init(10,60,0,0,dt)
    time.append(dt)
    error.append(100*(abs(p1.range()-analitical)/analitical))
    p1.reset()

fig= plt.figure(figsize=(20,10))

# x-y graf
time.reverse()
plt.plot(time,error)
plt.xlabel('dt [s]')
plt.ylabel('Absolute relative error [%]')
plt.title('Aboslute relative error for range of projectile')

fig.savefig("relative_error.pdf")
