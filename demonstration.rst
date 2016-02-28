==========================================
Démonstration de la conjecture de syracuse
==========================================

--------
Problème
--------

Conjecture de syracuse

Série Un tel que:

Un+1 = Un/2 si Un est pair
Un+1 = 3Un + 1 si Un est impair

Alors pour tout Un dans N*, il existe m > n tel que Um = 1.

-------------
Démonstration
-------------

Démonstration par récurrence du comportement de la série dans des sous-ensembles d'entiers fermés [2^m; 2^m+1[ où m = log2(Un).

Soit R l'ensemble des sous-ensembles d'entiers {[2^m, 2^m+1[|m dans N}.

Observons le comportement de la série sur les ensembles R0=[1; 2[, R1=[2; 4[, R2=[4; 8[, R3=[8; 16[, R4=[16; 32[ et R5=[32; 64[.

.. note::

	je ne prendrai que les nombres impairs car les nombres pairs d'un ensembleRx auront été calculés en fonction du sous-ensemble R(x-1).

Le tableau suivant comprend tous les entiers de 1 à 63, qui sont assimilés à des valeurs de Un. Ces valeurs de la suite sont suivis de la prochaine itération impair *Um*, avec un indicatif de série *remarquable* que j'expliquerai par la suite. Finalement, la durée du vol par valeur impairt est également donnée.

.. csv-table:: R0 et R1
	:header: Un, Um, Serie, vol

	1, 1, 2, 1
	3, 5, 1, 3

.. csv-table:: R2 et R3
	:header: Un, Um, Serie, vol

	5, 1, 3, 2
	7, 11, 1, 6
	9, 7, 2, 7
	11, 17, 1, 5
	13, 5, 3, 3
	15, 23, 1, 6
	17, 13, 2, 4
	19, 29, 1, 7
	21, 1, 3, 3
	23, 35, 1, 5
	25, 19, 2, 8
	27, 41, 1, 42
	29, 11, 3, 5
	31, 47, 1, 39

.. csv-table:: R4 et R5
	:header: Un, Um, Serie, vol

	33, 25, 2, 9
	35, 53, 1, 4
	37, 7, 3, 7
	39, 59, 1, 12
	41, 31, 2, 41
	43, 65, 1, 10
	45, 17, 3, 5
	47, 71, 1, 39
	49, 37, 2, 8
	51, 77, 1, 8
	53, 5, 3, 3
	55, 83, 1, 42
	57, 43, 2, 11
	59, 89, 1, 11
	61, 23, 3, 6
	63, 95, 1, 40

Découpage de R en sous-séries remarquables
==========================================

Afin de mieux isoler des comportements réccursifs de la suite U, je vais transformer l'ensemble des entiers naturels en trois séries bien distinctes (sans collision).

Serie 1 : S1
------------

Premièrement, intéressons-nous à la série 1.

Cette série a plusieurs propriétés remarquables :

Un
~~

Ses valeurs correspondent à la fonction linéaire y = 3 + 4x, n dans N.

Par exemple :

- Un = 3 = 4 + 4 * 0
- Un = 7 = 3 + 4 * 1
- Un = 11 = 3 + 4 * 2
- etc.

Um
~~

Et la suite Um est la fonction linéaire y = 5 + 6n, n dans N.

Par exemple, pour :

- Um = 5 = 5 + 6 * 0
- Um = 11 = 5 + 6 * 1
- Um = 17 = 5 + 6 * 2
- etc.

Et Um = Un * 2 - 2 * n - 1, donc toujours inférieur au double de sa valeur.

Transitions
~~~~~~~~~~~

Le passage de S1 vers une autre série ou elle-même dépend de n modulo 4 et de la séquence T1 = {S3, S1, S2, S1}.

Par exemple :

.. csv-table::
	:header: Un, Um, Serie de Um

	3, 5, 3 (n=0 => T1[0])
	7, 11, 1 (n=1 => T1[1])
	11, 17, 2 (n=2 => T2[2])
	15, 23, 1 (n=3 => T3[3])
	19, 29, 3 (n=4 => T3[0])

.. note::

	Si n est pair, alors Um quitte S1.
	Si n est impair alors Um reste dans S1.

Serie 2 : S2
------------

La seconde série est très proche de la première.

Un
~~

Les valeurs de Un sont déterminées par la fonction linéaire y = 1 + 8n, n dans N.

Par exemple :

- Un = 1 = 1 + 8 * 0
- Un = 9 = 1 + 8 * 1
- Un = 17 = 1 + 8 * 2
- etc.

Um
~~

Et les valeurs de Um correspondent à la fonction linéaire y = 1 + 6n, n toujours dans N.

Par exemple :

- Um = 1 = 1 + 6 * 0
- Um = 7 = 1 + 6 * 1
- Um = 13 = 1 + 6 * 2
- etc.

Transitions
~~~~~~~~~~~

Le passage de S2 vers une autre série ou elle-même dépend de n modulo 4 et de la séquence T2 = {S2, S1, S3, S1}.

Par exemple :

.. csv-table::
	:header: Un, Um, Serie de Um

	1, 1, 2 (n=0 => T2[0])
	9, 7, 1 (n=1 => T2[1])
	17, 13, 3 (n=2 => T2[2])
	25, 19, 1 (n=3 => T2[3])
	33, 25, 2 (n=4 => T2[0])

Et Um = Un * 2  - 2 * n, donc toujours inférieur au double de sa valeur.

.. note::

	Si n est impair, Um est dans S1
	Si n congru à 0 modulo 4, Um est dans S2
	Si n congru à 2 module 4, Um est dans S3

Serie 3 : S3
------------

Cette dernière série est plus particulière.

Un
~~

Les valeurs de Un sont déterminées par la fonction linéaire y = 5 + 8n, n dans N.

Par exemple :

- Un = 5 = 5 + 8 * 0
- Un = 13 = 5 + 8 * 1
- Un = 21 = 5 + 8 * 2
- etc.

Um
~~

Les valeurs de Um correspondent à la suite successive des valeurs de Um observées dans le sous-ensemble précédent celui de Um.

Par exemple :

Sur R4 et R5

- Un = {21, 29, 37, 45, 53}, Um = {1, 11, 7, 17, 5}

Sur R2 et R3

-



Et les valeurs de Um correspondent à la fonction linéaire y = 1 + 6n, n toujours dans N.

Par exemple :

- Um = 1 = 1 + 6 * 0
- Um = 7 = 1 + 6 * 1
- Um = 13 = 1 + 6 * 2
- etc.

Transitions
~~~~~~~~~~~

Le passage de S2 vers une autre série ou elle-même dépend de n modulo 4 et de la séquence T2 = {S2, S1, S3, S1}.

Par exemple :

.. csv-table::
	:header: Un, Um, Serie de Um

	1, 1, 2 (n=0 => T2[0])
	9, 7, 1 (n=1 => T2[1])
	17, 13, 3 (n=2 => T2[2])
	25, 19, 1 (n=3 => T2[3])
	33, 25, 2 (n=4 => T2[0])

Et Um = Un * 2  - 2 * n, donc toujours inférieur au double de sa valeur.

.. note::

	Si n est impair, Um est dans S1
	Si n congru à 0 modulo 4, Um est dans S2
	Si n congru à 2 module 4, Um est dans S3



Transitions entre séries
------------------------