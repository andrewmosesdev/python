# Need to run kernal for latexify w/ latex output code
import math
import latexify

@latexify.with_latex

def solve(a, b, c):
  return (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)

print('Answer:')
print(solve(1, 4, 3))