def main():
    print("String Manipulation")

    # Strings are immutable objects and almost all methods
    string_value =  "Python is becoming the worlds most popular programming language today"
    
    # get string length using  len() method
    print(len(string_value))

    # string concatenation using + sing or .join() method
    string_1 ="Hello"
    string_2 = "World"
    print(string_1 + " " + string_2)
    
    #W + Hello + o + Hello + r + Hello + l + Hello + d
    print(string_1.join(string_2))
    print(" ".join([string_1, string_2]))

    # how to get the substring or splices using [start,end + length]
    string_3 = string_value[0:6]
    string_4 = string_value[7:]
    string_5 = string_value[:-6]
    string_6 = string_value[43:54]
    print(string_3  +"\n" + string_4 + "\n" + string_5 + "\n" + string_6)
    
    # how to count any alphabet in string using .count()
    string_7 = string_value.count("a")
    print(string_7)
    
    # how to find the position of anything in string .find()
    string_8 = string_value.find("language")
    print(string_8)

    # How to remove the white/blank spaces  from the start and end
    string_9 = string_value.strip()
    print(string_9)
    
    # how to convert string in lower and upper case
    string_10 =  string_value.upper()
    string_11 = string_value.lower()
    print(string_10 + "\n" + string_11)
    
    # how to replace python word  with java
    string_12 = string_value.replace("Python" , "Java")
    print(string_12)
    
    # How  to split the string
    string_13 = string_value.split("most")
    print(string_13)
    
    string_14 = string_value.split(" ")
    print(string_14)
    
    string_15 = "popular"  in string_value
    string_16 = "POPULAR" not in string_value
    print(string_15)
    print(string_16)
    
    
if __name__ == "__main__":
    main()