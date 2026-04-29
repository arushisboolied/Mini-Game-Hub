NAME = Report

all: $(NAME).pdf

$(NAME).pdf: $(NAME).tex Bibliography.bib
	pdflatex $(NAME).tex
	bibtex $(NAME)
	pdflatex $(NAME).tex
	pdflatex $(NAME).tex

clean:
	rm -f $(NAME).aux $(NAME).bbl $(NAME).blg $(NAME).log $(NAME).out $(NAME).toc

cleanall: clean
	rm -f $(NAME).pdf

