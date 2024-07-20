# Project: Algorithmic Challenges

This repository contains solutions to three algorithmic problems. Each problem is solved using Python and the solutions are structured in separate Python scripts. Below are the descriptions of each problem and how to run the code.

## Problem 1: Well, where can I put my well?

### Description
Your mandate is to find the best location for a water well on a plot of land. You have geographical data indicating the presence of aquifers (water reserves) under the ground. This data divides the land into a grid, with each cell having a value of 1 if an aquifer lies beneath the ground and 0 if there is no trace of an aquifer in that cell. We want to locate the well where the water reserve will be the greatest, so we try to identify the largest aquifer. In this problem, we assume that an aquifer is a set of cells that are connected vertically (top and bottom) and horizontally (left and right) on the grid. Diagonal boxes are not connected. You are asked to return only the size of the largest aquifer. If there is no trace of water, then 0 is returned.

### Usage
To run the solution for this problem, use the following command:
```sh
python3 well_location.py <input_file>
```

![image](https://github.com/h-mbl/IFT2125_TP4/assets/125308992/a0819d3e-da53-46ab-8b8f-8b8cb56ac8da)



## Problem 2: Unruly schoolchildren

### Description
elementary school consults you about a problem with unruly schoolchildren. Teachers have noted that certain pairs of pupils are dangerous: when you put two children from a dangerous pair in the same group for an activity, you can almost certainly expect behavioral problems to arise at some point. With a list of schoolchildren and a list of dangerous pairs, determine whether the children can be separated into two groups such that each dangerous pair is separated between the two groups. If possible, return a combination of children in two groups that works, otherwise return "impossible".

```sh
<number of kids>
<name 1>
<name 2>
...
<name n>
<number of dangerous pairs>
<name A> <name B>
<name C> <name D>
```

### Usage
To run the solution for this problem, use the following command:

```sh
python3 schoolchildren.py <input_file>
```

## Problem 3: Prime numbers special sets

### Description
Let p and q be two prime numbers. This pair of numbers is said to be special when the concatenation of the two numbers in any order also gives a prime number. For example, 3 and 7 form a special pair because 37 and 73 are prime. On the other hand, 2 and 3 do not form a special pair because 23 is prime but 32 is not. Note that 307 cannot be considered a concatenation of 3 and 7 because of the extra 0. A set of primes is special when all pairs of numbers in the set form special pairs. In graph theory, this is called a clique. To characterize such a set, we can look at the sum of all its elements. For example, the special set of (67, 3, 37) has a sum of 107. This characterization is not necessarily unique. Find the set of 4 primes that is special and whose sum is the nth among all the special sets of 4 primes. 1 ≤ n ≤ 100. You must return this sum of the nth smallest special set in the file given as an argument. Your code must find and calculate these values and not keep the pre-calculated answers in the code.

Example
The first 3 special sets of 4 prime numbers in order of increasing total sum are:

(3, 7, 109, 673) with a sum of 792
(23, 311, 677, 827) with a sum of 1838
(3, 37, 67, 2377) with a sum of 2484

### Usage
To run the solution for this problem, use the following command:

```sh
python3 prime_special_groups.py <n> <output_file>
```
To run the test script, use the following command:

```sh
python3 test_prime_special_groups.py
```
![image](https://github.com/h-mbl/IFT2125_TP4/assets/125308992/ea892c6c-ee2d-440c-a00d-1d2f5106d246)

## Files
well_location.py: Solution for the water well location problem.
schoolchildren.py: Solution for the unruly schoolchildren problem.
prime_special_groups.py: Solution for the prime numbers special sets problem.
test_prime_special_groups.py: Test script for the prime numbers special sets problem.

## Installation
Ensure you have Python 3 installed. Clone the repository and navigate to the project directory:

