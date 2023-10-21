from typing import List

#O(n^2)
def bubble_sort(numbers: List[int]) -> List[int]:
    len_numbers = len(numbers)

    for i in range(len_numbers):
        for j in range(len_numbers - 1 - i):
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