# default behavior spits out a few examples.
# to 
default:
	python3 main.py 2021-09-25 "James Neal" | ./jgraph -P | ps2pdf - > test.pdf
custom:
	python3 main.py $(DATE) "$(PLAYER)" | ./jgraph -P | ps2pdf - > custom.pdf
clean:
	rm *.pdf *.ps *.json