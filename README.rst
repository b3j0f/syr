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

In observing those values, we can see an interesting property.

The maximal value is always the last one (23 for 15, and 95 for 63). Then, maxximal values decreases two by two (59, 55, 51, 47, 43, 39, 35, 31, 27, 23, 19). And this is the same for the previous space (15, 11, 7) with always a difference of 6.

So, recursively, this behavior will be the same whatever spaces and check a part of the conjecture.

All other values stay in this space wich is a solution for itself and lower spaces.

Therefore, recursively, all values of any space check the conjecture.

Thanks to the serie Pn, the conjecture is true.

----------
Conclusion
----------

I learned this problem is incredibly hard and we don't have tools to solve it. What I want to say is, if you don't understand the problem, simplify it. That's all !
