'''Write a Python program to get OS name, platform and release information.'''

import os
import platform as pl


print(os.name)
print(pl.platform())
print(pl.release())


'''output -
nt
Windows-10-10.0.18362-SP0
10
'''