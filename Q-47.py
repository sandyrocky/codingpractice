'''Write a Python program to find out the number of CPUs using.'''

import os

a = os.cpu_count()
print('Number of CPUs we are using : ',a)

"""output -
Number of CPUs we are using :  4
"""