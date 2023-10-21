

def bubble_sort(numbers):
    for i in range(len(numbers)-1):
        for j in range(len(numbers)-i):
            if(numbers[j] > numbers[j + 1]):
                buff = numbers[j]
                numbers[j] = numbers[j+1]
                numbers[j+1] = buff
            

if "__name__" == "__main__":
    print(bubble_sort([5, 2, 1, 3 , 4]))