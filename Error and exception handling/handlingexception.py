try:
    print(1/0)
except ZeroDivisionError:
    print(("Zero Division"))
else:
    print("Not going to get here")
finally:
    print("finishing up")


