import pyformulas as pf

pf_v01 = pf.download('https://github.com/pyformulas/pyformulas/releases/download/0.1/pyformulas.tar.gz')

print(len(pf_v01))

pf_v012 = pf.download('https://github.com/pyformulas/pyformulas/releases/download/0.1.2/pyformulas.tar.gz', out_path='./pyformulas.tar.gz')

print(len(pf_v012))