# Ariot18-FitTeam

## Concept

Our project focuses on a modern IoT approach for your training routines. Whether you are a gym rat or prefer to train at home we have a solution for you! 

- If you go to gym and want to monitor your weight lifting activity then our tiny IoT bluetooth device with a magnetic holder is what you need! You can instantly attach it to any strength training machine or individual weights that you use and directly monitor your activity, burned calories and all other possible statistics online.

- If you prefer to stay at home, using a simple web camera video, the FitTeam has put together a project solution which is detecting coordinates and movements of a pair of colorful dumbbells and motivates you to follow a specific training routing or just play some games while you are training. 

_By using the internet connected dumbells as controllers we can send signals to any game (Stepmania for example, which is btw one of the worlds greatest games!) and this turns your regular workout into a lot of fun._

![IoTdevice](https://i.imgur.com/yRF6c1u.jpg)
![Stepmania](https://media.giphy.com/media/SHdlF1DCQq0cE6uAzd/giphy.gif)

> While you are gaming, we are collecting data from your workout, and present it using breathtaking graphical technology.



## Technology

- Versioning Solutions: **Visual Studio Online** 
- Languages: [**Python**, Bash, C]
- Detector script: [Tracking HSV Codes in realtime](https://stackoverflow.com/questions/10948589/choosing-the-correct-upper-and-lower-hsv-boundaries-for-color-detection-withcv/26044115#26044115)
- Emulator controller: [**vJoy**](http://vjoystick.sourceforge.net/site/)
  - Device driver that bridges the gap between any device that is not a joystick and an application that requires a joystick
- Emulator bindings: [**pyvjoy**](https://github.com/tidzo/pyvjoy)
 - Library for setting vJoy controller inputs through python.
- Game: [**Stepmania**](https://github.com/stepmania/stepmania/releases/tag/v5.1.0-b1)


## Prerequirements
- Windows Vista (SP1), Windows 7, 8, 8.1 and 10
- [Python 3 or newer](https://wiki.python.org/moin/BeginnersGuide/Download)
- [StepMania 5](https://github.com/stepmania/stepmania/releases/tag/v5.1.0-b1)
- [vJoy](http://vjoystick.sourceforge.net/site/)
- [pyvjoy](https://github.com/tidzo/pyvjoy)

## Getting started

Put the x86 version of vJoyInterface.dll inside the extracted folder. Rename folder to pyvjoy. 
Copy the folder. Place it inside \Python\Python36-32\Lib\site-packages.
Download the repository.
Run Start.bat.
In StepMania: select options - Config Key/Joy Mappings. Add Joy1 B1 and Joy1 B2 to left and right at the bottom by lifting the pink dumbbell up when inserting the new key.
* You may want to edit the songs to not include the up and down arrows. Do this in the main menu Edit/Share option.



![Stepmania](https://thumbs.gfycat.com/ImpartialShyBoilweevil-size_restricted.gif)
