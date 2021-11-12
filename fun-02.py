

def check_multiple_of_3_5(num):
    if num % 5 == 0 and num % 3 == 0:
        return True 
    else:
        return False 

num = int(input("Enter number to test: "))
print(check_multiple_of_3_5(num))