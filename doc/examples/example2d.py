'''
Examples of use of the class BayesianOptimization
	- branin function

''' 
import GPy
import GPyOpt


# create the object function
f_true = GPyOpt.fmodels.experiments2d.branin()
f_sim = GPyOpt.fmodels.experiments2d.branin(sd= 0.1)
#f_true.plot()
bounds = f_true.bounds
H = 10

# starts the optimization with 3 data points 
myBopt = GPyOpt.methods.BayesianOptimizationUCB(bounds,acquisition_par=2)
myBopt.start_optimization(f_sim.f,H=H)
myBopt.plot_acquisition()
myBopt.plot_convergence()

# cotinue optimization for 10 observations more
myBopt.continue_optimization(H=1)
myBopt.plot_acquisition()
#myBopt.plot_convergence()
myBopt.suggested_sample
f_true.min
f_true.fmin











