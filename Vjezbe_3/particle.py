import math
import matplotlib.pyplot as plt

class Particle:
    g = -9.81

    def __init__(self):
        self.t = []
        self.x = []
        self.y = []
        self.v_x = []
        self.v_y = []
        self.a_x = []
        self.a_y = []

    def init(self, v, theta, x_0, y_0, dt=0.001):
        self.t.append(0)
        self.x.append(x_0)
        self.y.append(y_0)
        self.v_x.append(v*math.cos(math.radians(theta)))
        self.v_y.append(v*math.sin(math.radians(theta)))
        self.a_x.append(0)
        self.a_y.append(self.g)
        self.dt = dt

        self.name = "kosi_hitac_" + str(v) + "_" + str(theta)

    def reset(self):
        self.t.clear()
        self.x.clear()
        self.y.clear()
        self.v_x.clear()
        self.v_y.clear()
        self.a_x.clear()
        self.a_y.clear()

    def __move(self, i):
        self.t.append(self.t[i-1] + self.dt)
        self.a_x.append(0)
        self.a_y.append(self.g)
        self.v_x.append(self.v_x[i-1] + self.a_x[i]*self.dt)
        self.v_y.append(self.v_y[i-1] + self.a_y[i]*self.dt)
        self.x.append(self.x[i-1] + self.v_x[i]*self.dt)
        self.y.append(self.y[i-1] + self.v_y[i]*self.dt)
        #print("i={0}, x={1}, y={2}, vx={3}, vy={4}, ax={5}, ay={6}, t={7}".format(i, self.x[i], self.y[i],self.v_x[i], self.v_y[i],self.a_x[i], self.a_y[i], self.t[i]))


    def range(self):
        i = 0

        while self.y[i] >= 0:
            self.__move(i)
            i += 1

        return self.x[i]


    def plot_trajectory(self):
        fig= plt.figure(figsize=(20,10))

        # x-y graf
        plt.plot(self.x,self.y)
        plt.xlabel('x [m]')
        plt.ylabel('y [m]')
        plt.title('x-y graf')

        v= math.sqrt(self.v_x[0]**2 + self.v_y[0]**2)
        fig.savefig(self.name + ".pdf")
        #plt.show()
