# Exam Review: Ch4 (Number Theory & Cryptography) + Ch5 (Induction & Recursion)

> 整理自郑文庭班历年小测真题（2022-2025），仅收录 Ch4-Ch5 相关题目。

---

## Ch4: Number Theory & Cryptography (数论与密码学)

### 4.1 整除与模运算 / 4.3 素数、GCD、Euler 函数

#### Euler's Totient Function (欧拉函数) | Quiz 1 2025 Q5

**题目**：If all the positive integers that are relatively prime with 77 are arranged into a strictly increasing sequence, find the 600th term of this sequence.

**考点**：
- 与 $n$ 互质的正整数构成一个**缩系 (reduced residue system / reduced set of residues)**，其元素个数为 $\varphi(n)$（欧拉函数）。
- $\varphi(77) = \varphi(7 \times 11) = (7-1) \times (11-1) = 60$.
- 每 $77$ 个连续整数中恰有 $60$ 个与 $77$ 互质，即序列以 $60$ 为**周期**，且每增加 $60$ 项，数值增加 $77$：$a_{n+60} = a_n + 77$.
- 求第 600 项：$a_{600} = a_{60} + 77 \times \left(\frac{600}{60} - 1\right) = a_{60} + 77 \times 9 = 769$.

**相关知识点**：
- $\varphi(p) = p-1$ 当 $p$ 为素数。
- $\varphi(p^k) = p^k - p^{k-1}$.
- $\varphi(mn) = \varphi(m)\varphi(n)$ 当 $\gcd(m,n)=1$（积性函数）。
- **缩系**：模 $n$ 的缩系是与 $n$ 互质的剩余类构成的集合。

---

### 4.4 解同余方程（中国剩余定理）

#### Chinese Remainder Theorem (CRT) | Quiz 1 2025 Q6

**题目**：Use the construction in the proof of the Chinese Remainder Theorem to find all solutions to the system of congruences:
$$
\begin{cases}
x \equiv 1 \pmod{3} \\
x \equiv 2 \pmod{5} \\
x \equiv 3 \pmod{8}
\end{cases}
$$

**解法步骤**：
1. $m_1 = 3,\ m_2 = 5,\ m_3 = 8$，$m = 3 \times 5 \times 8 = 120$.
2. $M_1 = \frac{m}{m_1} = 40,\ M_2 = \frac{m}{m_2} = 24,\ M_3 = \frac{m}{m_3} = 15$.
3. 求 $y_k$ 满足 $M_k y_k \equiv 1 \pmod{m_k}$：
   - $40 y_1 \equiv 1 \pmod{3} \Rightarrow y_1 = 1$
   - $24 y_2 \equiv 1 \pmod{5} \Rightarrow y_2 = 4$
   - $15 y_3 \equiv 1 \pmod{8} \Rightarrow y_3 = 7$
4. $x \equiv \sum a_k M_k y_k = 1 \times 40 \times 1 + 2 \times 24 \times 4 + 3 \times 15 \times 7 = 40 + 192 + 315 = 547 \equiv 67 \pmod{120}$.

**答案**：$x \equiv 67 \pmod{120}$.

---

#### CRT 应用：连续整除问题 | Quiz 4 2024 Q2

**题目**：There are three consecutive positive integers that are divisible by 5, 7, and 11 respectively （依次能被 5, 7, 11 整除）. Find all the solutions.

**分析**：设第一个数为 $n$，则：
$$
\begin{cases}
n \equiv 0 \pmod{5} \\
n+1 \equiv 0 \pmod{7} \Rightarrow n \equiv 6 \pmod{7} \\
n+2 \equiv 0 \pmod{11} \Rightarrow n \equiv 9 \pmod{11}
\end{cases}
$$

**考点**：将连续整除条件转化为标准 CRT 形式。$m = 5 \times 7 \times 11 = 385$，解出 $n$ 模 385 的唯一解。

---

### 4.5 密码学（费马小定理）

#### Fermat's Little Theorem (费马小定理) | Quiz 1 2025 Q1(g)

**题目**：（判断）$2026^{2025} \equiv 1 \pmod{2027}$.

**分析**：
- 2027 是素数，2025 与 2027 互质。
- 由费马小定理：若 $p$ 为素数且 $p \nmid a$，则 $a^{p-1} \equiv 1 \pmod{p}$.
- 这里 $a = 2025$，$p = 2027$，$p-1 = 2026$。
- 注意指数是 2025 而不是 2026！$2025^{2026} \equiv 1 \pmod{2027}$ 才成立。
- 但是 $2025 \equiv -2 \pmod{2027}$，$2026 \equiv -1 \pmod{2027}$，计算 $2026^{2025} \equiv (-1)^{2025} = -1 \equiv 2026 \pmod{2027}$.
- 实际上题目可能标记为 True（答案中说"注意到 2027 是素数，且 2025<2027，所以...2025^(2027-1) ≡ 1 (mod 2027)"——但原题是 $2026^{2025}$，答案可能写的是 $2025^{2026}$）。

**重要**：
- 费马小定理：$a^{p-1} \equiv 1 \pmod{p}$ 对素数 $p$ 且 $p \nmid a$ 成立。
- 易错点：指数必须是 $p-1$，底数 $a$ 不能被 $p$ 整除。

---

## Ch5: Induction & Recursion (归纳与递归)

### 5.1 数学归纳法（基本归纳法）

#### 不等式归纳 | Quiz 1 2022 Q8

**题目**：Use mathematical induction to prove that $n^{n+1} > (n+1)^n$ for all positive integer $n \ge 3$.

**考点**：
- Basis step: $n=3$，验证 $3^4 = 81 > 4^3 = 64$，成立。
- Inductive step: 假设 $k^{k+1} > (k+1)^k$，证 $(k+1)^{k+2} > (k+2)^{k+1}$.
- 关键技巧：从 $k^{k+1} > (k+1)^k$ 两边同乘适当因子，或等价变形为 $\frac{k^{k+1}}{(k+1)^k} > 1$，然后证明 $\frac{(k+1)^{k+2}}{(k+2)^{k+1}} > 1$.

---

#### 平均不等式归纳 | Quiz 1 2024 Q9

**题目**：Use induction to prove that: if $x > 0, y > 0$, then
$$
\frac{x^n + y^n}{2} \ge \left(\frac{x+y}{2}\right)^n
$$
for all positive integers $n$.

**考点**：
- Basis step: $n=1$ 时取等号。
- Inductive step: 假设 $n=k$ 成立，证明 $n=k+1$ 成立。
- 常用技巧：$\frac{x^{k+1}+y^{k+1}}{2} = \frac{x\cdot x^k + y \cdot y^k}{2}$，结合归纳假设和 AM-GM 或排序不等式。

---

#### 分配律的推广 | Quiz 1 2022 Q5 / Quiz 1 2025 Q7

**Quiz 1 2022 Q5**：Prove that the distributive law
$$
A \cap (A_1 \cup A_2 \cup \cdots \cup A_n) = (A \cap A_1) \cup (A \cap A_2) \cup \cdots \cup (A \cap A_n)
$$
is true for all $n > 2$.

**Quiz 1 2025 Q7**：Prove that $A_1 \cup (A_2 \cap \cdots \cap A_n) = (A_1 \cup A_2) \cap \cdots \cap (A_1 \cup A_n)$ for all $n > 2$.

**考点**：集合运算分配律（De Morgan / 分配律）的归纳推广。
- Basis step: $n=2$（或 $n=3$，视题目要求）时的分配律已知成立。
- Inductive step: 假设对 $n=k$ 成立，将 $n=k+1$ 的情形分成 $(A_1 \cup A_2 \cup \cdots \cup A_k) \cup A_{k+1}$ 再应用归纳假设。
- 本质是反复应用二元分配律。

---

#### 几何配对问题 | Quiz 4 2024 Q5

**题目**：There are $n$ red points and $n$ green points on the plane, any three of them are not collinear. Use induction to prove: These $2n$ points can be connected in pairs to form $n$ non-intersecting line segments. Each line segment connects a red point and a green point.

**考点**：
- 归纳法在几何组合中的应用。
- Inductive step: 找到一条直线将点集分为非空的两部分（各含 $k$ 个红点和 $k$ 个绿点），分别应用归纳假设。
- 关键思想：取最左下的红点，找一个绿点与之配对使连线不与其他点相交。

---

### 5.2 强归纳法（Strong Induction）

#### 斐波那契数表示 | Quiz 1 2025 Q8 / Quiz 4 2022 Q6

**题目**：Prove that every positive integer ($n > 2$) can be expressed as the sum of different Fibonacci numbers.

**考点**：
- **Fibonacci 数定义**：$f_1 = 1, f_2 = 2, f_3 = 3, f_4 = 5, \dots$（注意此处 $f_1=1, f_2=2$，区别于标准定义 $F_1=1, F_2=1$）。
- **方法一（普通归纳法）**：
  - Basis: $n=3 = f_1 + f_2$，成立。
  - 假设 $n$ 可表示为 $f_{i_1} + f_{i_2} + \cdots + f_{i_k}$（互异），考虑 $n+1$.
  - 若 $i_1 > 1$，直接加 $f_1 = 1$ 即可。
  - 若 $i_1 = 1$，利用 Fibonacci 性质 $f_m + f_{m+1} = f_{m+2}$ 合并相邻项。
- **方法二（强归纳法）**：
  - 假设所有小于 $n$ 且大于 2 的正整数均可表示。
  - 设 $f$ 为小于 $n$ 的最大 Fibonacci 数，考虑 $n - f$.
  - 若 $n - f = 1$ 或 $2$，则 $n = f + 1$ 或 $n = f + 2$，是两不同 Fib 数之和。
  - 若 $n - f \ge 3$，由强归纳假设 $n-f$ 可表示，且所有加数都小于 $f$，合并即得 $n$ 的表示。

---

#### 球合并问题 | 期末回忆

**题目**：把 $2^k$ 个球放到若干个包里。可以通过下面的规则合并包：
- 若两个包的球的个数相同，则可以直接将其合并为一个包。
- 若两个包的球个数不同，分别为 $m, n\ (m > n)$，则可将两个包的个数变为 $m-n, 2n$。
- 利用归纳法证明：这里存在一个合适的算法将 $2^k$ 个球合并到一个包上。

**考点**：
- Strong induction on $k$.
- Basis: $k=0$（只有一个球）或 $k=1$（两个球，直接合并）显然成立。
- Inductive step: 将 $2^{k+1}$ 个球分成两堆各 $2^k$ 个，分别用归纳假设合并成一堆，再处理两堆的合并。

---

### 5.3 递归定义 / 母函数与递推

#### 递推关系 | Quiz 4 2022 Q3 / Quiz 4 2024 Q4

**Quiz 4 2024 Q4**：Use generating functions to solve the recurrence relation $a_k = 5a_{k-1} - 6a_{k-2}$ with initial conditions $a_0 = 6$ and $a_1 = 30$.

**考点**：
- 特征方程：$r^2 - 5r + 6 = 0$，根为 $r=2, 3$.
- 通解形式：$a_n = \alpha \cdot 2^n + \beta \cdot 3^n$.
- 代入初值解 $\alpha, \beta$.

**Quiz 4 2022 Q3**：$a_n = c_1 a_{n-1} + c_2 a_{n-2} + c_3$，已知 $a_0 = 0, a_1 = 1, a_2 = 4, a_3 = 11, a_4 = 26$，求通解。

**考点**：
- 先由前几项反解系数 $c_1, c_2, c_3$.
- 然后解非齐次线性递推（齐次解 + 特解）。

---

## 题型总结与答题技巧

### Ch4 常见题型

| 题型 | 频次 | 关键方法 |
|------|------|----------|
| CRT 解同余方程组 | 高频 | $M_k y_k \equiv 1 \pmod{m_k}$ 求逆元 |
| Euler 函数 + 缩系 | 高频 | $\varphi(n)$ 周期性，$a_{n+\varphi(n)} = a_n + n$ |
| 费马小定理判断 | 中频 | $a^{p-1} \equiv 1 \pmod{p}$ 条件 |
| RSA 相关 | 未考 | 但需掌握密钥生成、加密/解密过程 |

### Ch5 常见题型

| 题型 | 频次 | 关键方法 |
|------|------|----------|
| 不等式归纳证明 | 高频 | Basis step 验证 + 代数变形 |
| 集合/分配律的归纳推广 | 高频 | 反复应用二元分配律 |
| 强归纳法（Fibonacci 表示等） | 高频 | 取最大小于 n 的 Fib 数 |
| 几何组合归纳 | 中频 | 构造分割线，分治归纳 |
| 递推关系求解 | 中频 | 特征方程 / 母函数 |

### 易错点提醒

1. **CRT 求逆元**：$M_k y_k \equiv 1 \pmod{m_k}$ 中的 $y_k$ 是 $M_k$ 在模 $m_k$ 下的乘法逆元，可用扩展欧几里得算法或试凑法求解。
2. **费马小定理指数**：指数必须是 $p-1$ 而非 $p$，且底数不能是 $p$ 的倍数。
3. **归纳法的 Basis step**：务必检查题目要求的起始值（可能从 $n=3$ 而不是 $n=1$ 开始）。
4. **强归纳假设**：假设所有小于 $n$ 的命题成立，而不仅仅是 $n-1$。
5. **Fibonacci 数表示**：注意题目定义的 $f_1$ 值（有时 $f_1=1, f_2=1$，有时 $f_1=1, f_2=2$）。

---

## 附录：历年 Ch4/Ch5 题目索引

| 试卷 | 题号 | 章节 | 考点 |
|------|------|------|------|
| Quiz 1 2022 | Q5 | Ch5 | 归纳法证明分配律推广 |
| Quiz 1 2022 | Q8 | Ch5 | 不等式归纳 $n^{n+1} > (n+1)^n$ |
| Quiz 1 2024 | Q9 | Ch5 | 平均不等式归纳 |
| Quiz 1 2025 | Q1(g) | Ch4 | 费马小定理判断 |
| Quiz 1 2025 | Q5 | Ch4 | 缩系 + Euler 函数求第 600 项 |
| Quiz 1 2025 | Q6 | Ch4 | 中国剩余定理（CRT） |
| Quiz 1 2025 | Q7 | Ch5 | 归纳法证明分配律推广 |
| Quiz 1 2025 | Q8 | Ch5 | 强归纳法：Fibonacci 数表示 |
| Quiz 4 2022 | Q3 | Ch5 | 线性递推关系求解 |
| Quiz 4 2022 | Q6 | Ch5 | 强归纳法：Fibonacci 数表示 |
| Quiz 4 2024 | Q2 | Ch4 | CRT 应用（连续整除） |
| Quiz 4 2024 | Q4 | Ch5 | 母函数解递推关系 |
| Quiz 4 2024 | Q5 | Ch5 | 归纳法：红绿点配对连线 |
| 期末回忆 | - | Ch5 | 强归纳法：球合并问题 |
