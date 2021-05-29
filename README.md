<!--
*** Bintang Fajarianto
*** 27 Januari 2021
-->
<p align="center">
    <img align=center src="https://visitor-badge.laobi.icu/badge?page_id=bintangfrnz.Cryptarithmetic-Solver-with-Brute-Force" alt="Visitors">                     
</p>

## Cryptarithmetic-Solver-with-Brute-Force

<p align="center">
· <a href="https://github.com/bintangfrnz/Cryptarithmetic-Solver-with-Brute-Force/issues">Report Bug</a> ·
</p>

> note: This project is a rebuilt version of "Tucil 1 IF2211 Strategi Algoritma"

<!-- Contents -->
<details open="open">
    <summary>Contents</summary>
    <ol>
        <li><a href="#description">Description</a></li>
        <li><a href="#specifications">Specifications</a></li>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#how-to-run">How to run</a></li>
        <li><a href="#contact">Contact</a></li>
    </ol>
</details>

## Description

<b>Cryptarithms</b> or <b>Cryptarithmetic</b> are encrypted math problems, where numbers in a given mathematical expression are represented by letters or other symbols.
In this case, each digit in the addition puzzle is replaced by a different letter.
The point of this game is we have to find the number that represents the letters.

In this puzzle, there are two important components that we should know.<br>
> e.g.<br>
> SEND + MORE = MONEY<br>

(SEND, MORE) are <b>operands</b>. MONEY is the <b>result</b>.
<hr>

Here are the examples and solutions of <b>Cryptarithmetic</b>:

#### (1)

<p align="center">
  <img src="https://github.com/bintangfrnz/Cryptarithmetic-Solver-with-Brute-Force/blob/main/img/contoh.PNG" alt="contoh">
</p>

The result are:
F=2, O=9, R=7, T=8, Y=6,
E=5, N=0, S=3, I=1, X=4

#### (2)

```
    J U N E           9 2 5 7           9 2 5 3
+   J U L Y       +   9 2 0 3       +   9 2 0 7
  - - - - -         - - - - -         - - - - -      etc.
  A P R I L         1 8 4 6 0         1 8 4 6 0
```

The result is,
<p align="center">
    <img src="https://github.com/bintangfrnz/Cryptarithmetic-Solver-with-Brute-Force/blob/main/img/hasil1.PNG" alt="hasil1">
    <img src="https://github.com/bintangfrnz/Cryptarithmetic-Solver-with-Brute-Force/blob/main/img/hasil2.PNG" alt="hasil2">
</p>

## Specifications

- In this program, only (+) operation can be solved. 
- At least there are 2 operands in the puzzle.
- The maximum number of letters in an operand is 10.
- Each letter represents a unique number.
- The first letter should not represent a zero (0).
- This program should be able to display all available solutions.


## Prerequisites

This is the list of things you need to run the program and
how to install them.

[![Python](https://img.shields.io/badge/-Python-black?style=flat&logo=Python&link=https://www.python.org/)](https://www.python.org/)

Module:
- Timeit (used to calculate the run time of the program)
  ```sh
  pip install timeit
  ```

## How to Run
1. Clone repository
  ```sh
  git clone https://github.com/bintangfrnz/Cryptarithmetic-Solver-with-Brute-Force.git
  ```

2. Move to src
  ```sh
  cd src
  ```

3. Run
  ```sh
  python Cryptarithmetic.py
  ```

## Contact

[![Instagram](https://img.shields.io/badge/-@bintangfrnz__-E1306C?style=flat&logo=instagram&logoColor=EEEEEE&link=https://instagram.com/bintangfrnz_/)](https://instagram.com/bintangfrnz_)

<a href="#cryptarithmetic-solver-with-brute-force">Back to Top</a>
