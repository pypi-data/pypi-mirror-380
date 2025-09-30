import resources.runner.example_module_a as example_module_a
import resources.runner.example_module_b as example_module_b
from ordeq import run

run(example_module_a, example_module_b, verbose=True)
