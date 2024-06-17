# my_list = [1,2,'3', True] # We assume this list won't mutate for example
# len(my_list)
# my_list.index('3')
# my_list.count(2)


# my_list[3]
# my_list[1:]
# my_list[-1]
# my_list[::1]
# my_list[::-1]
# my_list[0:3:2]


# my_list * 2
# my_list + [100]
# my_list.append(100)
# my_list.extend([100, 200])
# my_list.insert(2,'!!!')
# ' '.join(['hello','there'])

# basket = ['apples','pears','oranges']
# new_basket = basket.copy()
# new_basket = basket[:]


# mList = [63, 21, 30, 14, 35, 26, 77, 18, 49, 10]
# first, *x, last = mList
# print(first) #63
# print(last) #10 

# # Matrix 
mx = [[1,2,3], 
          [4,5,6], 
          [7,8,9]]
mx[2][0]


for row in range(len(mx)):
    for col in range(len(mx[0])):
        print(mx[row][col])

# Transform into a list:
[mx[row][col] for row in range(len(mx)) for col in range(len(mx[0]))]

# list Comprehensions

# new_list[<action> for <item> in iterations if conditions]

a = [i for i in 'hello']
b = [i * 2 for i in [1,2,3]]
c = [i for i in range(0,10) if i%2 ==0 ]
