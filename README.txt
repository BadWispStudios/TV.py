      \  /
 ______\/_
|---------|
|- TV.py -|
|-------o-|
 =========

GitHub link: https://github.com/BadWispStudios/TV.py

Class Description: The TV class creates objects that model some of the main features of a television. 
Each TV created with this class has two main characteristics: it's screen size and it's service provider.
These two features affect the TV's "video feed."

-Class Variables-

Power: This boolean variable determines whether or not the TV is On (True) or Off (False). Power is set to False when a TV object is initially created.
Mute: This boolean variable is set to False by default. When True, the next channel's "audio" will become "muted," replacing text with ellipses representing silence.
Loud: This boolean variable is set to False by default. When True, the next channel's "audio" will "increase in volume," printing out text in all caps.
Quiet: This boolean variable is set to False by default. When True, the next channel's "audio" will "decrease in volume," printing out text in all lowercase.

-Data Variables-

When a new TV object is created, it's constructor method takes in two arguments which are then stored as data variables: "screen" and "service."
Screen: Represents the TV's screen size. There are two types of sizes: 4:3 and 16:9. The screen size affects the "frame" of the "video feed" (i.e. the number of text lines displayed)
Service: Represents the TV's service provider. There are two available services: xfinity and AT&T. The selected service affects the quality of the TV's broadcast.
Xfinity's service will produce satisfactory results (normal text) whilst AT&T's service will be incredibly laggy and somewhat unintelligble (text with omitted letters).

-Methods-
power_on: As the name implies, this method turns the TV object on. An accompanying message signifies this. (Sets Power to True)
power_off: In a similar manner to power_on, this method turns the TV object off, also indicated by a print statement. (Sets Power to False)
set_volume: This method takes in one argument which can be one of four options: "mute", "loud", "quiet", and "normal". 
Each of these options will print out a corresponding text graphic indicating the change in volume and (utilizing the three volume boolean variables) 
will alter the TV's "audio output."
change_channel: This method takes in one argument which can be one of three options: "CNN", "ESPN", and "HBO". The overall presentation of these channels will be
dependent upon the TV's screen size, service provider, and volume.


-Demo Program-

Description: The demo program showcases two TVs. One of them, labled Sony, features a 16:9 screen size and has xfinity as it's service provider.
The other, labled LG, features a 4:3 screen size and has AT&T as it's service provider. Both TV's will be turned on and display each of the three channels
at adjusted volumes before being turned back off.

How to run: Simply open your terminal, navigate to the folder in which TV.py is located and type "Python3 TV.py" into the command line 
and enjoy some good ole' Python TV!

         

   