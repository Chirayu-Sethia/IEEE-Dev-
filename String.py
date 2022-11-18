Input1 = int(input("Enter total number of test cases:\n"))
for i in range(Input1):

    Input2 = int(input('Enter length of string S:\n'))
    Input3 = str(input('Enter the string S:\n'))
    a = Input3[:len(Input3) // 2]
    b = Input3[len(Input3) // 2:len(Input3)]
    if a == b:
        print('yes');
    else:
        print('no');