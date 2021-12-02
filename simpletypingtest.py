"""
An example docstring that says what this
"""

from time import time

# This line is a long comment to illustrate how pylint
# might complain because it is more than 100 characters
totype='Hello world'
input(f'Type the following\n{totype}\nPress return when ready\n')
stime = time()
ii = input('')
etime = time()
if totype == ii:
    error = False
    text = 'You were successful'
else:
    error = True
    text = 'You were not successful'

elapsedtime = round(etime - stime, 2)

print(f'{text} and you needed {elapsedtime} seconds')