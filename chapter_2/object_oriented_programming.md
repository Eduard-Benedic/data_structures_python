# Goals, Principles and Patterns
instance variables aka **data members**
methods aka **member functions**

# Object Oriented Design Principles
One of the most important goals that OOP wishes to solve is:
1. Modularity
2. Abstraction
3. Encapsulation

## Modularity
Refers to an organizing principles in which different components of a software system are divided into separate functional units.


## Abstraction
This notion means to decompose a complicated system into its fundamental blocks. Describing a part of a system involes naming and explaining their functionality.
This gives rise to ADT (Abstract data Types)
The set of behaviors supported by an ADT as **public interface**
Python supports **Abstract Base Class** (ABC).


## Encapsulation
Different components of a software should **not** reveal the internal details of their implementations.
So for instance, just like a client who buys a certain product (shaker or sth) will only interact with the a interface provided by the manufacturer (buttons etc) so in the same way OO design enforces the clients of a component to only interact with that components through a  **public interface**. In this way the internal implementation is hidden from the client and improves robustness and adaptability of a component.


# Design Patterns
Design patterns offer a solution to a "typical" software design problem.
Provides a general template for a solution that can be applied in many different situations.

## Algorith Design patterns
1. Recuresion
2. Amortization
3. Divide-and-conquer
4. Prune-and-search, aka decrease-and-conquer
5. Brute force
6. Dynamic programming
7. The greey method

## Engineering design patterns
1. Iterator
2. Adapter
3. Position
4. Compositions
5. Template method
6. Locator
7. Factory method


Traditional software development involves 3 major phases
1. Design
2. Implementation (construction)
3. Testing and Debugging

## Design
One of the most principles phase as in this phase we decide what classes to build, what data will store and how to interact.
Few guidelines to follow when deciding over the design are:
1. Reponsiblities - divide the work into different **actors**(objects) each with a different respnsibility. Describe responsibilities using action verbs
2. Independence - each actor should be independent from other classes as possible.
3. Behaviors - Definec a clear interface as other classes will interact with my components through this actor.



Steps in designing good software

1. Define **CRC** (Class-Responsibility-Collaborator) cards. Using cards enforces me to keep my classes manageable and small.
2. Define **UML** (Unified Model Language)


The dependencies among the classes and functions of a program induce a **hierarchy**

Namely, a component A is above component B if A depends upon B.

## Testing strategies
1. Top-down used in conjuction with **stubbing**
2. Bottom-up - known as **unit testing**

Top-down is typically used in conjunctino with **stubbing**, a boot-strapping technique that replace a lower-level component with a **stub**
**stub** - replacement for the component that simulates the functionality of the original.

In the bottom-up approach the functionality of a specific component is tested in isolation of the larger software project.

**Regression testing** - when the code enters maintability all the previous tests are re run to ensure that the software works properly



# Iterators
An iterator is an object that supports the __iter__ and __next__ methods.

By convention the __iter__ method return the instance and the __next__ method will return the next element if there is one or will raise an **StopIteration** exception.

Another way of creating an iterator is by defining a __len__ and __getitem__ method on the class and Python will automatically will support iteration on that object.



# Inheritance

Let's say we have this hierarchy:  Building -> House -> Three story ouse
                                                     -> Ranch
Building is a **super set of house** and the three story house and ranch is a **subset of house** (mathematical terms)
In OOP tersm we call Building a **base class, parent class, super class** and the other classes that **inherit** from it as **derived class** or **sub class** or **child class**.
This organization is reffered as a **Is a relationship**.


A subclass can **specialize** an behaviors in two ways.
1. Overriding existing methods
2. Implementing new ones.


# Math

Progression

## Geometric Sequences
In a **Geometric Sequence** each term is found by multiplying the previous term by a constant.
In General such as sequence is written like:
{a, ar, ar^2, ar^3, ar^4...}
a - first term
r = common ration

In **Arithmetic Sequence** the difference between one term and the other is a constant.
{a, a + d, a + 2d, a + 3d, ...}
a - is the first term
d - the difference between the tersm (known as "common difference")


# Namespaces and Object-Orientation

Instant namespace
Class namespace - this namespace is used to manage members that are to be shared by all instances of a class


Python uses **dynamic dispatching** when resolving a name resolution which means that it figures out the attribute that has been accessed at runtime comapared to some other statically typed languages such as Java and C++ that use static dispatching.


## Shallow and Deep Copying

List - a container of references. Calling list(obj) will create a new container of references to the specific values. Adding or removing is possible without affecting the original obj, however when it comes to editing the references are pointing to the actual initial object !!


This is what is knows as **Shallow Copy**

To create a deep copy **copy** modules offers a solutin in Python.

A deep copy represents to the creation of an identical copy of that obj.