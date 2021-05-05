# https://www.quora.com/What-are-some-prime-examples-of-bad-python-code
from itertools import cycle 
(x or n+1 for n, x in enumerate(map(''.join, zip(cycle([''] * 2 + ['fizz']), cycle([''] * 4 + ['buzz']))))) 
