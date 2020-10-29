#
# Recursive code to store in github
#
# Prompt for small positive integer then calculate factorial
#
def calc_fact(integer_in):
    
    if integer_in == 1:
        return 1
    else:
        return(integer_in * calc_fact(integer_in - 1))
#
in_num = int(input("Please type in a positive integer between 1 and 15: "))
if in_num not in range(1,16):
    print(in_num,"is not a valid input")
else:
    print("The factorial of :",in_num, " is: ",calc_fact(in_num))