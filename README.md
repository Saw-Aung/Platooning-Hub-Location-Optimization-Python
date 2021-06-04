# Platooning-Hub-Location-Optimization-Python

This is the optimization algorithm using LocalSolver Optimizer on Python console.
This alogrithm is the same as my another repository using XpressIVE solver.

However, the XpressIVE can solve a bigger dataset within a shorter time than LocalSolver.

Localsolver can only effectively solve the dataset size of around 30 nodes.

Turkish_large.in represents the distance matrix and flow matrix of Turkish 81 cities by Prof Bahar Yetis Kara.
Since the algorithm cannot optimize the 81-cities dataset, the dataset size is reduced to 20 cities (Turkish_reduced_20.in), 30 cities (Turkish_reduced_30.in) and so on for optimization.

I recommend to use XpressIVE rather than LocalSolver because XpressIVE is far more efficient and more accurate in optimization than LocalSolver.
