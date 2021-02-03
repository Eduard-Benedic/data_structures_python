# Sequences
List, tuples and strings are represented similar in python.

In order to store one of this data structures Python needs to allocate the same memory for each item in an array. Thus, each element can be accesed via:

arr = [1,2,3]
arr[0]
start + cellsize * index = the memory location when you access an el via the index


# Referential Arrays
Referential arrays are arrays holding memory location addresses.
Instead of making every item in an array the same size an array will hold a memory location instead.
The number of bits to store each element is fixed (e.g 64 bits / address)

Dynamic array - an array that can expand apparently