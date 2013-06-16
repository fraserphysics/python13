henon.pdf: henon.tex dots.pdf
	pdflatex henon
dots.pdf: henon.py plot.py
	python plot.py --dots dots.pdf

#---------------
# Local Variables:
# eval: (makefile-mode)
# End:
