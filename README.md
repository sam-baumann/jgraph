# NHL shot selection visualizer
### This project is meant to help visualize NHL shot selection for an individual player in an individual game
### Written for Dr. James Plank's Advanced Programming and Algorithms class fall 2021

I've chosen to write this in Python because of my familiarity with it and easy access to a web requests api, and simple packages to parse the JSON that is returned by the NHL API.

Written in python 3.8.10 but should work for any python 3 version. Required libraries are: json, requests. Use pip to install these like so:

`python -m pip install [package_name]`

To generate the jgraph input, run

`python main.py [yyyy-mm-dd] "[player full name]"`

for example:

`python main.py 2019-06-12 "Ryan O'Reilly"`

By default, the makefile will generate a few example files.
You can also use the makefile to generate an output pdf like so:

`make custom DATE=[yyyy-mm-dd] PLAYER="[player full name]"`

for example:

`make custom DATE=2019-06-12 PLAYER="Ryan O'Reilly"`

The makefile requires ps2pdf to be installed, and needs a jgraph executable in the root folder

Here is a quick list of some functionality I would have liked to have added if I had more time

functionality to add:
- Making the playing space look more like a real hockey rink
- Game ranges rather than just one game. Players generally only have a few shots in a game so the graphs aren't as intersting as I thought they would be
- Shot density visualization, such as [here](http://www.stat.cmu.edu/cmsac/poster2020/posters/Kumagai-ClusteringNHLShot.pdf). Not sure if this is even possible with JGraph but seems like it could make for an interesting exercise.

todo as of sunday night sep 26:
- make examples to run in the makefile
- add pictures to readme