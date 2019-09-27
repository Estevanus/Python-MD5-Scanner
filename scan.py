import sub
import multiprocessing
import time
import os
import time

#put in this variable the md5 that you want to scan
md5text = '81dc9bdb52d04dc20036dbd8313ed055'

#number of threads that you want to utilize
numberOfCore = 3


def monitoring(procList):
	#checking if some process is already done scanning
	waktu = 0
	isDone = False
	while isDone == False:
		for i in procList:
			if i.is_alive() == False:
				print("some process is death or done working")
				hasil = q.get()
				if hasil != None:
					isDone = True
					print("result found, terminating other process now...")
					for j in procList:
						if j != i:
							print("killing process {0}...".format(str(j)))
							j.kill()
					break
				
		time.sleep(1)#use this to let the cpu work less
		waktu = time.time() - timeStart
		cek = waktu, isDone
		#print(cek)
		if isDone == True:#exiting process checking
			break
		
	
	return hasil
	


if __name__ == "__main__":
	ps = []
	q = multiprocessing.Queue()
	timeStart = time.time()
	gotit = False
	for i in range(numberOfCore):
		p = multiprocessing.Process(target = sub.scan3, args = (i, numberOfCore, md5text, timeStart, q))
		p.start()
		ps.append(p)
	
	hasil = monitoring(ps)
	endTime = time.time() - timeStart
	if hasil != None:
		print("After {0} seconds.The result found is {1}".format(endTime, hasil))
	else:
		print("Not Found")