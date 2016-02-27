======================
Conjecture de Syracuse
======================

Autor: Jonathan Labéjof

This project aims to demonstrate the conjecture of syracuse thanks to proportionality in a recurrent and close space.

-------
Problem
-------

Problem of syracuse:

Let the serie Un where Un is in |N* and

If Un is even, Un+1 = Un / 2
Otherwise, Un+1 = 3 * Un + 1

The conjecture says whatever Un in |N*, it exists Um = 1.

-------------
Demonstration
-------------

Serie Pn: Problem simplification
================================

In order to proove this, I choose to transform the serie Un into a closed and cyclic space of proportions.

Let consider *n* in |N and n % 2 = 0, the closed space of integers *[2^n; 2^n+1[* where Un is contained inside.

In this space, let consider the function *p* which calculates the proportional position of Un. For example, if Un = 10, Un is in [8; 16[. The proportional position equals 10 / 8 = 1.25

Now, beceause Un = 10, Un is even, let's divide it by 2. Un + 1 = 5. 5 is in [4; 8[ <=> f(5) = 5 / 4 = 1.25

Now, the problem of syracuse consists to analyse the behavior of positions in spaces of [2^n; 2^n+1[

Let Pn this new serie which focus on this proportional position on spaces of values of [2^n; 2^n+1[ of the conjecture.

If we proove we have a constant behavior for the serie Pn in the space [2^n; 2^n+1[, therefore, by reccursivity, it will be true in spaces [2^m; 2^m+1[ for m > n.

Recursivity
===========

First, the conjecture is true if there is a Un = 2^m (<=> Pn = 1), m in |N*.

Trivially, in Pn, it equals Pn = 1

In such condition, we admit Un-1 =

- 2^(m+1) if U(n-1) is even
- (2^m - 1) / 3 if U(n-1) is odd

Pn consider only odd values of Un.

Therefore, we simplify the step in questionning about values equal (2^m - 1) / 3. This value depends directly on the value of m in Pn. For example, 5 = (16 - 1) / 3, and 21 = (64 - 1) / 3 while 5/4 != 21/4.

Proportionnaly, we have a first rule which is 21 = ((5 * 2 + 1) * 2) + 1 thanks to spaces which are double of old one and where each step consists to move by 3 more old value and add 1.

That implies another rule which tells if there is at least one odd value of Un, then if the conjecture is true, pn = (pn-1) * 2 + 1 where p0 = 2.

The idea is to show by recursivity than all values of a space [2^n; 2^n+1[ finishes in the space [2^(n-1); 2^n[

Let's analyse the spaces of odd values in [4; 16[ and [16; 64[ and odd values of Un.

- 5, 1
- 7, 11
- 9, 7
- 11, 17, 13
- 13, 5
- 15, 23, 35, 53, 5

And what about [16; 64[

- 17, 13
- 19, 29
- 21, 1
- 23, 35
- 25, 19
- 27, 41
- 29, 11
- 31, 47
- 33, 25
- 35, 53
- 37, 7
- 39, 59
- 41, 31
- 43, 65
- 45, 17
- 47, 71
- 49, 37
- 51, 77
- 53, 5
- 55, 83
- 57, 43
- 59, 89
- 61, 23
- 63, 95

Repetitive values
-----------------

In observing those values, we can see an interesting property about proportionality between two spaces.

The maximal value is always the last one (23 for 15, and 95 for 63). Then, maximal values decreases two by two (63, 59, 55, 51, 47, 43, 39, 35, 31, 27, 23, 19). And this is the same for the previous space (15, 11, 7) with always a difference of 6.

This sequence always ends on 5 (proove it).

So, recursively, this behavior will be the same whatever spaces and check a part of the conjecture.

Sub-sequence
------------

Now we saw a recursive behaviour with half values, let's see other ones.

Let's focus on 5, 9 and 13 in [4; 16[

In this set, we see:

- 5 becoming 1,
- 9 becoming 7,
- 13 becoming 5.

Differences between all is 4, like the inferior bound.

Corresponding values in the next set are:

- 21 becoming 1.
- 37 becoming 7.
- 53 becoming 5.

Difference between all is 16, like the inferior bound. That's right, proportions are keept, and solutions are parts of the previous set. And initial values are 4 * old + 1 (21 = 5 * 4 + 1).

Now, let's analyse values of 17, between 21 and 37 and between 37 and 53, without simple solutions.

- 17 becomes 13.
- *21 becomes 1.*
- 25 becomes 19.
- 29 becomes 11.
- 33 becomes 25.
- *37 becomes 7.*
- 41 becomes 31.
- 45 becomes 17.
- 49 becomes 37.
- *53 becomes 5.*
- 57 becomes 43.
- 61 becomes 23.

The first thing we can see are values which successively increase and decrease, in opposition of the previous set (1, 7, 5).

Then, we see that:

- 13 + 6 = 19
- 19 + 6 = 25
- 25 + 6 = 31
- 31 + 6 = 37
- 37 + 6 = 43.

This constitute a new sequence.

What about:

1, 11, 7, 17, 5 and 23 ?

The same about 11, 17 and 23:

- 11 + 6 = 17
- 17 + 6 = 23

Therefore, four by four, we have the same logic which is a serie of addition of 6.

And 1, 7, 5 left. 7 is 1 + 6.

65, 49
67, 101
69, 13*
71, 107
73, 55
75, 113
77, 29*
79, 119
81, 61
83, 125
85, 1*
87, 131
89, 67
91, 137
93, 35*
95, 143
97, 73
99,
101, 19

This time, we recover a sequence of addition by 6 for

- two by two: 67, 71, 75, ...
- four by four: 65, 73, 81, 89, 97, ...

and a problem exists for 69, 77, 85 and 93 which are solutions of the old set.

For example:

- 25 * 4 + 1 = 101 like previously.
- 17 * 4 + 1 = 69
- 21 * 4 + 1 = 85

Whatever sets of [2^n; 2^n+1[, we find the same sequences and the same logic of application of the 3*n + 1.

...

All values have solution in analyzed spaces, and the behavior is totally proportional in spaces where values are 2^n bigger (n is the difference level of spaces). Then proportionally, all spaces have solutions, although the pivot which grows quietly of pn = (pn-1 * 2 + 1) * 2 + 1 in a space of 2^n, 2^n+2.

Thanks to the serie Pn, the conjecture is true.

----------
Conclusion
----------

I learned this problem is incredibly hard and we don't have tools to solve it. What I want to say is, if you don't understand the problem, simplify it. That's all !
