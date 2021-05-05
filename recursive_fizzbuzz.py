# https://www.quora.com/What-are-some-prime-examples-of-bad-python-code
(lambda f, n: f(f, n))(lambda f, n: [(not n %
                                      3 and "fizz" or "") +
                                     (not n %
                                      5 and "buzz" or "") or n] +
                       f(f, n +
                         1) if n <= 100 else [], 1)
