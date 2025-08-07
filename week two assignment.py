>>> my_list = [ ]
>>> my_list.append(10)
>>> my_list.append(20)
>>> my_list.append(30)
>>> my_list.append(40)
>>> print ("After step 2:", my_list)
After step 2: [10, 20, 30, 40]
>>> my_list.insert(1,15)
>>> print ("After step 3:", my_list)
After step 3: [10, 15, 20, 30, 40]
>>> my_list.extend([50,60,70])
>>> print ("After step 4:", my_list)
After step 4: [10, 15, 20, 30, 40, 50, 60, 70]
>>> my_list.pop()
70
>>> print ("Atfer step 5:", my_list)
Atfer step 5: [10, 15, 20, 30, 40, 50, 60]
>>> my_list.sort()
>>> print ("After step 6:", my_list)
After step 6: [10, 15, 20, 30, 40, 50, 60]
>>> index_of_30 = my_list.index(30)
>>> print ("Index of 30:", index_of_30)
Index of 30: 3
>>> print ("Final list:", my_list)
Final list: [10, 15, 20, 30, 40, 50, 60]
>>> print ("Index of 30:", my_list.index(30))
Index of 30: 3
>>>