# Knapsack problems

#### Authors: Lei Han, Handing Wang
#### Xidian University, China.
#### EMAIL: lhan_1@stu.xidian.edu.cn, hdwang@xidian.edu.cn
#### WEBSITE: https://sites.google.com/site/handingwanghomepage
#### DATE: January 2021
# ------------------------------------------------------------------------
# This code is part of the program that produces the results in the following paper:
#
# Lei Han, Handing Wang, A random forest assisted evolutionary algorithm using competitive neighborhood search for expensive constrained combinatorial optimization. Memetic Computing, accepted.
#
# You are free to use it for non-commercial purposes. However, we do not offer any forms of guarantee or warranty associated with the code. We would appreciate your acknowledgement.
# ------------------------------------------------------------------------
import numpy as np


def problem_01_knapsack(pop, knapsack_size):
    '''
    :param pop: 2D list, the population
    :param knapsack_size: the knapsack size for the knapsack problems
    :return: pop_value: 1D list, the value of every individual in the population
             pop_weight: 1D list, the weight of every individual in the population
             pop_violation: 1D list, the weight of every individual exceeds the knapsack size. If it does not 
             exceed the knapsack size, it is 0.
    '''
    n_pop, n_var = np.shape(pop)
    weight = (
        49, 63, 2, 43, 67, 92, 70, 5, 33, 79, 23, 51, 25, 90, 81, 34, 92, 41, 91, 85, 86, 56, 88, 85, 91, 15, 72,
        13, 6, 68, 40, 44, 60, 55, 15, 98, 52, 57, 58, 32, 82, 100, 87, 7, 9, 46, 86, 55, 15, 76)
    value = (
        21, 7, 96, 49, 95, 41, 33, 78, 8, 30, 27, 35, 36, 52, 11, 80, 85, 97, 53, 13, 28, 3, 21, 88, 33, 95, 100,
        41, 35, 82, 67, 67, 74, 11, 85, 98, 76, 44, 79, 33, 7, 32, 34, 5, 50, 82, 51, 2, 71, 11)
    pop_value = []
    pop_weight = []
    pop_violation = []
    for i in range(n_pop):
        val = 0
        for j in range(n_var):
            val = value[j] * pop[i][j] + val
        pop_value.append(val)
    for i in range(n_pop):
        wgh = 0
        for j in range(n_var):
            wgh = weight[j] * pop[i][j] + wgh
        pop_weight.append(wgh)
        if wgh > knapsack_size:
            pop_violation.append(wgh - knapsack_size)
        else:
            pop_violation.append(0)
    return pop_value, pop_weight, pop_violation


def problem_quadratic_knapsack(pop, knapsack_size):
    '''
    :param pop: 2D list, the population
    :param knapsack_size: the knapsack size for the knapsack problems
    :return: pop_value: 1D list, the value of every individual in the population
             pop_weight: 1D list, the weight of every individual in the population
             pop_violation: 1D list, the weight of every individual exceeds the knapsack size. If it does not 
             exceed the knapsack size, it is 0.
    '''
    pop = np.array(pop)
    n_pop, n_var = np.shape(pop)
    weight = (
        71, 34, 82, 23, 1, 88, 12, 57, 10, 68, 5, 33, 37, 69, 98, 24, 26, 83, 16, 26, 18, 43, 52, 71, 22, 65, 68, 8, 40,
        40,
        24, 72, 16, 34, 10, 19, 28, 13, 34, 98, 29, 31, 79, 33, 60, 74, 44, 56, 54, 17)
    value = np.mat([
        [2, 55, 87, 9, 93, 67, 75, 91, 2, 17, 40, 17, 6, 17, 66, 94, 14, 84, 17, 24, 44, 79, 69, 12, 17, 84, 83, 56, 80,
         16,
         73, 12, 12, 3, 33, 85, 60, 18, 57, 63, 1, 78, 85, 33, 41, 63, 56, 60, 13, 85],
        [12, 85, 72, 28, 76, 90, 85, 50, 17, 17, 93, 50, 56, 32, 50, 88, 67, 33, 40, 75, 63, 72, 16, 60, 30, 98, 100,
         74,
         53, 71, 19, 94, 98, 56, 33, 76, 48, 72, 34, 100, 16, 51, 51, 95, 69, 68, 83, 77, 26, 73],
        [77, 82, 81, 28, 70, 41, 7, 96, 8, 4, 55, 17, 62, 79, 37, 5, 3, 26, 12, 52, 84, 70, 62, 81, 30, 59, 13, 63, 5,
         63,
         92, 69, 60, 32, 10, 57, 8, 4, 1, 26, 80, 81, 49, 59, 62, 49, 85, 96, 83, 28],
        [15, 28, 8, 51, 1, 2, 73, 85, 81, 99, 46, 57, 33, 75, 73, 72, 46, 100, 55, 6, 46, 28, 99, 38, 16, 95, 20, 14,
         64,
         39, 36, 23, 52, 83, 55, 59, 21, 68, 77, 81, 23, 7, 100, 55, 67, 77, 67, 2, 50, 56],
        [45, 79, 34, 54, 95, 55, 84, 87, 55, 9, 79, 64, 28, 50, 33, 52, 49, 27, 95, 63, 40, 30, 74, 66, 27, 83, 64, 90,
         46,
         74, 67, 70, 70, 71, 44, 56, 44, 19, 27, 73, 86, 84, 52, 25, 33, 67, 50, 72, 62, 79],
        [24, 45, 43, 70, 52, 30, 61, 30, 38, 57, 97, 93, 54, 8, 85, 77, 15, 19, 52, 31, 99, 45, 99, 87, 58, 99, 29, 12,
         99,
         78, 66, 92, 27, 19, 65, 80, 24, 22, 70, 56, 72, 69, 28, 15, 71, 36, 89, 20, 14, 29],
        [6, 58, 64, 30, 66, 3, 4, 70, 91, 12, 22, 7, 92, 71, 100, 72, 26, 30, 3, 48, 93, 24, 94, 32, 97, 59, 94, 75, 56,
         56,
         5, 32, 25, 83, 65, 30, 12, 47, 47, 18, 45, 46, 30, 55, 70, 32, 78, 19, 25, 65],
        [36, 30, 89, 46, 12, 77, 97, 17, 41, 88, 38, 21, 17, 78, 35, 96, 62, 67, 83, 98, 38, 99, 51, 8, 35, 23, 42, 28,
         86,
         98, 71, 84, 31, 55, 26, 8, 7, 2, 71, 30, 92, 96, 38, 64, 8, 11, 13, 78, 28, 41],
        [46, 92, 60, 72, 33, 17, 22, 10, 64, 11, 26, 56, 97, 44, 7, 14, 47, 57, 99, 90, 78, 25, 82, 76, 9, 16, 53, 51,
         37,
         9, 53, 34, 85, 55, 87, 43, 41, 56, 1, 62, 79, 75, 54, 72, 27, 57, 43, 44, 9, 29],
        [45, 15, 8, 22, 57, 42, 95, 84, 98, 49, 71, 1, 86, 100, 49, 3, 54, 4, 44, 41, 58, 88, 28, 87, 85, 60, 34, 45,
         48,
         19, 81, 89, 5, 72, 65, 40, 81, 64, 26, 67, 81, 69, 28, 20, 88, 64, 54, 77, 79, 67],
        [67, 63, 45, 82, 92, 66, 37, 23, 27, 14, 39, 19, 51, 76, 84, 29, 8, 95, 84, 1, 6, 73, 19, 1, 83, 13, 17, 82, 92,
         43,
         32, 66, 78, 6, 54, 64, 23, 61, 85, 16, 93, 43, 74, 20, 42, 74, 30, 58, 93, 7],
        [68, 36, 51, 6, 90, 75, 48, 14, 33, 73, 82, 16, 50, 87, 41, 67, 89, 9, 84, 21, 9, 16, 7, 10, 88, 6, 21, 12, 50,
         10,
         11, 56, 99, 83, 19, 6, 54, 5, 55, 17, 56, 76, 72, 21, 6, 84, 19, 97, 20, 14],
        [55, 85, 64, 71, 54, 8, 77, 73, 13, 12, 60, 67, 13, 5, 52, 74, 22, 31, 85, 67, 77, 91, 44, 64, 10, 98, 46, 26,
         24,
         65, 45, 18, 2, 94, 43, 56, 5, 81, 45, 19, 19, 30, 5, 19, 30, 4, 16, 56, 35, 26],
        [91, 91, 47, 21, 52, 80, 34, 23, 95, 21, 12, 53, 43, 4, 26, 37, 42, 45, 3, 25, 47, 97, 33, 56, 68, 31, 79, 39,
         3,
         41, 30, 24, 61, 31, 34, 95, 80, 87, 12, 79, 31, 43, 10, 52, 43, 66, 64, 12, 67, 51],
        [81, 74, 32, 20, 40, 49, 77, 97, 69, 45, 70, 23, 60, 96, 23, 15, 24, 83, 28, 97, 15, 17, 86, 6, 56, 100, 42, 98,
         33,
         100, 23, 99, 36, 74, 85, 14, 98, 69, 90, 100, 35, 50, 3, 81, 40, 83, 99, 79, 7, 95],
        [17, 44, 90, 13, 86, 81, 82, 77, 28, 97, 32, 20, 26, 56, 66, 85, 85, 46, 24, 63, 59, 90, 96, 2, 71, 28, 28, 29,
         48,
         58, 41, 93, 83, 40, 10, 82, 56, 87, 59, 6, 86, 18, 69, 13, 38, 57, 2, 96, 89, 83],
        [72, 62, 76, 83, 16, 89, 2, 37, 32, 78, 99, 82, 44, 53, 57, 57, 23, 24, 27, 14, 96, 42, 89, 43, 1, 89, 90, 22,
         10,
         76, 36, 97, 63, 66, 77, 82, 76, 81, 13, 81, 2, 6, 36, 25, 6, 22, 98, 60, 95, 12],
        [94, 87, 47, 66, 53, 33, 84, 74, 36, 59, 13, 10, 22, 59, 47, 98, 78, 42, 75, 64, 100, 6, 77, 46, 45, 88, 28, 23,
         43,
         9, 30, 55, 14, 79, 95, 55, 62, 55, 61, 73, 31, 66, 50, 75, 52, 81, 82, 78, 52, 49],
        [26, 74, 30, 11, 3, 5, 10, 94, 83, 88, 46, 71, 96, 58, 58, 49, 23, 72, 53, 16, 13, 65, 7, 16, 95, 32, 84, 2, 31,
         21,
         94, 24, 69, 80, 82, 7, 82, 48, 92, 88, 15, 34, 84, 37, 41, 53, 28, 40, 66, 19],
        [13, 18, 78, 17, 53, 72, 28, 24, 74, 8, 8, 93, 86, 62, 28, 81, 16, 10, 43, 74, 16, 92, 39, 74, 22, 80, 61, 20,
         76,
         78, 5, 52, 95, 19, 76, 50, 4, 30, 36, 61, 26, 3, 4, 28, 13, 38, 44, 88, 78, 36],
        [89, 7, 23, 37, 70, 40, 26, 27, 40, 10, 57, 60, 60, 82, 27, 58, 51, 44, 8, 17, 82, 25, 25, 55, 75, 9, 95, 31,
         14, 2,
         78, 93, 85, 100, 16, 97, 89, 70, 47, 96, 53, 67, 7, 35, 87, 45, 59, 17, 33, 46],
        [41, 30, 7, 98, 99, 56, 67, 87, 70, 76, 68, 80, 73, 46, 31, 80, 83, 29, 36, 55, 92, 7, 20, 25, 90, 17, 98, 98,
         18,
         11, 45, 68, 44, 11, 58, 88, 90, 57, 46, 89, 4, 91, 47, 27, 47, 24, 95, 7, 61, 9],
        [29, 68, 15, 2, 73, 47, 100, 26, 45, 32, 34, 72, 89, 46, 89, 64, 56, 11, 87, 20, 31, 22, 11, 57, 41, 11, 59, 39,
         5,
         72, 15, 77, 4, 100, 48, 72, 28, 17, 41, 43, 16, 19, 4, 42, 100, 54, 90, 62, 2, 76],
        [13, 61, 26, 94, 52, 11, 18, 98, 2, 62, 83, 98, 70, 77, 32, 27, 13, 6, 1, 57, 50, 95, 80, 85, 6, 41, 11, 89, 56,
         45,
         80, 68, 57, 23, 19, 45, 90, 90, 57, 42, 99, 26, 54, 7, 22, 43, 20, 97, 49, 9],
        [41, 5, 32, 33, 75, 99, 31, 36, 68, 97, 34, 65, 46, 98, 55, 71, 58, 28, 19, 65, 58, 30, 30, 100, 41, 57, 84, 50,
         54,
         16, 27, 9, 5, 12, 65, 60, 30, 43, 82, 15, 61, 48, 96, 10, 63, 88, 50, 65, 62, 31],
        [56, 7, 70, 46, 40, 81, 98, 90, 84, 100, 26, 20, 79, 13, 12, 9, 75, 55, 79, 26, 67, 43, 78, 69, 6, 77, 14, 67,
         30,
         22, 50, 30, 1, 3, 68, 100, 83, 66, 44, 13, 78, 61, 67, 97, 71, 33, 51, 83, 52, 10],
        [12, 100, 57, 85, 26, 94, 51, 21, 92, 78, 41, 41, 15, 29, 9, 48, 82, 26, 70, 28, 28, 86, 79, 44, 6, 72, 8, 79,
         82,
         93, 6, 21, 79, 53, 30, 29, 13, 57, 11, 97, 68, 37, 98, 23, 79, 53, 47, 5, 86, 64],
        [28, 15, 20, 35, 44, 70, 97, 17, 3, 16, 31, 53, 98, 5, 16, 3, 64, 38, 24, 50, 45, 96, 37, 30, 90, 17, 92, 10,
         69,
         83, 41, 4, 86, 17, 31, 74, 39, 25, 37, 45, 21, 33, 46, 43, 70, 90, 45, 70, 46, 21],
        [30, 12, 44, 1, 61, 5, 36, 89, 62, 76, 41, 44, 69, 49, 98, 55, 48, 84, 81, 35, 16, 9, 75, 84, 7, 47, 77, 93, 68,
         81,
         17, 29, 81, 50, 32, 10, 84, 43, 74, 40, 50, 52, 68, 37, 36, 49, 40, 29, 17, 8],
        [7, 32, 50, 29, 23, 70, 45, 49, 39, 40, 80, 10, 88, 33, 66, 36, 4, 71, 23, 25, 38, 54, 19, 35, 75, 8, 75, 54,
         90,
         21, 14, 68, 25, 84, 35, 2, 23, 23, 15, 14, 94, 5, 15, 44, 72, 45, 63, 43, 68, 16],
        [1, 16, 35, 16, 17, 13, 24, 12, 15, 44, 63, 47, 20, 9, 45, 27, 13, 28, 20, 98, 37, 60, 34, 65, 70, 93, 99, 30,
         60,
         66, 21, 23, 20, 48, 78, 77, 96, 31, 99, 68, 69, 11, 13, 99, 25, 20, 14, 22, 20, 38],
        [74, 61, 94, 12, 34, 12, 56, 6, 25, 92, 73, 37, 70, 84, 64, 90, 100, 64, 53, 95, 16, 23, 7, 49, 69, 78, 21, 80,
         89,
         90, 67, 97, 52, 3, 100, 54, 71, 30, 31, 1, 2, 15, 63, 56, 64, 5, 45, 53, 47, 19],
        [95, 64, 15, 28, 64, 94, 34, 63, 34, 34, 60, 53, 83, 56, 33, 18, 55, 31, 28, 75, 100, 14, 4, 47, 47, 24, 88, 90,
         29,
         88, 95, 60, 72, 64, 55, 80, 76, 65, 97, 48, 33, 82, 39, 87, 77, 18, 68, 84, 33, 73],
        [96, 10, 61, 56, 6, 99, 81, 42, 73, 74, 38, 74, 51, 35, 37, 19, 17, 63, 49, 59, 78, 5, 94, 35, 29, 28, 48, 7,
         90,
         45, 54, 49, 2, 37, 85, 15, 28, 5, 96, 17, 61, 14, 11, 35, 1, 58, 62, 37, 79, 48],
        [73, 33, 17, 77, 38, 81, 49, 77, 6, 68, 99, 65, 76, 85, 54, 9, 77, 24, 82, 15, 62, 14, 66, 53, 50, 63, 3, 57,
         75,
         38, 54, 98, 75, 19, 18, 35, 96, 50, 20, 67, 52, 56, 98, 4, 37, 51, 53, 87, 13, 34],
        [66, 73, 57, 71, 45, 30, 41, 88, 46, 36, 81, 90, 24, 31, 63, 6, 45, 61, 74, 74, 47, 69, 13, 43, 17, 28, 16, 53,
         28,
         9, 40, 85, 67, 71, 71, 67, 11, 18, 1, 19, 61, 80, 31, 51, 90, 11, 63, 67, 49, 37],
        [40, 37, 78, 36, 1, 28, 27, 100, 86, 45, 46, 61, 82, 77, 27, 69, 58, 31, 31, 85, 94, 37, 98, 24, 34, 45, 5, 40,
         58,
         22, 7, 94, 55, 83, 41, 46, 91, 60, 8, 40, 9, 54, 7, 76, 100, 51, 67, 70, 75, 3],
        [44, 96, 57, 45, 65, 21, 71, 41, 69, 70, 37, 59, 97, 78, 49, 19, 41, 21, 11, 90, 54, 54, 33, 74, 81, 57, 53, 42,
         77,
         86, 94, 97, 94, 63, 60, 26, 38, 24, 53, 63, 29, 100, 37, 59, 48, 50, 33, 80, 51, 33],
        [49, 75, 83, 15, 48, 43, 71, 80, 75, 8, 81, 77, 11, 9, 26, 19, 13, 69, 31, 67, 39, 84, 99, 90, 50, 78, 94, 33,
         24,
         89, 6, 94, 21, 8, 26, 91, 41, 1, 16, 43, 19, 22, 38, 73, 99, 47, 47, 26, 12, 28],
        [30, 38, 27, 32, 5, 8, 39, 45, 59, 57, 44, 12, 39, 79, 60, 54, 73, 34, 29, 29, 24, 88, 94, 71, 1, 45, 78, 65,
         87,
         35, 61, 20, 87, 91, 25, 66, 66, 97, 14, 36, 78, 21, 22, 36, 74, 52, 10, 98, 65, 75],
        [22, 7, 70, 91, 85, 10, 87, 71, 28, 3, 23, 56, 6, 34, 94, 10, 45, 54, 80, 8, 62, 39, 52, 32, 79, 16, 66, 64, 44,
         46,
         34, 37, 78, 91, 28, 3, 25, 57, 5, 18, 42, 17, 86, 100, 83, 48, 81, 90, 18, 18],
        [17, 7, 17, 89, 36, 62, 80, 42, 56, 53, 67, 27, 26, 32, 58, 47, 93, 52, 2, 36, 25, 12, 13, 52, 25, 96, 54, 58,
         86,
         24, 58, 16, 64, 23, 84, 20, 52, 5, 83, 3, 4, 42, 28, 29, 94, 76, 97, 84, 95, 89],
        [55, 62, 18, 72, 75, 55, 30, 5, 19, 32, 48, 31, 14, 75, 9, 12, 21, 94, 53, 58, 93, 24, 81, 12, 74, 39, 27, 98,
         65,
         3, 33, 71, 78, 34, 76, 66, 78, 75, 9, 49, 43, 22, 77, 27, 39, 44, 14, 56, 79, 16],
        [9, 64, 27, 37, 91, 34, 8, 39, 53, 34, 89, 95, 82, 81, 34, 56, 63, 80, 54, 36, 97, 75, 44, 38, 21, 42, 93, 73,
         49,
         22, 39, 12, 16, 52, 50, 15, 86, 48, 74, 94, 70, 5, 98, 32, 71, 7, 22, 73, 29, 47],
        [53, 65, 24, 1, 52, 76, 24, 37, 55, 57, 71, 69, 38, 66, 80, 45, 13, 66, 10, 32, 40, 47, 62, 98, 38, 78, 15, 15,
         79,
         99, 81, 18, 82, 11, 99, 18, 63, 8, 22, 80, 65, 66, 32, 44, 47, 18, 55, 93, 53, 27],
        [86, 72, 95, 92, 60, 14, 76, 2, 31, 5, 61, 69, 80, 57, 96, 85, 34, 100, 38, 72, 98, 4, 70, 41, 17, 86, 7, 3, 74,
         6,
         28, 86, 47, 69, 93, 55, 84, 43, 20, 37, 97, 98, 12, 34, 41, 75, 89, 9, 50, 82],
        [40, 59, 64, 34, 21, 46, 72, 36, 81, 56, 89, 30, 65, 16, 1, 62, 39, 1, 56, 7, 47, 71, 98, 95, 45, 60, 52, 96,
         25,
         99, 27, 47, 100, 65, 75, 58, 98, 55, 73, 38, 94, 91, 29, 8, 27, 3, 88, 53, 70, 50],
        [30, 37, 92, 77, 38, 6, 60, 7, 98, 17, 82, 57, 63, 21, 57, 77, 81, 3, 78, 95, 80, 56, 92, 38, 36, 83, 77, 16,
         51,
         74, 74, 20, 56, 42, 25, 69, 58, 75, 92, 23, 76, 89, 2, 3, 58, 1, 42, 99, 23, 73],
        [15, 80, 28, 4, 63, 85, 66, 94, 35, 68, 2, 85, 28, 77, 48, 64, 59, 50, 9, 78, 90, 24, 6, 33, 28, 53, 68, 43, 22,
         26,
         28, 26, 62, 37, 70, 16, 17, 17, 76, 37, 53, 59, 98, 70, 51, 88, 81, 71, 96, 100],
        [98, 67, 24, 30, 58, 52, 78, 3, 34, 32, 91, 21, 17, 50, 19, 100, 58, 18, 50, 42, 87, 59, 10, 94, 2, 52, 91, 44,
         76,
         47, 58, 79, 95, 59, 89, 80, 89, 96, 50, 62, 29, 24, 89, 34, 58, 74, 44, 82, 66, 61]])
    pop_value = []
    pop_weight = []
    pop_violation = []
    for i in range(n_pop):
        x_t = pop[i].reshape(n_var, 1)
        val = pop[i] * value * x_t
        pop_value.append(val[0, 0])
    for i in range(n_pop):
        wgh = 0
        for j in range(n_var):
            wgh = weight[j] * pop[i][j] + wgh
        pop_weight.append(wgh)
        if wgh > knapsack_size:
            pop_violation.append(wgh - knapsack_size)
        else:
            pop_violation.append(0)
    return pop_value, pop_weight, pop_violation
