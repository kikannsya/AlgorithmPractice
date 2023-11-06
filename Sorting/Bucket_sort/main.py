from typing import List
from insertion import insertion_sort

def bucket_sort(numbers: List[int]) -> List[int]:
    max_num = max(numbers)
    len_numbers = len(numbers)
    size = max_num // len_numbers

    buckets = [[] for _ in range(size)]

    for num in numbers:
        i = num // size

        if i != size:
            buckets[i].append(num)
        
        else:
            buckets[size-1].append(num)
        
    for i  in range(size):
        insertion_sort(buckets[i])

    result = []

    for i in range(size):
        result += buckets[i]

    return result

if __name__ == '__main__':
    import random
    nums = [random.randint(0,1000) for _ in range(10)]
    print(bucket_sort(nums))
