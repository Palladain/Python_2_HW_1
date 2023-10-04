import pytest
import numpy as np
import random
from scipy.stats import qmc
import math

def test_diff_evolution_part_2():
    from diff_evolution import differential_evolution
    SEED = 21
    random.seed(SEED)
    np.random.seed(SEED)

    def rastrigin(array, A=10):
        return A * 2 + (array[0] ** 2 - A * np.cos(2 * np.pi * array[0])) + (array[1] ** 2 - A * np.cos(2 * np.pi * array[1]))
  
    def griewank(array):
        term_1 = (array[0] ** 2 + array[1] ** 2) / 2
        term_2 = np.cos(array[0]/ np.sqrt(2)) * np.cos(array[1]/ np.sqrt(2))
        return 1 + term_1 - term_2
  
    def rosenbrock(array):
        return (1 - array[0]) ** 2 + 100 * (array[1] - array[0] ** 2) ** 2

    assert list(differential_evolution(rosenbrock, [[0, 2], [0, 2]], init_setting=random, mutation_setting='rand1', selection_setting='current'))[-1][1] ==  3.379606654175286e-05
    assert list(differential_evolution(rosenbrock, [[0, 2], [0, 2]], init_setting=random, mutation_setting='rand2', selection_setting='current'))[-1][1] ==  0.0007829271144532441
    assert list(differential_evolution(rosenbrock, [[0, 2], [0, 2]], init_setting=random, mutation_setting='best1', selection_setting='current'))[-1][1] ==  2.9372280506324224e-08
    assert list(differential_evolution(rosenbrock, [[0, 2], [0, 2]], init_setting=random, mutation_setting='rand_to_p_best1', selection_setting='current'))[-1][1] ==  3.459298758896539e-08
    assert list(differential_evolution(rastrigin, [[-20, 20], [-20, 20]], init_setting=random, mutation_setting='rand1', selection_setting='current'))[-1][1] ==  1.197346524151044e-07
    assert list(differential_evolution(rastrigin, [[-20, 20], [-20, 20]], init_setting=random, mutation_setting='rand2', selection_setting='current'))[-1][1] ==  0.00041887219276759424
    assert list(differential_evolution(rastrigin, [[-20, 20], [-20, 20]], init_setting=random, mutation_setting='best1', selection_setting='current'))[-1][1] ==  0.0
    assert list(differential_evolution(rastrigin, [[-20, 20], [-20, 20]], init_setting=random, mutation_setting='rand_to_p_best1', selection_setting='current'))[-1][1] ==  6.927791673660977e-14
    assert list(differential_evolution(griewank, [[-20, 20], [-20, 20]], init_setting=random, mutation_setting='rand1', selection_setting='current'))[-1][1] ==  1.0215162049576065e-12
    assert list(differential_evolution(griewank, [[-20, 20], [-20, 20]], init_setting=random, mutation_setting='rand2', selection_setting='current'))[-1][1] ==  1.1605779670631478e-09
    assert list(differential_evolution(griewank, [[-20, 20], [-20, 20]], init_setting=random, mutation_setting='best1', selection_setting='current'))[-1][1] ==  0.0
    assert list(differential_evolution(griewank, [[-20, 20], [-20, 20]], init_setting=random, mutation_setting='rand_to_p_best1', selection_setting='current'))[-1][1] ==  0.0

