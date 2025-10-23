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
-C+M\phi*0=\left(\begin{matrix}
0 \\ 0
\end{matrix}\right)
$$
by definition of the replication portfolio. Otherwise, if $C_0<V_0(\phi^*)$, one can buy the option and sell the portfolio with immediate risk-free profit of $V_0(\phi^*)-C_0$. Such situations, however, are not realistic, and the option has normally an **arbitration price** $C_0=V_0(\phi^*)$.