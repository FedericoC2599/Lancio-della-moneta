import random as random

def lancio():
	'''
	Funzione che simula il lancio di una moneta
	stampando in output i valori testa o croce
	
	Parametri
		None
		
	Ritorna
		None
	'''
	valore = random.randrange(2)
	
	if valore == 0:
		print('Testa')
	else:
		print('Croce')
		
		
lancio()