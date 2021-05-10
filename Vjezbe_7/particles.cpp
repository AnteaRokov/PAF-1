#include <iostream>
#include <math.h>

using namespace std;

// declare a class
class Particle {
   private:
    double t, x, y, vx, vy;
    double dt;
    double g = -9.81;

    void evolve()
    {
      while(y >= 0)
      {
        vx += 0.;
        vy += g*dt;

        x += vx*dt;
        y += vy*dt;

        t += dt;
      }
    }

   public:
    // constructor
    Particle(double v, double theta, double x0, double y0, double step=0.001)
    {
        // initialize starting conditions
        vx = v*cos(theta*M_PI/180.);
        vy = v*sin(theta*M_PI/180.);
        x = x0;
        y = y0;
        t = 0.;
        dt = step;
    }

    double range()
    {
        if (t < dt) evolve();
        return x;
    }

    double time()
    {
      if (t < dt) evolve();
      return t;
    }
};

int main()
{
    Particle p1(100,45,0,0);
    Particle p2(10,60,0,0);

    cout << "Domet cestice 1: " << p1.range() << endl;
    cout << "Vrijeme leta cestice 1: " << p1.time() << endl;

    cout << "Domet cestice 2: " << p2.range() << endl;
    cout << "Vrijeme leta cestice 2: " << p2.time() << endl;

    return 0;
}
