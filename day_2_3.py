def addition(number_1, number_2):
    """calculate the addition of two numbers

    Args:
        number_1 (_type_): first number
        number_2 (_type_): second number
        return : sum of first number and second
    """
    total = number_1 + number_2
    return total


def payment_day(working_days, hourly_pay=25):
    total_payment = working_days * hourly_pay
    print("The total payment is : {}".format(total_payment))

def payment_day_not(working_days, hourly_pay=None):
    if hourly_pay is not None:
        total_payment = working_days  * hourly_pay
    else:
        total_payment = 0
    return total_payment
 
def main():
    number_1 =  55
    number_2 = 55
    total_sum = addition(number_1,number_1)
    print("The Total sum of two number is :{}".format(total_sum))
    
    payment_day(5)
    payment_day(5 ,10)

    total_sum_payment = payment_day_not(number_2,90)
    print("Total payment is {}".format(total_sum_payment))


if __name__ == "__main__":
    main()