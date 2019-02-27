#Program to flatten arbitrarily nested array of integers into a single list
#incidentally, this program will also work for arrays of characters and floats

#empty list 
flat_list = []

#flatten function accepts array as argument
def flatten(nest_list):

    #looping through array argument
    for i in nest_list:

        #element added to new list if it is a single entry
        if type(i) not in (list, tuple):

            flat_list.append(i)

        #recursive call on element if it is a list/tuple
        else: 

        	flatten(i)

    #return new flattened list
    return flat_list        

#test1
arr1 = []
print (flatten(arr1))

#test2
arr2 = [[],[],[[],[],[]],[],[[[]]]]
print (flatten(arr2))

#test3
arr3 = [1, 2, 3, 4, 5]
print (flatten(arr3))

#test4
arr4 = [1, 2, [3, 4, 5, 6, 6], [11, 12], 10]
print (flatten(arr4))

#test5
arr5 = [1, 2, [3, 4, [], [[], 9, []], 10]]
print (flatten(arr5))

#test6
arr6 = [1, 2.5, [3.8999, '4', [], 5, 6, 6, ['4', 3, 2.4567, []]],
      
       [], [5, '6sdfw3', 7, 8, [9,'sgdh10srh', [11, 1.2], []]], 10

       ]
print (flatten(arr6))
