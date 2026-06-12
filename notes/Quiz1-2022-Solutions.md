# DMA Quiz 1 题解 — 2022 年

## 一、判断题 (True/False) (12%)

### 题目 1a
**题目**：判断以下两个命题是否逻辑等价：  
\(p \to (\neg q \land r)\) 与 \(\neg p \lor \neg(r \to q)\)

**答案**：T

**考点**：第一章 命题逻辑（Propositional Logic）—— 逻辑等价（Logical Equivalence），蕴含律（Implication Law），德摩根律（De Morgan's Law）

**解析**：
\[\begin{aligned}
\text{LHS} &= p \to (\neg q \land r) \equiv \neg p \lor (\neg q \land r) \quad &\text{(蕴含律)}\\[4pt]
\text{RHS} &= \neg p \lor \neg(r \to q) \equiv \neg p \lor \neg(\neg r \lor q) \quad &\text{(蕴含律)}\\
&\equiv \neg p \lor (r \land \neg q) \quad &\text{(德摩根律)}
\end{aligned}\]

由于 \(\neg q \land r \equiv r \land \neg q\)（合取交换律），LHS 与 RHS 完全一致，故逻辑等价。答案为 **T**。

---

### 题目 1b
**题目**：若 \(A, B, C\) 是集合，则 \(A - (B \cap C) = (A - B) \cup (A - C)\)

**答案**：T

**考点**：第二章 集合（Sets）—— 集合运算（Set Operations），德摩根律的集合版本

**解析**：
\[\begin{aligned}
x \in A - (B \cap C) &\iff x \in A \land x \notin (B \cap C) \\
&\iff x \in A \land (x \notin B \lor x \notin C) \quad &\text{(德摩根律)}\\
&\iff (x \in A \land x \notin B) \lor (x \in A \land x \notin C) \quad &\text{(分配律)}\\
&\iff x \in (A - B) \cup (A - C)
\end{aligned}\]
由集合外延公理，两集合相等。答案为 **T**。

---

### 题目 1c
**题目**：判断以下命题是否为重言式（tautology）：\(((p \to q) \land \neg p) \to \neg q\)

**答案**：F

**考点**：第一章 命题逻辑 —— 重言式（Tautology），真值表法

**解析**：考虑赋值 \(p = \mathrm{F}, q = \mathrm{T}\)：
\[((\mathrm{F} \to \mathrm{T}) \land \neg\mathrm{F}) \to \neg\mathrm{T} = (\mathrm{T} \land \mathrm{T}) \to \mathrm{F} = \mathrm{T} \to \mathrm{F} = \mathrm{F}\]
存在使公式为假的赋值，故不是重言式。答案为 **F**。

或者化简：\(((\neg p \lor q) \land \neg p) \to \neg q \equiv \neg((\neg p \lor q) \land \neg p) \lor \neg q \equiv (p \land \neg q) \lor p \lor \neg q\)，当 \(p = \mathrm{F}, q = \mathrm{T}\) 时值为假。

---

### 题目 1d
**题目**：\(\mathrm{P}(A) = \mathrm{P}(B)\) 当且仅当 \(A = B\)，其中 \(\mathrm{P}(X)\) 是 \(X\) 的幂集

**答案**：T

**考点**：第二章 集合 —— 幂集（Power Set）

**解析**：
- (\(\Leftarrow\)) 若 \(A = B\)，则显然 \(\mathrm{P}(A) = \mathrm{P}(B)\)。
- (\(\Rightarrow\)) 若 \(\mathrm{P}(A) = \mathrm{P}(B)\)，则 \(A \in \mathrm{P}(A) = \mathrm{P}(B) \Rightarrow A \subseteq B\)。同理 \(B \subseteq A\)。故 \(A = B\)。

答案为 **T**。

---

## 二、谓词逻辑翻译 (16%)

**题目**：设变量 \(x\) 表示学生，\(y\) 表示课程，\(T(x,y)\) 表示"\(x\) 正在修 \(y\)"。将下列语句翻译为符号形式。

### 题目 2a
**题目**：没有课程被所有学生修读（No course is being taken by all students）

**答案**：\(\neg \exists y \forall x\, T(x,y)\) 或 \(\forall y \exists x\, \neg T(x,y)\)

**考点**：第一章 谓词与量词（Predicates and Quantifiers）—— 量词的翻译与否定

**解析**：
- "存在一门课程，所有学生都在修"：\(\exists y \forall x\, T(x,y)\)
- "没有……"即否定：\(\neg \exists y \forall x\, T(x,y)\)
- 等价形式：\(\forall y \neg \forall x\, T(x,y) \equiv \forall y \exists x\, \neg T(x,y)\)

---

### 题目 2b
**题目**：每个学生至少修一门课（Every student is taking at least one course）

**答案**：\(\forall x \exists y\, T(x,y)\)

**考点**：谓词与量词 —— 全称量词与存在量词的嵌套

**解析**："每个学生"对应 \(\forall x\)，"存在一门课"对应 \(\exists y\)，"正在修"即 \(T(x,y)\)。

---

### 题目 2c
**题目**：有些课程没有被任何学生修读（Some courses are being taken by no students）

**答案**：\(\exists y \forall x\, \neg T(x,y)\)

**考点**：谓词与量词 —— 量词的翻译

**解析**："存在课程 \(y\)，使得对所有学生 \(x\)，\(x\) 没有在修 \(y\)"。

---

### 题目 2d
**题目**：没有学生修读所有课程（No student is taking all courses）

**答案**：\(\neg \exists x \forall y\, T(x,y)\) 或 \(\forall x \exists y\, \neg T(x,y)\)

**考点**：谓词与量词 —— 量词的翻译与否定

**解析**：
- "存在学生修读所有课程"：\(\exists x \forall y\, T(x,y)\)
- "没有"即否定：\(\neg \exists x \forall y\, T(x,y)\)
- 等价形式：\(\forall x \exists y\, \neg T(x,y)\)

---

## 三、命题等价变换 (12%)

### 题目 3a
**题目**：写出一个与 \(p \lor \neg q\) 等价的命题，只使用 \(p, q, \neg\) 和联结词 \(\land\)（4%）

**答案**：\(\neg (\neg p \land q)\)

**考点**：第一章 命题逻辑 —— 联结词归约，德摩根律

**解析**：
\[p \lor \neg q \equiv \neg(\neg p \land \neg\neg q) \equiv \neg(\neg p \land q)\]
应用德摩根律：\(\neg(A \land B) \equiv \neg A \lor \neg B\)，取 \(A = \neg p, B = q\) 即得。

---

### 题目 3b
**题目**：写出一个与 \(p \land q\) 等价的命题，只使用 \(p, q\) 和联结词 \(|\)（NAND，与非）（8%）

**答案**：\((p \mid q) \mid (p \mid q)\)

**考点**：第一章 命题逻辑 —— 功能完全联结词（Functional Completeness），NAND

**解析**：由定义 \(p \mid q \equiv \neg(p \land q)\)。利用 NAND 可以构造非和合取：
- \(\neg p \equiv p \mid p\)（因为 \(p \mid p \equiv \neg(p \land p) \equiv \neg p\)）
- \(p \land q \equiv \neg(p \mid q) \equiv (p \mid q) \mid (p \mid q)\)

---

## 四、主析取范式与主合取范式 (16%)

**题目**：有一个包含三个变量 \(p, q, r\) 的命题公式，在最多一个变量为真时取真，否则取假。
- (a) 表达为全析取范式（full DNF）（8%）
- (b) 表达为全合取范式（full CNF）（8%）

**答案**：
- (a) \((\neg p \land \neg q \land \neg r) \lor (p \land \neg q \land \neg r) \lor (\neg p \land q \land \neg r) \lor (\neg p \land \neg q \land r)\)
- (b) \((p \lor q \lor \neg r) \land (p \lor \neg q \lor r) \land (\neg p \lor q \lor r) \land (p \lor q \lor r)\)

**考点**：第一章 命题逻辑 —— 主析取范式（DNF）、主合取范式（CNF）

**解析**：

公式为真的情况（0 或 1 个变量为真）：

| \(p\) | \(q\) | \(r\) | 取值 | 极小项 |
|:---:|:---:|:---:|:---:|:---:|
| F | F | F | T | \(\neg p \land \neg q \land \neg r\) |
| T | F | F | T | \(p \land \neg q \land \neg r\) |
| F | T | F | T | \(\neg p \land q \land \neg r\) |
| F | F | T | T | \(\neg p \land \neg q \land r\) |

**(a) 全 DNF**：将所有极小项析取即得：
\[(\neg p \land \neg q \land \neg r) \lor (p \land \neg q \land \neg r) \lor (\neg p \land q \land \neg r) \lor (\neg p \land \neg q \land r)\]

公式为假的情况（2 或 3 个变量为真）：

| \(p\) | \(q\) | \(r\) | 取值 | 极大项 |
|:---:|:---:|:---:|:---:|:---:|
| T | T | F | F | \(\neg p \lor \neg q \lor r\) |
| T | F | T | F | \(\neg p \lor q \lor \neg r\) |
| F | T | T | F | \(p \lor \neg q \lor \neg r\) |
| T | T | T | F | \(\neg p \lor \neg q \lor \neg r\) |

**(b) 全 CNF**：将所有极大项合取得：
\[(\neg p \lor \neg q \lor r) \land (\neg p \lor q \lor \neg r) \land (p \lor \neg q \lor \neg r) \land (\neg p \lor \neg q \lor \neg r)\]

---

## 五、集合分配律的推广 (12%)

**题目**：证明分配律 \(A_1 \cap (A_2 \cup \cdots \cup A_n) = (A_1 \cap A_2) \cup \cdots \cup (A_1 \cap A_n)\) 对所有 \(n > 2\) 成立。

**考点**：第二章 集合 —— 集合运算分配律，数学归纳法

**解析**：

**方法一（元素法）**：
\[
\begin{aligned}
x \in A_1 \cap (A_2 \cup \cdots \cup A_n)
&\iff x \in A_1 \land x \in (A_2 \cup \cdots \cup A_n) \\
&\iff x \in A_1 \land (x \in A_2 \lor \cdots \lor x \in A_n) \\
&\iff (x \in A_1 \land x \in A_2) \lor \cdots \lor (x \in A_1 \land x \in A_n) \\
&\iff x \in (A_1 \cap A_2) \cup \cdots \cup (A_1 \cap A_n)
\end{aligned}
\]

**方法二（数学归纳法）**：

归纳基础：\(n = 2\) 时，\(A_1 \cap (A_2 \cup A_3) = (A_1 \cap A_2) \cup (A_1 \cap A_3)\) 是集合的基本分配律，成立。

归纳假设：设 \(n = k\) (\(k \ge 2\)) 时命题成立。

归纳步骤（\(n = k + 1\)）：
\[
\begin{aligned}
A_1 \cap (A_2 \cup \cdots \cup A_k \cup A_{k+1})
&= A_1 \cap ((A_2 \cup \cdots \cup A_k) \cup A_{k+1}) \\
&= (A_1 \cap (A_2 \cup \cdots \cup A_k)) \cup (A_1 \cap A_{k+1}) \quad &\text{(基本分配律)}\\
&= ((A_1 \cap A_2) \cup \cdots \cup (A_1 \cap A_k)) \cup (A_1 \cap A_{k+1}) \quad &\text{(归纳假设)}\\
&= (A_1 \cap A_2) \cup \cdots \cup (A_1 \cap A_k) \cup (A_1 \cap A_{k+1})
\end{aligned}
\]
由数学归纳法，命题对所有 \(n > 2\) 成立。

---

## 六、Cantor 对角线法 (12%)

**题目**：改编 Cantor 对角线论证，证明 \((0,1)\) 中十进制表示只由 0 和 1 组成的正实数集合是不可数的。

**考点**：第二章 集合的基数（Cardinality of Sets）—— Cantor 对角线论证，不可数集

**解析**：

设 \(S = \{ r \in (0,1) \mid r\text{ 的十进制表示中只包含数码 0 和 1} \}\)。

假设 \(S\) 是可数的，则可以将 \(S\) 中的所有数排成一个序列 \(r_1, r_2, r_3, \ldots\)。

将每个 \(r_i\) 写成十进制小数形式：
\[
r_1 = 0.a_{11}a_{12}a_{13}\cdots \\
r_2 = 0.a_{21}a_{22}a_{23}\cdots \\
r_3 = 0.a_{31}a_{32}a_{33}\cdots \\
\vdots
\]
其中每个 \(a_{ij} \in \{0, 1\}\)。

构造一个新数 \(r = 0.b_1b_2b_3\cdots\)，其中
\[
b_i = \begin{cases}
1 & \text{若 } a_{ii} = 0 \\
0 & \text{若 } a_{ii} = 1
\end{cases}
\]

即 \(b_i = 1 - a_{ii}\)（在二进制意义下的"翻转"）。

那么 \(r \in S\)（因为每位都是 0 或 1），但 \(r\) 与每个 \(r_i\) 都在第 \(i\) 位上不同，所以 \(r \notin \{r_1, r_2, r_3, \ldots\}\)，与假设矛盾。

因此 \(S\) 是不可数的。

> 注意：这里需要处理 0.01111... = 0.1000... 的表示歧义问题。但因为我们限制只使用 0 和 1，且构造的 \(r\) 也不是有限小数（无限不循环），所以表示是唯一的。

---

## 七、算法复杂度分析 (8%)

### 题目 7a
**题目**：求打印集合 \(\{1, 2, \ldots, n\}\) 的所有三元子集的算法的复杂度（用最佳 Big-O 表示）（4%）

**答案**：\(O(n^3)\)

**考点**：第三章 算法复杂度（Complexity of Algorithms）—— Big-O 记号

**解析**：三元子集的个数为：
\[\binom{n}{3} = \frac{n(n-1)(n-2)}{6} = \frac{n^3 - 3n^2 + 2n}{6} = O(n^3)\]
打印每个子集的时间是常数，因此总复杂度为 \(O(n^3)\)。

---

### 题目 7b
**题目**：线性查找在最佳情况下的比较次数（对规模为 \(n\) 的列表）（4%）

**答案**：\(O(1)\)

**考点**：第三章 算法复杂度 —— Big-O 记号，最佳情况分析

**解析**：线性查找的最佳情况是目标元素恰好是列表的第一个元素，只需要 1 次比较即结束。因此复杂度为 \(O(1)\)（常数时间）。

---

## 八、数学归纳法 (12%)

**题目**：用数学归纳法证明 \(n^{n+1} > (n+1)^n\) 对所有正整数 \(n \ge 3\) 成立。

（注：试卷原题写为 \(n \le 3\)，但该不等式实际对 \(n = 1, 2\) 不成立，应为 \(n \ge 3\) 的笔误。）

**考点**：第五章 数学归纳法（Mathematical Induction）—— 不等式归纳证明

**解析**：

**归纳基础**：\(n = 3\)：
\[3^{4} = 81 > 4^{3} = 64\]
成立。

**归纳假设**：设 \(n = k\)（\(k \ge 3\)）时成立，即 \(k^{k+1} > (k+1)^k\)。

**归纳步骤**：需证 \((k+1)^{k+2} > (k+2)^{k+1}\)。

由归纳假设：
\[k^{k+1} > (k+1)^k \iff k > \left(\frac{k+1}{k}\right)^k = \left(1 + \frac{1}{k}\right)^k\]

已知数列 \(\left(1 + \frac{1}{n}\right)^n\) 单调递增且收敛到 \(e < 3\)。因此对 \(k \ge 3\)：
\[\left(1 + \frac{1}{k}\right)^k < e < 3 \le k\]

于是：
\[
(k+1)^{k+2} = (k+1) \cdot (k+1)^{k+1} 
= (k+1) \cdot (k+1)^k \cdot (k+1)
\]

也可以间接证明：

考虑比率：
\[
\frac{(k+1)^{k+2}}{(k+2)^{k+1}} = (k+1) \cdot \left(\frac{k+1}{k+2}\right)^{k+1} = (k+1) \cdot \left(1 - \frac{1}{k+2}\right)^{k+1}
\]

由归纳假设和伯努利不等式或已知的单调性可证该比率 \(> 1\)。具体地：

因为序列 \(\left(1 + \frac{1}{n}\right)^n\) 单调递增趋于 \(e\)，所以：
\[\left(1 + \frac{1}{k+1}\right)^{k+1} > \left(1 + \frac{1}{k}\right)^k\]

但我们需要比较的是 \((1 - \frac{1}{k+2})^{k+1}\)。利用不等式：
\[\left(1 - \frac{1}{m}\right)^{m-1} > \frac{1}{e} \text{ 对 } m > 1\]

代入 \(m = k+2\)：\(\left(1 - \frac{1}{k+2}\right)^{k+1} > \frac{1}{e}\)

所以：
\[
(k+1) \cdot \left(1 - \frac{1}{k+2}\right)^{k+1} > (k+1) \cdot \frac{1}{e} > \frac{k+1}{3} \ge \frac{4}{3} > 1
\]

故 \((k+1)^{k+2} > (k+2)^{k+1}\) 成立。

由数学归纳法，\(n^{n+1} > (n+1)^n\) 对所有 \(n \ge 3\) 成立。
