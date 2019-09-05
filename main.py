# You have to install matplotlib and numpy before running the script using these commands:
# python -m pip install -U matplotlib
# python -m pip install -U numpy
import sortingAlgs as alg
import numpy as np
import matplotlib.pyplot as plt
import time
from random import randint

algs = [alg.insertionSort, alg.bubbleSort, alg.mergeSort, alg.quickSort, alg.countingSort]
results = {"insertionSort": [], "bubbleSort": [], "mergeSort": [], "quickSort": [], "countingSort": []}
inputSizes = [10000, 30000, 50000, 70000, 90000]
counter = 1
for i in inputSizes:
  print("=> Implementing algorithms for n = ", i)
  file = "data\\input" + str(counter) + ".txt"
  counter += 1
  fr = open(file, "w")
  fr.writelines("%s\n" % item for item in [randint(0, 100000) for p in range(0, i)])
  fr.close()
  fr = open(file, "r")
  lines = fr.readlines()
  fr.close()

  for fun in algs:
    arr = [int(item.rstrip('\n')) for item in lines]
    
    start = time.time()
    if fun.__name__ is "insertionSort" or fun.__name__ is "bubbleSort":
      fun(arr)
    elif fun.__name__ is "mergeSort" or fun.__name__ is "quickSort":
      fun(arr,0,len(arr)-1)
    elif fun.__name__ is "countingSort":
      arr = fun(arr,100000)
    end = time.time()

    Tn = (end-start)*1000
    results[fun.__name__].append(Tn)

print("\n=> Results:")
for key, value in results.items():
  Tns = list(zip(inputSizes, value))
  print(key, ":")
  for t in Tns:
    print(t)
  print("\n")
  plt.figure()
  plt.plot(value)
  plt.savefig('plots\\' + key + '-plot.png')

  plt.figure()
  labels, ys = zip(*Tns)
  xs = np.arange(len(labels)) 
  plt.bar(xs, ys, 0.5, align='center')

  plt.xticks(xs, labels)
  plt.yticks(ys)

  plt.savefig('plots\\' + key + '-bar.png')
print("\n=> Plots saved to 'plots' folder.")