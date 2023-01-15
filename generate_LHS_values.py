from skopt.sampler import Lhs
import os
import numpy

num_samples = 50

LHS = Lhs(lhs_type="classic", criterion=None)
samples = LHS.generate([(1.5, 5), (1.5, 5)], num_samples)

file = open('D:/LHS_value_sampling.txt', 'w')

for i in range(0, num_samples):
    file.write(str(samples[i][0]))
    file.write(';')
    file.write(str(samples[i][1]))
    file.write('\n')