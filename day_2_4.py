def sum_of_number(*args):
    total_Sum =  sum(args)
    return total_Sum
def print_dictionary(**kwargs):
    for key , value in kwargs.items():
        print("The Dictionary is {} , {}".format(key, value))

def main():
    result_1 = sum_of_number(23,45,5,23,-6,76,34,546)
    print("The First Result is {}".format(result_1))
    
    result_2 = sum_of_number(1,2,3,4,5,6,7,8,9,10)
    print("The second Result is {}".format(result_2))
    
    print_dictionary(value1 = 101 , value2 = "Python" , value3 = "Passcode")    
if __name__ == "__main__":
     main()