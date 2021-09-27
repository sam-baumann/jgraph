# default behavior spits out a few examples.
# to 
default:
#The second longest NHL game ever, May 24th 2021. Winnipeg's Kyle Connor had only 4 shots out of his team's 43, but one of them was the 3OT winner 106 minutes into the game
	python3 main.py 2021-05-24 "Kyle Connor" | ./jgraph -P | ps2pdf - > makefile-examples/KyleConnor20210524.pdf
#Washington's Alex Ovechkin with 0 goals on 15 shots. This is the highest all time shot total I could find that had coordinate data (all the other ones were too old). Unfortunate that he couldn't find the back of the net in a 1-0 loss
	python3 main.py 2015-11-10 "Alex Ovechkin" | ./jgraph -P | ps2pdf - > makefile-examples/AlexOvechkin20151110.pdf
#Another Winnipeg one. Patrik Laine scored 5 goals on 5 shots against the St. Louis Blues. I was at this game, cheering for the Blues. Not a fun time
	python3 main.py 2018-11-24 "Patrik Laine" | ./jgraph -P | ps2pdf - > makefile-examples/PatrikLaine20181124.pdf
#My favorite of the bunch. Alex Pietrangelo's game winning goal in game 7 of the Stanley Cup Final to clinch the series and the first championship in St. Louis Blues 51-year history.
	python3 main.py 2019-06-12 "Alex Pietrangelo" | ./jgraph -P | ps2pdf - > makefile-examples/AlexPietrangelo20190612.pdf
custom:
	python3 main.py $(DATE) "$(PLAYER)" | ./jgraph -P | ps2pdf - > custom.pdf
clean:
	rm *.pdf *.ps *.json makefile-examples/*.pdf