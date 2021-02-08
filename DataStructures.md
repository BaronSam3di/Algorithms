# Data Structures 

## Memory
- Bit 
- Byte 
- Fixed Width Integer - eg 32 Bit , or 64 bit
- Endienness - https://en.wikipedia.org/wiki/Endianness


## Logarithm

$log_b (x) = y$ iif $b^y = x$

So the log 16 of base 2 is the same as saying 2 the powere of something equals 16, which will be $2^4$.


Its important to specify the base ($b$)
In Computer Science and Codeing Interviews , e always assume the base ($b$) is two.

BEWARE! In maths, ther is a convention to talk about ($b$) as base 10. 

## Strings

A string is a an array of integers mapped to a character encoding standard such as ASCII.


# Algorithms

**Recursive functions** are functions that call themselves. There are two main parts to recursive functions: [from here](https://www.cs.uregina.ca/Links/class-info/210/Recursion/)


- **general** (recursive) case --the case for which the solution is expressed in terms of a smaller version of itself. In other words, here, the problem space is made smaller and smaller. (the smaller problem space is sent to the calling function)
- **base case** --the case for which the solution can be stated nonrecursively. Here, a solid solution is found. 

# Big O Notation
This is the notation used to describe the `time` complexity and `space` complexity of algorithms; always in the **worst case scenario**.

Below are common complxities and their Big O notation, ordered from fastest to slowest.

- Constant      O(1)      
- Logarithmic   O(log(n)) 
- Linear        O(n)      
- Log-Linear    O(n log(n)) 
- Quadratic     O(n^2)    
- Cubic         O(n^3)    
- Exponential   O(2^n)    
- Factoral      O(n!)     

If you have multiple functions within a function, the complexity will be measured by the slowest function.