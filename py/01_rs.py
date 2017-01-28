from math import sqrt, log
import math as m
print("\n\n\n_______________________________________")

c =  299792458           #m/s
g =  9.81           # m/s^2
Y = 3600*24*365         # secondi in un anno

print("10^9 ANNI LUCE")
ly = Y             # m
d = 10e9 * Y  *c         # m

print("tempo necessario: ")
t = sqrt(d*d/(c*c) + 2*d/g) #ly
print(t/Y, " anni", )
    
print("tempo proprio:")
tau = log( sqrt(1 + pow(g*t/c,2)) + g*t/c ) *c/g #s
print(tau/Y, " anni")


print("\nPERCHE' NON ANDIAMO SU GIOVE?")
#distanza Terra-Giove = 8 ore-luce
lh = c * 3600 #m
TG = 8 * lh   #m
TM = TG / 2   #m

print("tempo classico: ")
tC = 4 * sqrt(2*TM/g) 
print(tC/Y, " anni")

print("tempo relativistico a meta' strada: ")
tTM = sqrt(TM*TM/(c*c) + 2*TM/g) #s
print(tTM/Y, " anni", )
    
print("velocita' a meta' strada: ")
vTM = g*tTM / (sqrt(1+pow(g*tTM/c,2)))
print(vTM/c, "volte la velocita' della luce")

print("tempo per la seconda meta'")
v = vTM
tMG = (v/sqrt(1-pow(v/c,2)) 
        + c * sqrt( 
            pow(v/c,2) /( 1-pow(v/c,2) )
            -2*g*TM/(c*c)* sqrt( 1+pow(v/c,2)/( 1-pow(v/c,2)  ))
            )  
      ) / g
print(tMG/Y, " anni")
