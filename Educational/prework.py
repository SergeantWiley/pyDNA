#Question 1
def hello_name(user_name):
    print(user_name)
hello_name("Corporal Rat")
#Question 2
def first_odds():
    for i in range(1,101,2):
        print(i)
first_odds()
# Question 3
def max_num_in_list(a_list):
    print(max(a_list))
max_num_in_list([1,2,3,5,8,13,21,34,55,89])
# Question 4
def is_leap_year(a_year):
    if a_year % 4 == 0:
        if  a_year % 100 != 0 or a_year % 400 == 0:
            print("Is leap year")
        else:
            print("is not leap year")
    else:
        print("is not leap year")
is_leap_year(2023)  
#Question 5
def is_consecutive(a_list):
    real_sum = sum(a_list)
    calculated_sum = len(a_list) * (a_list[0]+a_list[-1]) / 2
    if real_sum == calculated_sum:
        return True
    else:
        return False
print(is_consecutive([1,2,3,4,5]))
print(is_consecutive([1,3,4,31,6,8,8,9]))