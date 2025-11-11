# Lambda Functions we always make them inside the standard functions

def main():
    function_double = lambda x : x *2
    x = 10
    print("The value of x is : {}".format(function_double(x)))
    print("The value of x is : {}".format(function_double(100)))
    


if __name__ == "__main__":
    main()