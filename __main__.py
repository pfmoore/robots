from view import Display
from robots import make_robots

dsp = Display()
robots = make_robots()

def step(*args):
    for r in robots:
        dsp.hide(r)
        r.move()
        dsp.show(r)

if __name__ == '__main__':
    for r in robots:
        dsp.show(r)
    dsp.set_cr_action(step)
    dsp.run()
