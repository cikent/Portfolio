def spam(divideBy):
    return 42 / divideBy

print(spam(2))
print(spam(12))
print(spam(0))  # This will cause a ZeroDivisionError
print(spam(1))
