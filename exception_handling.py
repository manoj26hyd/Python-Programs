# Exception Handling

try:
    print(A)

except:
    print("An error occured")

print("Program Excecuted......") 

# Many Exceptions

try:
    print(x)
except NameError:
    print("'x' is not defined please check")
except:
    print("Some thing went wrong")    

try:
    print("Hello World")
except:
    print("Something went wrong")
else:
    print("Nothing we wrong code excuted successfully")    


try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("try and except are executed")

x = -1
if x < 0:
    raise Exception("Sorry negative numbers not allowed")

x = "hello"

if type(x) != int:
    raise TypeError("Only integers are allowed")