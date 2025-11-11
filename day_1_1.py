def main():
    # All Non-primitives are below
    
    # List
    list_example = [1,3,'harry',45,"UI",90,-4,"FU"]
    print("An example of a List is: {}".format(list_example))
    
    # tuple 
    tuple_example = (1,34,353,"Haroon", "Berlin","Money",11,-34)
    print("An example of a Tuple is: {}".format(tuple_example))
    
    # Dictionaries 
    dictionary_example = {"Name":"haroon", "City":"Berlin", "pin":191102}
    print("An example of Dictionaries is : {}".format(dictionary_example))
    
    # Sets
    set_example = set([1,34,4,7,57,686,45])
    print("An example of sets is :{}".format(set_example))
    
    # Frozenset
    frozensets_example = frozenset({1,4,64,55,575,234})
    print("An example of frozensets is : {}.".format(frozensets_example))
    
    
if __name__ == "__main__":
    main()