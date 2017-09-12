An Object Orientation Demo in Python
====================================

This is a simple demonstration of how to build classes and objects in
Python. The GUI code (in ```view.py``` and ```__main__.py```) works
in conjunction with a module ```robots.py``` that defines "Robot" objects
that will be displayed in a window.

Robots must have attributes ```row```, ```column``` and ```colour``` that
describe where they are (on an 8x8 grid) and what colour they are. They
must also have a ```move()``` method that instructs them to move once,
according to whatever rules they have on how to move.

The ```robots.py``` module should export a single function,
```make_robots()```, that returns a list of robots to display.

Running the ```__main__.py``` program will display the initial grid.
Pressing ```ENTER``` causes all the robots to move one step.
