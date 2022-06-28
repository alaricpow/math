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

#This program computes the sample mean, variance and standard deviation for a specified list of data.
import statistics
def main():
    list = []
    while True:
        try:
            n = int(input("How many values?  "))
            if n > 0:
                break
            if n <= 0:
                print("Key in a positive integer!")
        except:
            print("Key in a positive integer!")
   
    for i in range(n):
        while True:
            try:
                temp = float(input(f"Value {i+1}:  "))
                if temp >= 0 or temp < 0:
                    break
            except:
                print("Key in a number!")
        list.append(temp)
    s = statistics.stdev(list)
    u = sum(list)/n
   
    print(f"Sample standard deviation = {s}")
    print(f"Sample variance = {s*s}")
    print(f"Sample mean = {u}")


main()
