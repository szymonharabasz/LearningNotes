**Ring**: A set with two operations, $(R, +, \cdot, 0)$, where $(R,+,0)$ is an abelian group, and $(R, \cdot)$ is a semigroup, that is, the operation $\cdot$ is *associative*, $a\cdot(b\cdot c) = (a\cdot b)\cdot c$, and $\cdot$ is distributive with respect to $+$:
- $a\cdot(b+c) = (a\cdot b) + (a\cdot b)$
- $(b+c)\cdot a = (b\cdot a) + (b\cdot a)$
An **integral domain** is a ring in which a product of two non-zero elements is non-zero.
**Ring of sets**: A family $\cal R$ of subsets of $\mathbb R$, such that for $A, B\in\cal{R}$:
- $A\cup B\in\cal{R}$
- $A-B\in\cal{R}$
If also for each countable collection of $A_n$ in $\cal R$ it follows that $\bigcup_{n=1}^\infty A_n\in\cal{R}$, them $\cal R$ is a **$\sigma$-ring**. If it is also an algebra (it contains $\mathbb R$), is it **$\sigma$-algebra**. 

If $\cal R$ is a $\sigma$-ring, then a **positive measure** on $\cal R$ is a function $\mu:\cal{R}\rightarrow[0,\infty)$ , satisfying:
- $\mu(\varnothing) = 0$
- countable additivity: if $\{A_n\}_{n=1}$  is *pairwise disjoint*, then:
$$
\mu\left(\bigcup_{n=1}^\infty A_n\right)=\sum_{n=1}^\infty\mu(A_n).
$$
It has properties of:
- monotonicity
- continuity for increasing unions
- continuity for decreasing intersections
- countable subadditivity (for not necessarily disjoint subsets):
$$
\mu\left(\bigcup_{n=1}^\infty A_n\right)\leq\sum_{n=1}^\infty\mu(A_n).
$$

**Elementary subsets in $\mathbb R$** are finite unions of disjoint intervals. Their set is denoted $\cal{E}$. We define a measure $m:\cal{E}\rightarrow[0\infty)$ by:
- $m(\varnothing)=0$
- For a disjoint union of intervals $I_n$:
$$
m\left(\bigcup_{n=1}^N I_n\right)=\sum_{n=1}^N{\cal l}(I_n),
$$
where ${\cal l}(I_n)$ is the length of $I_n$.

For $A\subseteq\mathbb{R}$, the **outer measure** of $A$ is defined by
$$
m^*(A)=\inf\left\{\sum_{n=1}^\infty{\cal l}(I_n): 
I_n \rm{~is~an~open~interval~and~} 
A\subseteq\bigcup_{n=1}^\infty I_n
\right\}.
$$
It has the properties:
- It is well defined, although it may have infinite value
- $m^*(\varnothing)=0$ and $m^*(\{a\})=0$
- preserves $m$, i.e., if $A\subseteq{\cal E}$, then $m^*(A) =m(A)$
- monotonicity
- countable subaddtivity

A semi-metric on the set of subsets of $\mathbb R$ can be defined by:
$$
d(A,B)=m^*(A\Delta B),
$$
where $\Delta$ denotes the symmetric difference of sets.

We denote by $\overline {\cal E}$ the collection of subsets $A\subseteq\mathbb{R}$ for which there is a sequence $(A_n)$ in $\cal E$ with $\lim_{n\rightarrow\infty}d(A_n,A)=0$. *{\cal E} is a ring of sets and $m^*$ is a measure on $\overline {\cal E}$.* 
For a pairwise *disjoint collection* $\{A_n\}_{n=1}^\infty$ in $\overline{\cal E}$ such that $\bigcup_{n=1}A_n=A$:
$$
m^*(A)=\sum_{n=1}^\infty m^*(A_n).
$$
We denote by $\cal L$ the collection of subsets of $\mathbb R$ which can be written as a countable union of sets in $\overline{\cal E}$. Provided $A\in{\cal L}$, then $A\in\overline{\cal E}$ iff $m^*(A)<\infty$. The collection $\cal L$ is a $\sigma$-algebra in $\mathbb R$ and $m^*$ is countably additive on ${\cal L}$. It is called the **Lebesgue measurable subsets of $\mathbb R$**. and the measure defined on $\cal L$ by $m(A)=m^*(A)$ is called the **Lebesgue measure on $\mathbb R$**. We also define smaller collections of Lebesgue measurable sets:
$$
{\cal L}(A)=\{B\in{\cal L}: B\subseteq A\}.
$$