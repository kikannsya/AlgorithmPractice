from typing import List

def select_sort(numbers: List[int]) -> List[int]:
    len_numebers = len(numbers)
    for i in range(len_numebers):
        min_idx = i
        for j in range(i+1, len_numebers):
            if numbers[min_idx] > numbers[j]:
                min_idx = j
        
        numbers[i], numbers[min_idx] = numbers[min_idx], numbers[i]


    return numbers


if __name__ == '__main__':
    import random
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(select_sort(nums))
    
