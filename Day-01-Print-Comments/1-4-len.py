import sys
print("Print the Size of the input String : ")
string = input()
print("The size of " + string + " is -> ", len(string))

# sys gets the bytes size
print(sys.getsizeof(string))