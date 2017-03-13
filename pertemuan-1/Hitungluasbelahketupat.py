import time
start_time = time.time()
print('Hitung luas belah ketupat')
d1 = input('diagonal 1 = ' )
d2 = input('diagonal 2 = ' )
L = (d1 * d2) / 2
Luas = str(L)
if Luas == '1':
	x = 'satu'
elif Luas == '2':
	x = 'dua'	
elif Luas == '3':
	x = 'tiga'
elif Luas == '4':
	x = 'empat'
elif Luas == '5':
	x = 'lima'
elif Luas == '6':
	x = 'enam'
elif Luas == '7':
	x = 'tujuh'
elif Luas == '8':
	x = 'delapan'
elif Luas == '9':
	x = 'sembilan'
elif Luas == '0':
	x = 'nol'
else:
	x = 'lebih dari sembilan'

print('Hasil luas belah ketupat = ' + Luas + '(' + x + ')')
print("time : %s detik " % (time.time() - start_time))

