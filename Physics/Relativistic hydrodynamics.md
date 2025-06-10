Modes:
- long-lived - hydrodynamic, $\omega(k)\rightarrow 0$ when $k\rightarrow 0$
- transient - short-lived - non-hydrodynamic, $\omega(k)\neq 0$ when $k\rightarrow 0$

Energy momentum tensor at global equilibrium is given in the rest frame by
$$
T^{\mu\nu}_{EQ}=\left(
\begin{matrix}
\mathcal{E}_{EQ} & 0 & 0 & 0 \\
0 & \mathcal{P}(\mathcal{E}_{EQ}) & 0 & 0 \\
0 & 0 &\mathcal{P}(\mathcal{E}_{EQ}) & 0  \\
0 & 0 & 0 & \mathcal{P}(\mathcal{E}_{EQ}) \\
\end{matrix}
\right)
$$
The relation between pressure and energy density is assumed to be provided by the equation of state.
In other frames, the tensor is given by
$$
T^{\mu\nu}_{EQ}=\mathcal{E}_{EQ}u^\mu u^\nu-\mathcal{P}(\mathcal{E}_{EQ})\Delta^{\mu\nu},
$$
where $\Delta^{\mu\nu}$ projects to the space orthogonal to the fluid velocity $u$:
$$
\Delta^{\mu\nu}=g^{\mu\mu}-u^\mu u^\nu,\;\mathrm{and}\;\Delta^{\mu\mu}u_\nu=0.
$$
In the local equilibrium, we allow pressure and energy density to depend on position:
$$
T^{\mu\nu}_{eq}(x)=\mathcal{E}_{eq}(x)u^\mu(x) u^\nu(x)-\mathcal{P}(\mathcal{E}_{eq}(x))\Delta^{\mu\nu}(x).
$$
Local temperature $T(x)$ is fixed by the condition that non-equilibrium energy density agrees with equilibrium energy density at this value of temperature.

**Navier-Stokes hydrodynamics** adds a dissipative part to the energy-momentum tensor:
$$
\begin{aligned}
T^{\mu\nu}&= T_{eq}^{\mu\nu} + \Pi^{\mu\nu}\\
          &= T_{eq}^{\mu\nu} + \pi^{\mu\nu}+\Pi\Delta^{\mu\nu}\\
          &= T_{eq}^{\mu\nu} + 2\eta\sigma^{\mu\nu}-\zeta\theta\Delta^{\mu\nu},\\
\end{aligned}
$$
where:
- $\Pi$ is the bulk viscous pressure, the trace part of $\Pi^{\mu\mu}$, describing response of the system to changes of the volume
- $\pi^{\mu\nu}$ is the shear stress tensor, describing response to changes of shape, it is symmetric, traceless and orthogonal to the flow $u$.
- $\Pi=-\zeta\partial_\mu u ^\mu$, defines the bulk viscosity coefficient
- $\pi^{\mu\nu}=2\eta\sigma^{\mu\nu}$ defines the bulk viscosity coefficient, $\sigma^{\mu\nu}$ is also given by a gradient, $\sigma^{\mu\nu}=\Delta^{\mu\nu}_{\alpha\beta}\partial^\alpha u ^\beta$ with the projection operator:
  $$
   \Delta^{\mu\nu}_{\alpha\beta}=\frac{1}{2}\left(
   \Delta^\mu_\alpha\Delta^\nu_\beta+\Delta^\mu_\beta\Delta^\nu_\alpha
   \right)
   -\frac{1}{3}\Delta^{\mu\nu}\Delta_{\alpha\beta}.
   $$
One extends this by promoting $\Pi$ and $\pi^{\mu\nu}$ to dynamical variables that satisfy new differential equations of state:
$$
\begin{align}
\dot\Pi+\frac{\Pi}{\tau_\Pi}&=-\beta_\Pi\theta,\\

\dot\pi^{\langle\mu\nu\rangle}+\frac{\pi^{\mu\nu}}{\tau_\pi} &=2\beta_pu\sigma^{\mu\nu},
\end{align}
$$
where $\beta$ coefficients are chosen such that $\beta_\Pi\tau_\Pi=\zeta$ and $\beta_\pi\tau_\pi=\eta$, dots represent convective derivative $u^\mu\partia_\mu$, and angular bracket denotes contraction with the projector $\Delta^{\mu\nu}_{\alpha\beta}$.
More coefficients appear when hydrodynamic equations are derived from the kinetic theory, for example **Müller-Israel-Stewart**:
$$
\begin{align}
\dot\Pi+\frac{\Pi}{\tau_\Pi}&=-\beta_\Pi\theta
-\frac{\zeta T}{2\tau_\Pi}\Pi\partial_\lambda\left(
\frac{\tau_\Pi}{\zeta T}u^\lambda
\right),\\

\dot\pi^{\langle\mu\nu\rangle}+\frac{\pi^{\mu\nu}}{\tau_\pi} &=2\beta_pu\sigma^{\mu\nu}
-\frac{\eta T}{2\tau_\pi}\pi^{\mu\nu}\partial_\lambda\left(
\frac{\tau_\pi}{\eta T}u^\lambda
\right).
\end{align}
$$
In the **Denicol-Niemi-Molnar-Rischke** theory, expansion was made to second order in the Knudsen number and the inverse Reynolds number. For the relaxation time approximation (RTA) of the kinetic theory one finds:
$$
\begin{align}
\dot\Pi+\frac{\Pi}{\tau_\Pi}&=-\beta_\Pi\theta
-\delta_{\Pi\Pi}\Pi\theta+\lambda_{\Pi\pi}\pi^{\mu\nu}\sigma_{\mu\nu},\\

\dot\pi^{\langle\mu\nu\rangle}+\frac{\pi^{\mu\nu}}{\tau_\pi} &=2\beta_pu\sigma^{\mu\nu}
-\delta_{\pi\pi}\pi^{\mu\nu}\theta
-\tau_{\pi\pi}\pi_\gamma^{\langle\mu}\sigma^{\nu\rangle\gamma}
+\lambda_{\pi\Pi}\Pi\sigma^{\mu\nu}.
\end{align}
$$

**Baier-Romatschke-Son-Starinets-Stephanov** theory is derived without reference to any kinetic theory. It takes the form (when neglecting vorticity and spacetime curvature):
$$
\begin{align}
\Pi&=0,\\

\dot\pi^{\langle\mu\nu\rangle}+\frac{\pi^{\mu\nu}}{\tau_\pi} &=2\beta_pu\sigma^{\mu\nu}
-\frac{4}{3}\pi^{\mu\nu}\theta
+\frac{\lambda_I}{\tau_\pi\eta^2}\pi_\gamma^{\langle\mu}\pi^{\nu\rangle\gamma}.
\end{align}
$$
The first equation is characteristic for conformal systems.

In **Glauber model** one can distinguish between participants that interact inelastically and those that interact only elastically. The latter are called *wounded nucleons*.

Fluctuations in the initial state lead to non-zero values of odd flow harmonics.