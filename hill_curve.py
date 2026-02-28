import numpy as np
import matplotlib.pyplot as plt

# hill equation parameters
Emax = 1.0 #maxmimum effect the drug system can produce. Here you can normalise it to 1, so the top of the curve equals 1. think 100 percent repsonse
EC50 = 1e-6 #concentration that gives 50 percent of Emax. one micromolar
n = 1.0 #Hill coefficient. this controls steepness

# Dose range (log-spaced)
dose = np.logspace(-12, -3, 400) #here we are making 400 dose values between 10^-12 and 1-^-3 molar. log spaced.

# Hill equation
response = (Emax * (dose ** n)) / ((EC50 ** n) + (dose ** n)) #Hill equation implemented in code
#dose ** n, dose raised to the Hill coefficient 
#EC50 ** n, EC50 raised to the Hill coefficient
#Emax * dose^n, As dose increases, numerator increases toward Emax times large number.
#EC50^n + dose^n, at low dose, EC50^n dominates, response is near zero.
#at dose = EC50, dose^n equals EC50^n, so response become Emax * 1/( 1+1) = Emax/2.
#at high dose^n dominates, response approaches Emax.


# Plot
plt.figure() #start a new blank point
plt.semilogx(dose, response) #plot response against dose, but the x axis is logarithmic
plt.xlabel("Dose (M)") #label the x axis, molar concentration
plt.ylabel("Response (fraction of Emax)") #label the y axis, you are plotting response as fraction of Emax because Emax is 1.0
plt.title("Dose-response curve (Hill equation)") #title
plt.ylim(0, 1.05) #force y axis limits. so top is not clipped
plt.grid(True, which="both") #add gridlines for both major and minor ticks. it makes log plots easier to find.
plt.show() #display the plot line 
