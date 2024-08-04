def increment(num):
    try:
        return int(num) + 1
    except:
        raise ValueError("Enter number please")
        
try:
    print(increment('a'))
except Exception as e:
    print(e)


# custom exception with class

class 
