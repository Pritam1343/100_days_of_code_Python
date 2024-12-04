def calc_sum(a, b):
    return a + b


def calc_sub(a, b):
    return a - b


def cal_mul(a, b):
    return a * b


def cal_div(a, b):
    return a / b

continue_calculations = True
operations={

}

def Calculator():

first_number=int(input("What is the first number ?"))
isfirst=True
prev_result=0
result=0

while continue_calculations:
    print("+ \n- \n/ \n*")
    sign=input("Pick the operation:")
    if isfirst:
        prev_result=first_number
        isfirst=False
    else:
        prev_result=result
    next_num=int(input("What is the next number? :"))

    if sign == "+":
        result= calc_sum(prev_result,next_num)
    elif sign== "-":
        result= calc_sub(prev_result,next_num)
    elif sign== "*":
        result= cal_mul(prev_result,next_num)
    elif sign== "/":
        result= cal_div(prev_result,next_num)

    print(f"{prev_result} {sign} {next_num} = {result}")

    yes_or_no=input(f"Type 'y' to continue to calculating with {result} , or Type 'n' to start new calculation")
    if yes_or_no=="y":
        continue
    elif yes_or_no=='n':
        isfirst=True
        first_number = int(input("What is the first number ?"))
    else:
        print("You have entered wrong input")

