def ePotenciaDois(n):
	# caso base
	if n == 1:
                return True
	x = n%2
	if x != 0 or n <= 0:
		return False
	# caso recursivo
	if x == 0:
		return ePotenciaDois(n/2)

print(ePotenciaDois(8))
