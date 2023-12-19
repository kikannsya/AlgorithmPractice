from typing import List

#O(n^2)
def bubble_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)
## bubble sort
#searching next to number
# [1, 20, 10, 5]
# [1, 20, 10, 5]
# [1, 10, 20, 5]
# [1, 10, 5, 20]    
# [1, 5, 10, 20]
#  for i in range(10):
#      for j in range(10- 1 - i):   
    #      print(j,end=' ')
    #   print()
#
# 0 1 2 3 4 5 6 7 8 
# 0 1 2 3 4 5 6 7 
# 0 1 2 3 4 5 6
# 0 1 2 3 4 5
# 0 1 2 3 4
# 0 1 2 3
# 0 1 2
# 0 1
# 0

    for i in range(len_numbers):
        for j in range(len_numbers - 1 - i):
            #First you check the number of numbers[i]
            #Counts up to   
            if(numbers[j] > numbers[j + 1]):
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
                #修正前：　上のようにすると良い
                # buff = numbers[j]
                # numbers[j] = numbers[j+1]
                # numbers[j+1] = buff
    return numbers

if __name__ == '__main__':
    import random
    nums = [random.randint(0,1000) for i in range(19)]
    print(bubble_sort(nums))