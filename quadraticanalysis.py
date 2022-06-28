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

#This program does a thorough analysis on quadratic curves.
import math
def main():
    print("This tool will help you analyse quadratic curves. We'll be using the general form f(x) = ax^2 + bx + c. Input the coefficients to get started!")
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
    print(f"f(x) = {a}x^2 + ({b})x + ({c})")
    if (b*b - 4*a*c) < 0:
        print("The graph of y = f(x) has no x-intercept and one y-intercept.")
        vert1 = -(b/(2*a))
        stat1 = a*(vert1)*(vert1) + b*(vert1) + c
        if a > 0:
            print(f"The graph of y = f(x) lies above the x-axis, and has a minimum point at ({vert1}, {stat1}).")
        if a < 0:
            print(f"The graph of y = f(x) lies below the x-axis, and has a maximum point at ({vert1}, {stat1}).")
        temp1 = (1/(2*a))*(-b)
        temp = (1/(2*a))*(math.sqrt(4*a*c - b*b))
        print(f"y-intercept: (0, {c})")
        if temp1 != 0 and temp != 0:
            print(f"Solution to f(x) = 0: x = {temp1} + ({temp})i, x = {temp1} - ({temp})i")
        elif temp1 == 0 and temp != 0:
            print(f"Solution to f(x) = 0: x = {temp}i, x = - ({temp})i")
        print(f"Completed square form is {a}(x - ({vert1}))^2 + ({stat1})")
    if (b*b - 4*a*c) > 0:
        print("The graph of y = f(x) has two x-intercepts and one y-intercept.")
        vert2 = -b/(2*a)
        stat2 = a*(-b/(2*a))*(-b/(2*a)) + b*(-b/(2*a)) + c
        if a > 0:
            print(f"The graph of y = f(x) has a minimum point at ({vert2}, {stat2}).")
        if a < 0:
            print(f"The graph of y = f(x) and has a maximum point at ({vert2}, {stat2}).")
        temp2 = (1/(2*a))*(-b + math.sqrt(b*b - 4*a*c))
        temp3 = (1/(2*a))*(-b - math.sqrt(b*b - 4*a*c))
        print(f"x-intercepts: ({temp2}, 0), ({temp3}, 0)")
        print(f"y-intercept: (0, {c})")
        print(f"Solution to f(x) = 0: x = {temp2}, x = {temp3}")
        print(f"Completed square form is {a}(x - ({vert2}))^2 + ({stat2})")
    if (b*b - 4*a*c) == 0:
        print("The graph of y = f(x) has one x-intercept and one y-intercept.")
        vert3 = -b/(2*a)
        stat3 = a*(-b/(2*a))*(-b/(2*a)) + b*(-b/(2*a)) + c
        if a > 0:
            print(f"The graph of y = f(x) has a minimum point at ({vert3}, {stat3}).")
        if a < 0:
            print(f"The graph of y = f(x) has a maximum point at ({vert3}, {stat3}).")
        temp4 = (1/(2*a))*(-b + math.sqrt(b*b - 4*a*c))
        print(f"x-intercept: ({temp4}, 0)")
        print(f"y-intercept: (0, {c})")
        print(f"Solution to f(x) = 0: x = {temp4}")
        print(f"Completed square form is {a}(x - ({vert3}))^2 + ({stat3})")
   
main()
