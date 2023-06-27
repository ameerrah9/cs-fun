def implement_always(var):
    return (lambda var: var)(var)
    

f1 = (lambda var: var)
f2 = implement_always("pear")
f3 = implement_always("banana")

# print(f1()) # "apple"
# print(f3()) # "banana"
# print(f2("something else")) # "pear"
print(implement_always("hello"))

# sum = lambda arg1, arg2: arg1 + arg2;
# # Now you can call sum as a function
# print "Value of total : ", sum( 10, 20 )
print(f1("banana"))