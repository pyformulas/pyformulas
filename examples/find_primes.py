"""
Searches for prime numbers using pf.discrete_search (A*)
"""

import pyformulas as pf
import numpy as np
import random
import sympy

initial_state = round( random.random()*1e6 )

def expansion_fn(state):
    primes_below = np.array(list( sympy.primerange(0, state+1) ))
    possible_child_states = state / primes_below

    child_states = [s for s in possible_child_states if s == s//1]
    step_costs = np.ones_like(child_states)

    return child_states, step_costs

goal_fn = lambda state: state==1

def heuristic_fn(state):
    return 1 - 1/state

print('Composite:', initial_state)
path = pf.discrete_search(initial_state, expansion_fn, goal_fn, heuristic_fn)
print('Path to 1:', path)

primes = []
for sidx, step in enumerate(path[::-1][1:]):
    primes.append(step / path[::-1][sidx])

check_primes = lambda primes: all(map( lambda p:p in sympy.primerange(0,initial_state+1), primes ))
print('Primes:', primes, check_primes(primes))

print('Product:', np.prod(primes))