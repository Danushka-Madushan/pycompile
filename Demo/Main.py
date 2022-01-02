from time import sleep

num = 1
for x in range(100):
  print("$ Hello from Compiler! XD -> %i" % num, end='\r')
  num+=1
  sleep(0.1)
