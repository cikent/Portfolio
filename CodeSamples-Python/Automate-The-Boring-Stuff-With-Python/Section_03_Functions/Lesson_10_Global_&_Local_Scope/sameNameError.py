def spam():
    print(eggs)  # Error!
    eggs = 'spam local'  # this is a local

eggs = 'global'  # this is a global
spam()