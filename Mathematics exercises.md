# Real Analysis for the Undergraduate
###### Exercise 1.1.10 b
Let $p$ be a prime number. Show that there is no rational number which satisfies $r^2=p$.
**Answer** Assume that there is such a number, i.e., $\left(\frac{a}{b}\right)^2=p$ for $a\in\mathbb{Q}$, $b\in\mathbb{N}$  with $a$ and $b$ not having any common factor. Rearranging, we have:
$$
a^2=pb^2.
$$
So, $p$ divides $a^2$. By the Euclid's Lemma (*$p$ divides $ab$ if and only if $p$ divides $a$ or $p$ divides $b$*), $p$ divides $a$. Thus $a=pc$ for some $c\in\mathbb{Q}$ and we can rewrite:
$$
(pc)^2=p^2 c^2=pb^2.
$$
This gives:
$$
pc^2=b^2.
$$
But then $p$ divides $b^2$ and by the Euclid's Lemma it divides $b$. But this *contradicts* the assumption that $a$ and $b$ have no common factors. Therefore there is not such a number that $r^2=p$.
###### Exercise 1.1.11
For sets $A$ and $B$ we define a relation $A \sim B$ if $\rm{card}(A)=\rm{card}(B)$. Show that this is an equivalence relation.
**Answer** We say that two sets have the same cardinality if there is a bijection connecting them. For the relation $\rm{card}(A)=\rm{card}(B)$, the identity mapping $I: A\rightarrow A$ is bijective, so $\rm{card}(A)=\rm{card}(A)$ and $A\sim A$. 
If $A\sim B$ means that tbere is a bijection $f:A\rightarrow B$. This implies that there exists an inverse bijection $f^{-1}:B\rightarrow A$. Thus $B\sim A$.
If $\rm{card}(A)=\rm{card}(B)$ and $\rm{card}(B)=\rm{card}(C)$, then there exist $f: A\rightarrow B$ and $g:B\rightarrow C$, both bijective. This implies that $g\circ f: A\rightarrow C$ exists and is bijective and thus $\rm{card}(A)=\rm{card}(C)$.
###### Exercise 1.1.12
Let $A$ be an ucountable set and $B$ a countable set with $B\subseteq A$. Show that $A-B$ is uncountable.
**Answer** Denote $A-B=C$ and so $A=B\cup C$. Assume otherwise that $C$ is countable, so we can enumerate its elements as $C=\{c_1, c_2, c_3, ...\}$. But this means that we can enumerate the elements of $A$ for example as $A=\{b_1,c_1,b_2,c_2,b_3,c_3,...\}$. Thus $A$ is countable, contradicting the assumption.
###### Exercise 1.1.14
Write $\mathbb{Q}$ as a countable union of finite sets
**Answer** Denote by $A_{ijk}$ the set of rational numbers that can be written in the decimal representation as:
$$
a_i a_{i-1}...a_2a_1.b_1b_2...b_{j-1}b_j\overline{c_1c_2...c_{k-1}c_k},
$$
where overline signifies repeated digits in the decimal expansion. We can assume that $a_ic_k\neq0$ and if $\forall m\in\{1,...,k\}~c_m=0$, then $b_j\neq0$. Then each of these sets is finite, and their countable union,
$$
\bigcup_{i,j,k=0}^\infty A_{ijk}
$$
represents all the numbers with finite or repeated decimal expansion, that is, all $\mathbb{Q}$.
###### Exercise 1.1.15
Prove part (b) of Proposition 1.1.16: For each $n\in\mathbb{N}$ let $A_n$ be a countable set. Then $\bigcup_{n=1}^\infty A_n$ is countable.
**Answer** Generalizing the proof for $A_1\cup A_2$, we enumerate each $A_n$:
$$
\begin{split}
&A_1=\{a_{11},a_{12},a_{13},...\}\\
&A_2=\{a_{21},a_{22},a_{23},...\}\\
&...\\
&A_n=\{a_{n1},a_{n2},a_{n3},...\}\\
&...
\end{split}
$$
We can then define a function $f:\bigcup_{n=1}^\infty\rightarrow\mathbb{N}$ by $f(a_{ij})=2^i5^j$, where $i,j\in\mathbb{N}$. there might be restrictions on $j$ if any of $A_i$ is finite. This identification covers all points in $\bigcup_{n=0}^\infty$. The function $f$ is one-to-one by the uniqueness of the prime factorization. The fact that
$$
B=\{2^i5^j: i,j\in\mathbb{N}\}\subseteq\mathbb{N}
$$
guarantees that $\bigcup_{n=0}^\infty$ is countable.
###### Exercise 1.2.1
Prove parts (b), (e), and (g) of Theorem 1.2.2.
**Answer** (b) uniqueness of the additive inverse: let $y$ be an alternative inverse of $x$, then
$$
y=y+0=y+(x+(-x))=(y+x)+(-x)=0+(-x)=-x.
$$
(e) $-(x+y)=(-x)+(-y)$:
$$
\begin{split}
-(x+y)=&-(x+y)+x+(-x)+y+(-y)=-(x+y)+(x+y)+(-x)+(-y)\\=&0+(-x)+(-y)=(-x)+(-y)
\end{split}
$$
(g) $-(-x)=x$:
$$
-(-x)=-(-x)+0=-(-x)+(-x+x)=(-(-x)+(-x))+x=0+x.
$$
###### Exercise 1.2.2
Prove parts (a), (c), (e), (f), (h), and (i) of Theorem 1.2.3.
**Answer** (a) the multiplicative identity is unique: Let $1'$ be an alternative identity, then
$$
1=1\cdot1'=1'\cdot1=1'.
$$
(c) if $xz=yz$ and $z\neq0$ then $z=y$:
$$
0=0\cdot z^{-1}=(xz-yz)z^{-1}=(z-y)zz^{-1}=x-y.
$$
(e) if $x\neq0$ then $(x^{-1})^{-1}=x$:
$$
(x^{-1})^{-1}=(x^{-1})^{-1}\cdot1=(x^{-1})^{-1}\cdot x^{-1}\cdot x=1\cdot x=x.
$$
(f) $(xy)^n=x^ny^n$:
$$
(xy)^n=\underbrace{xyxy...xy}_{\text{n times}}=\underbrace{xx...x}_{\text{n times}}\underbrace{yy...y}_{\text{n times}}=n^ny^n.
$$
(g) $-(xy)=(-x)y=x(-y)$:
$$
-(xy)\stackrel{\text{1.2.2 (g)}}{=}-1\cdot xy=(-1\cdot x)y=(-x)y=
x(-1\cdot y)=x(-y).
$$
(h) $(-x)(-y)=xy$:
$$
(-x)(-y)=(-1)x(-1)y\stackrel{\text{1.2.2 (g)}}{=}(-1)(-y)xy\stackrel{\text{1.2.2 (h)}}{=}1\cdot xy=xy.
$$
(i) if $x,y\neq0$ then (xy)^{-1}=x^{-1}y^{-1}:
$$
(xy)^{-1}=(xy)^{-1}xx^{-1}yy^{-1}=(xy)^{-1}(xy)x^{-1}y^{-1}=1\cdot x^{-1}y^{-1}=x^{-1}y^{-1}.
$$
###### Exercise 1.2.3
Let $X$ be an ordered field and let $x\in X$:
(a) Show that $-0=0$:
**Answer** $-0=-1\cdot0=0$
(b) If $x\neq0$, show that $(-x)^{-1}=-x^{-1}$
Answer
$$
-x^{-1}=(-x^{-1})(-x)(-x)^{-1}=(-1)(-1)x^{-1}x(-x)^{-1}=x^{1}x(-x)^{-1}=
(-x)^{-1}
$$
###### Exercise 1.2.4
Prove parts (e), (f), and (h) of theorem 1.2.5
**Answer** (e) if $x<y$ and $z>0$ then $xz<yz$:
$$
0 < y-x\stackrel{\text{1.2.4 (d)}}{\Longrightarrow}0<(y-x)z=yz-xz\Rightarrow
xz<yz.
$$
(f) if $x<y$ and $z < 0$ then $xz>yz$
$$
0<y-x\stackrel{\text{1.2.4 (a) and 1.2.5 (b)}}{\Longrightarrow}
0<(y-x)(-z)=y(-z)-x(-z)=xz-yz\Rightarrow xz>yz.
$$
(h) if $0<x<y$ then $0<y^{-1}<x^{-1}$.
Positiveness comes from (g). Then assume $x<y$ and towards a contradiction $x^{-1}<y^{-1}. Then 
$$
1=x^{-1}x<y^{-1}x<y^{-1}y=1.
$$
Thus $1<1$ which contradicts the trichotomy axiom.
###### Exercise 1.2.6
Let $X$ be an ordered field and let $A\subseteq X$ be nonempty and bounded above. If $\sup(A)$ exists, show that it is unique.
**Answer** Let $x, y\in X$ fulfil the definition of supremum. Then:
- $x$ is an upper bound of $A$
- $y$ is an upper bound of $A$
- if $a$ is an upper bound of $A$ then $x\leq z$
- if $b$ is an upper bound of $A$ then $y\leq b$
Putting this together, $x\leq y$ and $y\leq x$ which means $x=y$.
###### Exercise 1.2.7
Let $X$ be an ordered field and let $A\subseteq X$ be nonempty and bounded below. 
(a) Provide a definition for the greatest lower bound or infimum of $A$.
**Answer** We say $A$ has a *greatest lower bound* or *infimum* if there is a point in $X$, denoted $\inf(A)$, such that:
- $\inf(A)$ is a lower bound of $A$;
- if $b$ is another upper bound of $A$, then $\inf(A)\geq b$,
(b) Show that $\inf(A)$ is unique if it exists.
**Answer** Let $x,y\in X$ fulfil the above conditions, that is:
- $x,y$ are lower bounds of $X$
- If $b$ is a lower bound of $A$, then $x\geq b$ and $y\geq b$.
Putting it together, $x\geq y$ and $y\geq x$, thus $x=y$
(c) Provide a version (including a proof) of Lemma 1.2.10 for infima
**Answer** Let $X$ be an ordered field and let $A\subseteq X$ be nonempty and bounded below. If $M\in X$ is a lower bound of $A$, then $M=\inf(A)$ if and only if for every $\epsilon\in X$ with $\epsilon>0$, there is a point $a\in A$ such that $M+\epsilon>a$.
*Proof.* Assume $M=\inf(A)$. Let $\epsilon>0$ in $X$ and consider $M+\epsilon>M$. Thus $M+\epsilon$ is not a lower bound, since $M$ is the greatest lower bound. By negating the definition of lower bound we see that there must exist a point $a\in A$ such that $M+\epsilon>a$. 
For the converse, assume that for every $\epsilon>0$ in $X$ there is a point $a\in A$ such that $M+\epsilon > a$. Let $b$ be a lower bound of $A$. To show that $M\geq b$, we exclude $M<b$. Towards the contradiction, we assume $M<b$. Setting $\epsilon=b-M$, there exists $a\in A$ such that $M+\epsilon = M+b-M=b > a$. This contradicts that $b$ is a lower bound of $A$. Consequently, $M\geq b$ and the second condition in the definition of infimum is fulfilled. 
###### Exercise 1.2.8
Let $X$ be a complete ordered field. Show that every set $A\subseteq X$ thet is nonemply and bounded below has a greatest lower bound in $X$.
**Answer** Let $-A = \{-a: a\in A\}$. Then by completeness of $X$, there exist $x$ such that:
- $x$ is an upper bound of $-A$
- if $b$ is another upper bound of $A$ then $x\leq b$. 
From the first condition, for each $a'=-a\in -A$, $a'\leq x$. Thus $a=-a'\geq -x$. Therefore for every $a\in A$, $a\geq -x$ and so $-x$ is a lower bound of $A$. 
Let $c$ be another lower bound of $A$. Then $-c$ is another upper bound of $-A$. Therefore $x\leq-c$ and $-x\geq c$. So $-x$ is the greatest lower bound of $A$, that is $-x=\inf(A)$.
###### Exercise 1.2.9
We define:
$$
\left(
\begin{split}
n\\k
\end{split}
\right)=\frac{n!}{k!(n-k)!}.
$$
(a) Show that:
$$
\left(\begin{matrix}
n\\k-1
\end{matrix}\right)+
\left(\begin{gathered}
n\\k
\end{gathered}\right)=
\left(\begin{matrix}
n+1\\k
\end{matrix}\right).
$$
Answer
$$
\begin{split}
&\left(\begin{matrix}
n\\k-1
\end{matrix}\right)+
\left(\begin{matrix}
n\\k
\end{matrix}\right)=
\frac{n!}{(k-1)!(n-(k-1))!}+\frac{n!}{k!(n-k)!}=
\frac{n!}{(k-1)!(n-k+1)!}+\frac{n!}{k!(n-k)!}\\
&=\frac{kn!}{k!(n-k)!(n-k+1)}+\frac{n!(n-k+1)}{k!(n-k)!(n-k+1)}=
\frac{n!(n-k+1+k)}{k!(n-k)!(n-k+1)}\\
&=\frac{n!(n+1)}{k!(n+1-k)!}=\frac{(n+1)!}{k!(n+1-k)!}=\left(
\begin{matrix}
n+1\\k
\end{matrix}\right).
\end{split}
$$
(b) Let $X$ be a field. For $x\in X$ show that
$$
(1+x)n=\sum_{k=0}^n\left(\begin{matrix}n\\k\end{matrix}\right)x^k
$$
**Answer** By induction, for $n=1$:
$$
1+x=x^0+x^1=\frac{1!}{0!(1-0)!}x^0+\frac{1!}{1!(1-1)!}x^1=
\left(\begin{matrix}1\\0\end{matrix}\right)x^0+
\left(\begin{matrix}1\\1\end{matrix}\right)x^1=
\sum_{k=0}^1\left(\begin{matrix}1\\k\end{matrix}\right)x^k.
$$
Inductive step:
$$
\begin{split}
(1+x)^{n+1}&=(1+x)^n(1+x)=\sum_{k=0}^n\left(\begin{matrix}n\\k\end{matrix}\right)x^k(1+x)=
\sum_{k=0}^n\left(\begin{matrix}n\\k\end{matrix}\right)x^k+
\sum_{k=0}^n\left(\begin{matrix}n\\k\end{matrix}\right)x^{k+1}\\
&=1+\sum_{k=1}^n\left(\begin{matrix}n\\k\end{matrix}\right)x^k+
\sum_{k'=1}^{n+1}\left(\begin{matrix}n\\k'-1\end{matrix}\right)x^{k'}
\stackrel{\left(\begin{matrix}n\\n+1\end{matrix}\right)=0}{=}
1+\sum_{k=1}^{n+1}\left(\begin{matrix}n\\k\end{matrix}\right)x^k+
\sum_{k'=1}^{n+1}\left(\begin{matrix}n\\k'-1\end{matrix}\right)x^{k'}\\
&=1+\sum_{k=1}^{n+1}\left(\begin{matrix}n+1\\k\end{matrix}\right)x^k=
\sum_{k=0}^{n+1}\left(\begin{matrix}n+1\\k\end{matrix}\right)x^k.
\end{split}
$$
(c) Show that
$$
(a+b)^n=\sum_{k=0}^n\left(\begin{matrix}n\\k\end{matrix}\right)a^kb^{n-k}.
$$
**Answer** For $b=0$ the only non-zero term on the right-hand side is for $n=k$, it is:
$$
\left(\begin{matrix}n\\n\end{matrix}\right)a^nb^{n-n}=1\cdot a^n\cdot b^0=a^n.
$$
For $b\neq0$:
$$
(a+b)^n=b^n\left(1+\frac{a}{b}\right)^n=
b^n\sum_{k=0}^n\left(\begin{matrix}n\\k\end{matrix}\right)
\left(\frac{a}{b}\right)^k=
\sum_{k=0}^n\left(\begin{matrix}n\\k\end{matrix}\right)a^kb^{n-k}.
$$
