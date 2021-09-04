# bounce.py
#
# Exercise 1.5

height_in = 100
n=1

while n<11:
    height_in=(3/5)*height_in
    n=n+1
    print('No. of bounces', n,'height',round(height_in,ndigits=4))
