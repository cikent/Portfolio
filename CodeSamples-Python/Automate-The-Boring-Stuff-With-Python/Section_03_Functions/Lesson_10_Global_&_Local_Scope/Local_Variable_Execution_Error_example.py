"""
Upon execution, the function 'spam()' throws an exception because eggs is utilized as a Local variable before assignment
"""
def spam():
    print(eggs) # ERROR!    -- can't use a local variable before it is assigned a value
    eggs = 'spam local'

eggs = 'global'
spam()