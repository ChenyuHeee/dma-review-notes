# DMA 摸底卷 — 详细题解

---

## Part 1: True/False 解析

### Ch1

**Q1 (F)** . $\forall x \exists y$ 和 $\exists y \forall x$ 一般不可交换。反例：$P(x,y)$ = "$x < y$"，论域 $\mathbb{N}$。$\forall x \exists y (x < y)$ 为真（每个数都有更大的数），但 $\exists y \forall x (x < y)$ 为假（不存在比所有数都大的数）。

**Q2 (T)** . 量词否定：$\neg \forall x (P \to Q) \equiv \exists x \neg (P \to Q) \equiv \exists x \neg (\neg P \lor Q) \equiv \exists x (P \land \neg Q)$。

**Q3 (T)** . 左边 $\equiv (\neg p \lor q) \land (\neg p \lor r) \equiv \neg p \lor (q \land r) \equiv p \to (q \land r) =$ 右边。

### Ch2

**Q4 (T)** . 笛卡尔积基数 = 两个集合基数的乘积，这是组合数学基本结论。

**Q5 (T)** . $f$ injective: $f(x)=f(y) \Rightarrow x=y$. $g$ injective: $g(u)=g(v) \Rightarrow u=v$. Then $(g \circ f)(x) = (g \circ f)(y) \Rightarrow g(f(x)) = g(f(y)) \Rightarrow f(x) = f(y) \Rightarrow x = y$。

**Q6 (T)** . 所有有限子集 = $\bigcup_{n=0}^{\infty} \mathcal{P}_n(\mathbb{N})$，每个 $\mathcal{P}_n$ 与 $\mathbb{N}^n$ 的一个子集等势，可数个可数集的并仍是可数的。

### Ch3

**Q7 (T)** . $f(n) = 3n^2 + 2n + 1 \le 3n^2 + 2n^2 + n^2 = 6n^2$ for $n \ge 1$，且 $f(n) \ge 3n^2$，所以 $f(n) = \Theta(n^2)$。

**Q8 (F)** . $n!$ 的增长比任何指数函数 $c^n$ 都快（Stirling 公式：$n! \sim \sqrt{2\pi n}(n/e)^n$）。所以 $n! = \Omega(2^n)$ 而非 $O(2^n)$。

### Ch4

**Q9 (T)** . 同余式的基本性质：$a \equiv b \pmod{m} \iff a = b + km$，$c \equiv d \pmod{m} \iff c = d + \ell m$，相乘 $(b+km)(d+\ell m) = bd + m(b\ell + dk + k\ell m)$，所以 $ac \equiv bd \pmod{m}$。

**Q10 (T)** . gcd 和 lcm 的基本关系，由素因子分解 $\gcd = \prod p^{\min(e,f)}$, $\operatorname{lcm} = \prod p^{\max(e,f)}$，乘积 = $\prod p^{e+f} = ab$。

### Ch5

**Q11 (T)** . 良序原理（$\mathbb{N}$ 的每个非空子集有最小元）与数学归纳法原理等价。

**Q12 (T)** . 强归纳法的定义：假设 $P(1), P(2), \dots, P(k)$ 都成立来证明 $P(k+1)$，而非只假设 $P(k)$。

### Ch6

**Q13 (T)** . $P(n,r) = n!/(n-r)!$, $C(n,r) = n!/(r!(n-r)!)$，所以 $C(n,r) = P(n,r)/r!$。

**Q14 (T)** . 13 个人分配到 12 个月 = 鸽巢原理的标准例子。

### Ch8

**Q15 (T)** . 特征方程 $r^2 - 3r + 2 = 0$，$(r-1)(r-2) = 0$，$r = 1, 2$。

**Q16 (T)** . $D_n = n! \sum_{i=0}^{n} (-1)^i / i! \approx n!/e$。

### Ch9

**Q17 (T)** . 等价关系 → 等价类 → 划分。这是等价关系和划分的一一对应定理。

**Q18 (F)** . 对称+传递不能推出自反。反例：$R = \emptyset$ 在 $A = \{1,2\}$ 上。$R$ 对称且传递（vacuously true），但不自反（$(1,1) \notin R$）。

### Ch10

**Q19 (F)** . $K_5$ 有 5 个顶点、10 条边。平面图的推论 $e \le 3v - 6$：$10 \le 3 \cdot 5 - 6 = 9$，不成立。所以 $K_5$ 非平面。

**Q20 (T)** . Euler 定理：连通多重图有欧拉回路 $\iff$ 所有顶点度数为偶数。

**Q21 (T)** . 二部图可以用 2 种颜色着色（每组一种），所以 $\chi \le 2$。如果至少有一条边，$\chi = 2$；如果没有边，$\chi = 1$。

**Q22 (T)** . Handshaking Theorem: $\sum \deg(v) = 2|E|$。奇度顶点度数和为奇数个奇数和 = 偶数，所以奇度顶点个数必为偶数。

### Ch11

**Q23 (T)** . 树的基本性质。

**Q24 (T)** . 满二叉树的性质：$n_0 = n_2 + 1$，其中 $n_0$ 是叶节点数，$n_2$ 是内部节点数。

### Network Flow

**Q25 (T)** . Max-Flow Min-Cut Theorem 的核心陈述。

---

## Part 2: 详解

### Q26 — NAND 表达 XOR

**解**：

$p \oplus q \equiv (p \land \neg q) \lor (\neg p \land q)$（XOR 定义）

利用 NAND 的性质：
- $\neg x \equiv x \mid x$
- $x \land y \equiv \neg(x \mid y) \equiv (x \mid y) \mid (x \mid y)$

所以：
$$\begin{aligned}
p \oplus q &\equiv \neg(\neg(p \land \neg q) \land \neg(\neg p \land q)) \\
&\equiv (p \land \neg q) \mid (\neg p \land q) \quad\text{(最外层 NAND = $\neg$(AND))}\\
&\equiv \big(p \mid (q \mid q)\big) \mid \big((p \mid p) \mid q\big)
\end{aligned}$$

**快捷记法**：$p \oplus q \equiv (p \mid (q \mid q)) \mid ((p \mid p) \mid q)$

---

### Q27 — 对称差与幂集

(a) $A \oplus B = (A - B) \cup (B - A) = \{1\} \cup \{4\} = \{1, 4\}$

(b) $A \cap B = \{2, 3\}$，$\mathcal{P}(\{2, 3\}) = \{\emptyset, \{2\}, \{3\}, \{2, 3\}\}$

---

### Q28 — 函数增长率排序

$n^{1/\log n}$：注意到 $\log_n n = 1$，$n^{1/\log n} = n^{\log_n 2} = 2$。实际上 $n^{1/\log_2 n} = 2$ 是常数！

排序（慢→快）：
$$n^{1/\log n} \quad\text{(常数)} < (\log n)^2 < n\log n < n^2 < 2^n < n!$$

---

### Q29 — 欧几里得算法

**(a)**

$$\begin{aligned}
252 &= 1 \cdot 198 + 54 \\
198 &= 3 \cdot 54 + 36 \\
54 &= 1 \cdot 36 + 18 \\
36 &= 2 \cdot 18 + 0
\end{aligned}$$

最后非零余数：$\gcd(252, 198) = 18$

**(b)** 回代求 Bézout 系数：

$$\begin{aligned}
18 &= 54 - 1 \cdot 36 \\
36 &= 198 - 3 \cdot 54 \\
54 &= 252 - 1 \cdot 198
\end{aligned}$$

代入：
$$\begin{aligned}
18 &= 54 - 1 \cdot (198 - 3 \cdot 54) = 4 \cdot 54 - 1 \cdot 198 \\
&= 4 \cdot (252 - 1 \cdot 198) - 1 \cdot 198 \\
&= 4 \cdot 252 - 5 \cdot 198
\end{aligned}$$

所以 $18 = 4 \cdot 252 - 5 \cdot 198$（$s = 4, t = -5$）

---

### Q30 — 归纳法证奇数求和

**Basis Step** ($n=1$)：$\sum_{i=1}^{1} (2i-1) = 1 = 1^2$ ✓

**Inductive Hypothesis**：假设 $\sum_{i=1}^{k} (2i-1) = k^2$ 成立。

**Inductive Step** ($n=k+1$)：
$$\begin{aligned}
\sum_{i=1}^{k+1} (2i-1) &= \sum_{i=1}^{k} (2i-1) + (2(k+1) - 1) \\
&= k^2 + (2k + 1) \quad\text{(by IH)}\\
&= (k+1)^2
\end{aligned}$$

证毕。$\square$

---

### Q31 — 字符串计数

**(a)** 容斥原理：总数 - 不含 'a' 的 = $26^4 - 25^4 = 456976 - 390625 = 66351$

**(b)** $P(26, 4) = 26 \cdot 25 \cdot 24 \cdot 23 = 358800$

**(c)** 第一位：5 种（元音），第四位：21 种（辅音），中间两位：$26^2$。
$5 \cdot 21 \cdot 26^2 = 105 \cdot 676 = 70980$

---

### Q32 — 解齐次线性递推

特征方程：$r^2 - 5r + 6 = 0$，$(r-2)(r-3) = 0$，$r = 2, 3$

通解：$a_n = \alpha \cdot 2^n + \beta \cdot 3^n$

代入初始条件：
$$\begin{aligned}
n=0&: \alpha + \beta = 2 \\
n=1&: 2\alpha + 3\beta = 7
\end{aligned}$$

解得：$\alpha = -1 + 2 = 3$？重新算：
$\beta = 2 - \alpha$，$2\alpha + 3(2-\alpha) = 7 \Rightarrow 2\alpha + 6 - 3\alpha = 7 \Rightarrow -\alpha = 1 \Rightarrow \alpha = -1$? 

等一等：$2\alpha + 6 - 3\alpha = 7 \Rightarrow -\alpha + 6 = 7 \Rightarrow -\alpha = 1 \Rightarrow \alpha = -1$，$\beta = 2 - (-1) = 3$。

校验：$n=0$: $-1+3=2$ ✓, $n=1$: $2(-1)+3(3)=-2+9=7$ ✓

所以 $a_n = -2^n + 3 \cdot 3^n = 3 \cdot 3^n - 2^n = 3^{n+1} - 2^n$

---

## Part 3: 详解

### Q33 — 偏序关系

**(a)** 自反：$a \mid a$ 对任意 $a \in A$ 成立 ✓
反对称：若 $a \mid b$ 且 $b \mid a$ 则 $a = b$ ✓
传递：若 $a \mid b$ 且 $b \mid c$ 则 $a \mid c$ ✓
所以 $R$ 是偏序。

**(b)** Hasse 图（省略传递边和自环边）：

```
       12
      /  \
     6    4
    / \   |
   2   3  |
    \ /   |
     1 ---┘
```

实际上：1→2→6→12, 1→3→6, 1→4→12, 1→2→4→12

```
        12
       /  \
      6    4
     / \   /
    2   3 /
     \ / /
      1
```

**(c)** 极大元 = {12}（没有元素能整除 12 或 4 或 6 之后得到更大值... wait. 极大元：没有其他元素"大于"它。12 是唯一极大元，因为 $12 \mid a \Rightarrow a = 12$）。实际上 4 和 6 呢？$4 \mid 12$ 所以 12 > 4，4 不是极大元。极大元 = {12}。最大元 = 12。

极小元：没有其他元素"小于"它。1 是唯一极小元。最小元 = 1。

**(d)** 在 $(A, \mid)$ 中，任意两个元素 $a, b$：
$\operatorname{lub}(a, b) = \operatorname{lcm}(a, b)$，$\operatorname{glb}(a, b) = \gcd(a, b)$。

A = {1, 2, 3, 4, 6, 12} 对 lcm/gcd 封闭：任意两个元素的 lcm 和 gcd 都在 A 中吗？
- $\operatorname{lcm}(4, 6) = 12 \in A$ ✓
- $\operatorname{lcm}(3, 4) = 12 \in A$ ✓
- $\operatorname{gcd}(4, 6) = 2 \in A$ ✓

所有组合的 lcm 和 gcd 都在 A 中！所以是 lattice。事实上 $(\{正因子\}, \mid)$ 总是 lattice。

---

### Q34 — 图论综合

**(a) Dijkstra 算法**（图：A=0 起点）

```
     2      1      5      2      3
  A --- C --- B --- D --- E --- F
   \         \               /
    4         8             6
     \         \           /
      +---------+---------+
```

实际上边是：
A-B:4, A-C:2, B-C:1, B-D:5, C-D:8, C-E:10, D-E:2, D-F:6, E-F:3

| Step | 已确定 | A | B | C | D | E | F |
|:--:|--------|:--:|:--:|:--:|:--:|:--:|:--:|
| 0 | — | 0 | ∞ | ∞ | ∞ | ∞ | ∞ |
| 1 | A | **0** | 4 | 2 | ∞ | ∞ | ∞ |
| 2 | C | 0 | 3₁ | **2** | 10 | 12 | ∞ |
| 3 | B | 0 | **3₁** | 2 | 8₂ | 12 | ∞ |
| 4 | D | 0 | 3₁ | 2 | **8₂** | 10₃ | 14₄ |
| 5 | E | 0 | 3₁ | 2 | 8₂ | **10₃** | 13₅ |
| 6 | F | 0 | 3₁ | 2 | 8₂ | 10₃ | **13₅** |

最短路径：A → C → B → D → E → F，长度 = 2 + 1 + 5 + 2 + 3 = **13**

路径标记：A→C (2), C→B 通过 B=3 (via C-B=1), B→D=8 (via B-D=5), D→E=10 (via D-E=2), E→F=13 (via E-F=3)

**(b)**

度数：deg(A)=2, deg(B)=3, deg(C)=3, deg(D)=3, deg(E)=3, deg(F)=2

- **Euler circuit?** 有 4 个奇度顶点（B,C,D,E）→ 不存在 Euler circuit。
- **Euler path?** 要求恰好 2 个奇度顶点 → 不存在。
- **Hamilton circuit?** Dirac 定理：$\deg(v) \ge 3 \ge 6/2 = 3$，刚好满足 Dirac 条件！所以存在 Hamilton circuit。一条路径：A → B → D → F → E → C → A（验证：A-B, B-D, D-F, F-E, E-C, C-A，全部是图中的边 ✓）

---

### Q35 — Huffman 编码

**(a)** 频率：A=0.15, B=0.25, C=0.05, D=0.20, E=0.10, F=0.25

合并过程（每次选频率最小的两个）：

| Step | 合并 | 新节点频率 |
|:--:|------|:--:|
| 1 | C(0.05) + E(0.10) | CE = 0.15 |
| 2 | A(0.15) + CE(0.15) | A-CE = 0.30 |
| 3 | D(0.20) + B(0.25) | D-B = 0.45... 等等，B=0.25, D=0.20, F=0.25。最小两个是 D(0.20) + F(0.25)？不对，B(0.25)=F(0.25)=D(0.20)，最小是 D(0.20) + B(0.25)? 实际是 D(0.20) < F(0.25)=B(0.25)。取 D(0.20) 和 F(0.25) |
| 3 | D(0.20) + F(0.25) | DF = 0.45 |
| 4 | A-CE(0.30) + B(0.25) | A-CE-B = 0.55 |
| 5 | A-CE-B(0.55) + DF(0.45) | ROOT = 1.00 |

编码（左=0, 右=1，从根向叶走）：
```
ROOT
├── 0: A-CE-B (0.55)
│   ├── 0: B (0.25)          → B: 00
│   └── 1: A-CE (0.30)
│       ├── 0: A (0.15)      → A: 010
│       └── 1: CE (0.15)
│           ├── 0: C (0.05)  → C: 0110
│           └── 1: E (0.10)  → E: 0111
└── 1: DF (0.45)
    ├── 0: D (0.20)          → D: 10
    └── 1: F (0.25)          → F: 11
```

| 符号 | 编码 | 长度 |
|:--:|------|:--:|
| B | 00 | 2 |
| D | 10 | 2 |
| F | 11 | 2 |
| A | 010 | 3 |
| C | 0110 | 4 |
| E | 0111 | 4 |

**(b)** 平均比特数：
$$2 \cdot (0.25+0.20+0.25) + 3 \cdot 0.15 + 4 \cdot (0.05+0.10) = 2 \cdot 0.70 + 3 \cdot 0.15 + 4 \cdot 0.15 = 1.40 + 0.45 + 0.60 = 2.45$$

**(c)** 定长编码：6 个符号需要 $\lceil \log_2 6 \rceil = 3$ bits。Huffman 节省了 $(3 - 2.45)/3 \approx 18.3\%$。
