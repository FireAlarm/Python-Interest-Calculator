#formula I=prt
import random
p = 7600
r = 0.048
t = 9

I = (p*r*t)

finalsimple = round(I, 2)
print( "Simple interest " + str(finalsimple)) 

# compound interest formula A = P(1+(R/N)^NT
# the principal goes here
principal = 1500
# rate as a decimal 
rate = 0.024
# number of years
years = 3
# number of times per year it compounds
compoundsPerYear = 1
# meat and potatos of the script
A = principal*(1 + rate/compoundsPerYear)**(compoundsPerYear*years)

finalCompound = round(A, 2)



print( "Compound interest " + str(finalCompound))
