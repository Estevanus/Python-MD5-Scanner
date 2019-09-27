import time
import hashlib

debug = False

def loop(start, end):
	for i in range(start, end):
		print(i)
		
		
def scan(start, end, ygScan, forHasil, timeStart):
	print("process start scanning from {0} to {1}".format(start, end))
	isFound = False
	blen = 1
	
	#defineding blen
	while True:
		try:
			bi = start.to_bytes(blen, 'little')
			break
		except:
			blen += 1
	
	for i in range(start, end):
		if i == ygScan:
			dapat = i.to_bytes(blen, 'little').decode()
			waktuDidapati = time.time() - timeStart
			print("hasil ditemukan, nilainya ialah " + dapat + " dalam waktu " + str(waktuDidapati))
			isFound = True
			forHasil.put(dapat)
			break
			
		if (i + 1) ** (1/blen) > 255:
			blen += 1
			
	if isFound == False:
		try:
			print("hasil akhir dari process ini ialah :")
			print(i)
		except:
			pass
		forHasil.put(None)
	print(isFound)
	
def scan2(urutan, beda, ygScan, timeStart):
	rangeStart = urutan * beda
	rangeEnd = (urutan + 1) * beda - 1
	#cek = urutan, beda, rangeStart
	#print(cek)
	i = 0
	bedaKe = 0
	n = 0
	hasil = 0
	while n < ygScan:
		n = i + rangeStart + beda * beda * bedaKe
		cek = n, i, rangeStart, beda, bedaKe
		#print(n)
		if i < beda - 1:
			i += 1
		else:
			bedaKe += 1
			i = 0
			
		if n == ygScan:
			hasil = n
			
	endTime = time.time() - timeStart
	print("hasilnya ialah {0} dalam waktu {1}".format(hasil, endTime))
	
	
def getDigitKe(nilai):
	i = 0
	while nilai / 256 >= 256:
		nilai /= 256
		i+=1
	return i + 1
	
def scan3(urutan, beda, md, timeStart, forHasil):
	'''
	urutan = index of Process
	beda = number of Process
	md = md5 text to compare it
	timeStart = Starting point where the time is start, this will be remove in future
	forHasil = A queue object to share between process
	'''
	rangeStart = urutan * beda
	rangeEnd = (urutan + 1) * beda - 1
	i = 0
	bedaKe = 0
	n = 0
	hasil = 0
	digitKe = 1
	while True:
		n = i + rangeStart + beda * beda * bedaKe
		cek = n, i, rangeStart, beda, bedaKe
		if i < beda - 1:
			i += 1
		else:
			bedaKe += 1
			i = 0
			
		cek = n, digitKe
		try:
			b1 = n.to_bytes(digitKe, 'little')
			cek = n, b1
		except OverflowError:
			digitKe += 1
			print("it's already {0} digits used".format(digitKe))
		if hashlib.md5(b1).hexdigest() == md:
			hasil = b1.decode()
			break
			
		
	forHasil.put(hasil)

