"""Profile different stack implementations to analyze performance."""
import cProfile
import pstats
from pstats import SortKey
import random

from typing import Type
from stacks.stack import Stack
from stacks.stack_dynamic_array import Stack as ArrayStack

ITERATIONS = 10000000
RUNS = 1

def random_actions(prof, actions: int, stack: Type[Stack], array_stack: Type[ArrayStack]) -> None:
    """Generate random push/pop actions on the stack."""
    for i in range(actions):
        action = random.choice(["push", "push", "pop"])
        if action == "push":
            val = random.randint(0, 100)
            prof.runcall(stack.push, val)
            prof.runcall(array_stack.push, val)
        else:
            try:
                prof.runcall(stack.pop)
                prof.runcall(array_stack.pop)
            except ValueError as _:
                pass


def start_profiling(prof, iterations: int) -> None:
    stack = Stack()
    array_stack = ArrayStack()
    random_actions(prof, iterations, stack, array_stack)

if __name__ == '__main__': 
    pro = cProfile.Profile()
    for _ in range(RUNS):
        start_profiling(pro, ITERATIONS)
        st = pstats.Stats(pro).sort_stats(SortKey.FILENAME, SortKey.CUMULATIVE).strip_dirs()
        #ps = st.strip_dirs().stats
        print(st.print_stats('stack'))
        print(st.print_stats('linked_list'))
