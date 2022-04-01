def function(limit):
    sum =0
    for i in range(1,limit+1):
        if(i%3==0 or i%5==0):
            sum =sum+i

    print(sum)

print(function(20))