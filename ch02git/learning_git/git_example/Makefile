
MDS=$(wildcard *.md)
PDFS=$(MDS:.md=.pdf)

default: $(PDFS)

%.pdf: %.md
	pandoc $< -o $@