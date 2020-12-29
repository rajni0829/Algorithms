#DP using Fibonacci Series

#BRUTE FORCE APPROACH
print("\nn : Last Value untill where you want the series. \n")

bruteF_count = 0
def bruteForce(len):      #simplest way of solving
    global bruteF_count
    bruteF_count += 1
    if len <= 1:
        return len
    else:
        bruteF = bruteForce(len-1) + bruteForce(len-2)
        return bruteF

#TABULATION           #store nd solve huge problem by using the stored data (solve small problem 1st)
botUp_count = 0
def bottomUp(len):
    global botUp_count
    botUp_count += 1
    if len <= 1:
        return len
    fib_lis = []
    fib_lis.append(0)
    fib_lis.append(1)

    for j in range(2,len+1):
        fib_lis.append(fib_lis[j - 1] + fib_lis[j - 2])
    return fib_lis[len]

topD_count = 0
def topDown(len):      #solve huge solve nd chote apne aap hotte rahenege
    global topD_count
    topD_count +=1

    if len in fib_dic:
        return fib_dic[len]
    else:
        fib_dic[len] = topDown(len-1) + topDown(len - 2)
        return fib_dic[len]

# for i in range(len):
#     print(bruteForce(i))
# print(bruteF_count)

while True:
    try:
        fib_dic = {0:0,1:1}
        fib_num = int(input("Enter the nth value of Fib Series : "))
        print("\nFibonacci series is :")
        for i in range(fib_num):
            print(bruteForce(i+1),end=" ")
        print("\n\nWhen n:{} , fibonacci no. is {}".format(fib_num, bottomUp(fib_num)))
        print("({}) is Total no. of calls in BottomUp or TABULATION".format(botUp_count))
        topDown(fib_num)
        print("\n({}) is Total no. of calls in topDown or MEMOIZATION".format(topD_count))
        bruteForce(fib_num)
        print("\n({}) is Total no. of calls in BRUTE FORCE APPROACH\n".format(bruteF_count))
        break
    except:
        print()
        break
