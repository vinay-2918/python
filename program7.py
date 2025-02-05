def even(number):
    return number % 2 ==0

number=[1,2,3,4,5,6,7,8,9,10]
is_even = list(filter(even,number))
print(is_even)