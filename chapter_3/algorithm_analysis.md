# Data structure
data structure - a systematic way or organizing and accessing data.
algorithm - step by step procedure for performing some task in a finite amount of time.


The goal is to develop an approach to analyzng the efficiency of algorithms that:
1. Allow to evaluate the efficiency in a way that is independent of the hardware and software environment.
2. Is performed by studying a high level description of the algorith without need for implementation.
3. Takes into account all possible inputs



I. Counting Privimite Operations

In order to perform a relevant algorithm analysis excluding the environment variable such as clock speed, hardware etc we consider the following primitive operations:
1. assignin  an identifier to an object
2. determining the object associated with an identifier
3. performing an rithmetic opertions (addtion, subtraction, multiplicaion etc)
4. comparing 2 numbers
5. accesing a single element of apythin list by index
6. calling a function
7. returning form a function


II. Measuring operations as a functino of input size

In order to capture the growth of an algorithm's running time
f(n) - characterizes the number of primitive operations that are performed as a function of the input size n


III. Focusing on the Wrost-Case Input
Worst case analyisis.



The 7 Functionis (most important) ysed ub the analysis of algorithms.

1. The Constant Function
f(n) = c

2. The Logarithm Function 
f(n) = log<sub>b</sub> n
x = log<sub>b</sub>b if b<super>x</super> = n

b - base
Because computers work in binary
log n = log<sub>2</sub>n

Logarithmic Rules

1. log *b* (ac)  = log *b* a + log *b* c
2. log *b* (a / c) = log *b* a - log *b* c
3. log *b* (a) ^ c = c log *b* a
4. log *b* (a) = log *d* a / log *d* b

Equivalent representation of algorithms in base 2.

1. log(2n)  = log 2 + log n = 1 + log n    , by rule 1
2. log (n / 2) = log n - log 2 = log n - 1 , by rule 2
3. log n^3 = 3 log n                       , by rule 3
4. log 2^n = n log 2 = n                   , by rule 3
5. log *4* n = log n / log 4 = (log n) / 2 , by rule 4
6. 2^ log n = n ^ log 2 = n ^ 1 = n        , by rule 5#

3. The Linear Function
f(n) = n

4. The N-Log-N Function
f(n) = n log n

5. The Quadratic Function
f(n) = n ^ 2

6. The Cubic Function and Other Polynomials

6.1 Cubic function
f(n) = n ^ 3


6.2 Polynomials
Most of the functions described can actually be viewed as being part of a largee class of function **polynomials**.

Poly - many
nomial - term  => Polynomials - many terms


7. The Exponential Function
f(n) = b^n
b - base
n - exponent




# The "Big O " Notation

Suppose we have a function f(n) and g(n) that maps positive integers to real positive integers. We say that f(n) is the Big O of g(n) if 
f(n) <= c g(n) - if there is an n >= n0 and c > 0

# The Big Omega 
The opposite of Big O
 
# The big Teta