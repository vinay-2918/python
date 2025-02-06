filename = input("Enter the filename:")
try:
    fd = open(filename , 'r')
    data = fd.read()
    fd.close()
except FileNotFoundError:
    print("the file does not exist")
else:
    count = {}
    for char in data:
        if char in count:
            count[char] +=1
        else:
            count[char] = 1
    print(count)