# LPC3D
A code to do mesoscopic simulations of ions diffusing in carbon particles and of full supercapacitors.

This code is developed in the context of the MultiXscale project.

This code was written by El Hassane Lahrar and Céline Merlet, with contributions from Rudolf Weber, and was used in one published work:

"Investigating the effect of particle size distribution and complex exchange dynamics on NMR spectra of ions diffusing in disordered porous carbons through a mesoscopic model", Faraday Discuss., Advance article, https://pubs.rsc.org/en/Content/ArticleLanding/2024/FD/D4FD00082J 

Here, a manual and example input files are provided.

Compared to the previous version of the program, written in C and serial (https://github.com/cmerlet/LPC3D-C-serial), this code is written using pystencils (https://pypi.org/project/pystencils/) - is parallel - and can use CPU and GPU.

