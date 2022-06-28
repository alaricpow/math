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

#This program allows you to compute basic probabilities related to binomial distributions with specified parameters.
import math
def main():
    while True:
        try:
            n = int(input("Number of trials:  "))
            if n > 0:
                break
            elif n <= 0:
                print("Key in a positive number!")
        except:
                print("Key in a positive number!")
    while True:
        try:
            p = float(input("Probability of success:  "))
            if p > 0 and p < 1:
                break
            else:
                print("Key in a number between 0 and 1 (non-inclusive)!")
        except:
                print("Key in a number between 0 and 1 (non-inclusive)!")
    print(f"X ~ B({n}, {p})")
   
    while True:
        try:
            s = input("If finding probability in the form P(X = k), type 0. If finding probability in the form P(X <= k), type 1. If finding probability in the form P(X >= k), type 2.  ")
            if s == '0' or s == '1' or s == '2':
                break
            else:
                print("Read the instructions carefully!")
        except:
            print("Read the instructions carefully!")
   
    while True:
        try:
            k = int(input("Value of k:  "))
            if k >= 0 and k <= n:
                break
            else:
                print(f"k is a non-negative integer which cannot be more than {n}!")
        except:
                print(f"k is a non-negative integer which cannot be more than {n}!")
   
    r = math.comb(n, k)
    if s == '0':
        p1 = r * (p ** (k))*((1 - p)**(n - k))
        print(f"P(X = {k}) = {p1}")
    if s == '1':
        p2 = 0
        for i in range(k + 1):
            p2 = p2 + math.comb(n, i) * (p ** (i))*((1 - p)**(n - i))
        print(f"P(X <= {k}) = {p2}")
    if s == '2':
        p3 = 0
        for i in range(k):
            p3 = p3 + math.comb(n, i) * (p ** (i))*((1 - p)**(n - i))
        print(f"P(X >= {k}) = {1 - p3}")
main()
