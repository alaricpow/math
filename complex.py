#MIT License

#Copyright (c) 2022 alaricpow

#Permission is hereby granted, free of charge, to any person obtaining a copy
#of this software and associated documentation files (the "Software"), to deal
#in the Software without restriction, including without limitation the rights
#to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#copies of the Software, and to permit persons to whom the Software is
#furnished to do so, subject to the following conditions:

#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.

#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.

#This program computes the argument and modulus of any complex number in the form a + bi, for real numbers a and b.
import math
def main():
    print("This simple program helps you evaluate the argument and modulus of any complex number a + bi, where a and b are real numbers. Note that the argument is restricted to (-pi, pi].")
    while True:
        try:
            a = float(input("a = "))
            if a == 0 or a > 0 or a < 0:
                break
        except:
            print("a has to be a real number.")
    while True:
        try:
            b = float(input("b = "))
            if b == 0 or b > 0 or b < 0:
                break
        except:
            print("b has to be a real number.")
    print(f"{a} + ({b})i")
    if a == 0 and b == 0:
        print("Modulus = 0")
        print("Argument is undefined")
    elif a > 0 and b > 0:
        mod1 = math.sqrt(a*a + b*b)
        arg1 = math.atan(b/a)
        print(f"Modulus = {mod1}")
        print(f"Argument = {arg1}")
    elif a > 0 and b < 0:
        mod2 = math.sqrt(a*a + b*b)
        arg2 = math.atan(b/a)
        print(f"Modulus = {mod2}")
        print(f"Argument = {arg2}")
    elif a < 0 and b < 0:
        mod2 = math.sqrt(a*a + b*b)
        arg2 = math.atan(b/a) - math.pi
        print(f"Modulus = {mod2}")
        print(f"Argument = {arg2}")
    elif a < 0 and b > 0:
        mod3 = math.sqrt(a*a + b*b)
        arg3 = math.pi + math.atan(b/a)
        print(f"Modulus = {mod3}")
        print(f"Argument = {arg3}")
   
   
main()
