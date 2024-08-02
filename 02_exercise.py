""" Se tiene un n ́umero natural n, crear una funci ́on que retorne
una lista de todos los pares de n ́umeros naturales que sumen
el número n. n < 10^6
"""

def pair_numbers_sum(number: int) -> list:
    
    if number > 1000000:
        return "number to large, type a number < 1000000"
    
    list_numbers = [num for num in range(1, number + 1)]

    # print(list_numbers)

    pair_numbers = []

    for i in list_numbers:
        # print(f"current number: {i}")
        for j in range(len(list_numbers)):
            x = i + list_numbers[j]
            # print(f"{i} + {list_numbers[j]} = {x}")
            if x == number:
                pair_numbers.append([i, list_numbers[j]])
                
    return pair_numbers

typed_number = int(input("type a number: "))

print(pair_numbers_sum(typed_number))
