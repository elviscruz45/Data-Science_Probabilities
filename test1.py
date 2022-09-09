from scipy.stats import binom

dist=binom(3,0.5)


print(dist.pmf(0))
print(dist.pmf(1))
print(dist.pmf(2))
print(dist.pmf(3))