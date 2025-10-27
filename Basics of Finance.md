#### Two-state economy
Discounting:
$$
D(c_1)=\frac{c_1}{1+i},
$$
because:
$$
c_1 = c_0(1+i).
$$
Net present value (NPV):
$$
NPV(c)=c_0+D(c_1).
$$
If $NPV(c)>0$, investment project should be realised, otherwise not.

Price process: $(S_0, (S^u_1,S^u_2))$.

Expected return: $E^p(R)=E^p(S_1)-S_0$.

Expected return rate: $E^p(r) = \frac{E^p(R)}{S_0}$, where $r=\frac{S_1-S_0}{S_0}$.

Volatility: $\sigma(r)$.

**Call option** gives a payout of:
$$
C_1(S_1(\omega))=\max(S_1(\omega)-K,0),~\mathrm{where}~\omega\in\Omega
$$
and $K$ is the **strike price**.

**Short selling** involves borrowing a certain number of units of a given financial asset from another agent today and immediately selling those units on the market. In a year's time, the borrower buys exactly the same number of units of the financial asset on the market at the then current price and returns them to the other agent.

Payment of a conditional claim (e.g., option) is redundant if there is a unoque solution $\phi^*$ of
$$
{\cal M}\phi=C_1,
$$
where:
$$
{\cal M}=\left(
\begin{matrix}
B_1 & S^u_1 \\
B_1 & S^d_1
\end{matrix}
\right),~\phi=(b~~~s)^T,~C_1=(C^u_1~~~C^d_1)^T.
$$
Then the conditional claim is replicated by a certain portfolio. The present value of this portfolio is:
$$
V_0(\phi)=\phi\cdot\left(
\begin{matrix}
B_0 \\ S_0
\end{matrix}
\right).
$$
Uncertain value of this portfolio in one year is:
$$
V_1(\phi)={\cal M}\phi.
$$
This gives a price process for the portfolio: $V_(\phi)=(V_0(\phi),V_1{\phi})$.
If the price of a conditional claim is not equal to the cost of creating a replication portfolio, there is a possibility of **arbitrage** in the economy. This holds if:
$$
V_0(\phi=0)~\mathrm{and}E^p(\phi)>0
$$
or
$$
V_0(\phi)>0~\mathrm{and}~V_1(\phi)=0.
$$
For example, if $C_0 > V_0(\phi*)$, one can sell the option and buy the portfolio, which gives immediate risk-free profit of $C_0-V_0(\phi^*)$. After a year, profits from the portfolio and from the option cancel out:
$$
-C+M\phi^*=\left(\begin{matrix}
0 \\ 0
\end{matrix}\right)
$$
by definition of the replication portfolio. Otherwise, if $C_0<V_0(\phi^*)$, one can buy the option and sell the portfolio with immediate risk-free profit of $V_0(\phi^*)-C_0$. Such situations, however, are not realistic, and the option has normally an **arbitration price** $C_0=V_0(\phi^*)$.
<<<<<<< HEAD

Expected payout from a portfolio:
$$
E^p({\cal M}\phi)=bB_1+sE^p(S_1),
$$
where $\phi=(b,s)^T$. Defining a **matrix of return rates**:
$$
{\cal R}=
\left(\begin{matrix}
i & r^u_1 \\ i & r^d_1
\end{matrix}\right),
$$
one gets:
$$
E^p({\cal R}\phi)=bi+s\mu,
$$
where $\mu$ is the expected return rate from shares.
Volatility of the portfolio is:
$$
\sigma({\cal R}\phi)=s\sigma(r_1).
$$
**Arrow-Debreu security** yields a payoff of exactly one unit in a given state in the future. In a two-state economy there are exactly two such instruments. They are replicated portfolios fulfilling:
$$
{\cal M}\phi=
\left(\begin{matrix}
1 \\ 0
\end{matrix}\right)
$$
and
$$
{\cal M}\phi=
\left(\begin{matrix}
0 \\ 1
\end{matrix}\right).
$$
If their price processes are $\gamma^u=(\gamma^u_0,(1,0)^T)$ and $\gamma^d=(\gamma^d_0,(0,1)^T)$. For the portfolio consisting of these securities we define:
$$
{\cal M}^\gamma=
\left(\begin{matrix}
1 & 0 \\ 0 & 1
\end{matrix}\right)=\mathbb{1}_2.
$$
The replication portfolio $\phi^\gamma$ for any conditional claim 
$$
C_1=
\left(\begin{matrix}
C^u_1 \\ c^d_1
\end{matrix}\right)
$$
is then simply
$$
V_1(\phi^\gamma)={\cal M}^\gamma\phi^\gamma=\mathbb{1}_2\phi^\gamma=C_1
$$
and therefore $\phi^\gamma=C_1$. The arbitration price is then:
$$
C_0=V_0(\phi^\gamma)=C^u_1\gamma^u_0+C^d_1\gamma^d_0.
$$
###### Martingale pricing
An asset is a martingale if:
$$
S_0=\frac{1}{1+i}E^Q(S_1).
$$
**Martingale measure** is a probability measure $Q:2^\Omega\rightarrow\mathbb{R}$ with respect to which it holds. 
Define:
$$
q:=Q(u),
$$
then:
$$
S_0(1+i)=qS^u_1+(1-q)S^d_q
$$
or
$$
q=\frac{S_0(1+i)-S^d_1}{S^u_1-S^d_1}.
$$
For $q$ in order to define a correct probability measure it must hold:
$$
S^u_1>S_0(1+i)>S^d_1.
$$
If these conditions are not fulfilled, a simple arbitrage consists of buying or selling the instrument $S$. If inequalities are replaced with equality, there is a weak arbitrage, because risk-free profit can be expected only on average and not for certain.

###### First fundamental theorem of asset pricing
The following two statements are equivalent:
- There exists a martingale probability measure
- The economy is arbitration-free
###### Second fundamental theorem of asset pricing
The following two statements are equivalent:
- The martingale measure is unique
- The market model is complete
#### Three-state economy
**Attainable contingent claims** are:
$$
\mathbb{A}=\{{\cal M}\phi,~\phi\in\mathbb{R}^2\}
$$
when short selling is allowed, or
$$
\mathbb{A}=\{{\cal M}\phi,~\phi\in\mathbb{R}^2_+\}
$$
when it is not allowed. There are three equations for only two variables. Then, $\mathbb{A}$ is only a subspace of $\mathbb{R}^3$. Contingent claims that are not attainable cannot be replicated. One says that the **market model is incomplete**. 

In this case, the conditions that martingale measure is a probability measure puts inequality constraints on the probabilities $q\in\mathbb{Q}$. According to the first fundamental theorem, the martingale measure is not unique and the market model is again incomplete.
###### Superreplication
A portfolio $\phi$ superreplicates a contingent claim if
$$
V_1(\phi)\geq C_1~\mathrm{(matrix~element~wise)}
$$
For example, a portfolio with bonds only superreplicates first Arrow-Debrue secutiy $\gamma^u:~C_1=(1,0,0)^T$. One can then try to minimize the cost of obtaining the portfolio:
$$
\min_\phi V_0(\phi)~\mathrm{such~that}~V_1(\phi)\geq C_1.
$$
###### Approximate replication
Can be obtained by minimizing:
$$
\min_\phi\mathrm{MSE}(V_1(\phi)-C_1).
$$
Line of $\mu$ versus $\sigma$ is called **capital market line (CML)**. The equation of its upper, increasing branch is:
$$
\mu=i-\frac{\mu_s-i}{\sigma_s}\sigma,
$$
where $\mu_s$, $\sigma_s$ describe a **market portfolio**, e.g., some large stock index.
