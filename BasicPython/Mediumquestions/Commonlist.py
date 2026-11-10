'''* Common Elements Using Sets: Given two lists:
 
    ```python
    list1 = [1, 2, 3, 4, 5]
    list2 = [3, 4, 5, 6, 7]
    ```
 
    Find:
 
    * Common elements.
 
    * Elements present only in the first list.
 
    * All unique elements from both lists.'''

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
a=set(list1)
b=set(list2)
print("Common elements=",a&b)
print("Elements present only in the first list=",a-b)
print("All unique elements from both lists=",a.union(b))
