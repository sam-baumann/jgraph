PYTHON = python3
# default behavior spits out a few examples.
default: jgraph
#The second longest NHL game ever, May 24th 2021. Winnipeg's Kyle Connor had only 4 shots out of his team's 43, but one of them was the 3OT winner 106 minutes into the game
	$(PYTHON) main.py 2021-05-24 "Kyle Connor" | ./jgraph -P | ps2pdf - > makefile-examples/Connor2021.pdf
#San Jose's Patrick Marleau scored 4 goals, each in the third period on January 23, 2017. Tied for most goals in one period ever.
	$(PYTHON) main.py 2017-01-23 "Patrick Marleau" | ./jgraph -P | ps2pdf - > makefile-examples/Marleau2017.pdf
#Washington's Alex Ovechkin with 0 goals on 15 shots. This is the highest all time shot total I could find that had coordinate data (all the other ones were too old). Unfortunate that he couldn't find the back of the net in a 1-0 loss
	$(PYTHON) main.py 2015-11-10 "Alex Ovechkin" | ./jgraph -P | ps2pdf - > makefile-examples/Ovechkin2015.pdf
#Another Winnipeg one. Patrik Laine scored 5 goals on 5 shots against the St. Louis Blues. I was at this game, cheering for the Blues. Not a fun time
	$(PYTHON) main.py 2018-11-24 "Patrik Laine" | ./jgraph -P | ps2pdf - > makefile-examples/Laine2018.pdf
#My favorite of the bunch. Alex Pietrangelo's game winning goal in game 7 of the Stanley Cup Final to clinch the series and the first championship in St. Louis Blues 51-year history.
	$(PYTHON) main.py 2019-06-12 "Alex Pietrangelo" | ./jgraph -P | ps2pdf - > makefile-examples/Pietrangelo2019.pdf
custom: jgraph
	$(PYTHON) main.py $(DATE) "$(PLAYER)" | ./jgraph -P | ps2pdf - > custom.pdf
jgraph:
	cd jgraph-files; make
	cp jgraph-files/jgraph .
clean:
	rm -f *.pdf *.ps *.json makefile-examples/*.pdf jgraph
	cd jgraph-files; make clean