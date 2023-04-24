import sys
print("Print the Size of the input String : ")
string = input()
print("The size of " + string + " is -> ", len(string))

# sys gets the bit size
print(sys.getsizeof(string))