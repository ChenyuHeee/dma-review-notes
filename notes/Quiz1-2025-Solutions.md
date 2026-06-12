# DMA Quiz 1 题解 — 2025 年

## 一、判断题 (True/False) (35%)

**评分规则**：答对 +5 分，空白 0 分，答错 -2 分（倒扣机制，防止乱猜）

### 题目 1a
**题目**：若 \(x\) 不在 \(A\) 中出现，则 \(\exists x(P(x) \to A) \equiv \forall x P(x) \to A\)。

**答案**：T

**考点**：第一章 谓词与量词 —— 量词的分配律，蕴含律

**解析**：
\[
\begin{aligned}
\exists x(P(x) \to A) &\equiv \exists x(\neg P(x) \lor A) \quad &\text{(蕴含律)}\\
&\equiv (\exists x \neg P(x)) \lor A \quad &\text{(}\exists\text{ 对 }\lor\text{ 分配，}x\text{ 在 }A\text{ 中不自由)}\\
&\equiv \neg(\forall x P(x)) \lor A \quad &\text{(量词否定)}\\
&\equiv \forall x P(x) \to A \quad &\text{(蕴含律)}
\end{aligned}
\]
关键步骤：由于 \(x\) 在 \(A\) 中不出现（即 \(A\) 是闭公式或不含变量 \(x\)），存在量词可以直接分配于析取式。答案为 **T**。

---

### 题目 1b
**题目**：若 \(A, B, C\) 是集合，则 \(A - (B \cap C) = (A - B) \cup (A - C)\)。

**答案**：T

**考点**：第二章 集合运算 —— 德摩根律的集合版本

**解析**：
\[
\begin{aligned}
x \in A - (B \cap C) &\iff x \in A \land x \notin (B \cap C) \\
&\iff x \in A \land (x \notin B \lor x \notin C) \quad &\text{(德摩根律)}\\
&\iff (x \in A \land x \notin B) \lor (x \in A \land x \notin C) \quad &\text{(分配律)}\\
&\iff x \in (A - B) \cup (A - C)
\end{aligned}
\]
集合相等得证。答案为 **T**。

---

### 题目 1c
**题目**：若 \(n\) 是整数，则 \(\lceil n/2 \rceil + \lfloor n/2 \rfloor = n\)。

**答案**：T

**考点**：第二章 序列与求和 —— 取整函数（Ceiling & Floor）

**解析**：
- 若 \(n = 2k\)（偶数）：\(\lceil k \rceil + \lfloor k \rfloor = k + k = 2k = n\)
- 若 \(n = 2k - 1\)（奇数）：\(\lceil k - 0.5 \rceil + \lfloor k - 0.5 \rfloor = k + (k - 1) = 2k - 1 = n\)

答案为 **T**。

---

### 题目 1d
**题目**：设 \(P(x, y)\) 是一个谓词，论域为 \(\{1, 2, 3, 4\}\)。已知 \(P(1,3), P(2,1), P(2,4), P(3,2), P(3,4), P(4,1), P(4,4)\) 为真，其余为假。则 \(\forall x \exists y ((x \le y) \land P(x, y))\) 为真。

**答案**：T

**考点**：第一章 嵌套量词 —— 量词真值判定

**解析**：逐 \(x\) 验证：

| \(x\) | 可选择 \(y\) | \((x \le y) \land P(x, y)\) |
|:---:|:---:|:---:|
| 1 | \(y = 3\) | \((1 \le 3) \land P(1,3) \equiv \mathrm{T} \land \mathrm{T} \equiv \mathrm{T}\) |
| 2 | \(y = 4\) | \((2 \le 4) \land P(2,4) \equiv \mathrm{T} \land \mathrm{T} \equiv \mathrm{T}\) |
| 3 | \(y = 4\) | \((3 \le 4) \land P(3,4) \equiv \mathrm{T} \land \mathrm{T} \equiv \mathrm{T}\) |
| 4 | \(y = 4\) | \((4 \le 4) \land P(4,4) \equiv \mathrm{T} \land \mathrm{T} \equiv \mathrm{T}\) |

每个 \(x\) 都能找到满足条件的 \(y\)，故全称量化命题为真。答案为 **T**。

---

### 题目 1e
**题目**：\(n^{0.01}\) 是 \(O(\log n)\)。（注：原卷文字略有损毁，根据参考答案推断为此题）

**答案**：F

**考点**：第三章 函数的增长 —— Big-O 记号，多项式与对数的比较

**解析**：
对于任意正常数 \(a > 0, b > 0\)，有 \(n^a = \Omega((\log n)^b)\)，即多项式函数增长严格快于任何对数函数的幂。特别地，\(n^{0.01} / \log n \to \infty\) 当 \(n \to \infty\)。

因此 \(n^{0.01}\) 不是 \(O(\log n)\)。答案为 **F**。

> 注意：若函数趋于 0（如 \((0.01)^n\)），则它会是 \(O(\log n)\)，但这里 \(n^{0.01}\) 是增长函数。

---

### 题目 1f
**题目**：\((0,1)\) 中十进制表示只由 0 和 1 组成的正实数集合是可数的。

**答案**：F

**考点**：第二章 集合的基数 —— Cantor 对角线论证

**解析**：
此题与 2022 年第六题完全相同。该集合实际上是**不可数**的（由 Cantor 对角线法可证）。

假设可数，列出所有元素 \(r_1, r_2, r_3, \ldots\)，构造新数 \(r = 0.b_1b_2b_3\cdots\)，其中：
\[
b_i = \begin{cases}
1 & \text{若 } r_i\text{ 的第 }i\text{ 位 } = 0 \\
0 & \text{若 } r_i\text{ 的第 }i\text{ 位 } = 1
\end{cases}
\]
则 \(r\) 的每个数码都是 0 或 1，故 \(r\) 属于该集合；但 \(r\) 与每个 \(r_i\) 都至少在第 \(i\) 位不同，矛盾。

故该集合不可数，原题为假。答案为 **F**。

---

### 题目 1g
**题目**：\(2025^{2026} \equiv 1 \pmod{2027}\)。

**答案**：T

**考点**：第四章 数论 —— 费马小定理（Fermat's Little Theorem）

**解析**：
- 2027 是素数（可验证：\(\sqrt{2027} \approx 45\)，不能被小于 45 的任何素数整除）。
- 2025 与 2027 互素（\(\gcd(2025, 2027) = 1\)，因为 \(2027 - 2025 = 2\)，而 2025 是奇数）。
- 由费马小定理：若 \(p\) 为素数且 \(p \nmid a\)，则 \(a^{p-1} \equiv 1 \pmod{p}\)。
- 这里 \(p = 2027\)，\(a = 2025\)，\(p-1 = 2026\)，故：
\[
2025^{2026} \equiv 1 \pmod{2027}
\]
答案为 **T**。

---

## 二、命题等价变换 (12%)

**题目**：写出一个与 \(p \oplus q\)（异或）等价的命题：
- (a) 只使用 \(p, q, \neg\) 和联结词 \(\land\)（6%）
- (b) 只使用 \(p, q\) 和联结词 \(|\)（NAND）（6%）

### 题目 2a 解析
\[
p \oplus q \equiv (p \land \neg q) \lor (\neg p \land q)
\]

用 \(\land\) 和 \(\neg\) 表示 \(\lor\)（德摩根律）：
\[
p \oplus q \equiv \neg(\neg(p \land \neg q) \land \neg(\neg p \land q))
\]

**答案**：\(\neg(\neg(p \land \neg q) \land \neg(\neg p \land q))\)

### 题目 2b 解析

NAND 定义：\(p \mid q \equiv \neg(p \land q)\)

逐步构造：
- \(\neg q \equiv q \mid q\)
- \(\neg p \equiv p \mid p\)
- \(p \land \neg q \equiv \neg(p \mid (q \mid q)) \equiv (p \mid (q \mid q)) \mid (p \mid (q \mid q))\)
- \(\neg p \land q \equiv \neg((p \mid p) \mid q) \equiv ((p \mid p) \mid q) \mid ((p \mid p) \mid q)\)
- \((A) \lor (B) \equiv \neg(\neg A \land \neg B)\)

代入化简后得简洁形式：

**答案**：\((p \mid (q \mid q)) \mid ((p \mid p) \mid q)\)

验证：
\[
\begin{aligned}
(p \mid (q \mid q)) \mid ((p \mid p) \mid q)
&= \neg(p \land \neg q) \mid \neg(\neg p \land q) \\
&= \neg(\neg(p \land \neg q) \land \neg(\neg p \land q)) \\
&= (p \land \neg q) \lor (\neg p \land q) \\
&= p \oplus q
\end{aligned}
\]

---

## 三、主合取范式 (9%)

**题目**：求 \((p \oplus q) \lor r\) 的全合取范式（full CNF）。

**答案**：\((p \lor q \lor r) \land (\neg p \lor \neg q \lor r)\)

**考点**：第一章 命题逻辑 —— 主合取范式，异或

**解析**：

计算真值表：

| \(p\) | \(q\) | \(r\) | \(p \oplus q\) | \((p \oplus q) \lor r\) |
|:---:|:---:|:---:|:---:|:---:|
| F | F | F | F | F |
| F | F | T | F | T |
| F | T | F | T | T |
| F | T | T | T | T |
| T | F | F | T | T |
| T | F | T | T | T |
| T | T | F | F | F |
| T | T | T | F | T |

公式为假的行：\((F,F,F)\) 和 \((T,T,F)\)。

对应的极大项（maxterm）：
- \((F,F,F)\)：\(p \lor q \lor r\)
- \((T,T,F)\)：\(\neg p \lor \neg q \lor r\)

全 CNF（所有极大项的合取）：
\[
(p \lor q \lor r) \land (\neg p \lor \neg q \lor r)
\]

---

## 四、函数的枚举与分类 (8%)

**题目**：列出所有从 \(A = \{1, 2\}\) 到 \(B = \{a, b\}\) 的函数，并指出哪些是双射（bijection），哪些是满射（surjection）。

**考点**：第二章 函数 —— 映射的种类：单射、满射、双射

**解析**：

从 \(A\) 到 \(B\) 共有 \(|B|^{|A|} = 2^2 = 4\) 个函数：

| 函数 | \(f(1)\) | \(f(2)\) | 单射? | 满射? | 双射? |
|:---:|:---:|:---:|:---:|:---:|:---:|
| \(f_1\) | \(a\) | \(a\) | 否（1 和 2 都映射到 \(a\)） | 否（\(b\) 无原像） | 否 |
| \(f_2\) | \(a\) | \(b\) | 是 | 是 | **是** |
| \(f_3\) | \(b\) | \(a\) | 是 | 是 | **是** |
| \(f_4\) | \(b\) | \(b\) | 否 | 否（\(a\) 无原像） | 否 |

**结果**：
- 所有函数：\(f_1, f_2, f_3, f_4\)
- 双射：\(f_2, f_3\)
- 满射：\(f_2, f_3\)
- 无双射以外的满射（因为 \(|A| = |B|\)，此时单射等价于满射等价于双射）

---

## 五、简化剩余系 (9%)

**题目**：将所有与 77 互质的正整数排成严格递增序列，求第 600 项。

**答案**：769

**考点**：第四章 数论 —— 欧拉函数 \(\varphi\)，简化剩余系（Reduced Residue System），周期性

**解析**：

\[
77 = 7 \times 11
\]

与 77 互质的正整数就是不被 7 整除也不被 11 整除的数。

每 77 个连续整数中，与 77 互质的个数为欧拉函数 \(\varphi(77)\)：
\[
\varphi(77) = \varphi(7 \times 11) = 77 \times \left(1 - \frac{1}{7}\right) \times \left(1 - \frac{1}{11}\right) = 77 \times \frac{6}{7} \times \frac{10}{11} = 60
\]

即序列以 60 为周期，每增加 77，序列的值增加 77：
\[
a_{n+60} = a_n + 77
\]

因此：
\[
a_{600} = a_{60} + 77 \times \left(\frac{600}{60} - 1\right) = a_{60} + 77 \times 9 = a_{60} + 693
\]

\(a_{60}\) 是小于 77 且与 77 互质的最大正整数。由于 \(77 - 1 = 76\) 与 77 互质，\(a_{60} = 76\)。

故：
\[
a_{600} = 76 + 693 = 769
\]

---

## 六、中国剩余定理 (9%)

**题目**：利用中国剩余定理证明中的构造方法，求解同余方程组：
\[
x \equiv 1 \pmod{3},\quad x \equiv 2 \pmod{5},\quad x \equiv 3 \pmod{8}
\]

**考点**：第四章 求解同余式 —— 中国剩余定理（Chinese Remainder Theorem）

**解析**：

**步骤 1**：确定模数及总模。
\[
m_1 = 3,\; m_2 = 5,\; m_3 = 8,\quad M = 3 \times 5 \times 8 = 120
\]

**步骤 2**：计算各 \(M_k = M / m_k\)。
\[
M_1 = 120 / 3 = 40,\quad M_2 = 120 / 5 = 24,\quad M_3 = 120 / 8 = 15
\]

**步骤 3**：求解 \(y_k\) 使 \(M_k y_k \equiv 1 \pmod{m_k}\)。
- \(40 y_1 \equiv 1 \pmod{3}\)：\(40 \equiv 1 \pmod{3}\)，所以 \(1 \cdot y_1 \equiv 1 \pmod{3} \Rightarrow y_1 = 1\)
- \(24 y_2 \equiv 1 \pmod{5}\)：\(24 \equiv 4 \pmod{5}\)，\(4 y_2 \equiv 1 \pmod{5} \Rightarrow y_2 = 4\)（因为 \(4 \times 4 = 16 \equiv 1\)）
- \(15 y_3 \equiv 1 \pmod{8}\)：\(15 \equiv 7 \pmod{8}\)，\(7 y_3 \equiv 1 \pmod{8} \Rightarrow y_3 = 7\)（因为 \(7 \times 7 = 49 \equiv 1\)）

**步骤 4**：构造解。
\[
\begin{aligned}
x &\equiv \sum_{k=1}^{3} a_k M_k y_k \pmod{M} \\
&= 1 \times 40 \times 1 + 2 \times 24 \times 4 + 3 \times 15 \times 7 \\
&= 40 + 192 + 315 \\
&= 547 \\
&\equiv 547 - 4 \times 120 = 67 \pmod{120}
\end{aligned}
\]

**答案**：\(x \equiv 67 \pmod{120}\)，即 \(x = 67 + 120k\)，\(k \in \mathbb{Z}\)。

**验证**：
- \(67 \bmod 3 = 1\) ✓
- \(67 \bmod 5 = 2\) ✓
- \(67 \bmod 8 = 3\) ✓

---

## 七、集合分配律的推广 (9%)

**题目**：证明分配律
\[
A_1 \cup (A_2 \cap \cdots \cap A_n) = (A_1 \cup A_2) \cap \cdots \cap (A_1 \cup A_n)
\]
对所有 \(n > 2\) 成立。

**考点**：第二章 集合运算 —— 分配律，元素法证明

**解析**：

用元素法直接证明：
\[
\begin{aligned}
x \in A_1 \cup (A_2 \cap \cdots \cap A_n)
&\iff x \in A_1 \lor x \in (A_2 \cap \cdots \cap A_n) \\
&\iff x \in A_1 \lor (x \in A_2 \land \cdots \land x \in A_n) \\
&\iff (x \in A_1 \lor x \in A_2) \land \cdots \land (x \in A_1 \lor x \in A_n) \quad &\text{(分配律)}\\
&\iff x \in (A_1 \cup A_2) \cap \cdots \cap (A_1 \cup A_n)
\end{aligned}
\]

由集合外延公理，等式成立。

也可用数学归纳法证明：
- 基础 \(n = 2\) 即基本分配律 \(A_1 \cup (A_2 \cap A_3) = (A_1 \cup A_2) \cap (A_1 \cup A_3)\)。
- 归纳步骤与 2022 年第五题类似。

---

## 八、斐波那契表示定理 (9%)

**题目**：证明每个大于 2 的正整数都可以表示为不同的斐波那契数之和。

**注**：此处斐波那契数定义为 \(f_1 = 1, f_2 = 2, f_3 = 3, f_4 = 5, f_5 = 8, \ldots\)（即略去 \(f_0 = 0\)，直接从 \(f_1 = 1, f_2 = 2\) 开始）。

**考点**：第五章 数学归纳法与强归纳法 —— 菲波那契数的性质，Zeckendorf 定理

**解析**：

**方法一（普通归纳法）**：

**归纳基础**：\(n = 3\)。\(3 = f_1 + f_2 = 1 + 2\)，成立。

**归纳假设**：设 \(n\) 可表示为不同斐波那契数之和：\(n = f_{i_1} + f_{i_2} + \cdots + f_{i_k}\)，其中 \(i_1 < i_2 < \cdots < i_k\)。

**归纳步骤**：考虑 \(n + 1\)。\(n + 1 = 1 + f_{i_1} + f_{i_2} + \cdots + f_{i_k}\)。

- 若 \(i_1 > 1\)（即 \(f_{i_1} \neq 1\)），则 \(1\) 与所有 \(f_{i_j}\) 均不同，故 \(n+1\) 已被表示为不同斐波那契数之和。

- 若 \(i_1 = 1\)，则 \(f_{i_1} = f_1 = 1\)，此时出现重复的 1。设最大的 \(m\) 满足 \(i_j = j\)（即 \(i_1 = 1, i_2 = 2, \ldots, i_m = m\)），且 \(i_{m+1} \ge m + 2\)。

  利用斐波那契性质 \(f_j + f_{j+1} = f_{j+2}\)，将连续的项逐对合并：

  - 若 \(m\) 为偶数：
    \[
    \begin{aligned}
    n + 1 &= 1 + (f_1 + f_2) + (f_3 + f_4) + \cdots + (f_{m-1} + f_m) + \sum_{j=m+1}^k f_{i_j} \\
    &= f_3 + f_5 + \cdots + f_{m+1} + \sum_{j=m+1}^k f_{i_j}
    \end{aligned}
    \]
    由于 \(f_{m+1} < f_{m+2} \le f_{i_{m+1}}\)（关键的不等关系保证了合并后的项互不相同且大于前面的项），所有项互异。

  - 若 \(m\) 为奇数：
    \[
    \begin{aligned}
    n + 1 &= 1 + f_1 + (f_2 + f_3) + \cdots + (f_{m-1} + f_m) + \sum_{j=m+1}^k f_{i_j} \\
    &= f_2 + f_4 + \cdots + f_{m+1} + \sum_{j=m+1}^k f_{i_j}
    \end{aligned}
    \]
    同样所有项互异。

因此 \(n+1\) 可表示为不同斐波那契数之和。由归纳法，命题对所有 \(n > 2\) 成立。

---

**方法二（强归纳法）**：

**归纳基础**：\(n = 3 = f_1 + f_2\)，成立。

**强归纳假设**：假设所有大于 2 且小于 \(n\) 的整数都可以表示为不同斐波那契数之和。

**归纳步骤**：设 \(f_k\) 是小于 \(n\) 的最大斐波那契数（由于 \(n > 2\)，\(f_k \ge 3\)）。

- 若 \(n - f_k = 1\) 或 \(2\)，则 \(n = f_k + 1\) 或 \(n = f_k + 2\)。由于 1 和 2 本身就是斐波那契数（\(f_1 = 1, f_2 = 2\)），且 \(f_k > f_2 = 2\)（因为 \(n > 3\)），所以这些斐波那契数互异。

- 若 \(n - f_k \ge 3\)，由强归纳假设，\(n - f_k\) 可表示为不同斐波那契数之和：\(n - f_k = f_{i_1} + f_{i_2} + \cdots + f_{i_t}\)。由于 \(f_k\) 是小于 \(n\) 的最大斐波那契数，所有 \(f_{i_j} < f_k\)，因此这些斐波那契数与 \(f_k\) 互异。

故 \(n = f_k + f_{i_1} + \cdots + f_{i_t}\) 是不同斐波那契数之和。

由强归纳法，命题对所有 \(n > 2\) 成立。证毕。
