# DMA 薄弱点记录

> 持续更新，考前逐条消灭

---

## 2026-06-22 摸底卷暴露问题

### 🔴 Ch9 Relations — 整章空白

- **Q17**: 不认识 equivalence relation（等价关系），不认识 partition（划分）
  - 已补：等价关系 = reflexive + symmetric + transitive，等价类构成划分
- **Q18**: 忘记 symmetric / transitive / reflexive 的定义
  - 已补：Reflexive = 每个元素和自己有关系；Symmetric = 如果 aRb 则 bRa；Transitive = 如果 aRb 且 bRc 则 aRc
- **Q33**: 不知道 partial order, Hasse diagram, maximal/minimal/maximum/minimum, lattice
  - 已补：偏序 = reflexive + antisymmetric + transitive；Hasse 图 = 省略传递边和自环的偏序图
  - ⚠️ 需要专门做几道偏序/Hasse 图/格的练习题

### 🔴 Ch4 Number Theory — Euclidean 算法空白

- **Q29**: 不知道 Euclidean algorithm 和 Bézout coefficients
  - 已补：辗转相除法 + 回代求线性组合
  - ⚠️ 需要练习 Chinese Remainder Theorem 和 Fermat's Little Theorem

### 🔴 Ch11 Trees — Huffman 完全不会

- **Q35**: 完全不知道 Huffman coding
  - 已补：贪心合并最小频率、生成二叉树、编码规则
  - ⚠️ 需要同时复习 Prim / Kruskal / 遍历

### 🟡 Ch10 Graphs — 术语遗忘

- **Q19**: 忘记 planar graph（平面图）
  - 已补：$e \le 3v-6$ 判定，$K_5$ 和 $K_{3,3}$ 非平面
- **Q21**: 不知道 chromatic number（色数）
  - 已补：$\chi(G)$，四色定理，常见图的色数
- **Q20**: Euler circuit 虽然记得，但 Q34(b) 做度数统计时会出错
  - ⚠️ 需要多练习 Euler/Hamilton 判定题

### 🟡 Ch8 Recurrence — 通解形式遗忘

- **Q15**: 知道要代入特征方程但不知道 roots 怎么用
  - 已补：$r^n$ 形式通解，互异根 = $αr_1^n + βr_2^n$，重根 = $(α+βn)r^n$
- **Q16**: 不认识 derangements（错排）
  - 已补：$D_n = n!\sum(-1)^i/i! \approx n!/e$
- **Q32**: 求出 roots 2,3 后忘记通解形式
  - 已补：$a_n = α·2^n + β·3^n$，代入初始条件解 α, β

### 🟡 Ch2 Sets — 英文术语不熟

- **Q4**: 不认识竖线绝对值符号（实际是 cardinality）
  - 已补：$|A|$ = 集合 A 的元素个数
- **Q5**: 不知道 injective 是什么
  - 已补：injective（单射）= $f(x)=f(y) \Rightarrow x=y$；surjective（满射）= 值域等于陪域；bijective（双射）= 单射 + 满射

### 🟡 Ch3 Algorithms — 渐进记号混淆

- **Q7**: Big-O / Big-Ω / Big-Θ / little-o 分不清
  - 已补：O = 上界，Ω = 下界，Θ = 紧界，o = 严格上界
  - ⚠️ 需要做增长率排序题

### 🟡 Ch1 Logic — 特殊符号不熟

- **Q26**: 不知道 NAND（与非），不认识 XOR 符号 $p \oplus q$
  - 已补：NAND = $\neg(p \land q) = p \mid q$；XOR = $(p \land \neg q) \lor (\neg p \land q)$

### 🟢 能做对但概念模糊

| 题号 | 内容 | 状态 |
|:--:|------|:--:|
| Q10 | gcd/lcm 关系 | 猜对，需补证明 |
| Q11 | Well-ordering principle | 没学过但推理正确 |
| Q12 | Strong induction | 推理正确 |
| Q14 | Pigeonhole principle | 猜出来是抽屉原理 |
| Q17-Q25 | 大量关系/图论术语 | 好多靠猜 |

---

## 复习优先级

| 优先级 | 章节 | 需补内容 | 预计时间 |
|:--:|------|------|:--:|
| 🔴 P0 | Ch9 Relations | 整章从头学 | 2h |
| 🔴 P0 | Ch4 Number Theory | Euclidean + Bézout + CRT + 费马 | 1.5h |
| 🔴 P0 | Ch11 Huffman | Huffman 编码 + Prim/Kruskal 复习 | 1h |
| 🟡 P1 | Ch10 Graphs | 平面图/色数/Euler/Hamilton 专项练 | 1h |
| 🟡 P1 | Ch8 Recurrence | 通解公式 + 生成函数 + 错排 | 1h |
| 🟡 P1 | Ch2/Ch3 | 英文术语 + Big-O 排序 | 0.5h |
| 🟢 P2 | Ch1 Logic | NAND/NOR + CNF/DNF 练题 | 0.5h |
| 🟢 P2 | Ch5/Ch6 | 归纳法模板 + 排列组合公式 | 0.5h |

---

## 消灭记录

| 日期 | 消灭项 | 验证方式 |
|------|--------|---------|
| | | |

---

> 规则：每消灭一个薄弱点，在上方表格记录。考前确保所有项都有消灭记录。
