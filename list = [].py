# list = []
list = [1,2,3,4,5,6,7,8,9,10]
def new(list):
    new_list = []
    for numbers in list:
        
        if numbers % 3 == 0:
            new_list.append("Fizz")
        elif numbers % 5 == 0:
            new_list.append("Buzz")
        elif numbers % 3 == 0 and numbers % 5 == 0:
            new_list.append("FizzBuzz")
        elif numbers %3 != 0 or numbers %5 != 0:
            new_list.append(numbers)
    return(new_list)
print(new(list))


'''provide a list of whole numbers: 
if the numbers in the list is a number that divisable by 3 add Fizz to result 
if the number that divisable by 5 then add Buzz to result  
if the number can be bothe divided by 3 and 5add Fizzbuzz to the result
if the number isn't divisable by 3 and 5 then it return the same
return and print out result  '''
