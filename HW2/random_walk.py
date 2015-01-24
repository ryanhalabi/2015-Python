'''
A two-dimensional random walk simulator and animator.
'''

# The turtle package is part of Python's standard library. It provides some
# very primitive graphics capabilities. For more details see
#
#   https://docs.python.org/3/library/turtle.html
#
import turtle

import numpy as np

def random_walk(n, x_start=0, y_start=0,P = None ):
    ''' Simulate a two-dimensional random walk.

    Args:
        n           number of steps

    Returns:
        Two Numpy arrays containing the x and y coordinates, respectively, at
        each step (including the initial position).
    '''
    
    if P != None:
        if (sum(P) != 1)  | (len(P) != 4) :
            raise ValueError('p does not have length 4!')
    
    
    x =0
    y =0
    z = np.zeros([n,2])
    zz = np.zeros([n,2])
    
    A = np.array([0,1,2,3])
    
    for i in range (1,n):
    
        dir = np.random.choice( A,replace = True, p = P)
        if dir == 0:
            z[i,0] = 1
        if dir == 1:
            z[i,0] = -1
        if dir == 2:
            z[i,1] = 1
        if dir == 3:
            z[i,1] = -1

    xx = np.cumsum(z[:,0])
    yy = np.cumsum(z[:,1])
    zz[:,0] = xx + x_start
    zz[:,1] = yy + y_start

    x = sum(z[:,0])
    y = sum(z[:,1])
    
    x = x+x_start
    y = y+y_start

    print(x , y)
    print(zz)
    return zz



# Notice that the documentation automatically shows up when you use ?
def draw_walk(x, y, speed = 'slowest', scale = 20):
    ''' Animate a two-dimensional random walk.

    Args:
        x       x positions
        y       y positions
        speed   speed of the animation
        scale   scale of the drawing
    '''
    # Reset the turtle.
    turtle.reset()
    turtle.speed(speed)

    # Combine the x and y coordinates.
    walk = zip(x * scale, y * scale)
    start = next(walk)

    # Move the turtle to the starting point.
    turtle.penup()
    turtle.goto(*start)

    # Draw the random walk.
    turtle.pendown()
    for _x, _y in walk:
        turtle.goto(_x, _y)



P = [.35,.15,.45,.05]
a = random_walk(1000)


draw_walk( a[:,0], a[:,1])











