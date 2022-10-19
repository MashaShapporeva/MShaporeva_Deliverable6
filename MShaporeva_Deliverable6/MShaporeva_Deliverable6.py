
upTo, now, prev, counter = 0, 1, 0, 0
while upTo < 1:
    print ("Enter an integer greater than 0: ")
    upTo = int(input())
evenNum = []
oddNum = []
fibonacciNum = [0, 1]
for a in range(0, upTo):
    evenNum.append(counter)
    counter+=2
    oddNum.append(counter-1)
for a in range(0, upTo-2):
    fibonacciNum.append(fibonacciNum[-1] + fibonacciNum[-2])
print ("\tEven\tOdd\tFibonacii" )
for a in range(0, upTo):
    print (str(a) + "\t" + str(evenNum[a])+ "\t" + str(oddNum[a]) + "\t" + str(fibonacciNum[a]))