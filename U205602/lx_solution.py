__author__ = "@MTX5148635"


def knightTravel(x, y):
    # 输入某个点的理论可行邻域，返回对可行邻域按其下一可行邻域数升序排序的（x，y，实际可行数）元组列表
    def sortNeighbors(neighbors):
        sortNeighborS = []
        for i in range(len(neighbors)-1):  # 减去列表最后一项：可行领域数
            nei = neighbors[i]
            countIndex = len(dic[nei])-1  # 邻居的理论可行邻域数
            newTurple = (nei[0], nei[1], dic[nei][countIndex])  # （x，y，实际可行领域数）
            sortNeighborS.append(newTurple)
            # 构造三元元组
        sortNeighborS.sort(key=lambda x: (x[2], x[0], x[1]))  # 按照实际可行邻域排序,升序
        return sortNeighborS

    # 返回单个点的单个邻域元组
    def count(x, y, dx, dy):
        return (x+dx, y+dy) if 0 <= x+dx <= 7 and 0 <= y+dy <= 7 else -1

    # 输入位置元组，返回单个点的可行落脚点元组数列,末尾添加了实际可行领域初始值，即理论可行邻域数
    def direction(loc):
        plus = [(1, 2), (-1, -2), (1, -2), (-1, 2),
                (2, 1), (-2, -1), (-2, 1), (2, -1)]
        dirs = []  # 理论可行邻域元组数组+实际可行邻域数单元组
        countNum = 0
        for i in plus:
            dir = count(loc[0], loc[1], i[0], i[1])
            if dir != -1:
                countNum += 1
                dirs.append(dir)
                # print(dir)
        dirs.append((countNum))
        return dirs

    # 返回包含所有点的directions（可行邻域元组列表）的字典
    def dictionary():
        dic = {}
        for i in range(8):
            for j in range(8):
                loc = (i, j)
                dic[loc] = direction(loc)  # 字典赋值语句
        return dic

    # 打印可行点数量分布矩阵
    # def distributeMatrix():
    #     matrix=direction()
    #     a=list(matrix.values())
    #     b=[]
    #     print("------------------------")
    #     for i in a:
    #         b.append(len(i))
    #     for i in range(64):
    #         if i%8==0:
    #             print("\n")
    #         print(b[i],end=" ")
    #     print("------------------------")
    # distributeMatrix()

    def walkInOrOut(next, state):
        nextNeighbors = dic[next][:-1]  # 取出落脚点的理论可行邻域
        for i in nextNeighbors:  # 令next的neightbors的count--/++
            newNeightbors = dic[i]
            count_ = newNeightbors[len(newNeightbors)-1]  # 读出最后一项
            if state == 1:  # 走一步
                newNeightbors.append(newNeightbors.pop()-1)
            elif state == -1:  # 退一步
                newNeightbors.append(newNeightbors.pop()+1)
            dic[i] = newNeightbors  # 修改字典中的可行count

    def perm(nowTurple):
        nonlocal dic
        nonlocal path
        nonlocal travelList
        if (len(path) == 64):
            return path[:]
        Neighbors = dic[nowTurple]
        # print("Neighbors",Neighbors)
        sorted_Neighbors = sortNeighbors(Neighbors)  # 对邻域进行升序排序
        # print("sorted_Neighbors",sorted_Neighbors)
        # print("path.len", len(path),"\t","path",path)
        for i in range(len(sorted_Neighbors)):
            # result=0
            next = (sorted_Neighbors[i][0], sorted_Neighbors[i][1])
            # print("next",next)
            if next not in path:
                walkInOrOut(next, 1)
                path.append(next)
                # print("pa.apend",path)
                # print("append Success")
                result = perm(next)
                if result:
                    if result not in travelList:
                        travelList.append(result)
                    return 0
                # print("46465464654")
                walkInOrOut(next, -1)
                path.pop()

    dic = dictionary()
    travelList = []
    path = [(x, y)]
    perm((x, y))
    for i in travelList:
        print(i)
    print("travelListLen", len(travelList))
    return len(travelList)


if __name__ == "__main__":
    (x_, y_) = list(map(int, input().split(" ")))
    knightTravel(x_, y_)
    # max_=0
    # for i in range(8):
    #     for j in range(8):
    #         print(i,j)
    #         max_=max(max_,knightTravel(i,j))
    # print(max_)


"""
改造元组列表，列表最后放置单元组（count）代表实际可行邻域数，count初始值=理论可行邻域数
每走一步，落脚点的所有可行邻域的count值减一（可行邻域减一）
每返回一步，出脚点所有可行邻域count+1
每层perm先对邻域排序，选出实际可行领域最小的（z最小），再遍历所有邻域
"""


# # import  numpy as np
# # 打表算法：
# str="33 30 57 20 55 18 5 2 58 21 32 29 6 3 54 17 31 34 23 56 19 52 1 4 22 59 28 35 64 7 16 53 45 24 63 8 43 36 51 14 60 9 44 27 48 15 42 39 25 46 11 62 37 40 13 50 10 61 26 47 12 49 38 41"
# arr=list(map(int,str.split(" ")))
# matrix = []
# for r in range(8):
#     for c in range(8):
#         if c == 0:
#             matrix.append([])
#         matrix[r].append(arr[8*r+c])
# # print(matrix)
# x,y=list(map(int,input().split(" ")))
# dis=matrix[x][y]
# # print("dis",dis)
# for i in range(8):
#     for j  in range(8):
#         matrix[i][j]=(matrix[i][j]-dis)%64+1
#
# for i in range(8):
#     for j in range(7):
#         print(matrix[i][j]," ",end="")
#     print(matrix[i][7])
