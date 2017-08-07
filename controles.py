
# Ciclo While
contador = 0
while contador < 5:
	print("Numero %i" % contador)
	contador = contador +1


# Ciclo For
for x in xrange(1,10):
	print('Numero %i' % x)


# Ciclo For
# Rango de 1 a 100 de 5 en 5
for x in xrange(1,100,5):
	print('Numero %i' % x)


# Ciclo para hacer un factorial
factorial = 5
acum = 1
while  factorial>0:
	acum = acum * factorial
	factorial = factorial - 1



print ("%i" % acum)


# Factorial por medio de recursion
# 5! = 5 * 4!
def factorial(x):
	if x == 0:
		return 1
	else:
		return x * factorial(x -1)

print(factorial(5))

