# #Create a function that returns the CSV representation of a two-dimensional numeric array.
# my_array = [[0,1,2,3,4],
#             [10,11,12,13,14],
#             [20,21,22,23,24],
#             [30,31,32,33,34]]
# result = ''
# for row in my_array:
#     for item in row:
#         result += str(item) + ','
#     result += '\n'
# print(result)

# 3.1. Count by X. Create a function with two arguments that will return
# an array of the first n multiples of x.

# def count_by(x, y):
  #var1
    # my_array = []
    # for item in range(x, x*y+1, x):
    #     my_array.append(item)
    # print(my_array)

#   #var2
#     result = list(range(x, x*y+1, x))
#     print(result)
#
# count_by(2, 9)

# Caesar encription
def rot_13(message):
    abc = 'abcdefghijklmnopqrstuvwxyzabcdefghijklm' \
          'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLM'
    r = ''
    for c in message:
        if c in abc:
            r += abc[abc.index(c)+13]
        else:
            r += c
    print(r)

rot_13('Hallo!')



