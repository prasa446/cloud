"""
Transfer statements in Python are used to alter the flow of execution in a program. 
They are particularly useful in loops and conditional statements
"""
# The three types of transfer statements are:
# 1. break
# 2. continue
# 3. pass statements


# 1. break statement-- the loop stops and exits
'''
for i in range(10):
    if i == 5:
        break
    print(i)
'''


#2. continue satement-- skips the execution if particular condition obeys
'''
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
'''

# 3. pass statement -- does nothing.useful in situations where a statement is syntactically required but you do not want to execute any code.
'''
for i in range(10):
    if i % 2 == 0:
        pass
    else:
        print(i)
'''



