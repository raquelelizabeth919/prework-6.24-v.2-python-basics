# Question 1
# Write a function to print "hello_USERNAME!" USERNAME is the input of the function. The first line of the code has been defined as below.

def hello_name(user_name):
        """Send hello message to user"""
        user = {'username' : user_name}
        print("Hello " + user_name.upper() + "!")
        return user

Ralph = hello_name('ralphlauren15')


# Question 2
# Write a python function, first_odds that prints the odd numbers from 1-100 and returns nothing

def first_odds(current_number):
        """Odds from 1-100"""
        current_number = 0
        while current_number < 100:
                current_number += 1
                if current_number % 2 == 0:
                        continue
                print(current_number)
                
number = first_odds(1)
     
  
# Question 3
# Please write a Python function, max_num_in_list to return the max number of a given list. The first line of the code has been defined as below.

def max_num_in_list(a_list):
        """Returns max number of list"""
        max = a_list[0]
        for num in a_list:
                if num > max:
                        max = num
        return max

numbers = [5, 7, 10, 1, 3, 24, 13, 70, 33]
print(max_num_in_list(numbers))


# Question 4
# Write a function to return if the given year is a leap year. A leap year is divisible by 4, but not divisible by 100, unless it is also divisible by 400. The return should be boolean Type (true/false).

def is_leap_year(a_year):
        if a_year % 4 == 0:
                if a_year % 100 == 0:
                        if a_year % 400 == 0:
                                return True
                        else:
                                return False
          
print(is_leap_year(2021))
print(is_leap_year(2020))
# I could not figure this one out


# Question 5
# Write a function to check to see if all numbers in list are consecutive numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5] are not consecutive numbers. The return should be boolean Type.

#     def is_consecutive(a_list):