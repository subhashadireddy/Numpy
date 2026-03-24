import numpy as np 
ages = np.array([[21,17,19,20,26,30,18,65],
                 [39,22,15,99,18,19,20,21]])

teenagers = ages[ages < 18]
print(teenagers)
print(ages)

not_teenagers = ages[ages >= 18]
print(not_teenagers)

adults = ages[(ages>=18) & (ages<65)] #dont use and -- or use &--|
print(adults)

seniors =ages[ages>65]
print(seniors)

evens = ages[ages%2 ==0]
print(evens)
odds = ages[ages%2 !=0]
print(odds)

#to preserve original shape 
adults = np.where(ages >= 18,ages,0)
print(adults)