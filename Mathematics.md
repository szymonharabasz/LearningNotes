**Zorn's Lemma:** If $(P,\leq)$ is a partially ordered set (poset) with the property that every partially ordered subset is bounded from above, then $P$ has a maximal element.
**Ring**: A set with two operations, $(R, +, \cdot, 0)$, where $(R,+,0)$ is an abelian group, and $(R, \cdot)$ is a semigroup, that is, the operation $\cdot$ is *associative*, $a\cdot(b\cdot c) = (a\cdot b)\cdot c$, and $\cdot$ is distributive with respect to $+$:
- $a\cdot(b+c) = (a\cdot b) + (a\cdot b)$
- $(b+c)\cdot a = (b\cdot a) + (b\cdot a)$
An **integral domain** is a ring in which a product of two non-zero elements is non-zero.
**Ring of sets**: A family $\cal R$ of subsets of $\mathbb R$, such that for $A, B\in\cal{R}$:
- $A\cup B\in\cal{R}$
- $A-B\in\cal{R}$
If also for each countable collection of $A_n$ in $\cal R$ it follows that $\bigcup_{n=1}^\infty A_n\in\cal{R}$, them $\cal R$ is a **$\sigma$-ring**. If it is also an algebra (it contains $\mathbb R$), is it **$\sigma$-algebra**. 
#### Measure and integral
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
- **only** countable subaddtivity
It is countably additive on pairwise disjoint **compact** sets.

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
1. **Null sets** Given $\epsilon>0$, there exists a sequence of intervals $\{I_n:n\geq1\}$ wuch that
$$
A\subseteq\bigcup_{n=1}I_n
$$
and
$$
\sum_{n=1}^\infty l(I_n)<\epsilon.
$$
2. Countable union of null sets is null.
3. Outer measure of any set $A\subseteq\mathbb{R}$ is given by
	$$
	m^*(A)=\inf Z_A
	$$
	$$
	Z_A=\left\{
	\sum_{n=1}^\infty l(I_n):I_n\text{ are intervals, }
	A\subseteq\bigcup_{n=1}^\infty I_n
	\right\}.
	$$
4. Properties of outer measures:-
	- $A\subseteq\mathbb{R}$ is null if and only if $m^*(A)=0$.
	- If $A\subset B$, then $m^*(A)\leq m^*(B)$.
	- $m^*(I) = l(I)$
	- Outer measure is countably **subadditive**
	- Outer measure is **translation-invariant**
5. A set $E\subseteq\mathbb{R}$ is **Lebesgue-measurable** if for every $A\subseteq\mathbb{R}$ we have
	$$
	m^*(A)=m^*(A\cap E)+m^*(A\cap E^c)
	$$
	and we write $E\in{\cal M}$, 
6. Properties:
	- Any null set is measurable
	- Any interval is measurable
	- $\mathbb{R}\in{\cal M}$
	- If $E\in{\cal M}$ then $E^c\in{\cal M}$.
	- If $E_n\in{\cal M}$ for all $n=1,2,...$ then $\bigcup_{n=1}^\infty E_n\in{\cal M}$, if further $E_j\capE_k=\emptyset$ for $j\neq k$ then 
	  $$
	   m^*\left(\bigcup_{n=1}^\infty E_n\right)=
	   \sum_{n=1}^\infty m^*(E_n).
	   $$
	   For $A\in{\cal M}$ we write $m(A)$ instead of $m^*(A)$.
	- If $A\subset B$ and $m(A)$ is finite then $m(B\backslash A)=m(B)-m(A)$. 
	- If $A\in{\cal M}$ and $m(A\Delta B)=0$ then $B\in{\cal M}$ and $m(A)=m(B)$.
	- For any $\epsilon>0$ and $A\subset\mathbb{R}$ we can find an open set $O$ such that:
	  $$
	   A\subset O,~~~m(O)\leq m^*(A)+\epsilon
	   $$
	   and so for every $E\in{\cal M}$ we can find an open set $O$ containing $E$ such that $(O\backslash E)<\epsilon.$
	- For any $A\subset\mathbb{R}$ we can find a sequence of open sets $O_n$ such that
	  $$
	   A\subset\bigcap_nO_n,~~~m\left(\bigcap_nO_n\right)=m^*(A).
	   $$
	- Suppose that $A_n\in{\cal M}$ for all $n\geq 1$ Then if $A_n\subset A_{n+1}$ for all $n$,
	  $$
	   m(\bigcup_nA_n)=\lim_{n\rightarrow\infty}m(A_n),
	   $$
	  If $A_n\supset A_{n+1}$ for all $n$ and $m(A_1)<\infty$, 
	  $$
	   m(\bigcap_nA_n)=\lim_{n\rightarrow\infty}m(A_n).
	   $$
	- $m$ is a function continuous at $\emptyset$ 
7. A family of sets is called a **$\sigma$-field** if it contains a base set and is closed under complements and countable unions. A $[0\infty]$-valued function defined on a $\sigma$-field is called a **measure** if it is countably additive.
8. The intersection of a family of $\sigma$-fields is a $\sigma$-field.
9. We say that ${\cal G}$ is a $\sigma$-field generated by a family of sets $\cal A$ if
   $$
   {\cal G}=\bigcap\left\{{\cal F}:{\cal F}\text{ is a }\sigma
   \text{-field such that } {\cal F}\supset{\cal A}\right\}.
   $$
   We denote $\cal B$ the $\sigma$ field generated by all intervals and its elements **Borel sets**.
10. A measure space $(X, {\cal F}, \mu)$ is **complete** if for all $F\in{\cal F}$ with $\mu(F)=0$, for all $N\subset F$ we have $N\in{\cal F}$ (and so $\mu(N)=0$).
11. The **completion** of a $\sigma$-field ${\cal G}$, relative to $\mu$, is the smallest $\sigma$-field ${\cal F}\supset{\cal G}$ such that if $N\subset G\in{\cal G}$, and $\mu(G)=0$, then $N\in{\cal F}$.
12. The completion of $\cal G$ has the form
    $$
	    \left\{G\supset N:G\in{\cal G},N\subset F\in{\cal F}
    \text{ with }\mu{F}=0\right\}.      
    $$
13. $\cal M$ is the completion of $\cal B$.
14. If $E\in{\cal M}$, then for $\epsilon>0$ there exists a closed set $F\subset E$ such that $m(E\backslash F)<\epsilon$. Hence, there exists $B\subset E$ in the form $B=\bigcup_nF_n$, where all the $F_n$ are closed, and $m(E\backslash B)=0$.  
#### Topology
A topological space $(X\tau)$ is:
- **compact** if every open covering has a finite subcover.
- **Hausdorff** if every pair of disjoint points in $X$ have disjoint neighborhoods
- **normal** if for every pair of disjoint sets $A$, $B$ there exists a continuous function:
$$
f:X\rightarrow[0,1]: f(x)=0~\forall x\in A,~f(x)=1~\forall x\in B,~
0\leq f(x)\leq1~\forall x\in X.
$$
- a **regular space** if for every neighborhood $U$ of any point $p\in X$ there exists another neighborhood $U$ of $p$ such that $\overline{V}\subset U$.

**Heine-Borel** theorem states that a set in $\mathbb{R}^n$ is compact iff it is closed and bounded.
There is an isomorphism:
$$
{\rm im}T\cong V/{\rm ker}T.
$$
Also:
$$
u-v\in W\Rightarrow u+W=v+W.
$$
