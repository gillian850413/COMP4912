import nbformat as nbf

nb = nbf.read(open('kmeans.py', 'r'), 'py') 
nbf.write(nb, open('test.ipynb', 'w'), 'ipynb')