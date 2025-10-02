#!/usr/bin/env python3

# script che controlla se ci sono simboli nella stringa

# .isSymbols     True se nella stringa trova almeno 1 simbolo
# .isonlySybols  True se la stringa è composta solo da simboli

# Realizzato da Biagio Costigliola alias h4rck4n0

class myStringa():

    # set di simboli
    simboli = {
               '+', '-', '*', '/', '%', '(', ')', 
               '[', ']', '{', '}', '=', '<', '>', 
               '!', '?', '@', '€', '|', '"', '£', 
               '&', '^', 'ç', '#', '°', '§', ',',
               '.', ';', ':', '_', '~', '`', '¿',
              }                                      
    

    def __init__(self, stringa):
        self.stringa = stringa

   
    @property
    def isSymbols(self):
        my_set_string = set(self.stringa)
        for x in my_set_string:
            if set(x) <= self.simboli:
                return True
        return False
    
    @property
    def isonlySymbols(self):
        my_set_string = set(self.stringa)
        for x in my_set_string:
            if set(x) <= self.simboli:
                pass
            else:
                return False
        return True
        


'''
################################# Esempi ################################## 

##  .isSymbols  

## print(myStringa("Hello+").isSymbols) # True contiene simboli '+'

##  print(myStringa("New York").isSymbols) # False NON contiene simboli


## .isonlySymbols

## print(myStringa("/&%!^^").isonlySymbols) # True contiene solo simboli

## print(myStringa("Ciao!!!").isonlySymbols) # False non contiene solo symboli


############################################################################
'''
