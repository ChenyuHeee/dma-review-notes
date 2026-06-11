# Network Flow 网络流

> **考试语言**: 英文 | **概念解释**: 中文
> 本笔记覆盖: Flow network definition, Max flow problem, Min cut, Ford-Fulkerson algorithm, Residual graph, Augmenting path

---

## 1. Network Flow Definitions (网络流定义)

### 1.1 Flow Network (流网络)

A **flow network** (流网络) is a directed graph $G = (V, E)$ with:

- A **source** (源点) $s$ — where flow originates
- A **sink** (收点/汇点) $t$ — where flow terminates
- Each edge $e \in E$ has a **capacity** (容量) $c(e) \ge 0$, representing the maximum amount of flow that can pass through it

> **图示描述**: 在一个流网络中，每条边上标注的是容量值 $c(e)$。箭头方向表示允许流动的方向。源点 $s$ 只有出边，收点 $t$ 只有入边。

### 1.2 Flow (可行流)

**Definition**. An **s-t flow** (可行流) is a function $f: E \to \mathbb{R}$ that satisfies:

1. **Capacity constraint** (容量约束): For each $e \in E$:
   $$0 \le f(e) \le c(e)$$

2. **Flow conservation** (守恒约束): For each vertex $v \in V - \{s, t\}$:
   $$\sum_{e \text{ into } v} f(e) = \sum_{e \text{ out of } v} f(e)$$
   > 流入量 = 流出量（除了源点和收点）

**Definition**. The **value** of a flow $f$ is:
$$v(f) = \sum_{e \text{ out of } s} f(e)$$

即从源点 $s$ 流出的总流量。

> **特例**: **零流** (zero flow) — 所有 $f(e) = 0$，显然是一个可行流。

### 1.3 Multiple Sources or Sinks (多源点多收点)

当问题中有多个源点或多个收点时，可以通过添加一个 **supersource** (超级源点) 和一个 **supersink** (超级收点) 来转化：

- 从 supersource $s$ 到每个原始源点连一条容量为 $\infty$ 的边
- 从每个原始收点到 supersink $t$ 连一条容量为 $\infty$ 的边

> **图示描述**: 多个源点 $a, b, c$ 通过容量 $\infty$ 的边连接到新的超级源点 $s$；多个收点 $k, l$ 通过容量 $\infty$ 的边连接到新的超级收点 $t$。这样就把多源多收问题转化为标准单源单收问题。

---

## 2. Maximum Flow Problem (最大流问题)

**Max flow problem**: Find an s-t flow of maximum value.

在所有可行流中，找出流量值 $v(f)$ 最大的流。

> **图示描述**: 
> - 一个可行流示例中，每条边上有两个数字：灰色标注的是**流量** $f(e)$，黑色标注的是**容量** $c(e)$。例如边 $s \to a$ 上写有 $\frac{10}{10}$ 表示 $f=10, c=10$。
> - 随着不断调整流量分配，可以从初始流值 $v(f)=4$ 逐步增大到 $v(f)=24$，最终达到最大流 $v(f)=28$。

---

## 3. Cuts in a Graph (图中的割)

### 3.1 Definition of Cut (割的定义)

**Definition**. An **s-t cut** is a partition $(A, B)$ of $V$ with $s \in A$ and $t \in B$.

即将顶点集 $V$ 划分为两部分 $A$ 和 $B$，其中源点 $s$ 必须在 $A$ 中，收点 $t$ 必须在 $B$ 中。

**Definition**. The **capacity of a cut** (割的容量) $(A, B)$ is:
$$\text{cap}(A, B) = \sum_{e \text{ out of } A} c(e)$$

即从 $A$ 指向 $B$ 的所有边的容量之和。

> **图示描述**: 
> - 第一个割例: $A$ 包含 $s$ 及其相邻的一些顶点，从 $A$ 到 $B$ 的边容量为 $10 + 5 + 15 = 30$
> - 第二个割例: 另一个不同的划分，容量为 $9 + 15 + 8 + 30 = 62$
> - 第三个割例: 更优化的划分，容量为 $10 + 8 + 10 = 28$

### 3.2 Cap(S,T) and Flow(S,T)

对于一个割 $(A, B)$:
- **Cap(S,T)**: 从 $A$ 到 $B$ 的所有边的容量之和
- **Flow(S,T)**: 从 $A$ 到 $B$ 的净流量（流出 $A$ 的流量减去流入 $A$ 的流量）

关系: $\text{Flow}(S,T) \le \text{Cap}(S,T)$ — 净流量不可能超过割容量。

### 3.3 Minimum Cut Problem (最小割问题)

**Min s-t cut problem**: Find an s-t cut of minimum capacity.

在所有可能的 s-t 割中，找出容量最小的割。

---

## 4. Flows and Cuts — Key Lemmas (流与割的关键引理)

### 4.1 Flow Value Lemma (流值引理)

**Flow value lemma**. Let $f$ be any flow, and let $(A, B)$ be any s-t cut. Then the net flow sent across the cut is equal to the value of the flow:
$$\sum_{e \text{ out of } A} f(e) - \sum_{e \text{ in to } A} f(e) = v(f)$$

> **解释**: 对于任意一个割，从 $A$ 侧净流出的流量（流出 $A$ 减去流入 $A$）总是等于整个流的流量 $v(f)$。

**Proof**:
$$
\begin{aligned}
v(f) &= \sum_{e \text{ out of } s} f(e) \\
&= \sum_{v \in A} \left( \sum_{e \text{ out of } v} f(e) - \sum_{e \text{ in to } v} f(e) \right) \\
&= \sum_{e \text{ out of } A} f(e) - \sum_{e \text{ in to } A} f(e)
\end{aligned}
$$

- **从顶点角度**: 除了 $s$ 外，$A$ 中所有其他顶点的出入流量在求和中相互抵消
- **从边角度**: 位于 $A$ 内部的边，其出入流量在求和中相互抵消，只有 $A$ 和 $B$ 之间的边才起作用

> **图示验证**:
> - 一个 $v(f)=24$ 的流，取一个割 $(A,B)$，
> - 计算: $10 + 3 + 11 = 24$（直接从 $A$ 流出的边）
> - 或计算: $6 + 0 + 8 - 1 + 11 = 24$（考虑反向流量后净流出）

### 4.2 Weak Duality (弱对偶性)

**Weak duality**. Let $f$ be any flow, and let $(A, B)$ be any s-t cut. Then the value of the flow is at most the capacity of the cut:
$$v(f) \le \text{cap}(A, B)$$

**Proof**:
$$
v(f) = \sum_{e \text{ out of } A} f(e) - \sum_{e \text{ in to } A} f(e) \le \sum_{e \text{ out of } A} f(e) \le \sum_{e \text{ out of } A} c(e) = \text{cap}(A, B)
$$

> **直觉**: 割容量是流必须经过的"瓶颈"，流的流量不可能超过任何割的容量。

### 4.3 Certificate of Optimality (最优性凭证)

**Corollary**. Let $f$ be any flow, and let $(A, B)$ be any cut. If $v(f) = \text{cap}(A, B)$, then $f$ is a **max flow** and $(A, B)$ is a **min cut**.

> **意义**: 当我们找到一个流的流量等于某个割的容量时，我们就同时证明了该流是最大流、该割是最小割。这是最优性的充要条件。

---

## 5. Residual Graph (残差图)

### 5.1 Definition (定义)

Given a flow network $G$ with flow $f$, the **residual graph** (残差图) $G_f = (V, E_f)$ is constructed as follows:

For each original edge $e = (u, v) \in E$:
- If $f(e) < c(e)$: add a **forward edge** $e = (u, v)$ with residual capacity $c_f(e) = c(e) - f(e)$
  > 前向边：剩余容量 = 容量 - 已用流量
- If $f(e) > 0$: add a **reverse edge** $e_R = (v, u)$ with residual capacity $c_f(e_R) = f(e)$
  > 反向边：容量 = 已用流量（允许"撤销"已发送的流量）

Formally:
$$c_f(e) = \begin{cases} c(e) - f(e) & \text{if } e \in E \\ f(e) & \text{if } e_R \in E \end{cases}$$

$$E_f = \{ e : f(e) < c(e) \} \cup \{ e_R : f(e) > 0 \}$$

### 5.2 Intuition (直观理解)

残差图告诉我们**还能发送多少额外流量**以及**可以撤销多少已有流量**。

- **前向边** (forward edge): 表示还可以在原方向上发送 $c(e) - f(e)$ 单位流量
- **反向边** (reverse edge): 表示可以撤销 $f(e)$ 单位已发送的流量（即把流量"退回去"）

> **图示描述**: 
> - 原图: 从 $u$ 到 $v$ 的一条边，容量 $c$，流量 $f$，记为 $\frac{f}{c}$
> - 残差图: 拆成两条边 ——
>   - 前向边 $u \to v$，残差容量 $c - f$
>   - 反向边 $v \to u$，残差容量 $f$

---

## 6. Augmenting Path (增广路径)

### 6.1 Definition (定义)

An **augmenting path** (增广路径) is a path $P = v_1, v_2, \ldots, v_k$ in the residual graph $G_f$ where:
- $v_1 = s$ (起点是源点)
- $v_k = t$ (终点是收点)
- For each consecutive pair $(v_j, v_{j+1})$, the edge has **positive** residual capacity $c_f(v_j, v_{j+1}) > 0$

找到一条从 $s$ 到 $t$ 的路径，路径上的每条边在残差图中都有正的剩余容量。

### 6.2 Bottleneck Capacity (瓶颈容量)

The **bottleneck** of an augmenting path $P$ is:
$$b = \min_{(u,v) \in P} c_f(u, v)$$

即路径上所有边的最小残差容量，也就是通过这条路径最多能增加的流量。

---

## 7. Ford-Fulkerson Algorithm (福特-福克森算法)

### 7.1 Algorithm Description (算法描述)

**Ford-Fulkerson** (1956) is a greedy-based algorithm for finding the maximum flow.

```
Ford-Fulkerson(G, s, t, c) {
    foreach e in E
        f(e) <- 0
    Gf <- residual graph

    while (there exists augmenting path P in Gf) {
        f <- Augment(f, c, P)
        update Gf
    }
    return f
}

Augment(f, c, P) {
    b <- bottleneck(P)
    foreach e in P {
        if (e in E)              // forward edge: 前向边
            f(e) <- f(e) + b
        else                     // reverse edge: 反向边
            f(e_R) <- f(e_R) - b
    }
    return f
}
```

### 7.2 Manual Steps (手动步骤)

1. **初始化**: 所有边流量 $f(e) = 0$
2. **构建残差图**: 根据当前流量构造 $G_f$
3. **找增广路径**: 在 $G_f$ 中找一条从 $s$ 到 $t$ 的路径 $P$（每条边残差容量 $>0$）
4. **增广**: 计算瓶颈 $b$，沿 $P$ 增加 $b$ 单位流量（前向边加，反向边减）
5. **更新残差图**: 重新计算残差容量
6. **重复**: 直到残差图中不存在 $s$ 到 $t$ 的路径

> **图示描述**: 算法执行过程示例——
> - 初始所有边流量为 0
> - 第一次迭代选择某条路径，增广后流值变为 20
> - 由于贪心选择的局部最优性，可能无法直接达到全局最优
> - 但在残差图中利用反向边可以"纠正"之前的决策，最终达到最大流 30

### 7.3 Greedy vs. Ford-Fulkerson (贪心 vs. FF 算法)

- **贪心算法**: 只使用前向边，一旦选择路径就不会改变 → 可能陷入局部最优
- **Ford-Fulkerson**: 使用残差图，通过反向边允许"撤销"之前的选择 → 可以达到全局最优

> **核心洞见**: 反向边是 FF 算法的关键创新。它允许算法"反悔"之前做出的次优决策，从而保证能找到全局最大流。

---

## 8. Max-Flow Min-Cut Theorem (最大流最小割定理)

### 8.1 Statement (陈述)

**Augmenting path theorem**. Flow $f$ is a max flow iff there are **no augmenting paths** in the residual graph $G_f$.

**Max-flow min-cut theorem** (Elias-Feinstein-Shannon 1956, Ford-Fulkerson 1956). The value of the **maximum flow** equals the capacity of the **minimum cut**:
$$\max_f v(f) = \min_{(A,B)} \text{cap}(A, B)$$

即最大流的值等于最小割的容量。

### 8.2 Proof (证明)

We prove the following three statements are equivalent (TFAE):

**(i) There exists a cut $(A, B)$ such that $v(f) = \text{cap}(A, B)$.**
存在一个割的容量等于流 $f$ 的值。

**(ii) Flow $f$ is a max flow.**
$f$ 是最大流。

**(iii) There is no augmenting path relative to $f$.**
对于 $f$ 没有增广路径。

---

**(i) $\Rightarrow$ (ii):**

由弱对偶性 (Weak Duality) 的直接推论。若存在割 $(A,B)$ 使得 $v(f) = \text{cap}(A,B)$，则对于任意其他流 $f'$ 有 $v(f') \le \text{cap}(A,B) = v(f)$，所以 $f$ 是最大流。

---

**(ii) $\Rightarrow$ (iii):**

采用逆否命题证明 (contrapositive)。若存在增广路径，则我们可以沿该路径增广，得到更大的流值，因此 $f$ 不是最大流。逆否命题成立。

---

**(iii) $\Rightarrow$ (i):**

设 $f$ 是一个没有增广路径的流。定义集合 $A$ 为在残差图 $G_f$ 中从 $s$ 出发可达的所有顶点。

- $s \in A$ (显然)
- $t \notin A$ (因为没有增广路径)

令 $B = V - A$，则 $(A, B)$ 是一个 s-t 割。

对于从 $A$ 到 $B$ 的边: 在残差图中不可达，所以前向边必须是满的 ($f(e) = c(e)$)，反向边流量必须为 0 ($f(e) = 0$)。

对于从 $B$ 到 $A$ 的边: 在残差图中反向边不可达，所以 $f(e) = 0$。

因此:
$$
\begin{aligned}
v(f) &= \sum_{e \text{ out of } A} f(e) - \sum_{e \text{ in to } A} f(e) \\
&= \sum_{e \text{ out of } A} c(e) - 0 \\
&= \text{cap}(A, B)
\end{aligned}
$$

> **图示描述**: 在证明中，$A$ 集合由残差图中从 $s$ 可达的所有顶点组成。由于没有增广路径，$t$ 不在 $A$ 中。从 $A$ 到 $B$ 的所有前向边必须已满容量（否则残差图上仍有边，$B$ 中的顶点就可达了），从 $B$ 到 $A$ 的所有边流量必须为 0（否则反向边会让 $B$ 中顶点可达）。由此可推导出 $v(f) = \text{cap}(A, B)$。

### 8.3 Key Consequences (关键推论)

- **Ford-Fulkerson 算法正确性**: FF 算法找到的流使得残差图不再连通（$s$ 到 $t$ 不可达），因此由定理，该流是最大流
- **找最小割**: 先运行 FF 算法找到最大流，然后在最终残差图中，从 $s$ 出发可达的顶点集合就是最小割的 $A$ 侧
  > 找最小割的方法: 先求最大流，再在残差图中做 BFS/DFS 从 $s$ 出发找所有可达顶点，即为最小割的 $A$ 侧。

---

## 9. Performance and Improvements (性能与改进)

### 9.1 Integer Capacity Assumption (整数容量假设)

**Assumption**: All capacities are integers between 1 and $C$.

**Invariant**: Every flow value $f(e)$ and every residual capacity $c_f(e)$ remains an **integer** throughout the algorithm.

**Theorem**: The algorithm terminates in at most $v(f^*) \le nC$ iterations.
> 证明: 每次增广至少增加 1 单位流量，而最大流值不超过 $nC$。

### 9.2 Worst-Case Performance (最坏情况性能)

Ford-Fulkerson 算法的最坏情况非常糟糕，可能需要进行 $C$ 次迭代（指数级）。

> **图示描述**: 经典反例——
> - 一个简单的三角网络，$s \to u$ 容量 $C$，$s \to v$ 容量 $C$，$u \to v$ 容量 $1$，$u \to t$ 容量 $C$，$v \to t$ 容量 $C$
> - 如果每次选择的增广路径都经过中间容量为 1 的边，则每次只能增加 1 单位流量
> - 总共需要 $C$ 次增广，当 $C$ 很大时效率极低

**Q**: Is generic Ford-Fulkerson algorithm polynomial in input size ($m$, $n$, $\log C$)?
**A**: No. If max capacity is $C$, the algorithm can take $C$ iterations.

### 9.3 Integrality Theorem (整数性定理)

**Integrality theorem**. If all capacities are integers, then there exists a max flow $f$ for which every flow value $f(e)$ is an integer.

> 所有容量为整数时，存在一个最大流使得每条边上的流量也是整数。FF 算法保证输出整数流。

**Corollary**: If $C = 1$, Ford-Fulkerson runs in $O(mn)$ time.
> 当所有容量为 1 时，每次增广至少增加 1，最大流值 $\le n$，故最多 $n$ 次增广。

### 9.4 Choosing Good Augmenting Paths (选择好的增广路径)

> **重要注意**: 如果容量是**无理数** (irrational capacities)，Ford-Fulkerson 算法不保证终止！因此在选择增广路径时需要谨慎。

使用不同的策略选择增广路径可以显著改善性能:

| Strategy | Description | Time Complexity |
|----------|-------------|-----------------|
| **Max bottleneck capacity** | 选瓶颈容量最大的路径 | $O(m^2 \log C)$ |
| **Shortest path (Edmonds-Karp/Dinitz)** | 选边数最少的路径 (BFS) | $O(m^2 n)$ |
| **Blocking flow** | 在残差图中找阻塞流 | $O(mn \log n)$ |

### 9.5 Capacity Scaling (容量缩放算法)

**Intuition**: 选择瓶颈容量大的路径，每次尽可能多地增加流量。

**Algorithm** (Scaling Max-Flow):
```
Scaling-Max-Flow(G, s, t, c) {
    foreach e in E
        f(e) <- 0
    Δ <- smallest power of 2 >= C
    Gf <- residual graph

    while (Δ >= 1) {
        Gf(Δ) <- Δ-residual graph (only edges with capacity >= Δ)
        while (there exists augmenting path P in Gf(Δ)) {
            f <- Augment(f, c, P)
            update Gf(Δ)
        }
        Δ <- Δ / 2
    }
    return f
}
```

**Theorem**: The scaling max-flow algorithm finds a max flow in $O(m \log C)$ augmentations, and can be implemented to run in $O(m^2 \log C)$ time.

> **核心思想**: 先处理大容量边（$\Delta$ 较大时），确保快速增加流量；然后逐渐减小 $\Delta$，精细化调整。整体迭代次数从 $C$ 减少到 $O(\log C)$ 轮。

---

## 10. Application – Bipartite Matching (应用——二分图匹配)

### 10.1 Bipartite Graph (二分图)

A **bipartite graph** (二分图) is an undirected graph $G = (V, E)$ in which $V$ can be partitioned into two sets $V_1$ and $V_2$ such that every edge $(u, v) \in E$ implies $u \in V_1$ and $v \in V_2$ (or vice versa).

即所有边都连接两个集合之间的顶点，集合内部没有边。

### 10.2 Matching Problem (匹配问题)

- **问题**: 有 $n$ 个男人和 $m$ 个女人，已知某些配对是兼容的。最大化成功配对的数量（不允许一夫多妻或一妻多夫）
- **数学模型**: 在二分图中找到最大匹配 (maximum matching)，即最多的边数，使得没有两条边共享顶点

### 10.3 Solution Using Max Flow (用最大流求解)

将二分图匹配问题转化为最大流问题：

**Construction**:
1. 添加一个 **supersource** $s$ 连接到所有左侧顶点（男人），每条边容量为 1
2. 添加一个 **supersink** $t$，所有右侧顶点（女人）连接到 $t$，每条边容量为 1
3. 将原二分图中的每条无向边替换为容量为 1 的有向边（从男人指向女人）
4. 所有边容量均为 1

**Why it works**:
- 容量为 1 的边确保每个顶点最多匹配一次（流量守恒约束）
- 从 $s$ 到 $t$ 的最大流值即为最大匹配数

> **图示描述**: 
> - 左侧: 男人集合 $\{A, B, C, D\}$，右侧: 女人集合 $\{X, Y, Z\}$，兼容关系用边连接
> - 加入 $s$ 和 $t$ 后，所有从 $s$ 出发和进入 $t$ 的边容量为 1
> - 最大流的整数性保证每个单位的流量对应一对匹配
> - 例子中最大匹配为 3（$A-X, B-Y, C-Z$，或 $A-Y, B-X, C-Z$ 等）

---

## 11. Summary and Exam Tips (小结与考点提示)

### 11.1 Key Concepts Checklist (关键概念检查表)

| 中文 | English | Importance |
|------|---------|------------|
| 流网络 | Flow Network | 基础定义 |
| 容量 | Capacity $c(e)$ | 基础定义 |
| 可行流 | Flow $f(e)$ | 基础定义 |
| 容量约束 | Capacity constraint $0 \le f(e) \le c(e)$ | 基础定义 |
| 守恒约束 | Flow conservation | 基础定义 |
| 流值 | Flow value $v(f)$ | 基础定义 |
| 源点/收点 | Source $s$ / Sink $t$ | 基础定义 |
| 割 | s-t Cut $(A,B)$ | **核心概念** |
| 割容量 | Cut capacity $\text{cap}(A,B)$ | **核心概念** |
| 残差图 | Residual Graph $G_f$ | **核心概念** |
| 增广路径 | Augmenting Path | **核心概念** |
| 瓶颈 | Bottleneck | **核心概念** |
| Ford-Fulkerson | Ford-Fulkerson Algorithm | **核心算法** |
| 最大流最小割定理 | Max-Flow Min-Cut Theorem | **核心定理** |
| 弱对偶性 | Weak Duality | 重要引理 |
| 流值引理 | Flow Value Lemma | 重要引理 |
| 整数性定理 | Integrality Theorem | 重要定理 |
| 容量缩放 | Capacity Scaling | 算法改进 |
| 二分图匹配 | Bipartite Matching | 重要应用 |

### 11.2 Typical Exam Questions (典型考题)

1. **Find max flow**: 给定一个流网络，用 Ford-Fulkerson 算法计算最大流
   - 步骤: 初始化 → 画残差图 → 找增广路径 → 增广 → 重复 → 直到无增广路径
   - 每次迭代都要记录流量和残差图的变化

2. **Find min cut**: 在最大流的基础上找出最小割
   - 方法: 在最终残差图中从 $s$ 出发做 BFS/DFS，所有可达顶点构成 $A$，其余为 $B$

3. **Prove optimality**: 证明找到的流是最大流
   - 方法: 找到一个割，使得 $v(f) = \text{cap}(A,B)$

4. **Apply to bipartite matching**: 将实际问题建模为二分图匹配，再转化为最大流问题

### 11.3 Common Pitfalls (常见错误)

- **忘记反向边**: 在构建残差图时必须同时考虑前向边和反向边
- **割容量计算错误**: 只计算从 $A$ 到 $B$ 的边，**不**计算从 $B$ 到 $A$ 的边
- **流值 vs 割容量的混淆**: 流值是净流量（考虑双向），割容量只考虑单向
- **增广路径必须用残差图**: 在原图中可能找不到路径，但在残差图中能找到

### 11.4 Summary of Key Relationships (关键关系总结)

```
弱对偶性: v(f) ≤ cap(A, B)  对于任意流 f 和任意割 (A,B)

推理: 若 v(f) = cap(A,B) → f 是最大流, (A,B) 是最小割 (Certificate of Optimality)

最大流最小割定理: max v(f) = min cap(A,B)
                  (最大流值)  (最小割容量)

算法: Ford-Fulkerson 通过不断在残差图中找增广路径逼近这个值
```

### 11.5 Formula Reference Card

| Formula | Description |
|---------|-------------|
| $0 \le f(e) \le c(e)$ | Capacity constraint |
| $\sum_{e \text{ into } v} f(e) = \sum_{e \text{ out of } v} f(e)$ | Flow conservation |
| $v(f) = \sum_{e \text{ out of } s} f(e)$ | Flow value |
| $\text{cap}(A, B) = \sum_{e \text{ out of } A} c(e)$ | Cut capacity |
| $\sum_{e \text{ out of } A} f(e) - \sum_{e \text{ in to } A} f(e) = v(f)$ | Flow value lemma |
| $v(f) \le \text{cap}(A, B)$ | Weak duality |
| $c_f(e) = c(e) - f(e)$ (forward), $c_f(e_R) = f(e)$ (reverse) | Residual capacity |
| $b = \min_{(u,v) \in P} c_f(u, v)$ | Bottleneck capacity |
| $\max_f v(f) = \min_{(A,B)} \text{cap}(A, B)$ | Max-flow min-cut theorem |

---

> **Final tip**: 考试中如果要求"Prove that the flow is maximum"，最直接的方法就是构造一个割使得流值等于割容量。找最小割的方法是：在最终残差图中从 $s$ 做 BFS。
