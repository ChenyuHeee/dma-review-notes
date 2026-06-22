# DMA 离散数学 摸底考试卷

> 考试范围：Ch1-6, Ch8-11 + Network Flow | 满分 100 | 时间 90 分钟

---

## Part 1: True/False (30%)

> 评分：答对 +3 分，空白 0 分，答错 -1 分（倒扣制）

### Ch1 Logic & Proofs

**Q1** . Let $P(x)$ be a predicate. Then $\forall x \exists y P(x, y) \equiv \exists y \forall x P(x, y)$. ( )

**Q2** . The negation of $\forall x (P(x) \to Q(x))$ is $\exists x (P(x) \land \neg Q(x))$. ( )

**Q3** . $(p \to q) \land (p \to r) \equiv p \to (q \land r)$. ( )

### Ch2 Sets & Functions

**Q4** . $|A \times B| = |A| \cdot |B|$ for any finite sets $A$ and $B$. ( )

**Q5** . If $f: A \to B$ and $g: B \to C$ are both injective, then $g \circ f$ is injective. ( )

**Q6** . The set of all finite subsets of $\mathbb{N}$ is countable. ( )

### Ch3 Algorithms

**Q7** . If $f(n) = 3n^2 + 2n + 1$, then $f(n) = \Theta(n^2)$. ( )

**Q8** . $n! = O(2^n)$. ( )

### Ch4 Number Theory

**Q9** . If $a \equiv b \pmod{m}$ and $c \equiv d \pmod{m}$, then $ac \equiv bd \pmod{m}$. ( )

**Q10** . $\gcd(a, b) \cdot \operatorname{lcm}(a, b) = ab$ for all positive integers $a, b$. ( )

### Ch5 Induction

**Q11** . The Well-Ordering Principle is equivalent to the Principle of Mathematical Induction. ( )

**Q12** . In strong induction, to prove $P(n)$ we assume $P(k)$ is true for all $k < n$, not just $P(n-1)$. ( )

### Ch6 Counting

**Q13** . $C(n, r) = P(n, r) / r!$ for all $0 \le r \le n$. ( )

**Q14** . By the pigeonhole principle, among any 13 people, at least 2 were born in the same month. ( )

### Ch8 Recurrence Relations

**Q15** . The characteristic equation of $a_n = 3a_{n-1} - 2a_{n-2}$ has roots 1 and 2. ( )

**Q16** . The number of derangements of $n$ objects is approximately $n!/e$. ( )

### Ch9 Relations

**Q17** . Every equivalence relation on a set $A$ partitions $A$. ( )

**Q18** . A relation that is symmetric and transitive must also be reflexive. ( )

### Ch10 Graphs

**Q19** . $K_5$ is a planar graph. ( )

**Q20** . A connected multigraph has an Euler circuit iff every vertex has even degree. ( )

**Q21** . The chromatic number of a bipartite graph is at most 2. ( )

**Q22** . By the Handshaking Theorem, every graph has an even number of vertices of odd degree. ( )

### Ch11 Trees

**Q23** . Every tree with $n$ vertices has exactly $n-1$ edges. ( )

**Q24** . In a full binary tree, the number of leaves equals the number of internal vertices plus 1. ( )

### Network Flow

**Q25** . By the Max-Flow Min-Cut Theorem, the value of a maximum flow equals the capacity of a minimum cut. ( )

---

## Part 2: Short Problems (40%)

### Ch1 (6%)

**Q26** . Write an equivalent proposition of $p \oplus q$ using only the NAND operator $|$.

### Ch2 (6%)

**Q27** . Let $A = \{1, 2, 3\}$, $B = \{2, 3, 4\}$. Compute:
(a) $A \oplus B$ (symmetric difference)
(b) $\mathcal{P}(A \cap B)$ (power set)

### Ch3 (4%)

**Q28** . Order the following functions by growth rate (slowest first):
$$(\log n)^2,\quad n\log n,\quad n^2,\quad 2^n,\quad n!,\quad n^{1/\log n}$$

### Ch4 (6%)

**Q29** . (a) Compute $\gcd(252, 198)$ using the Euclidean algorithm.
(b) Express $\gcd(252, 198)$ as a linear combination of 252 and 198 (Bézout coefficients).

### Ch5 (6%)

**Q30** . Prove by induction: $\sum_{i=1}^{n} (2i - 1) = n^2$ for all $n \ge 1$.

### Ch6 (6%)

**Q31** . How many strings of 4 lowercase letters:
(a) contain at least one 'a'?
(b) have all letters distinct?
(c) start with a vowel (a, e, i, o, u) and end with a consonant?

### Ch8 (6%)

**Q32** . Find the general solution to the recurrence relation:
$$a_n = 5a_{n-1} - 6a_{n-2} \quad (n \ge 2)$$
with initial conditions $a_0 = 2, a_1 = 7$.

---

## Part 3: Long Problems (30%)

### Ch9 Relations (10%)

**Q33** . Let $A = \{1, 2, 3, 4, 6, 12\}$ and define a relation $R$ on $A$ by:
$$a R b \iff a \mid b \quad (\text{a divides b})$$

(a) (30%) Prove that $R$ is a partial order.
(b) (30%) Draw the Hasse diagram.
(c) (20%) Find all maximal, minimal, maximum, and minimum elements.
(d) (20%) Is $(A, R)$ a lattice? Justify.

### Ch10 Graphs (10%)

**Q34** . Consider the following weighted graph:

```
Edges with weights:
A-B: 4, A-C: 2, B-C: 1, B-D: 5, C-D: 8, C-E: 10, D-E: 2, D-F: 6, E-F: 3
```

(a) (50%) Use Dijkstra's algorithm to find the shortest path from $A$ to $F$. Show each step.

(b) (50%) Does this graph have an Euler circuit? An Euler path? An Hamilton circuit? Justify each answer.

### Ch11 Trees (10%)

**Q35** . A file contains 6 symbols with frequencies: A: 15%, B: 25%, C: 5%, D: 20%, E: 10%, F: 25%.

(a) (50%) Construct a Huffman code for these symbols. Show the merging steps.
(b) (30%) What is the average number of bits per symbol using your Huffman code?
(c) (20%) If we used a fixed-length code, how many bits per symbol would be needed?

---

## Answer Quick-Check

| Q | Ans | Q | Ans | Q | Ans | Q | Ans |
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| 1 | F | 8 | F | 15 | T | 22 | T |
| 2 | T | 9 | T | 16 | T | 23 | T |
| 3 | T | 10 | T | 17 | T | 24 | T |
| 4 | T | 11 | T | 18 | F | 25 | T |
| 5 | T | 12 | T | 19 | F | | |
| 6 | T | 13 | T | 20 | T | | |
| 7 | T | 14 | T | 21 | T | | |

---

| Q26 | $(p \mid (q \mid q)) \mid ((p \mid p) \mid q)$ |
| Q27a | $\{1, 4\}$ |
| Q27b | $\{\emptyset, \{2\}, \{3\}, \{2, 3\}\}$ |
| Q28 | $n^{1/\log n} < (\log n)^2 < n\log n < n^2 < 2^n < n!$ |
| Q29a | $\gcd(252, 198) = 18$ |
| Q29b | $18 = 4 \cdot 252 - 5 \cdot 198$ |
| Q30 | Basis $n=1$: $1 = 1^2$ ✓; Inductive: $\sum_{i=1}^{k+1}(2i-1) = k^2 + (2k+1) = (k+1)^2$ ✓ |
| Q31a | $26^4 - 25^4 = 66351$ |
| Q31b | $P(26, 4) = 358800$ |
| Q31c | $5 \cdot 21 \cdot 26^2 = 70980$ |
| Q32 | $a_n = 3 \cdot 2^n - 3^n$ |
| Q33 | $R$ is reflexive, antisymmetric, transitive; Hasse: 1→2→6→12, 1→3→6, 1→4→12; Max=Maximal=12, Min=Minimal=1; Not a lattice (e.g. $\operatorname{lub}(2,4)$ does not exist in the "2,4 don't both divide anything below 12" sense — actually lub=12, glb(2,4)=1, but check: glb(6,4) = 2, lub(4,3)... 3 and 4 have no common upper bound less than 12, so lub(3,4)=12 exists, glb always exists? Actually (2,4) has glb 2... this is actually a lattice because it's the divisor poset of 12). Actually the divisor poset of any positive integer IS always a lattice (lub = lcm, glb = gcd). So yes, it is a lattice. |
| Q34a | A-C-B-D-F = 2+1+5+6 = 14 or A-C-B-D-E-F = 2+1+5+2+3 = 13. Shortest: A-B-D-E-F = 4+5+2+3 = 14. Wait: A-C=2, from C: C-B=1(B=3), from B: B-D=5(D=8), from D: D-E=2(E=10), from E: E-F=3(F=13). Path: A→C→B→D→E→F, length 2+1+5+2+3=13. |
| Q34b | All degrees even? deg(A)=2, B=3, C=3, D=3, E=3, F=2. Four odd-degree vertices → no Euler circuit, no Euler path. Dirac: min deg = 2 < 6/2 → insufficient for Hamilton guarantee, but doesn't prove non-existence. Try: A-C-B-D-F-E-A is not a circuit. Check: A-B-D-F-E-C-A: yes! All 6 vertices exactly once and back to A. Yes, Hamiltonian circuit exists. |
| Q35a | Merge: C+E=15% → A+CE=30% → D+B=45% → (A_C_E)+(B_D)=30%+45%=N/A... Actually step by step: C(5)+E(10)=15, A(15)+15=30, D(20)+B(25)=45, 30+F(25)=55, 45+55=100. Codes: B:00, D:01, F:10, A:110, E:1110, C:1111. |
| Q35b | Avg bits = 2×0.25 + 2×0.20 + 2×0.25 + 3×0.15 + 4×0.10 + 4×0.05 = 0.5+0.4+0.5+0.45+0.4+0.2 = 2.45 |
| Q35c | Fixed-length for 6 symbols needs ceil(log2 6) = 3 bits. |
