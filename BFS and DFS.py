#BFS

# dict = {0:[1,3],1:[0,3,2,5,6],2:[1,3,4,5],3:[0,1,2,4],4:[2,3,6],5:[1,2],6:[1,4]}
dict = {1: [2, 3], 2: [1, 4], 3: [1, 4, 5], 4: [2, 3], 5: [3, 6], 6: [5]}
visited = []
lis_queue = []
var = list(dict.keys())[0]
lis_queue.append(var)

for i in dict.keys():
    value = list(dict[i])
    # print(value)
    if i not in visited:
        visited.append(i)
# print(visited)

def neighbor():
    for i in dict.values():
        for j in i:
            if j not in lis_queue:
                lis_queue.append(j)

neighbor()
# print(lis_queue)
print("\nBFS Traversal :")
for k in range(len(lis_queue)):
    l = lis_queue.pop(0)
    print(l,end=" ")
print("\n")


#DFS
print("DFS Traversal :")

# dict = {0:[1,3],1:[0,3,2,5,6],2:[1,3,4,5],3:[0,1,2,4],4:[2,3,6],5:[1,2],6:[1,4]}
visited = []
lis_stack = []

fir_visited_node = list(dict.keys())[0]
# visited.append(fir_visited_node)
lis_stack.append(fir_visited_node)

while len(lis_stack) != 0:
    curr = lis_stack.pop(-1)
    if curr not in visited:
        print(curr,end=" ")
        visited.append(curr)
        for i in dict[curr]:
            lis_stack.append(i)
print("\n")
            # print(lis_stack)
# print(visited)
 # dict = {1: [2, 3], 2: [1, 4], 3: [1, 4, 5], 4: [2, 3], 5: [3, 6], 6: [5]}

    # values = dict[i]
    # print(values)
    # for j in values:
    #     # print(j)
    #     if j not in visited:
    #         print(j)
    #         visited.append(j)
    #         lis_stack.append(j)


# print(visited)
# print(lis_stack)
# def reverse(visited):
#     visited.reverse()
#     return visited
# rev_visited = (reverse(visited))

# i = len(lis_stack)-1 #7
# while i <= len(lis_stack):      #7 < 8
#     p = lis_stack.pop(i)
#     i -= 1
#     if i not in visited:
#         lis_stack.append(i)
#         i -= 1
#
# print("\n\n")
# ver = len(lis_stack) - 1      #5
# while lis_stack:               #1 > -1
#     p = lis_stack.pop(ver)
#     print(p," " ,lis_stack)
#     ver-=1        #i = 0
#     # print(lis_stack[i])
#     for l in dict[ver]:
#         # print("l",dict[ver])
#         if l not in visited:   #visited/lis_stack ?
#             lis_stack.append(l)
#             print(lis_stack)
