count=0
sumCost=10000
# 参数为index
def perm(shuzu,start,end):
    global count
    if(start==end):
        compare(matrix,shuzu)
        # print("shuzu",shuzu,"sumCost",sumCost )
        count+=1
    else:
        for i in range(start,end):
            # print(start,"start")
            shuzu[start],shuzu[i]=shuzu[i],shuzu[start]
            perm(shuzu,start+1,end)
            shuzu[start], shuzu[i] = shuzu[i], shuzu[start]

def compare(matrix,shuzu):
    sum=0
    global sumCost
    for i in range(len(shuzu)-1):
        x=shuzu[i]
        y=shuzu[i+1]
        if matrix[x][y]==-1:
            return -1
        # print("matrix[x][y]",matrix[y][y],sep=" ")
        sum+=matrix[x][y]
    if(sum<sumCost):
        # print("sum",sum)
        sumCost=sum

num=int(input())
matrix=[[0 for i in range(num)]for j in range(num)]#t（n^2），m(n^2)
for i in range(num):
    matrix[i]=input().split(" ")
    matrix[i]=[int(j) for j in matrix[i]]#t(n^2)
# shuzu=[int (j) for j in range(num)] #t(n)
perm([int (j) for j in range(num)],1,num)
print(sumCost)

# 计算阶乘
# def jiechen(num,jc):
#     if(num==1):
#         return jc
#     else:
#         return jiechen(num-1,jc*num)