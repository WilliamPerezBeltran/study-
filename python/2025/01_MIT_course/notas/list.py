l = [2,1,3]
print(l)
l.append(5)
print(l)
l.append([12,23])
print(l)
print("~~~~~~~ objecto.extend()~~~~~~~~")
a = [1,2,3]
b = [10,20,30]
c = a + b 
print(c)
c = a.extend(b)
print(c)

"""
MUTATION, ALIASING, CLONING
IMPORTANT
and
TRICKY!
Again, Python Tutor is your best friend
to help sort this out!
http://www.pythontutor.com/

"""

import matplotlib.pyplot as plt
import numpy as np



fig, ax = plt.subplots()             # Create a figure containing a single Axes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Plot some data on the Axes.
plt.show()  
