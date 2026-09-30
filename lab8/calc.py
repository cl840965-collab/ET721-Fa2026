def addtwonumbers(a=0, b=0):
    return a + b

def subtractingnumbers(a= 0, b=0):
    return a-b

def multiplynumbers(a=1, b=1):
    return a*b

def dividenumbers(a =0, b=0):
    try:
        return a/b
    except ZeroDivisionError:
        print("Error")
    except ValueError:
        print("error")
    except:
        print("erorr")