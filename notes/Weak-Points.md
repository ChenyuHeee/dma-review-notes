# DMA 薄弱点记录

> 6/22 摸底暴露 → 6/27 逐个消灭 → 6/28 考试

---

## 今日消灭计划（6/27）

```
09:00-10:30  [1] Ch9 Relations        整章 2h
10:30-12:00  [2] Ch4 Number Theory     Euclidean+Bézout+CRT+Fermat 1.5h
12:00-13:00  午饭
13:00-14:00  [3] Ch11 Trees           Huffman+Prim+Kruskal 1h
14:00-15:00  [4] Ch10 Graphs          平面图/色数/Euler/Hamilton 1h
15:00-15:30  [5] Ch8 Recurrence       通解+生成函数+derangement 0.5h
15:30-16:00  [6] Ch2+Ch3              术语+Big-O 0.5h
16:00-16:30  [7] Ch1 Logic            NAND+CNF/DNF 0.5h
16:30-17:30  [8] 真题实战            做一套 Quiz3 或 Quiz4
17:30-18:30  晚饭
18:30-20:00  [9] 错题回顾+公式默写   1.5h
20:00-21:00  [10] 快速过所有笔记     扫一遍防遗忘
```

---

## 2026-06-22 摸底卷暴露问题

### 🔴 Ch9 Relations — 整章空白

- **Q17**: 不认识 equivalence relation（等价关系），不认识 partition（划分）
- **Q18**: 忘记 symmetric / transitive / reflexive 的定义
- **Q33**: 不知道 partial order, Hasse diagram, maximal/minimal/maximum/minimum, lattice

| 知识点 | 对应笔记 | 消灭? |
|--------|---------|:--:|
| Relations, reflexive/symmetric/antisymmetric/transitive | Ch09-9.1 | ⬜ |
| Representing relations, closures | Ch09-9.2, 9.3, 9.4 | ⬜ |
| Equivalence relations, partitions | Ch09-9.5 | ⬜ |
| Partial order, Hasse diagram, lattice | Ch09-9.6 | ⬜ |

### 🔴 Ch4 Number Theory — Euclidean 算法空白

- **Q29**: 不知道 Euclidean algorithm 和 Bézout coefficients

| 知识点 | 对应笔记 | 消灭? |
|--------|---------|:--:|
| Divisibility, modular arithmetic | Ch04-4.1 | ⬜ |
| Euclidean algorithm, Bézout's theorem | Ch04-4.3 | ⬜ |
| Chinese Remainder Theorem | Ch04-4.4 | ⬜ |
| Fermat's Little Theorem, RSA | Ch04-4.4, 4.5 | ⬜ |

### 🔴 Ch11 Trees — Huffman 完全不会

- **Q35**: 完全不知道 Huffman coding

| 知识点 | 对应笔记 | 消灭? |
|--------|---------|:--:|
| Tree basics, rooted trees | Ch11-11.1 | ⬜ |
| Huffman coding | Ch11-11.2 | ⬜ |
| Tree traversal (pre/in/post order) | Ch11-11.3 | ⬜ |
| Spanning trees, Prim, Kruskal | Ch11-11.4, 11.5 | ⬜ |

### 🟡 Ch10 Graphs — 术语遗忘

- **Q19**: 忘记 planar graph（平面图，Euler 公式 $r=e-v+2$，$e\le 3v-6$）
- **Q21**: 不知道 chromatic number（色数 $\chi(G)$，四色定理）
- **Q20/Q34**: Euler circuit / Euler path / Hamilton circuit 判定会但会算错度数

| 知识点 | 对应笔记 | 消灭? |
|--------|---------|:--:|
| Planar graphs, Euler's formula, $K_5$/$K_{3,3}$ | Ch10-10.7 | ⬜ |
| Graph coloring, chromatic number | Ch10-10.8 | ⬜ |
| Euler/Hamilton 判定（练 3 道题） | Ch10-10.5 | ⬜ |

### 🟡 Ch8 Recurrence — 通解形式遗忘

- **Q15**: roots 不知道有什么用 → $a_n = αr_1^n + βr_2^n$
- **Q16**: 不认识 derangements（错排 $D_n \approx n!/e$）
- **Q32**: 求出 roots 后忘记通解形式

| 知识点 | 对应笔记 | 消灭? |
|--------|---------|:--:|
| Linear homogeneous RR, characteristic eqn | Ch08-8.2, 8.3 | ⬜ |
| Nonhomogeneous RR, divide-and-conquer | Ch08-8.4 | ⬜ |
| Generating functions | Ch08-8.5 | ⬜ |
| Derangements, inclusion-exclusion | Ch08-8.6 | ⬜ |

### 🟡 Ch2 + Ch3 — 英文术语不熟

- **Q4**: $|A|$ = cardinality（集合元素个数）
- **Q5**: injective = 单射, surjective = 满射, bijective = 双射
- **Q7**: O = 上界, Ω = 下界, Θ = 紧界, o = 严格上界

| 知识点 | 对应笔记 | 消灭? |
|--------|---------|:--:|
| Functions, injective/surjective/bijective | Ch02-2.3 | ⬜ |
| Cardinality, countability | Ch02-2.5 | ⬜ |
| Big-O / Big-Ω / Big-Θ / little-o | Ch03-3.2 | ⬜ |

### 🟡 Ch1 Logic — 特殊符号

- **Q26**: 不知道 NAND = `|`, XOR = `⊕`
- 需要复习：NAND/NOR 表达、Full CNF/DNF 计算

| 知识点 | 对应笔记 | 消灭? |
|--------|---------|:--:|
| NAND/NOR, CNF/DNF, minterm/maxterm | Ch01-1.3 | ⬜ |

### 🟢 次优先

| 知识点 | 对应笔记 | 消灭? |
|--------|---------|:--:|
| Well-ordering principle | Ch05-5.2 | ⬜ |
| Strong induction form | Ch05-5.2 | ⬜ |
| Pigeonhole principle | Ch05-5.2 | ⬜ |
| Counting formulas P(n,r), C(n,r) | Ch06-6.3 | ⬜ |
| Network Flow, Ford-Fulkerson | Network-Flow | ⬜ |

---

## 消灭记录

| 日期 | 消灭项 | 验证方式 |
|------|--------|---------|
| 6/22 | 摸底卷 35 题对答案 | 单次 |
| | | |
