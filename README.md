## picascii
A terminal JPG to ASCII art converter, now with squirrels!

by Jocalexryem


## Inspiration
Squirrel! 

And also, we thought ASCII art was super fun, so we wanted a way to convert any picture to an ASCII picture. Do things like this exist already? Of course, probably. But are they convenient and easy-to-use? Are they lightweight but also fancy schmancy? Are they of good quality? _Are they charismatic??_

Our goal is to incorporate all of that into one neat package. 
We present:
```
         __                                                 __     __
        /\_\                                               /\_\   /\_\
 ______ \/_/_     ______     ______     ______     ______  \/_/_  \/_/_
/\  __ \  /\ \   /\  ___\   /\____ \   /\  ___\   /\  ___\   /\ \   /\ \   
\ \ \_\ \ \ \ \  \ \ \____  \ \  __ \  \ \___  \  \ \ \____  \ \ \  \ \ \  
 \ \  ___\ \ \_\  \ \_____\  \ \_____\  \/\_____\  \ \_____\  \ \_\  \ \_\ 
  \ \ \__/  \/_/   \/_____/   \/_____/   \/_____/   \/_____/   \/_/   \/_/ 
   \ \ \                                   BY JOCALEXRYEM
    \/_/

```

## What it does
It converts a given image file into ASCII art!
The user has the option to either pick an existing image or take a picture with the camera, then either save it as a .txt or a .jpg.
Videos can also be uploaded and converted to ASCII videos.

## How we built it
In python.

## Challenges we ran into

* accounting for line spacing while doing the ASCII conversion
* slow computation time (for video conversion)
* working out webcam shenanigans
* connecting all the pieces together as the code got longer
* documentation
* an attempt to make this a mobile app through expo, but decided not to for our mental health.

## Accomplishments that we're proud of

* cleaning up the quality of the ASCII
* getting ASCII videos to work
* not going insane

## What we learned
The power of friendship! :D

And the cv2 library for image processing.

## What's next for picascii
Streamlining it to be even faster and easier to use!

Giving it a GUI / moving to mobile! 

Implementing ASCII video call! 

Physical ASCII cameras that print out the ASCII art!
