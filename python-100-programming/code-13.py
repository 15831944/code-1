#打印出所有的水仙花数，水仙花数指一个三位数，其各位数字立方和等于该数本身
#例如，153，1的立方加5的立方加3的立方等于153
for n in range(100,1000):
    i = n//100
    j = (n//10)%10
    k = n%10

    if n == (i*i*i + j*j*j + k*k*k):
        print(n)
