# PaintingSquirrel.py created by Caden Z. with the help of ChatGPT

import time
import os

unusedFrame = r""" 
 (\__/)
 (o'.'o)
(")_(||)
     \/
"""

frame1 = r""" 
 (\__/)
 (o'.'o)
(")___(|)
       v
    ----
    |  |
    ----

Converting.
"""

frame2 = r""" 
 (\__/)
 (o'.'o)
(")__(|)
      v
    ----
    |. |
    ----

Converting..
"""

frame3 = r""" 
 (\__/)
 (o'.'o)
(")_(|))
     v
    ----
    |: |
    ----

Converting...
"""

frame4 = r""" 
 (\__/)
 (o'.'o)
(")(|)_)
    v
    ----
    |:3|
    ----

Converting....
"""

frames = [frame1, frame2, frame3, frame4, frame3, frame2]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def loadingSquirrel(sec):
    for i in range(sec):
        for frame in frames:
            print(frame)
            time.sleep(0.5)
            clear_screen()
