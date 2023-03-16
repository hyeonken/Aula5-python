# Metodo mais rapido e pratico

import time
 
def convert(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(n))
     
# Driver program
n = 4000
print(convert(n))