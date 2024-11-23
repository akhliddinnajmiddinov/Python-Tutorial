from datetime import datetime
from numba import jit, prange
import random

@jit(parallel=True)
def monte_carlo_pi(nsamples):
    acc = 0
    for i in prange(nsamples):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
    return 4.0 * acc / nsamples


startTime = datetime.now()
print(monte_carlo_pi(1000000000))
endTime = datetime.now()
total = endTime - startTime
print(total.seconds)