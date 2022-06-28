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

#This program helps to solve quadratic equations.
import math
def main():
    print("This tool will help you tackle quadratic equations. We'll be using the general form ax^2 + bx + c = 0. Input the coefficients to get started!")
    while True:
        try:
            a = float(input("a = "))
            if a == 0:
                print("a must be a non-zero real number!")
            if a != 0:
                break
        except:
            print("a must be a non-zero real number!")
    while True:
        try:
            b = float(input("b = "))
            if b > 0 or b < 0 or b == 0:
                break
        except:
            print("b must be a real number!")
    while True:
        try:
            c = float(input("c = "))
            if c > 0 or c < 0 or c == 0:
                break
        except:
            print("c must be a real number!")
    print(f"{a}x^2 + ({b})x + ({c}) = 0")
    if (b*b - 4*a*c) < 0:
        print("No real roots.")
        temp1 = (1/(2*a))*(-b)
        temp = (1/(2*a))*(math.sqrt(4*a*c - b*b))
        if temp1 != 0 and temp != 0:
            print(f"x = {temp1} + {temp}i, x = {temp1} - {temp}i")
        elif temp1 == 0 and temp != 0:
            print(f"x = {temp}i, x = - {temp}i")
    if (b*b - 4*a*c) > 0:
        print("2 distinct real roots.")
        temp2 = (1/(2*a))*(-b + math.sqrt(b*b - 4*a*c))
        temp3 = (1/(2*a))*(-b - math.sqrt(b*b - 4*a*c))
        print(f"x = {temp2}, x = {temp3}")
    if (b*b - 4*a*c) == 0:
        print("1 distinct real root.")
        temp4 = (1/(2*a))*(-b + math.sqrt(b*b - 4*a*c))
        print(f"x = {temp4}")
   

main()

