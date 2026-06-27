#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate the comprehensive DMA exam checklist HTML with collapsible exam points."""

from html import escape

# ============================================================
# DATA: All exam points organized by chapter
# ============================================================

chapters_raw = r'''
[
  {
    "id": "ch1",
    "name": "Ch1: 命题逻辑与谓词逻辑",
    "points": [
      {"id":"ch1-equiv-prop","name":"命题逻辑等价判断","freq":3,"diff":"★★☆",
       "qs":[
         ["判断以下两个命题是否逻辑等价: $p \\to (\\neg q \\land r)$ 与 $\\neg p \\lor \\neg(r \\to q)$",
          "化简LHS: $p \\to (\\neg q \\land r) \\equiv \\neg p \\lor (\\neg q \\land r)$(蕴含律). RHS: $\\neg p \\lor \\neg(r \\to q) \\equiv \\neg p \\lor \\neg(\\neg r \\lor q) \\equiv \\neg p \\lor (r \\land \\neg q)$(德摩根律). $\\neg q \\land r \\equiv r \\land \\neg q$(合取交换), LHS $\\equiv$ RHS, 故等价. 答案T.",
          "2022 Quiz1 1a"],
         ["判断: $p \\to (q \\to r)$ 与 $(p \\to q) \\to r$ 是否逻辑等价",
          "LHS: $p \\to (q \\to r) \\equiv \\neg p \\lor \\neg q \\lor r$. RHS: $(p \\to q) \\to r \\equiv (p \\land \\neg q) \\lor r$. 取反例$p = \\mathrm{F}, q = \\mathrm{T}, r = \\mathrm{F}$: LHS=T, RHS=F. 不等价. 答案F.",
          "2024 Quiz1 1a"]
       ]},
      {"id":"ch1-equiv-pred","name":"谓词逻辑等价判断","freq":2,"diff":"★★☆",
       "qs":[
         ["判断: $\\forall x P(x) \\lor \\exists x Q(x)$ 与 $\\forall x \\exists y\\, (P(x) \\lor Q(y))$ 是否等价",
          "从左到右: 若$\\forall x P(x)$真, 则$P(x)\\lor Q(y)$对任意$y$真. 若$\\exists x Q(x)$真, 设$c$使$Q(c)$真, 则对任意$x$取$y=c$使右式真. 从右到左: 反证. 等价. 答案T.",
          "2023 Quiz1 1a"]
       ]},
      {"id":"ch1-tautology","name":"重言式与矛盾式判断","freq":2,"diff":"★☆☆",
       "qs":[
         ["判断: $((p \\to q) \\land \\neg p) \\to \\neg q$ 是否为重言式",
          "赋值$p = \\mathrm{F}, q = \\mathrm{T}$: $((\\mathrm{F}\\to\\mathrm{T})\\land\\neg\\mathrm{F})\\to\\neg\\mathrm{T} = (\\mathrm{T}\\land\\mathrm{T})\\to\\mathrm{F} = \\mathrm{T}\\to\\mathrm{F} = \\mathrm{F}$. 存在假赋值, 非重言式. 答案F.",
          "2022 Quiz1 1c"],
         ["判断: $\\neg(p \\to q) \\land q$ 是否为重言式",
          "化简: $\\neg(p \\to q) \\land q \\equiv (p \\land \\neg q) \\land q \\equiv p \\land (\\neg q \\land q) \\equiv p \\land \\mathrm{F} \\equiv \\mathrm{F}$. 是矛盾式, 非重言式. 答案F.",
          "2023 Quiz1 1e"]
       ]},
      {"id":"ch1-red-and","name":"用$\\neg,\\land$表达$\\lor$","freq":2,"diff":"★★☆",
       "qs":[
         ["写出与$p \\lor \\neg q$等价的命题, 只使用$p, q, \\neg$和$\\land$",
          "$p \\lor \\neg q \\equiv \\neg(\\neg p \\land \\neg\\neg q) \\equiv \\neg(\\neg p \\land q)$. 应用德摩根律 $\\neg(A\\land B)\\equiv\\neg A\\lor\\neg B$.",
          "2022 Quiz1 3a"]
       ]},
      {"id":"ch1-red-or","name":"用$\\neg,\\lor$表达$\\land$","freq":3,"diff":"★★☆",
       "qs":[
         ["写出与$p \\land q$等价的命题, 只使用$p, q, \\neg$和$\\lor$",
          "$p \\land q \\equiv \\neg(\\neg p \\lor \\neg q)$. 由德摩根律, 合取可用非和析取表示.",
          "2023 Quiz1 3a"],
         ["写出与$(p \\land \\neg q)$等价的命题, 只使用$p, q, \\neg$和$\\lor$",
          "$p \\land \\neg q \\equiv \\neg(\\neg p \\lor q)$. 真值表验证等价.",
          "2024 Quiz4 1a"]
       ]},
      {"id":"ch1-nand-basic","name":"NAND构造基本联结词","freq":2,"diff":"★★☆",
       "qs":[
         ["写出与$p \\land q$等价的命题, 只使用$p, q$和联结词$|$(NAND)",
          "$p \\mid q \\equiv \\neg(p \\land q)$. 构造: $\\neg p \\equiv p \\mid p$. $p \\land q \\equiv \\neg(p \\mid q) \\equiv (p \\mid q) \\mid (p \\mid q)$.",
          "2022 Quiz1 3b"],
         ["写出与$p \\land \\neg q$等价的命题, 只使用$p, q$和NAND",
          "$\\neg q \\equiv q \\mid q$; $\\neg(p\\land\\neg q) \\equiv p \\mid (q \\mid q)$; $p\\land\\neg q \\equiv \\neg(p \\mid (q \\mid q)) \\equiv (p \\mid (q \\mid q)) \\mid (p \\mid (q \\mid q))$.",
          "2024 Quiz1 4"]
       ]},
      {"id":"ch1-nand-xor","name":"NAND表达异或运算","freq":1,"diff":"★★★",
       "qs":[
         ["写出与$p \\oplus q$(异或)等价的命题, 只使用$p, q$和NAND",
          "$p \\oplus q \\equiv (p\\land\\neg q)\\lor(\\neg p\\land q)$. 用NAND表达各部分得: $(p \\mid (q \\mid q)) \\mid ((p \\mid p) \\mid q)$.",
          "2025 Quiz1 2b"]
       ]},
      {"id":"ch1-nor","name":"NOR功能完全性","freq":1,"diff":"★★☆",
       "qs":[
         ["写出与$p \\land q$等价的命题, 只使用$p, q$和联结词$\\downarrow$(NOR)",
          "$p \\downarrow q \\equiv \\neg(p \\lor q)$. 构造否定: $p \\downarrow p \\equiv \\neg p$. 构造合取: $p\\land q \\equiv \\neg(\\neg p\\lor\\neg q) \\equiv \\neg p \\downarrow \\neg q \\equiv (p \\downarrow p) \\downarrow (q \\downarrow q)$.",
          "2023 Quiz1 3b"]
       ]},
      {"id":"ch1-dnf-basic","name":"全析取范式(公式法)","freq":2,"diff":"★★☆",
       "qs":[
         ["求公式的全DNF: 三个变量$p,q,r$, 公式在最多一个变量为真时取真",
          "真值行(0或1个真): $(\\neg p\\land\\neg q\\land\\neg r)\\lor(p\\land\\neg q\\land\\neg r)\\lor(\\neg p\\land q\\land\\neg r)\\lor(\\neg p\\land\\neg q\\land r)$.",
          "2022 Quiz1 4a"],
         ["求$(p \\leftrightarrow \\neg r) \\to (q \\leftrightarrow r)$的全DNF",
          "为真的6行极小项析取: $(\\neg p\\land\\neg q\\land\\neg r)\\lor(\\neg p\\land q\\land r)\\lor(p\\land\\neg q\\land\\neg r)\\lor(p\\land\\neg q\\land r)\\lor(p\\land q\\land\\neg r)\\lor(p\\land q\\land r)$.",
          "2023 Quiz1 5b"]
       ]},
      {"id":"ch1-dnf-xor","name":"全析取范式(异或)","freq":1,"diff":"★★☆",
       "qs":[
         ["求$p \\oplus (q \\oplus r)$的全DNF",
          "$p\\oplus q\\oplus r$为真当且仅当奇数个为真. 全DNF: $(\\neg p\\land\\neg q\\land r)\\lor(\\neg p\\land q\\land\\neg r)\\lor(p\\land\\neg q\\land\\neg r)\\lor(p\\land q\\land r)$.",
          "2024 Quiz1 5a"]
       ]},
      {"id":"ch1-cnf-basic","name":"全合取范式(公式法)","freq":2,"diff":"★★☆",
       "qs":[
         ["同上题, 求全CNF",
          "为假的4行极大项合取: $(\\neg p\\lor\\neg q\\lor r)\\land(\\neg p\\lor q\\lor\\neg r)\\land(p\\lor\\neg q\\lor\\neg r)\\land(\\neg p\\lor\\neg q\\lor\\neg r)$.",
          "2022 Quiz1 4b"],
         ["求$(p \\leftrightarrow \\neg r) \\to (q \\leftrightarrow r)$的全CNF",
          "假行$(F,F,T),(F,T,F)$. 极大项: $(p\\lor q\\lor\\neg r)\\land(p\\lor\\neg q\\lor r)$.",
          "2023 Quiz1 5a"]
       ]},
      {"id":"ch1-cnf-xor","name":"全合取范式(异或类)","freq":2,"diff":"★★☆",
       "qs":[
         ["求$p \\oplus (q \\oplus r)$的全CNF",
          "假行4行. 全CNF: $(p\\lor q\\lor r)\\land(p\\lor\\neg q\\lor\\neg r)\\land(\\neg p\\lor q\\lor\\neg r)\\land(\\neg p\\lor\\neg q\\lor r)$.",
          "2024 Quiz1 5b"],
         ["求$(p \\oplus q) \\lor r$的全CNF",
          "假行$(F,F,F),(T,T,F)$. 全CNF: $(p\\lor q\\lor r)\\land(\\neg p\\lor\\neg q\\lor r)$.",
          "2025 Quiz1 3"]
       ]},
      {"id":"ch1-bicond","name":"双条件(Biconditional)真值","freq":1,"diff":"★☆☆",
       "qs":[
         ["判断: $8+3=9$ 当且仅当 $8-3=7$",
          "$8+3=9$假, $8-3=7$假. 双条件$\\mathrm{F}\\leftrightarrow\\mathrm{F}\\equiv\\mathrm{T}$. 命题真. 答案T.",
          "2024 Quiz1 1c"]
       ]},
      {"id":"ch1-pred-student","name":"谓词逻辑翻译(学生课程)","freq":2,"diff":"★★☆",
       "qs":[
         ["设$T(x,y)$表示$x$正在修$y$, 翻译: 没有课程被所有学生修读",
          "$\\neg \\exists y \\forall x\\, T(x,y)$ 或 $\\forall y \\exists x\\, \\neg T(x,y)$. 存在一门课程所有学生都在修为$\\exists y \\forall x\\, T(x,y)$, 否定之.",
          "2022 Quiz1 2a"],
         ["翻译: 有一门课程被所有学生修读",
          "$\\exists y \\forall x\\, T(x, y)$. 存在课程$y$, 对所有学生$x$, $x$在修$y$.",
          "2024 Quiz1 2a"]
       ]},
      {"id":"ch1-pred-leader","name":"谓词逻辑翻译(比较级)","freq":1,"diff":"★★☆",
       "qs":[
         ["用taller(x,y)翻译: Lincoln was the tallest leader",
          "$\\forall x\\, (\\text{leader}(x) \\land x \\neq \\text{Lincoln} \\to \\text{taller}(\\text{Lincoln}, x))$.",
          "2022 Quiz4 1a"]
       ]},
      {"id":"ch1-qneg","name":"量词否定与翻译","freq":3,"diff":"★★☆",
       "qs":[
         ["翻译: 没有学生修读所有课程",
          "$\\neg \\exists x \\forall y\\, T(x, y)$ 或 $\\forall x \\exists y\\, \\neg T(x, y)$. 存在学生修读所有课程: $\\exists x \\forall y\\, T(x,y)$, 否定之.",
          "2024 Quiz1 2b"],
         ["写出$\\exists x\\exists y P(x,y)\\land\\forall x\\forall y Q(x,y)$的否定, 使否定紧邻谓词",
          "$\\neg[\\exists x\\exists y P(x,y)\\land\\forall x\\forall y Q(x,y)] \\equiv \\forall x\\forall y\\neg P(x,y)\\lor\\exists x\\exists y\\neg Q(x,y)$.",
          "2024 Quiz4 1b"]
       ]},
      {"id":"ch1-qdist","name":"量词分配律","freq":2,"diff":"★★☆",
       "qs":[
         ["下列哪个等价成立? A.$\\forall x(P(x)\\land Q(x))\\equiv\\forall xP(x)\\land\\forall xQ(x)$ B.$\\exists x(P(x)\\land Q(x))\\equiv\\exists xP(x)\\land\\exists xQ(x)$ C.$\\forall x(P(x)\\to Q(x))\\equiv\\forall xP(x)\\to\\forall xQ(x)$ D.$\\exists x(P(x)\\to Q(x))\\equiv\\exists xP(x)\\to\\exists xQ(x)$",
          "A正确: $\\forall$对$\\land$可分配. B错误: $\\exists$对$\\land$不可分配. C,D错误. 选A.",
          "2023 Quiz1 2"],
         ["判断: 若$x$不在$A$中出现, 则$\\exists x(P(x)\\to A)\\equiv\\forall xP(x)\\to A$",
          "$\\exists x(P(x)\\to A)\\equiv\\exists x(\\neg P(x)\\lor A)\\equiv(\\exists x\\neg P(x))\\lor A\\equiv\\neg(\\forall xP(x))\\lor A\\equiv\\forall xP(x)\\to A$. 关键: $x$在$A$中不自由, $\\exists$可直接分配于$\\lor$. 答案T.",
          "2025 Quiz1 1a"]
       ]},
      {"id":"ch1-qtruth","name":"量词真值判定","freq":1,"diff":"★★☆",
       "qs":[
         ["设$P(x,y)$论域$\\{1,2,3,4\\}$, 已知$P(1,3),P(2,1),P(2,4),P(3,2),P(3,4),P(4,1),P(4,4)$为真. 判断$\\forall x\\exists y((x\\le y)\\land P(x,y))$",
          "$x=1$选$y=3$: $(1\\le3)\\land P(1,3)=T$; $x=2$选$y=4$: T; $x=3$选$y=4$: T; $x=4$选$y=4$: T. 命题真. 答案T.",
          "2025 Quiz1 1d"]
       ]},
      {"id":"ch1-contra","name":"逆否命题证明法","freq":1,"diff":"★☆☆",
       "qs":[
         ["证明: 若$x^3$是无理数, 则$x$是无理数",
          "逆否命题: 若$x$是有理数, 则$x^3$是有理数. 设$x=p/q$($\\gcd(p,q)=1$), $x^3=p^3/q^3$为有理数. 原命题与其逆否等价, 故成立.",
          "2024 Quiz1 8"]
       ]}
    ]
  },
  {
    "id": "ch2",
    "name": "Ch2: 集合与函数",
    "points": [
      {"id":"ch2-setop-eq","name":"集合运算恒等式(元素法)","freq":2,"diff":"★☆☆",
       "qs":[
         ["判断: $A-(B\\cap C)=(A-B)\\cup(A-C)$",
          "$x\\in A-(B\\cap C)\\iff x\\in A\\land x\\notin(B\\cap C)\\iff x\\in A\\land(x\\notin B\\lor x\\notin C)$(德摩根)$\\iff (x\\in A\\land x\\notin B)\\lor(x\\in A\\land x\\notin C)$(分配)$\\iff x\\in(A-B)\\cup(A-C)$. 成立. 答案T.",
          "2022 Quiz1 1b"]
       ]},
      {"id":"ch2-setop-false","name":"集合运算恒等式(反例法)","freq":1,"diff":"★☆☆",
       "qs":[
         ["判断: $(A-C)-(B-C)=A-B$",
          "反例: $A=\\{1,2,3\\},B=\\{1\\},C=\\{1,2\\}$. $A-C=\\{3\\},B-C=\\varnothing,(A-C)-(B-C)=\\{3\\}$, $A-B=\\{2,3\\}$. 不成立. 答案F.",
          "2023 Quiz1 1b"]
       ]},
      {"id":"ch2-powerset","name":"幂集性质判断","freq":2,"diff":"★★☆",
       "qs":[
         ["判断: $\\mathrm{P}(A)=\\mathrm{P}(B)$当且仅当$A=B$",
          "($\\Leftarrow$)若$A=B$则显然. ($\\Rightarrow$)若$\\mathrm{P}(A)=\\mathrm{P}(B)$, 则$A\\in\\mathrm{P}(A)=\\mathrm{P}(B)\\Rightarrow A\\subseteq B$, 同理$B\\subseteq A$. 故$A=B$. 答案T.",
          "2022 Quiz1 1d"],
         ["判断: 若$\\mathrm{P}(A)\\in\\mathrm{P}(B)$, 则$A\\in B$",
          "$\\mathrm{P}(A)\\in\\mathrm{P}(B)$意味着$\\mathrm{P}(A)\\subseteq B$. 由于$A\\in\\mathrm{P}(A)$, 得$A\\in B$. 答案T.",
          "2023 Quiz1 1d"]
       ]},
      {"id":"ch2-symdiff","name":"对称差运算性质","freq":2,"diff":"★☆☆",
       "qs":[
         ["判断: $A\\oplus(B\\oplus C)=(A\\oplus B)\\oplus C$",
          "对称差满足结合律. $x\\in A\\oplus(B\\oplus C)$当且仅当$x$属于$A,B,C$中的奇数个, 与$(A\\oplus B)\\oplus C$等价. 答案T.",
          "2024 Quiz1 1b"],
         ["判断: $(A\\cap B)\\oplus C=(A\\oplus C)\\cap(B\\oplus C)$",
          "成员关系表验证, 两列不完全一致, 恒等式不成立. 答案F.",
          "Final 2022 Q3"]
       ]},
      {"id":"ch2-cantor","name":"Cantor对角线论证","freq":3,"diff":"★★★",
       "qs":[
         ["改编Cantor对角线论证, 证明$(0,1)$中十进制表示只由0和1组成的正实数集合不可数",
          "设$S=\\{r\\in(0,1)\\mid r$的十进制只含数码0和1$\\}$. 假设$S$可数, 列出$r_1,r_2,\\ldots$. 构造$r=0.b_1b_2\\cdots$, $b_i=1-a_{ii}$. $r\\in S$但$r$与每个$r_i$在第$i$位不同, 矛盾. 故$S$不可数.",
          "2022 Quiz1 6"],
         ["判断: $(0,1)$中只由6和8组成的正实数集合不可数",
          "同2022年论证, 将数码换成$\\{6,8\\}$. 构造$r$第$i$位为8(若$r_i$第$i$位=6)或6(若=8). 矛盾. 答案T.",
          "2024 Quiz1 1d"],
         ["判断: 只由0和1组成的正实数集合可数(2025)",
          "实际不可数! 由Cantor对角线法可证. 假设可数, 列出$r_1,r_2,\\ldots$, 构造$r=0.b_1b_2\\cdots$翻转对角线, 导矛盾. 答案F.",
          "2025 Quiz1 1f"]
       ]},
      {"id":"ch2-cnt-equation","name":"代数方程解的可数性","freq":2,"diff":"★★☆",
       "qs":[
         ["判断: 整系数三次方程$ax^3+bx^2+cx+d=0$的实数解集合不可数",
          "每个方程由$(a,b,c,d)\\in\\mathbb{Z}^4$确定, $\\mathbb{Z}^4$可数. 每个方程最多3实根. 所有实根是可数多个有限集的并, 故可数. 答案F.",
          "2023 Quiz1 1c"],
         ["判断: 整系数二次方程$ax^2+bx+c=0$的实数解集合可数",
          "$\\mathbb{Z}^3$可数, 每个方程最多2实根. 故可数. 答案T.",
          "2024 Quiz1 1e"]
       ]},
      {"id":"ch2-cnt-coord","name":"有理数坐标的可数性","freq":1,"diff":"★★☆",
       "qs":[
         ["三维直角坐标中有理数坐标的点有多少个?",
          "$\\mathbb{Q}$可数无穷($\\aleph_0$). $\\mathbb{Q}^3$为可数无穷个可数集之积, 仍为可数无穷. 答案是$\\aleph_0$.",
          "2024 Quiz4 1d"]
       ]},
      {"id":"ch2-card-inj","name":"集合势比较(单射存在性)","freq":1,"diff":"★★☆",
       "qs":[
         ["判断: 存在从$\\mathbb{R}$到$\\mathbb{Z}\\times\\mathbb{Z}$的单射",
          "$|\\mathbb{Z}\\times\\mathbb{Z}|=|\\mathbb{Z}|=\\aleph_0$, $|\\mathbb{R}|=\\mathfrak{c}$. 若存在单射, 则$\\mathfrak{c}\\le\\aleph_0$, 矛盾. 不存在. 答案F.",
          "2023 Quiz1 1f"]
       ]},
      {"id":"ch2-card-dim","name":"集合势比较(不同维度)","freq":1,"diff":"★★☆",
       "qs":[
         ["3维单位立方体与2维单位正方形内点的个数比较",
          "$[0,1]^3$和$[0,1]^2$皆为不可数无穷, 势均为$\\mathfrak{c}=|\\mathbb{R}|$, 相等.",
          "Final 2022 Q2"]
       ]},
      {"id":"ch2-func-comp","name":"函数复合","freq":1,"diff":"★☆☆",
       "qs":[
         ["$g:A\\to B,f:B\\to C$, $A=\\{1,2,3,4\\},B=\\{a,b,c\\},C=\\{2,7,10\\}$, $g=\\{(1,b),(2,a),(3,a),(4,b)\\},f=\\{(a,10),(b,7),(c,2)\\}$. 求$f\\circ g$",
          "$(f\\circ g)(1)=f(b)=7$, $(2)=f(a)=10$, $(3)=10$, $(4)=7$. $f\\circ g=\\{(1,7),(2,10),(3,10),(4,7)\\}$.",
          "2024 Quiz1 3"]
       ]},
      {"id":"ch2-map","name":"函数映射分类(单射/满射/双射)","freq":1,"diff":"★☆☆",
       "qs":[
         ["列出所有从$A=\\{1,2\\}$到$B=\\{a,b\\}$的函数, 指出双射和满射",
          "共$2^2=4$个: $f_1:(a,a)$非单非满; $f_2:(a,b)$双射; $f_3:(b,a)$双射; $f_4:(b,b)$非单非满. $|A|=|B|$时单射$\\iff$满射$\\iff$双射.",
          "2025 Quiz1 4"]
       ]},
      {"id":"ch2-ceil","name":"取整函数性质","freq":1,"diff":"★☆☆",
       "qs":[
         ["判断: 若$n$是整数, 则$\\lceil n/2\\rceil+\\lfloor n/2\\rfloor=n$",
          "$n=2k$偶: $\\lceil k\\rceil+\\lfloor k\\rfloor=k+k=2k=n$. $n=2k-1$奇: $\\lceil k-0.5\\rceil+\\lfloor k-0.5\\rfloor=k+(k-1)=2k-1=n$. 答案T.",
          "2025 Quiz1 1c"]
       ]},
      {"id":"ch2-distrib","name":"集合分配律推广证明","freq":2,"diff":"★★★",
       "qs":[
         ["证明$A_1\\cap(A_2\\cup\\cdots\\cup A_n)=(A_1\\cap A_2)\\cup\\cdots\\cup(A_1\\cap A_n)$对所有$n>2$成立",
          "元素法: $x\\in A_1\\cap(A_2\\cup\\cdots\\cup A_n)\\iff x\\in A_1\\land(x\\in A_2\\lor\\cdots\\lor x\\in A_n)\\iff(x\\in A_1\\land x\\in A_2)\\lor\\cdots\\lor(x\\in A_1\\land x\\in A_n)\\iff x\\in(A_1\\cap A_2)\\cup\\cdots\\cup(A_1\\cap A_n)$. 也可用数学归纳法.",
          "2022 Quiz1 5"]
       ]}
    ]
  },
  {
    "id": "ch3",
    "name": "Ch3: 算法复杂度",
    "points": [
      {"id":"ch3-bigo-est","name":"算法复杂度估算","freq":1,"diff":"★★☆",
       "qs":[
         ["求打印$\\{1,2,\\ldots,n\\}$的所有三元子集的算法复杂度",
          "三元子集个数$\\binom{n}{3}=n(n-1)(n-2)/6=O(n^3)$. 总复杂度$O(n^3)$.",
          "2022 Quiz1 7a"]
       ]},
      {"id":"ch3-bigo-judge","name":"Big-O关系判断","freq":2,"diff":"★★☆",
       "qs":[
         ["判断: $n$个数中查找最小数的时间复杂度是$\\Theta(n\\log n)$",
          "需$n-1$次比较, 时间复杂度$\\Theta(n)$. 答案F.",
          "2024 Quiz1 1f"],
         ["判断: $n^{0.01}$是$O(\\log n)$",
          "对任意$a>0,b>0$, $n^a=\\Omega((\\log n)^b)$. $n^{0.01}/\\log n\\to\\infty$, 故不是$O(\\log n)$. 答案F.",
          "2025 Quiz1 1e"]
       ]},
      {"id":"ch3-growth-2023","name":"函数增长率排序(2023)","freq":1,"diff":"★★☆",
       "qs":[
         ["将以下函数按增长率从小到大排列: $(1.2)^n,7n^6,(\\log n)^3,3^n,\\log\\log n,n^2(\\log n)^3,3^n(n^3+1),n^3+n(\\log n)^2,1000000,10n!$",
          "$1000000\\prec\\log\\log n\\prec(\\log n)^3\\prec n^2(\\log n)^3\\prec n^3+n(\\log n)^2\\prec7n^6+n+323\\prec(1.2)^n\\prec3^n\\prec3^n(n^3+1)\\prec10n!$.",
          "2023 Quiz1 4"]
       ]},
      {"id":"ch3-growth-2024","name":"函数增长率排序(2024)","freq":1,"diff":"★★☆",
       "qs":[
         ["将以下排序: $(1.01)^n,10n!,(\\log n)^3,2^n,\\log\\log n,999n^2(\\log n)^3,(n^4+1)/(n^3+3),n^3+n(\\log n)^2,9^{999}$",
          "$9^{999}\\prec\\log\\log n\\prec(\\log n)^3\\prec(n^4+1)/(n^3+3)\\sim n\\prec999n^2(\\log n)^3\\prec n^3+n(\\log n)^2\\prec(1.01)^n\\prec2^n\\prec10n!$.",
          "2024 Quiz1 6"]
       ]},
      {"id":"ch3-linear","name":"算法最佳/最差情况分析","freq":1,"diff":"★☆☆",
       "qs":[
         ["线性查找在最佳情况下的比较次数(规模$n$)",
          "最佳情况目标为第一个元素, 1次比较. 复杂度$O(1)$.",
          "2022 Quiz1 7b"]
       ]}
    ]
  },
  {
    "id": "ch4",
    "name": "Ch4: 数论",
    "points": [
      {"id":"ch4-fermat-basic","name":"费马小定理计算","freq":2,"diff":"★★☆",
       "qs":[
         ["判断: $2025^{2026}\\equiv1\\pmod{2027}$",
          "2027是素数, 费马小定理$2025^{2026}\\equiv1\\pmod{2027}$. 答案T.",
          "2025 Quiz1 1g"],
         ["求$3^{2023}\\bmod1997$",
          "1997为素数. $3^{1996}\\equiv1$, $2023=1996+27$, $3^{2023}\\equiv3^{27}\\equiv583\\pmod{1997}$.",
          "2023 Quiz2 1c"]
       ]},
      {"id":"ch4-fermat-proof","name":"费马小定理证明应用","freq":1,"diff":"★★★",
       "qs":[
         ["证明: 对素数$p\\neq2,5$, 序列$1,11,111,\\ldots$中有无穷多项被$p$整除",
          "$a_k=(10^k-1)/9$. $p\\mid a_k\\iff10^k\\equiv1\\pmod{p}$. 由费马小定理$10^{p-1}\\equiv1$, 故$k=t(p-1)$均为解, 无穷多.",
          "2023 Quiz2 5"]
       ]},
      {"id":"ch4-euler","name":"欧拉函数与简化剩余系","freq":1,"diff":"★★☆",
       "qs":[
         ["将所有与77互质的正整数排成递增序列, 求第600项",
          "$77=7\\times11$, $\\varphi(77)=77\\times(1-1/7)\\times(1-1/11)=60$. 周期60, 每周期+77. $a_{600}=a_{60}+77\\times9=76+693=769$.",
          "2025 Quiz1 5"]
       ]},
      {"id":"ch4-crt-basic","name":"CRT方程组求解","freq":2,"diff":"★★☆",
       "qs":[
         ["求解: $x\\equiv1\\pmod{3}, x\\equiv2\\pmod{5}, x\\equiv3\\pmod{8}$",
          "$M=120$. $M_1=40,y_1=1$; $M_2=24,y_2=4$; $M_3=15,y_3=7$. $x=1\\cdot40+2\\cdot96+3\\cdot105=547\\equiv67\\pmod{120}$.",
          "2025 Quiz1 6"],
         ["求解: $x\\equiv1\\pmod{2},2\\pmod{3},3\\pmod{5},4\\pmod{7}$",
          "$M=210$. $y_1=1,y_2=1,y_3=3,y_4=4$. $x=105+140+378+480=1103\\equiv53\\pmod{210}$.",
          "2023 Quiz2 1e"]
       ]},
      {"id":"ch4-crt-app","name":"CRT应用(连续整除)","freq":1,"diff":"★★☆",
       "qs":[
         ["求三个连续正整数, 依次能被5,7,11整除",
          "设$n,n+1,n+2$, 得同余式组. CRT解得$n=385t+20$, 即$20,21,22$等.",
          "2024 Quiz4 2"]
       ]},
      {"id":"ch4-square","name":"完全平方数与因子个数","freq":1,"diff":"★★☆",
       "qs":[
         ["2023个杯子编号1-2023开口向上, 从$k=2$到2023翻转$k$的倍数. 最终多少开口向上?",
          "杯子$n$被翻转次数$=d(n)-1$. 偶次翻转$\\iff d(n)$奇$\\iff n$为完全平方数. $\\lfloor\\sqrt{2023}\\rfloor=44$. 答案44.",
          "2023 Quiz2 3"]
       ]},
      {"id":"ch4-seq","name":"序列整除性证明","freq":1,"diff":"★★★",
       "qs":[
         ["证明: 对任意正整数$m$, Fibonacci数列中存在一项被$m$整除",
          "考虑$(F_k\\bmod m,F_{k+1}\\bmod m)$余数对(共$m^2$种). 前$m^2+1$个中必有重复. 设$(F_i,F_{i+1})\\equiv(F_j,F_{j+1})$, 可逆推得$F_0\\equiv F_{j-i}$, 而$F_0=0$, 故$m\\mid F_{j-i}$.",
          "2023 Quiz2 6"]
       ]}
    ]
  },
  {
    "id": "ch5",
    "name": "Ch5: 数学归纳法",
    "points": [
      {"id":"ch5-ineq-pow","name":"不等式归纳(幂比较)","freq":1,"diff":"★★★",
       "qs":[
         ["用归纳法证$n^{n+1}>(n+1)^n$对$n\\ge3$成立",
          "基础$n=3$: $3^4=81>4^3=64$. 假设$k^{k+1}>(k+1)^k$, 需证$(k+1)^{k+2}>(k+2)^{k+1}$. 由假设$k>(1+1/k)^k$, 已知$(1+1/n)^n<e<3$, 可证比值$>1$.",
          "2022 Quiz1 8"]
       ]},
      {"id":"ch5-ineq-avg","name":"不等式归纳(平均值)","freq":1,"diff":"★★★",
       "qs":[
         ["用归纳法证: $x,y>0$, $(x^n+y^n)/2\\ge((x+y)/2)^n$",
          "基础$n=1$等号. 假设$n=k$. 需证$k+1$. 等价于$(x-y)(x^k-y^k)\\ge0$, 对$x,y>0$恒成立.",
          "2024 Quiz1 9"]
       ]},
      {"id":"ch5-fib5","name":"斐波那契模5整除性","freq":1,"diff":"★★☆",
       "qs":[
         ["用归纳法证: $f_{5n}\\equiv0\\pmod{5}$, $f_0=0,f_1=1,f_{n+2}=f_{n+1}+f_n$",
          "基础$n=0$成立. 假设$f_{5k}\\equiv0$, 展开$f_{5k+5}=5f_{5k+1}+3f_{5k}\\equiv0$.",
          "2023 Quiz1 7a"]
       ]},
      {"id":"ch5-fib-id","name":"斐波那契恒等式","freq":1,"diff":"★★★",
       "qs":[
         ["证$f_n^2+f_{n+1}^2=f_{2n+1}$",
          "用加法公式$f_{m+n}=f_mf_{n+1}+f_{m-1}f_n$, 取$m=n+1$: $f_{2n+1}=f_{n+1}f_{n+2}+f_nf_{n+1}=f_n^2+f_{n+1}^2$.",
          "2023 Quiz1 7b"]
       ]},
      {"id":"ch5-zeck","name":"强归纳法--Zeckendorf定理","freq":2,"diff":"★★★",
       "qs":[
         ["证每个$>2$正整数可表示为不同斐波那契数之和($f_1=1,f_2=2$)",
          "基础$n=3=1+2$. 强归纳假设$<n$成立. 取最大$f_k\\le n$. 若$n=f_k$成立. 否则$m=n-f_k<f_{k-1}$, 由归纳假设$m$可表示且与$f_k$互异.",
          "2025 Quiz1 8"]
       ]},
      {"id":"ch5-ball","name":"球合并问题(归纳法)","freq":1,"diff":"★★★",
       "qs":[
         ["$2^k$个球到若干包, 规则1同数合并, 规则2$m>n$变$m-n$和$2n$. 证可合并到一包",
          "对$k$归纳. 基础$k=0$平凡. 先将所有包变偶数, 整体除以2降到$2^{k-1}$, 由归纳假设合并, 再乘2还原.",
          "Final 2022 Q4-1"]
       ]},
      {"id":"ch5-rgb","name":"红绿点配对连线(归纳法)","freq":1,"diff":"★★★",
       "qs":[
         ["$n$红$n$绿点, 任意三点不共线, 证可两两配对连成$n$条不相交线段",
          "对$n$归纳. 考虑凸包. 若有异色相邻直接连. 若全同色用旋转直线法找平分线.",
          "2024 Quiz4 5"]
       ]}
    ]
  },
  {
    "id": "ch6",
    "name": "Ch6: 排列组合与计数",
    "points": [
      {"id":"ch6-lexperm-2022","name":"字典序排列后继(2022)","freq":1,"diff":"★★☆",
       "qs":[
         ["求76154238的下一个字典序排列",
          "从右左找首个$a_i<a_{i+1}$: $a_7=3<a_8=8$. 右边找比3大的最小: 8. 交换得76154283, 反转末尾. 结果76154283.",
          "2022 Quiz2 1a"]
       ]},
      {"id":"ch6-lexperm-2023","name":"字典序排列后继(2023)","freq":1,"diff":"★★☆",
       "qs":[
         ["求276154389的下一排列",
          "$p_7=3<p_8=8$, 交换得276154839, 反转末尾得276154893.",
          "2023 Quiz2 1a"]
       ]},
      {"id":"ch6-lexcomb-2022","name":"字典序组合后继(2022)","freq":1,"diff":"★★☆",
       "qs":[
         ["求$\\{1,\\ldots,8\\}$中$\\{3,4,5,7,8\\}$的下一个5-组合",
          "$a_3=5<6$, 加1得6, 后续递增得$\\{3,4,6,7,8\\}$.",
          "2022 Quiz2 1b"]
       ]},
      {"id":"ch6-lexcomb-2023","name":"字典序组合后继(2023)","freq":1,"diff":"★★☆",
       "qs":[
         ["求$\\{1,\\ldots,9\\}$中$\\{1,3,5,7,9\\}$的下一个5-组合",
          "$a_4=7<8$, 加1得8, $a_5=9$. 得$\\{1,3,5,8,9\\}$.",
          "2023 Quiz2 1b"]
       ]},
      {"id":"ch6-string-cnt","name":"字符串计数(综合)","freq":1,"diff":"★★☆",
       "qs":[
         ["从0-9选字符构成6位字符串, 求(a)含'1'(b)恰一个'1'(c)含'1''2'且'1'左(d)字符不同且'1'左(e)首尾同(f)恰3种字符",
          "(a)$10^6-9^6=468559$. (b)$6\\times9^5=354294$. (c)$(10^6-2\\cdot9^6+8^6)/2=99631$. (d)$\\binom{8}{4}\\times6!/2=25200$. (e)$10^5=100000$. (f)$\\binom{10}{3}(3^6-3\\cdot2^6+3)=64800$.",
          "2022 Quiz2 2"]
       ]},
      {"id":"ch6-string-all","name":"包含全部数字的字符串","freq":1,"diff":"★★☆",
       "qs":[
         ["求$n$位十进制字符串包含全部10个数字的个数",
          "包含排斥: $\\sum_{i=0}^{10}(-1)^i\\binom{10}{i}(10-i)^n$.",
          "Final 2022 Q4-8"]
       ]},
      {"id":"ch6-binom","name":"二项式定理展开系数","freq":1,"diff":"★★☆",
       "qs":[
         ["求$(x/2-3/x)^{15}$中$x^9$系数",
          "一般项$\\binom{15}{k}(x/2)^{15-k}(-3/x)^k= \\binom{15}{k}(-3)^k/2^{15-k}\\cdot x^{15-2k}$. $15-2k=9$, $k=3$. 系数$-12285/4096$.",
          "2022 Quiz2 3"]
       ]},
      {"id":"ch6-genbinom","name":"广义二项式系数","freq":1,"diff":"★★☆",
       "qs":[
         ["求$\\binom{-3}{4}$",
          "$\\binom{-3}{4}=(-3)(-4)(-5)(-6)/4!=360/24=15$.",
          "2023 Quiz2 1d"]
       ]},
      {"id":"ch6-multinom","name":"多项式定理展开系数","freq":1,"diff":"★★☆",
       "qs":[
         ["求$(x/3-2/x+y)^{12}$中$x^6y^4$系数",
          "$c=4$, $a-b=6$, $a+b=8$, 得$a=7,b=1$. 系数$= \\frac{12!}{7!1!4!}(1/3)^7(-2)=-880/243$.",
          "2023 Quiz2 1f"]
       ]},
      {"id":"ch6-balls-labeled","name":"有标号球入盒","freq":1,"diff":"★★☆",
       "qs":[
         ["4有标号球入6有标号盒: (a)无限允许空? (b)每盒至多1球? (c)一一对应?",
          "(a)$6^4=1296$. (b)$\\binom{6}{4}=15$. (c)$6!=720$.",
          "2023 Quiz2 2"],
         ["4有标号球入6无标号盒恰3非空",
          "$\\binom{4}{3}\\times S(4,3)=\\binom{4}{3}\\times6=24$种(划分3组再分配).",
          "2023 Quiz2 2g"]
       ]},
      {"id":"ch6-balls-unlabeled","name":"无标号球入盒","freq":1,"diff":"★★★",
       "qs":[
         ["6无标号球入6有标号盒恰3非空",
          "$\\binom{6}{3}\\times\\binom{5}{2}=200$.",
          "2023 Quiz2 2e"],
         ["4无标号球入6有标号盒无空盒",
          "$\\binom{4-1}{6-1}$不适用($n<k$). 实际$4^6-3^6=3367$.",
          "2023 Quiz2 2f"],
         ["3种球各3个同种无标号, 取6个球",
          "$x_1+x_2+x_3=6$, $0\\le x_i\\le3$. 无上限$\\binom{8}{2}=28$, 减违反上限$3\\times\\binom{4}{2}=18$, 得10.",
          "2023 Quiz2 2h"]
       ]},
      {"id":"ch6-multiset-basic","name":"多重集组合计数","freq":2,"diff":"★★☆",
       "qs":[
         ["不考虑花色, 取3张牌多少种?",
          "13种点数选3张可重复: $\\binom{13+3-1}{3}=\\binom{15}{3}=455$.",
          "2024 Quiz4 3e"],
         ["从$\\{5,6,7,8\\}$选5个构成非降序列",
          "$\\binom{5+4-1}{5}=\\binom{8}{5}=56$.",
          "Final 2022 Q4-7"]
       ]},
      {"id":"ch6-pigeon-subset","name":"鸽巢原理(子集和相等)","freq":1,"diff":"★★★",
       "qs":[
         ["$A$有10个不同的两位数(10-99). 证$A$有两个不相交子集和相等",
          "$2^{10}=1024$个子集, 和范围0-945共946种. 鸽巢知存在两个不同子集和相等, 移除公共部分得不相交子集.",
          "2022 Quiz2 7"]
       ]},
      {"id":"ch6-pigeon-cards","name":"鸽巢原理(扑克牌)","freq":2,"diff":"★★☆",
       "qs":[
         ["至少取多少张牌才能保证必有一个对子?",
          "13种点数, 最坏取13张各不同, 第14张必重复. 答案14.",
          "2024 Quiz4 3c"],
         ["至少取多少张牌才能保证必有顺子?",
          "10种顺子. 最坏取44张(取A-4,6-9,J-K各4张)仍无顺子, 第45张构成. 答案45.",
          "2024 Quiz4 3d"]
       ]},
      {"id":"ch6-hall","name":"Hall婚姻定理","freq":1,"diff":"★★★",
       "qs":[
         ["52张牌排4行13列, 证从每列选一张可使13张点数各不相同",
          "构造二分图, 左13列右13点数. 任意$k$列有$4k$张牌, 每点数至多4张, 故覆盖至少$k$种点数. Hall条件满足, 存在完美匹配.",
          "2024 Quiz4 3f"]
       ]},
      {"id":"ch6-palindrome","name":"Almost-palindrome计数","freq":1,"diff":"★★☆",
       "qs":[
         ["四位数称为almost-palindrome如果恰改一位变回文. 求个数",
          "Type A($d_1\\neq d_4,d_2=d_3$): $9\\times9\\times10=810$. Type B($d_1=d_4,d_2\\neq d_3$): $9\\times10\\times9=810$. 总数1620.",
          "2022 Quiz4 2"]
       ]},
      {"id":"ch6-8stu","name":"8学生8题(鸽巢/线性代数)","freq":1,"diff":"★★★",
       "qs":[
         ["8学生8判断题, 无两人答案相同. 证可去掉一题后仍无相同",
          "反证: 若去掉任意一题后都有两人相同, 则对每列$i$存在一对只在$i$不同的学生. 差值$e_i$在差空间中. 但8向量差空间最多7维, 而$e_1,\\ldots,e_8$张成$\\mathbb{F}_2^8$(8维), 矛盾.",
          "2024 Quiz3 11"]
       ]}
    ]
  },
  {
    "id": "ch8",
    "name": "Ch8: 递推关系与生成函数",
    "points": [
      {"id":"ch8-gfseq-pos","name":"生成函数到序列(正项)","freq":1,"diff":"★★☆",
       "qs":[
         ["写出$(1+x)/(1-x)$确定的序列前6项",
          "$\\frac{1+x}{1-x}=(1+x)\\sum x^n=1+2\\sum_{n\\ge1}x^n$. 序列: $1,2,2,2,2,2$.",
          "2022 Quiz2 5"]
       ]},
      {"id":"ch8-gfseq-neg","name":"生成函数到序列(交错)","freq":1,"diff":"★★☆",
       "qs":[
         ["写出$(1-x)/(1+x)$确定的序列前6项",
          "$\\frac{1-x}{1+x}=(1-x)\\sum(-1)^n x^n=1-2x+2x^2-2x^3+\\cdots$. 序列: $1,-2,2,-2,2,-2$.",
          "2023 Quiz2 1g"]
       ]},
      {"id":"ch8-rechomo","name":"齐次线性递推求解","freq":2,"diff":"★★☆",
       "qs":[
         ["用生成函数求解$a_k=5a_{k-1}-6a_{k-2}$, $a_0=6,a_1=30$",
          "$A(x)=6/(1-2x)(1-3x)=-12/(1-2x)+18/(1-3x)$. $a_k=18\\cdot3^k-12\\cdot2^k$.",
          "2024 Quiz4 4"]
       ]},
      {"id":"ch8-recnonhomo-1","name":"非齐次递推(指数+常数特解)","freq":2,"diff":"★★★",
       "qs":[
         ["求解$a_n=5a_{n-1}-6a_{n-2}+2^n+3$, $a_0=1,a_1=1$",
          "齐次$\\alpha2^n+\\beta3^n$. 特解$An2^n+B$. 得$A=-2,B=3/2$. 初值得$\\alpha=-5,\\beta=9/2$. $a_n=(9\\cdot3^n-(4n+10)2^n+3)/2$.",
          "2022 Quiz2 6"]
       ]},
      {"id":"ch8-recnonhomo-2","name":"非齐次递推(指数+线性特解)","freq":2,"diff":"★★★",
       "qs":[
         ["求解$a_n=4a_{n-1}-3a_{n-2}+2^n+1$, $a_0=1,a_1=3$",
          "齐次$\\alpha+\\beta3^n$. 特解$A2^n+Bn$. 得$A=-4,B=-1/2$. 初值得$a_n=(13\\cdot3^n-16\\cdot2^n-2n+7)/4$.",
          "2023 Quiz2 4"]
       ]},
      {"id":"ch8-gfderiv","name":"生成函数变换(导数)","freq":1,"diff":"★★☆",
       "qs":[
         ["设$G(x)=\\sum a_n x^n$, 求$a_0,2a_1,3a_2,\\ldots$的生成函数",
          "$\\sum (n+1)a_n x^n = \\sum n a_n x^n + \\sum a_n x^n = xG'(x)+G(x)$.",
          "Final 2022 Q4-6"]
       ]},
      {"id":"ch8-gffib","name":"生成函数与斐波那契数列","freq":1,"diff":"★★☆",
       "qs":[
         ["$G(x)=1/(1-x-x^2)=\\sum a_n x^n$, 求$a_n$",
          "$a_n=F_{n+2}$, $F_1=F_2=1$. 满足$a_n=a_{n-1}+a_{n-2},a_0=1,a_1=1$. 通项$a_n=(\\varphi^{n+2}-\\psi^{n+2})/\\sqrt5$.",
          "Final 2022 Q4-4"]
       ]},
      {"id":"ch8-recparam","name":"待定系数法反推递推","freq":1,"diff":"★★☆",
       "qs":[
         ["已知$a_n=c_1a_{n-1}+c_2a_{n-2}+c_3$, $a_0=0,a_1=1,a_2=4,a_3=11,a_4=26$, 求通项",
          "代入解得$c_1=3,c_2=-2,c_3=1$. 齐次$A+B2^n$, 特解$-n$. 初值得$a_n=2^{n+1}-n-2$.",
          "2022 Quiz4 3"]
       ]}
    ]
  },
  {
    "id": "ch9",
    "name": "Ch9: 关系",
    "points": [
      {"id":"ch9-trans","name":"传递闭包与Warshall算法","freq":2,"diff":"★★☆",
       "qs":[
         ["求$R$在$\\{a,b,c,d\\}$上的传递闭包, $R=\\{(a,a),(b,a),(b,c),(c,a),(c,c),(c,d),(d,a),(d,c)\\}$",
          "Warshall算法逐轮引入中间节点. $R^*=\\{(a,a),(b,a),(b,c),(b,d),(c,a),(c,c),(c,d),(d,a),(d,c),(d,d)\\}$.",
          "2022 Quiz3 1"],
         ["给定$R=\\{(C,A),(A,B),(B,D),(D,E),(E,B)\\}$, 求传递闭包",
          "关系图有环$B\\to D\\to E\\to B$. $R^+$为所有可达对共16个有序对.",
          "Final 2022 Q3-1"]
       ]},
      {"id":"ch9-closure","name":"自反对称传递闭包构造","freq":1,"diff":"★★☆",
       "qs":[
         ["$R=\\{(a,a),(a,b),(b,d),(a,d)\\}$在$\\{a,b,c,d\\}$上, 求最小偏序和对称传递关系",
          "偏序: 加自反过来$(b,b),(c,c)$, 得$R'=17$个有序对. 对称传递: 取对称闭包再加传递闭包, $a,b,d$两两相连.",
          "2024 Quiz3 1"]
       ]},
      {"id":"ch9-hasse-gen","name":"Hasse图构造(关系法)","freq":1,"diff":"★★☆",
       "qs":[
         ["求$\\{a,b,c,d,e,f\\}$上包含$(a,c),(c,b),(c,d),(b,e),(b,f)$的最小偏序, 画Hasse图, 求极值元",
          "加自反和传递得17对. Hasse: $a\\to c\\to b\\to e/f$及$c\\to d$. 极大$d,e,f$, 极小$a$, 最小元$a$, 无最大元. $\\{d,e\\}$无上界.",
          "2022 Quiz3 2"]
       ]},
      {"id":"ch9-hasse-div","name":"Hasse图(整除格)","freq":1,"diff":"★★☆",
       "qs":[
         ["$S=\\{2,3,5,6,12,20,27,36,60\\}$按整除画Hasse图, 求极值元",
          "覆盖: $2\\to6,3\\to6,3\\to27,5\\to20,6\\to12,12\\to36,12\\to60,20\\to60$. 极大27,36,60. $\\{2,3\\}$的上界6,12,36,60.",
          "2024 Quiz3 7"]
       ]},
      {"id":"ch9-equiv","name":"等价关系计数(Bell数)","freq":2,"diff":"★★☆",
       "qs":[
         ["$n=4$时等价关系数",
          "等价关系$\\iff$划分. $|A|=4$划分数$=1+4+3+6+1=15$即$B_4=15$.",
          "2022 Quiz2 4e"],
         ["$|A|=4$, 求等价关系数",
          "与上同, $B_4=15$.",
          "2024 Quiz3 6"]
       ]},
      {"id":"ch9-relcnt-basic","name":"关系计数(自反对称等)","freq":1,"diff":"★★★",
       "qs":[
         ["$n$元集上满足条件的关系数: (a)自反对称 (b)对称且反对称 (c)既不自反也不反自反",
          "(a)$2^{n(n-1)/2}$. (b)$2^n$. (c)$(2^n-2)\\cdot2^{n(n-1)}$.",
          "2022 Quiz2 4"]
       ]},
      {"id":"ch9-relcnt-special","name":"关系计数(传递偏序等)","freq":1,"diff":"★★★",
       "qs":[
         ["$n$元集上满足条件: (d)$n=2$传递关系数 (e)$n=4$等价关系数 (f)$n=2$偏序关系数",
          "(d)13种. (e)15种. (f)3种.",
          "2022 Quiz2 4"]
       ]}
    ]
  },
  {
    "id": "ch10",
    "name": "Ch10: 图论",
    "points": [
      {"id":"ch10-dijkstra","name":"Dijkstra最短路径","freq":2,"diff":"★★☆",
       "qs":[
         ["用Dijkstra算法求1到6的最短路径, 有向边: 1-2:1,1-3:12,2-3:9,2-4:3,3-5:5,4-3:4,4-5:13,4-6:15,5-6:4",
          "逐步运行Dijkstra, dist[6]=17. 路径: $1\\to2\\to4\\to3\\to5\\to6$, 总长$1+3+4+5+4=17$.",
          "2022 Quiz3 4"],
         ["Dijkstra在$n$顶点图中的最坏时间复杂度",
          "简单数组$O(n^2)$. 二叉堆$O((n+E)\\log n)$. 斐波那契堆$O(E+n\\log n)$.",
          "2024 Quiz4 1g"]
       ]},
      {"id":"ch10-iso-q3","name":"图同构(Q3图判定)","freq":1,"diff":"★★☆",
       "qs":[
         ["判断Fig.1和Fig.2的两图是否同构",
          "两图均为$Q_3$的不同画法(8顶点, 各度3, 12边). 存在一一对应保持边结构, 故同构.",
          "2022 Quiz3 8"]
       ]},
      {"id":"ch10-iso-invar","name":"图同构(不变量法)","freq":1,"diff":"★★☆",
       "qs":[
         ["判断给定的一对图是否同构",
          "检查顶点度序列/环长分布等不变量, 一致则尝试构造同构映射.",
          "2024 Quiz3 9"]
       ]},
      {"id":"ch10-euler","name":"欧拉回路/通路判定","freq":2,"diff":"★★☆",
       "qs":[
         ["网格图$G_{m,n}$($m\\le n$)哪些有欧拉回路/通路?",
          "欧拉回路: 所有顶点度偶, $G_{1,1}$和$G_{2,2}$. 欧拉通路无回路: 恰2奇度顶点, $G_{1,n}(n\\ge2)$和$G_{2,3}$.",
          "2022 Quiz4 4ab"]
       ]},
      {"id":"ch10-hamilton-grid","name":"网格图哈密顿回路","freq":2,"diff":"★★☆",
       "qs":[
         ["网格图$G_{m,n}$哪些有哈密顿回路/通路?",
          "回路: $m,n\\ge2$且至少一个偶. 通路无回路: $m=1$或$m,n$皆奇.",
          "2022 Quiz4 4cd"],
         ["判断12顶点网格图是否有哈密顿回路",
          "存在: $a\\to b\\to f\\to j\\to k\\to g\\to c\\to d\\to h\\to l\\to i\\to e\\to a$.",
          "2024 Quiz4 1f"]
       ]},
      {"id":"ch10-hypercube-prop","name":"$Q_n$综合性质","freq":1,"diff":"★★★",
       "qs":[
         ["$Q_n$的顶点数/边数/欧拉回路/哈密顿/色数/平面性?",
          "顶点$2^n$, 边$n\\cdot2^{n-1}$. 欧拉回路$n$偶时有. 哈密顿回路$n\\ge2$时有. 色数2(二分图). 平面$Q_1,Q_2,Q_3$.",
          "Final 2022 Q4-2"]
       ]},
      {"id":"ch10-hypercube-calc","name":"$Q_5$具体计算","freq":1,"diff":"★★☆",
       "qs":[
         ["求$Q_5$边数/色数, 判断是否有哈密顿回路",
          "$|E(Q_5)|=5\\cdot2^4=80$. 色数$\\chi(Q_5)=2$. $Q_5$有哈密顿回路.",
          "2024 Quiz3 10"]
       ]},
      {"id":"ch10-planar-calc","name":"欧拉公式计算区域数","freq":2,"diff":"★★☆",
       "qs":[
         ["连通平面图20顶点各度3, 求区域数",
          "$2E=60$, $E=30$. $V-E+F=2$, $F=12$.",
          "2024 Quiz4 1c"]
       ]},
      {"id":"ch10-planar-nonplanar","name":"欧拉公式证非平面图","freq":2,"diff":"★★☆",
       "qs":[
         ["用欧拉公式证$K_{3,3}$非平面",
          "$n=6,m=9$. $f=5$. $K_{3,3}$无奇环, 每个面边界$\\ge4$, 面度和$\\ge20$, 但$2m=18<20$, 矛盾.",
          "2022 Quiz3 6"],
         ["Petersen图非平面的欧拉公式证明",
          "$n=10,m=15$. $f=7$. 最小环长5, 面和$\\ge35$, $2m=30<35$, 矛盾.",
          "2022 Quiz3 8c"]
       ]},
      {"id":"ch10-color-basic","name":"图的色数判定","freq":2,"diff":"★★☆",
       "qs":[
         ["求Petersen图的色数",
          "3-正则含奇环(长5), 色数$\\ge3$. 可3-着色, 故$=3$.",
          "2022 Quiz3 8a"]
       ]},
      {"id":"ch10-color-poly","name":"正多面体着色","freq":1,"diff":"★★☆",
       "qs":[
         ["求正四面体/正方体/正八面体的色数",
          "正四面体$(K_4)$: $\\chi=4$. 正方体(二分图): $\\chi=2$. 正八面体: $\\chi=3$.",
          "2022 Quiz4 5b"]
       ]},
      {"id":"ch10-maflow","name":"最大流与最小割","freq":1,"diff":"★★★",
       "qs":[
         ["在给定的网络中求A到J的最大流并证明",
          "用增广路径法得最大流15. 割{A,B,C,D,F,H,I}/{G,J}容量15. 由最小割定理确认.",
          "2024 Quiz3 8"]
       ]},
      {"id":"ch10-petersen","name":"Petersen图综合","freq":2,"diff":"★★★",
       "qs":[
         ["Petersen图色数/平面性/哈密顿?",
          "色数3. 非平面(欧拉公式). 非哈密顿(有哈密顿路径).",
          "2022 Quiz3 8"]
       ]},
      {"id":"ch10-tournament","name":"竞赛图哈密顿路径","freq":1,"diff":"★★★",
       "qs":[
         ["证$n$选手循环赛可排成$p_1,\\ldots,p_n$使$p_i$击败$p_{i+1}$",
          "对$n$归纳. 去掉$v$, 余者有路径$p_1\\to\\cdots\\to p_k$. 若$v$击败$p_1$放开头; 若$p_k$击败$v$放末尾; 否则存在$i$使$p_i$击败$v$且$v$击败$p_{i+1}$, 插入中间.",
          "2022 Quiz3 7"]
       ]},
      {"id":"ch10-poly","name":"正多面体分类(欧拉公式)","freq":1,"diff":"★★★",
       "qs":[
         ["用欧拉定理证明凸正多面体只有5种",
          "$pF=2E,qV=2E$, 代入欧拉公式得$(p-2)(q-2)<4$, $p,q\\ge3$. 解为(3,3),(3,4),(4,3),(3,5),(5,3)对应5种柏拉图立体.",
          "2022 Quiz4 5c"]
       ]}
    ]
  },
  {
    "id": "ch11",
    "name": "Ch11: 树",
    "points": [
      {"id":"ch11-kruskal-exec","name":"Kruskal算法执行","freq":2,"diff":"★★☆",
       "qs":[
         ["求带权图MST, 边权:6-7:1,2-8:2,5-6:2,0-1:4,2-5:4,2-3:7,0-7:8,3-4:9",
          "Kruskal升序选:6-7(1),2-8(2),5-6(2),0-1(4),2-5(4),2-3(7),0-7(8),3-4(9). MST总重37.",
          "2022 Quiz3 3"]
       ]},
      {"id":"ch11-kruskal-method","name":"MST构造方法","freq":1,"diff":"★★☆",
       "qs":[
         ["Kruskal算法求MST并写出边的添加顺序",
          "边权升序排序, 依次选不形成环的边至全部连通.",
          "2024 Quiz3 2a"]
       ]},
      {"id":"ch11-huffman-code","name":"Huffman编码构造","freq":2,"diff":"★★☆",
       "qs":[
         ["对频率a:0.15,b:0.22,c:0.26,d:0.19,e:0.08,f:0.1做Huffman编码, 求平均码长",
          "d:2位,b:2位,c:2位,a:3位,e:4位,f:4位. 平均$=0.15\\times3+0.22\\times2+0.26\\times2+0.19\\times2+0.08\\times4+0.10\\times4=2.51$位/字符.",
          "2022 Quiz3 5"]
       ]},
      {"id":"ch11-huffman-avg","name":"Huffman平均码长计算","freq":1,"diff":"★★☆",
       "qs":[
         ["频率0.09,0.05,0.2,0.25,0.3,0.11的Huffman编码平均码长",
          "c:2,f:3,b:4,a:4,d:2,e:2. 平均$=2.39$位/字符.",
          "2024 Quiz3 3"]
       ]},
      {"id":"ch11-mary","name":"满$m$-ary树叶子数","freq":1,"diff":"★☆☆",
       "qs":[
         ["满7-ary树有2024顶点, 求叶子数",
          "$n=mi+1$, $i=(n-1)/m$. 叶子$l=n-i=((m-1)n+1)/m$. 代入$m=7,n=2024$得$l=1735$.",
          "2024 Quiz3 4"]
       ]},
      {"id":"ch11-tree","name":"$K_{r,s}$为树的判定","freq":1,"diff":"★☆☆",
       "qs":[
         ["求使$K_{r,s}$为树的正整数$r,s$",
          "$rs=r+s-1$. $(r-1)(s-1)=0$, $r=1$或$s=1$. 即星形图$K_{1,s}$或$K_{r,1}$.",
          "2024 Quiz3 5"]
       ]},
      {"id":"ch11-degree","name":"树的顶点度数与叶子计数","freq":1,"diff":"★★☆",
       "qs":[
         ["树有7叶子, 3内点度3, 余内点度4. 求度4内点个数",
          "设$x$个度4. $V=10+x$, $E=9+x$. $2(9+x)=7+9+4x$, $x=1$.",
          "Final 2022 Q4-1"]
       ]},
      {"id":"ch11-dfs","name":"DFS生成树","freq":1,"diff":"★★☆",
       "qs":[
         ["用DFS按字母序从$a$开始求图的生成树",
          "DFS序: $a\\to b\\to d\\to c\\to e$(回溯)$\\to f$. 生成树边: $a-b,b-d,d-c,c-e,b-f$.",
          "2024 Quiz3 2b"]
       ]}
    ]
  },
  {
    "id": "ch-extra",
    "name": "其他综合",
    "points": [
      {"id":"extra-poker-four","name":"扑克牌牌型(四条)","freq":1,"diff":"★★☆",
       "qs":[
         ["52张牌, 求四条(Four of a kind, xxxx y)的个数",
          "选点数$\\binom{13}{1}=13$, 全取该点数4张$\\binom{4}{4}=1$, 选第5张点数$\\binom{12}{1}=12$, 选花色$\\binom{4}{1}=4$, 总计$13\\times12\\times4=624$.",
          "2024 Quiz4 3a"]
       ]},
      {"id":"extra-poker-two","name":"扑克牌牌型(两对)","freq":1,"diff":"★★☆",
       "qs":[
         ["52张牌, 求两对(Two pairs, xx yy z, 无三条)的个数",
          "选两对点数$\\binom{13}{2}=78$, 对子1选花色$\\binom{4}{2}=6$, 对子2选花色$\\binom{4}{2}=6$, 第5张点数$\\binom{11}{1}=11$, 花色$\\binom{4}{1}=4$, 总计$78\\times6\\times6\\times11\\times4=123552$.",
          "2024 Quiz4 3b"]
       ]},
      {"id":"extra-setcnt","name":"集合计数(包含排斥)","freq":1,"diff":"★★☆",
       "qs":[
         ["$A\\cup B\\cup C=\\{1,2,3,4,5\\}$, $A\\cap B=\\{1,2\\}$, 求$(A,B,C)$组合数",
          "1,2必在$A\\cap B$, 各2种. 3,4,5各有5种合法状态. 总数$=4\\times125=500$.",
          "Final 2022 Q4-3"]
       ]},
      {"id":"extra-team","name":"球队分组计数(二项式定理)","freq":1,"diff":"★★☆",
       "qs":[
         ["$n$球员, 选偶$k$人分红蓝两队, 求所有偶$k$的分组方式总数",
          "总和$\\sum_{k\\text{偶}}\\binom{n}{k}2^k=(3^n+(-1)^n)/2$.",
          "Final 2022 Q4-4"]
       ]},
      {"id":"extra-subset","name":"和差整除子集构造","freq":1,"diff":"★★★",
       "qs":[
         ["$S=\\{1,\\ldots,2022\\}$, 求最大子集$T$使$a\\neq b$时$a+b$不被$|a-b|$整除",
          "取$T=\\{1,4,7,\\ldots,2020\\}$($\\equiv1\\pmod{3}$). $d=3(j-i)\\nmid2a=2+6i$. $|T|=674$.",
          "Final 2022 Q4-3"]
       ]},
      {"id":"extra-dom","name":"最小支配集","freq":1,"diff":"★★☆",
       "qs":[
         ["12顶点网格图加额外边, 求最小支配集的顶点数",
          "可取$\\{b,e,h,k\\}$支配全部12顶点. 3个顶点不够, 故最小支配集为4.",
          "2024 Quiz4 1e"]
       ]},
      {"id":"extra-scc","name":"强连通分量与传递闭包","freq":1,"diff":"★★☆",
       "qs":[
         ["给定有向图, 求强连通分量和传递闭包",
          "SCC用Kosaraju或Tarjan算法. 传递闭包用Warshall算法$O(n^3)$.",
          "Final 2022 Q3-3"]
       ]},
      {"id":"extra-partial","name":"偏序关系计数(Dedekind数)","freq":1,"diff":"★★★",
       "qs":[
         ["3元集上有多少种不同的偏序关系?",
          "$n=3$时Dedekind数为19. 可枚举Hasse图结构: 反链1, 含1可比3, 链+孤立3, V形3, L形3, 全序扩展变形3, 共计19.",
          "Final 2022 Q2"]
       ]},
      {"id":"extra-prefix","name":"字符串前缀后缀(容斥原理)","freq":1,"diff":"★★☆",
       "qs":[
         ["求满足至少一个条件的字符串个数: 以66开头, 或以5开头, 或以88结尾",
          "用容斥原理$|A\\cup B\\cup C|=|A|+|B|+|C|-|A\\cap B|-|A\\cap C|-|B\\cap C|+|A\\cap B\\cap C|$.",
          "Final 2022 Q4-9"]
       ]}
    ]
  }
]
'''

import json

def gen_html():
    chapters = json.loads(chapters_raw)

    total_points = sum(len(ch["points"]) for ch in chapters)
    total_freq = sum(p["freq"] for ch in chapters for p in ch["points"])

    # Build top 16
    all_pts = [(p["freq"], p["name"], ch["id"]) for ch in chapters for p in ch["points"]]
    all_pts.sort(key=lambda x: (-x[0], x[1]))
    top16 = all_pts[:16]

    # Build chapter nav
    ch_nav = "".join(
        f'<a href="#{ch["id"]}" class="nav-link">{ch["id"].replace("ch","Ch").replace("-extra","综合")}</a>'
        for ch in chapters
    )

    h = f'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>DMA 历年真题考点总清单 -- 交互式复习</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.js"></script>
<script defer src="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/contrib/auto-render.min.js"
  onload="renderMathInElement(document.body,{{delimiters:[{{left:\'$$\',right:\'$$\',display:true}},{{left:\'$\',right:\'$\',display:false}}],throwOnError:false}});"></script>
<style>
:root {{
  --bg: #f5f7fa; --card: #ffffff; --text: #1e293b; --text-light: #64748b;
  --border: #e2e8f0; --accent: #2563eb; --accent-light: #eff6ff;
  --green: #16a34a; --green-light: #f0fdf4; --amber: #d97706;
  --red: #dc2626; --red-light: #fef2f2; --purple: #7c3aed;
  --radius: 10px; --shadow: 0 1px 3px rgba(0,0,0,.06);
}}
* {{ box-sizing: border-box; margin: 0; padding: 0; }}
html {{ scroll-behavior: smooth; }}
body {{
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, 'Noto Sans SC', sans-serif;
  background: var(--bg); color: var(--text); line-height: 1.7; padding: 20px;
}}
.container {{ max-width: 1000px; margin: 0 auto; }}
/* Header */
header {{
  background: linear-gradient(135deg,#1e293b 0%,#334155 50%,#475569 100%);
  color: #fff; padding: 28px 32px; border-radius: var(--radius); margin-bottom: 20px;
}}
header h1 {{ font-size: 1.5rem; font-weight: 700; }}
header .sub {{ font-size: .85rem; opacity: .75; margin-top: 6px; }}
/* Stats */
.stats {{ display: grid; grid-template-columns: repeat(4,1fr); gap: 10px; margin-bottom: 18px; }}
.stat-card {{
  background: var(--card); border-radius: var(--radius); padding: 16px 12px;
  text-align: center; box-shadow: var(--shadow); border-left: 4px solid var(--accent);
}}
.stat-card:nth-child(2) {{ border-left-color: var(--purple); }}
.stat-card:nth-child(3) {{ border-left-color: var(--green); }}
.stat-card:nth-child(4) {{ border-left-color: var(--amber); }}
.stat-card .val {{ font-size: 1.6rem; font-weight: 800; color: var(--accent); }}
.stat-card:nth-child(2) .val {{ color: var(--purple); }}
.stat-card:nth-child(3) .val {{ color: var(--green); }}
.stat-card:nth-child(4) .val {{ color: var(--amber); }}
.stat-card .label {{ font-size: .75rem; color: var(--text-light); margin-top: 2px; }}
/* Controls */
.controls {{ display: flex; gap: 8px; flex-wrap: wrap; align-items: center; margin-bottom: 16px; }}
.btn {{
  padding: 7px 16px; border: none; border-radius: 6px; font-size: .82rem;
  font-weight: 600; cursor: pointer; transition: all .15s; background: var(--accent); color: #fff;
}}
.btn:hover {{ opacity: .85; }}
.btn-outline {{ background: var(--card); color: var(--text); border: 1px solid var(--border); }}
.btn-outline:hover {{ background: var(--accent-light); border-color: var(--accent); color: var(--accent); }}
/* Nav links */
.nav-links {{
  display: flex; gap: 4px; flex-wrap: wrap; margin-bottom: 18px;
  background: var(--card); padding: 8px 12px; border-radius: var(--radius);
  box-shadow: var(--shadow); align-items: center;
}}
.nav-link {{
  padding: 3px 10px; border-radius: 5px; font-size: .8rem; font-weight: 500;
  text-decoration: none; color: var(--text-light); transition: all .1s;
}}
.nav-link:hover {{ background: var(--accent-light); color: var(--accent); }}
/* Top 16 */
.top-wrap {{ background: var(--card); border-radius: var(--radius); box-shadow: var(--shadow); overflow: hidden; margin-bottom: 20px; }}
.top-title {{ font-size: 1.05rem; font-weight: 700; padding: 14px 16px 0; }}
.top-title small {{ font-size: .78rem; font-weight: 400; color: var(--text-light); }}
.top-table {{ width: 100%; border-collapse: collapse; font-size: .82rem; }}
.top-table th {{ background: #f8fafc; padding: 8px 12px; text-align: left; font-weight: 600; font-size: .75rem; color: var(--text-light); border-bottom: 2px solid var(--border); }}
.top-table td {{ padding: 7px 12px; border-bottom: 1px solid #f1f5f9; }}
.top-table tr:hover td {{ background: #f8fafc; }}
.rank-hot td {{ color: var(--red); font-weight: 700; }}
/* Chapter */
.chapter {{ margin-bottom: 18px; scroll-margin-top: 12px; }}
.chapter > details {{
  background: var(--card); border-radius: var(--radius); box-shadow: var(--shadow); overflow: hidden;
}}
.chapter > details > summary {{
  padding: 13px 16px; cursor: pointer; font-size: 1rem; font-weight: 700;
  color: var(--accent); display: flex; align-items: center; justify-content: space-between;
  transition: background .12s; list-style: none;
}}
.chapter > details > summary::-webkit-details-marker {{ display: none; }}
.chapter > details > summary:hover {{ background: var(--accent-light); }}
.chapter > details[open] > summary {{ border-bottom: 1px solid var(--border); }}
.ch-info {{ font-size: .78rem; font-weight: 400; color: var(--text-light); white-space: nowrap; }}
.chapter-body {{ padding: 2px 0; }}
/* Point */
.point {{ border-bottom: 1px solid #f1f5f9; }}
.point:last-child {{ border-bottom: none; }}
.point > summary {{
  padding: 10px 16px; cursor: pointer; font-size: .9rem; font-weight: 500;
  display: flex; align-items: center; gap: 8px; flex-wrap: wrap;
  transition: background .08s; list-style: none;
}}
.point > summary::-webkit-details-marker {{ display: none; }}
.point > summary:hover {{ background: #f8fafc; }}
.point-name {{ flex: 1; }}
.badge {{ display: inline-block; padding: 1px 7px; border-radius: 8px; font-size: .68rem; font-weight: 700; white-space: nowrap; }}
.b-freq {{ background: var(--accent-light); color: var(--accent); }}
.b-diff {{ background: #fef3c7; color: #92400e; }}
/* Q&A */
.qa-item {{ margin: 8px 0; border-radius: 6px; overflow: hidden; }}
.qa-q {{
  background: #f8fafc; padding: 10px 12px; border-left: 3px solid var(--border);
  font-size: .85rem;
}}
.qa-label {{ font-weight: 700; font-size: .72rem; display: block; margin-bottom: 2px; color: var(--text-light); }}
.qa-a {{
  background: var(--accent-light); padding: 10px 12px; border-left: 3px solid var(--accent);
  font-size: .85rem;
}}
.qa-a .qa-label {{ color: var(--accent); }}
.qa-year {{ font-size: .72rem; color: var(--text-light); margin-top: 3px; font-style: italic; }}
details {{ transition: all .1s; }}
footer {{ text-align: center; padding: 20px; color: var(--text-light); font-size: .78rem; }}
@media (max-width:640px) {{
  .stats {{ grid-template-columns: repeat(2,1fr); }}
  header {{ padding: 20px 18px; }}
  header h1 {{ font-size: 1.2rem; }}
  .top-table {{ font-size: .75rem; }}
  .point > summary {{ padding: 8px 12px; }}
}}
</style>
</head>
<body>
<div class="container">

<header>
  <h1>DMA 历年真题考点总清单</h1>
  <div class="sub">
    郑文庭班 &middot; Quiz1-4 (2022-2025) + 期末回忆卷 (2022) &middot;
    共 <strong>{total_points}</strong> 个考点 / <strong>{total_freq}</strong> 频次
  </div>
</header>

<div class="stats">
  <div class="stat-card"><div class="val">{total_points}</div><div class="label">独特考点</div></div>
  <div class="stat-card"><div class="val">{len(chapters)}</div><div class="label">章节数</div></div>
  <div class="stat-card"><div class="val">{total_freq//total_points if total_points else 0}</div><div class="label">平均频次</div></div>
  <div class="stat-card"><div class="val">{len(top16)}</div><div class="label">高频考点</div></div>
</div>

<div class="controls">
  <button class="btn" onclick="toggleAll(true)">展开全部</button>
  <button class="btn btn-outline" onclick="toggleAll(false)">折叠全部</button>
</div>

<div class="nav-links">
  <span style="font-size:.78rem;color:var(--text-light);font-weight:600;padding:2px 4px;">跳转:</span>
  {ch_nav}
</div>

<!-- Top16 -->
<div class="top-wrap">
  <div class="top-title">高频考点 TOP16 <small>(出现 3 次及以上)</small></div>
  <table class="top-table">
    <tr><th style="width:30px">#</th><th>考点</th><th style="width:50px">频次</th><th style="width:50px">难度</th></tr>
'''
    for i, (freq, name, ch_id) in enumerate(top16):
        rk = "rank-hot" if freq >= 4 else ""
        # Find difficulty
        diff = "★★☆"
        for ch in chapters:
            for p in ch["points"]:
                if p["name"] == name:
                    diff = p["diff"]
                    break
        h += f'    <tr class="{rk}"><td>{i+1}</td><td>{escape(name)}</td><td style="font-weight:700">{freq}</td><td>{diff}</td></tr>\n'
    h += '''  </table>
</div>

'''

    for ch in chapters:
        ch_freq = sum(p["freq"] for p in ch["points"])
        h += f'<div class="chapter" id="{ch["id"]}">\n'
        h += f'  <details>\n'
        h += f'    <summary><span>{escape(ch["name"])}</span><span class="ch-info">{len(ch["points"])} 考点 / {ch_freq} 频次</span></summary>\n'
        h += f'    <div class="chapter-body">\n'

        for p in ch["points"]:
            h += f'      <details class="point">\n'
            h += f'        <summary><span class="point-name">{escape(p["name"])}</span><span class="badge b-freq">{p["freq"]}</span><span class="badge b-diff">{p["diff"]}</span></summary>\n'
            h += f'        <div class="point-body" style="padding:0 16px 12px;">\n'

            for q_text, a_text, year in p["qs"]:
                h += f'          <div class="qa-item">\n'
                h += f'            <div class="qa-q"><span class="qa-label">题目</span>{q_text}<div class="qa-year">{year}</div></div>\n'
                h += f'            <div class="qa-a"><span class="qa-label">解答</span>{a_text}</div>\n'
                h += f'          </div>\n'

            h += f'        </div>\n'
            h += f'      </details>\n'

        h += f'    </div>\n'
        h += f'  </details>\n'
        h += f'</div>\n'

    h += '''
<script>
function toggleAll(open) {
  document.querySelectorAll('.chapter > details').forEach(d => d.open = open);
  document.querySelectorAll('.point').forEach(d => d.open = open);
}
</script>

<footer>生成于 2026-06-27 &middot; DMA 期末复习 &middot; 郑文庭班</footer>

</div>
</body>
</html>
'''
    return h

if __name__ == '__main__':
    h = gen_html()
    path = '/Users/hechenyu/end-term/dma/qa/exam-checklist.html'
    with open(path, 'w', encoding='utf-8') as f:
        f.write(h)
    print(f"Written {len(h)} bytes ({len(h)//1024} KB) to {path}")
    import json
    chs = json.loads(chapters_raw)
    total = sum(len(c["points"]) for c in chs)
    freq_tot = sum(p["freq"] for c in chs for p in c["points"])
    print(f"Total exam points: {total}")
    print(f"Total frequency: {freq_tot}")
