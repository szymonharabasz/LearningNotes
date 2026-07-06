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