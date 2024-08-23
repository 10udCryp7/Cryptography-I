import primefac
n = 510143758735509025530880200653196460532653147
p = primefac.ecm(n)
q = n // p
print(min(p, q))