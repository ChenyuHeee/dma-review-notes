# DMA Quiz 1 题解 — 2024 年

## 一、判断题 (True/False) (30%)

### 题目 1a
**题目**：判断以下两个命题是否逻辑等价：
$$p \to (q \to r),\quad (p \to q) \to r$$

**答案**：F

**考点**：第一章 命题逻辑 —— 逻辑等价，蕴含律

**解析**：
$$
\begin{aligned}
p \to (q \to r) &\equiv \neg p \lor (\neg q \lor r) \equiv \neg p \lor \neg q \lor r \\
(p \to q) \to r &\equiv \neg(\neg p \lor q) \lor r \equiv (p \land \neg q) \lor r
\end{aligned}
$$

取反例：$p = \mathrm{F}, q = \mathrm{T}, r = \mathrm{F}$：
- LHS：$\mathrm{F} \to (\mathrm{T} \to \mathrm{F}) \equiv \mathrm{F} \to \mathrm{F} \equiv \mathrm{T}$
- RHS：$(\mathrm{F} \to \mathrm{T}) \to \mathrm{F} \equiv \mathrm{T} \to \mathrm{F} \equiv \mathrm{F}$

两者不等价。答案为 **F**。

---

### 题目 1b
**题目**：若 $A, B, C$ 是集合，则 $A \oplus (B \oplus C) = (A \oplus B) \oplus C$（其中 $\oplus$ 为对称差）

**答案**：T

**考点**：第二章 集合运算 —— 对称差（Symmetric Difference）

**解析**：对称差定义为 $A \oplus B = (A - B) \cup (B - A) = (A \cup B) - (A \cap B)$。
对称差运算满足结合律，即 $A \oplus (B \oplus C) = (A \oplus B) \oplus C$。

一种理解方式：$x \in A \oplus B$ 当且仅当 $x$ 恰好在 $A$ 和 $B$ 中的一个中。因此 $x \in A \oplus (B \oplus C)$ 当且仅当 $x$ 属于 $A, B, C$ 中的奇数个（1 个或 3 个），这与 $(A \oplus B) \oplus C$ 等价。答案为 **T**。

---

### 题目 1c
**题目**：$8 + 3 = 9$ 当且仅当 $8 - 3 = 7$。

**答案**：T

**考点**：第一章 命题逻辑 —— 双条件（biconditional）的真值

**解析**：
- $8 + 3 = 9$ 为假
- $8 - 3 = 7$ 为假
- 双条件 $\mathrm{F} \leftrightarrow \mathrm{F} \equiv \mathrm{T}$

因此整个命题为真。答案为 **T**。

---

### 题目 1d
**题目**：$(0,1)$ 中十进制表示只由 6 和 8 组成的正实数集合是不可数的。

**答案**：T

**考点**：第二章 集合的基数 —— Cantor 对角线论证

**解析**：此题与 2022 年第六题本质相同，只是将数码从 $\{0,1\}$ 换成了 $\{6,8\}$。

通过 Cantor 对角线论证：假设该集合可数，列出所有元素 $r_1, r_2, r_3, \ldots$，构造新数 $r$ 使得
$$
r\text{ 的第 }i\text{ 位} = \begin{cases}
8 & \text{若 } r_i\text{ 的第 }i\text{ 位} = 6 \\
6 & \text{若 } r_i\text{ 的第 }i\text{ 位} = 8
\end{cases}
$$
则 $r$ 属于该集合但不等于任何 $r_i$，矛盾。故不可数。答案为 **T**。

---

### 题目 1e
**题目**：满足整系数二次方程 $ax^2 + bx + c = 0$ 的实数解集合是可数的。

**答案**：T

**考点**：第二章 集合的基数 —— 可数集的性质

**解析**：
- 每个二次方程由整数系数 $(a, b, c) \in \mathbb{Z}^3$ 确定，$\mathbb{Z}^3$ 是可数的。
- 每个二次方程最多有 2 个实根。
- 所有实根的集合是"可数多个有限集"的并，故可数。

答案为 **T**。

---

### 题目 1f
**题目**：在 $n$ 个数的列表中线性查找最小数的时间复杂度是 $\Theta(n \log n)$。

**答案**：F

**考点**：第三章 算法复杂度 —— 线性查找

**解析**：查找最小数需要逐个比较每个元素，总共 $n-1$ 次比较，时间复杂度为 $\Theta(n)$，而非 $\Theta(n \log n)$。答案为 **F**。

---

## 二、谓词逻辑翻译 (10%)

**题目**：设变量 $x$ 表示学生，$y$ 表示课程，$T(x, y)$ 表示"$x$ 正在修 $y$"。翻译为符号形式。

### 题目 2a
**题目**：有一门课程被所有学生修读（There is a course that is being taken by all students）

**答案**：$\exists y \forall x\, T(x, y)$

**考点**：第一章 谓词与量词 —— 嵌套量词

**解析**："存在一门课程 $y$，使得对所有学生 $x$，$x$ 在修 $y$。"

---

### 题目 2b
**题目**：没有学生修读所有课程（No student is taking all courses）

**答案**：$\neg \exists x \forall y\, T(x, y)$ 或 $\forall x \exists y\, \neg T(x, y)$

**考点**：第一章 谓词与量词 —— 量词的否定

**解析**：
- "存在一个学生修读所有课程"：$\exists x \forall y\, T(x, y)$
- "没有"即否定：$\neg \exists x \forall y\, T(x, y)$
- 等价形式（将否定内移）：$\forall x \neg \forall y\, T(x, y) \equiv \forall x \exists y\, \neg T(x, y)$

---

## 三、函数复合 (5%)

**题目**：设 $g: A \to B$ 和 $f: B \to C$，其中 $A = \{1, 2, 3, 4\}, B = \{a, b, c\}, C = \{2, 7, 10\}$，且
$$
g = \{(1, b), (2, a), (3, a), (4, b)\}, \quad f = \{(a, 10), (b, 7), (c, 2)\}
$$
求 $f \circ g$。

**考点**：第二章 函数（Functions）—— 函数复合

**解析**：
$$
\begin{aligned}
(f \circ g)(1) &= f(g(1)) = f(b) = 7 \\
(f \circ g)(2) &= f(g(2)) = f(a) = 10 \\
(f \circ g)(3) &= f(g(3)) = f(a) = 10 \\
(f \circ g)(4) &= f(g(4)) = f(b) = 7
\end{aligned}
$$

因此：
$$
f \circ g = \{(1, 7), (2, 10), (3, 10), (4, 7)\}
$$

---

## 四、命题等价变换 (7%)

**题目**：写出一个与 $p \land \neg q$ 等价的命题，只使用 $p, q$ 和联结词 $|$（NAND）。

**答案**：$(p \mid (q \mid q)) \mid (p \mid (q \mid q))$

**考点**：第一章 命题逻辑 —— NAND 功能完全性

**解析**：
由 NAND 定义：$p \mid q \equiv \neg(p \land q)$

逐步构造：
- 否定：$\neg q \equiv q \mid q$
- 合取逆用：$\neg(p \land \neg q) \equiv p \mid \neg q \equiv p \mid (q \mid q)$
- 再否定回来：$p \land \neg q \equiv \neg(p \mid (q \mid q)) \equiv (p \mid (q \mid q)) \mid (p \mid (q \mid q))$

---

## 五、主析取范式与主合取范式 (14%)

**题目**：求 $p \oplus (q \oplus r)$（其中 $\oplus$ 表示异或 XOR）的：
- (a) 全析取范式（full DNF）（7%）
- (b) 全合取范式（full CNF）（7%）

**考点**：第一章 命题逻辑 —— 异或，主范式

**解析**：

异或运算满足结合律：$p \oplus (q \oplus r) \equiv (p \oplus q) \oplus r \equiv p \oplus q \oplus r$。

$p \oplus q \oplus r$ 为真当且仅当 $p, q, r$ 中有奇数个为真（即 1 个或 3 个为真）。

真值表：

| $p$ | $q$ | $r$ | $p \oplus q \oplus r$ |
|:---:|:---:|:---:|:---:|
| F | F | F | F |
| F | F | T | T |
| F | T | F | T |
| F | T | T | F |
| T | F | F | T |
| T | F | T | F |
| T | T | F | F |
| T | T | T | T |

公式为真的行（4 行）：$(F,F,T), (F,T,F), (T,F,F), (T,T,T)$
公式为假的行（4 行）：$(F,F,F), (F,T,T), (T,F,T), (T,T,F)$

**(a) 全 DNF**：
$$
(\neg p \land \neg q \land r) \lor (\neg p \land q \land \neg r) \lor (p \land \neg q \land \neg r) \lor (p \land q \land r)
$$

**(b) 全 CNF**：
$$
(p \lor q \lor r) \land (p \lor \neg q \lor \neg r) \land (\neg p \lor q \lor \neg r) \land (\neg p \lor \neg q \lor r)
$$

---

## 六、函数阶的排序 (7%)

**题目**：将以下函数按顺序排列，使得每个函数是下一个函数的 Big-O。

$$
\begin{aligned}
f_1(n) &= (1.01)^n & f_2(n) &= 10n! & f_3(n) &= (\log n)^3 \\
f_4(n) &= 2^n & f_5(n) &= \log \log n & f_6(n) &= 999n^2(\log n)^3 \\
f_7(n) &= \frac{n^4+1}{n^3+3} & f_8(n) &= n^3 + n(\log n)^2 & f_9(n) &= 9^{999}
\end{aligned}
$$

**答案**：$f_9 \to f_5 \to f_3 \to f_7 \to f_6 \to f_8 \to f_1 \to f_4 \to f_2$

**考点**：第三章 函数的增长 —— 常见函数增长阶比较

**解析**：

| 函数 | 简化阶 | 排序 |
|:---|:---|:---:|
| $f_9(n) = 9^{999}$ | $O(1)$ 常数 | 1 |
| $f_5(n) = \log \log n$ | 对数-对数 | 2 |
| $f_3(n) = (\log n)^3$ | 多对数 | 3 |
| $f_7(n) = \dfrac{n^4+1}{n^3+3} \sim n$ | $\Theta(n)$ | 4 |
| $f_6(n) = 999n^2(\log n)^3$ | $\Theta(n^2(\log n)^3)$ | 5 |
| $f_8(n) = n^3 + n(\log n)^2$ | $\Theta(n^3)$ | 6 |
| $f_1(n) = (1.01)^n$ | 指数（底 1.01） | 7 |
| $f_4(n) = 2^n$ | 指数（底 2） | 8 |
| $f_2(n) = 10n!$ | 阶乘 | 9 |

说明：
- $f_7(n) = \dfrac{n^4+1}{n^3+3} = n - \dfrac{3n}{n^3+3} + \dfrac{1}{n^3+3} \sim n$，为线性增长
- $\log \log n \prec (\log n)^3 \prec n \prec n^2(\log n)^3 \prec n^3$
- $(1.01)^n \prec 2^n$ 因为 $(1.01/2)^n \to 0$
- $n!$ 比任何指数函数增长都快

---

## 七、取整函数与集合基数 (10%)

**题目**：设集合
$$
A = \{\lceil x \rceil + \lceil 2x \rceil + \lceil 3x \rceil \mid x \in \mathbb{R}\}, \quad
B = \{x \mid x\text{ 是小于 2024 的正整数}\}
$$
求 $|A \cap B|$。

**考点**：第二章 集合与函数 —— 取整函数（Ceiling Function），集合的计数

**解析**：

将 $x$ 写成 $x = n + \varepsilon$，其中 $n \in \mathbb{Z}$，$\varepsilon \in [0, 1)$。

当 $\varepsilon = 0$（$x$ 为整数）时：
$$
\lceil x \rceil = n,\; \lceil 2x \rceil = 2n,\; \lceil 3x \rceil = 3n \implies f(x) = 6n
$$

当 $\varepsilon > 0$ 时，$\lceil x \rceil = n + 1$。按 $\varepsilon$ 范围分段讨论：

| $\varepsilon$ 范围 | $\lceil 2x \rceil$ | $\lceil 3x \rceil$ | $f(x)$ |
|:---:|:---:|:---:|:---:|
| $(0, \frac{1}{3}]$ | $2n + 1$ | $3n + 1$ | $6n + 3$ |
| $(\frac{1}{3}, \frac{1}{2}]$ | $2n + 1$ | $3n + 2$ | $6n + 4$ |
| $(\frac{1}{2}, \frac{2}{3}]$ | $2n + 2$ | $3n + 2$ | $6n + 5$ |
| $(\frac{2}{3}, 1)$ | $2n + 2$ | $3n + 3$ | $6n + 6$ |

所以对每个整数 $n$，$A$ 包含的值为：$6n, 6n+3, 6n+4, 6n+5, 6n+6$。

即 $A = \mathbb{Z} \setminus \{6k+1, 6k+2 \mid k \in \mathbb{Z}\}$（缺少形如 $6k+1$ 和 $6k+2$ 的整数）。

$B = \{1, 2, 3, \ldots, 2023\}$。

$A \cap B$ 即 $B$ 中不被排除的数。排除的数形如 $6k+1$ 或 $6k+2$ 且小于 2024：
- $6k+1 < 2024 \Rightarrow k \le 337$，共 338 个（$k = 0, 1, \ldots, 337$）
- $6k+2 < 2024 \Rightarrow k \le 336$，共 337 个（$k = 0, 1, \ldots, 336$）

排除总数 = $338 + 337 = 675$

因此：
$$
|A \cap B| = 2023 - 675 = 1348
$$

---

## 八、反证法与有理数 (10%)

**题目**：证明：若 $x^3$ 是无理数，则 $x$ 是无理数。

**考点**：第一章 证明方法 —— 逆否命题

**解析**：

采用**逆否命题**进行证明。原命题的逆否命题为：

> 若 $x$ 是有理数，则 $x^3$ 是有理数。

证明：设 $x$ 是有理数，则可写为 $x = \dfrac{p}{q}$，其中 $p, q \in \mathbb{Z}$，$q \neq 0$，且 $\gcd(p, q) = 1$（既约分数）。则：
$$
x^3 = \left(\frac{p}{q}\right)^3 = \frac{p^3}{q^3}
$$
由于 $p^3, q^3 \in \mathbb{Z}$，且 $q^3 \neq 0$，所以 $x^3$ 是有理数。

原命题与其逆否命题等价，故原命题成立。

---

## 九、数学归纳法——幂平均不等式 (10%)

**题目**：用归纳法证明：若 $x > 0, y > 0$，则
$$
\frac{x^n + y^n}{2} \ge \left(\frac{x + y}{2}\right)^n
$$
对所有正整数 $n$ 成立。

**考点**：第五章 数学归纳法 —— 不等式证明；幂平均不等式（Power Mean Inequality）特例

**解析**：

**归纳基础**：$n = 1$：
$$
\frac{x + y}{2} \ge \frac{x + y}{2}
$$
等号成立。

**归纳假设**：设 $n = k$ 时命题成立，即：
$$
\frac{x^k + y^k}{2} \ge \left(\frac{x + y}{2}\right)^k
$$

**归纳步骤**：需证 $n = k + 1$ 时：
$$
\frac{x^{k+1} + y^{k+1}}{2} \ge \left(\frac{x + y}{2}\right)^{k+1}
$$

由归纳假设两边乘以 $\dfrac{x+y}{2}$：
$$
\left(\frac{x + y}{2}\right)^{k+1} \le \frac{x + y}{2} \cdot \frac{x^k + y^k}{2}
$$

只需证明：
$$
\frac{x + y}{2} \cdot \frac{x^k + y^k}{2} \le \frac{x^{k+1} + y^{k+1}}{2}
$$

等价于：
$$
(x + y)(x^k + y^k) \le 2(x^{k+1} + y^{k+1})
$$

展开左边：
$$
x^{k+1} + xy^k + yx^k + y^{k+1} \le 2x^{k+1} + 2y^{k+1}
$$

移项：
$$
0 \le x^{k+1} + y^{k+1} - xy^k - yx^k
$$

因式分解：
$$
x^{k+1} + y^{k+1} - xy^k - yx^k = x^k(x - y) + y^k(y - x) = (x - y)(x^k - y^k)
$$

由于 $x > 0, y > 0$：
- 若 $x \ge y$，则 $x - y \ge 0$ 且 $x^k - y^k \ge 0$，乘积 $\ge 0$
- 若 $x < y$，则 $x - y < 0$ 且 $x^k - y^k < 0$，乘积 $> 0$

因此 $(x - y)(x^k - y^k) \ge 0$ 恒成立。

于是：
$$
\frac{x + y}{2} \cdot \frac{x^k + y^k}{2} \le \frac{x^{k+1} + y^{k+1}}{2}
$$

结合归纳假设：
$$
\left(\frac{x + y}{2}\right)^{k+1} \le \frac{x + y}{2} \cdot \frac{x^k + y^k}{2} \le \frac{x^{k+1} + y^{k+1}}{2}
$$

由数学归纳法，对所有正整数 $n$ 成立。证毕。
