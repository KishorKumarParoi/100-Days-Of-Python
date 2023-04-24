import sys
print("Print the Size of the input String : ")
string = input()
print("The size of " + string + " is -> ", len(string))

print(sys.getsizeof(string))