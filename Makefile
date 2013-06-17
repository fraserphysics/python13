henon.pdf: henon.tex dots.pdf colors.pdf dim.pdf count.pdf henon.bbl
	pdflatex henon
dots.pdf: henon.py plot.py
	python plot.py --dots dots.pdf
dim.pdf: henon.py plot.py
	python plot.py --N 10000 --dim_pars .2 20 --dim dim.pdf
count.pdf: henon.py plot.py
	python plot.py --N 100000 --dx .009 --dy .003 --count count.pdf
colors.pdf: henon.py plot.py
	python plot.py --N 10000 --dx 0.009 --dy 0.003 --colors colors.pdf
henon.aux: henon.tex
	pdflatex henon
henon.bbl: henon.aux local.bib
	bibtex henon

#---------------
# Local Variables:
# eval: (makefile-mode)
# End:
