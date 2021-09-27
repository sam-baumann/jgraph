default:
	python3 main.py | ./jgraph -P | ps2pdf - > test.pdf
clean:
	rm *.pdf *.ps *.json