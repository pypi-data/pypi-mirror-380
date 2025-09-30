# Storages
**Storages** have one incoming and one outgoing **[Flow](Flow.md)** with a charging and discharging efficiency.
A storage has a state of charge $c(\text{t}_i)$ which is limited by its `size` $\text C$ and relative bounds $\eqref{eq:Storage_Bounds}$.

$$ \label{eq:Storage_Bounds}
    \text C \cdot \text c^{\text{L}}_{\text{rel}}(\text t_{i})
    \leq c(\text{t}_i) \leq
    \text C \cdot \text c^{\text{U}}_{\text{rel}}(\text t_{i})
$$

Where:

- $\text C$ is the size of the storage
- $c(\text{t}_i)$ is the state of charge at time $\text{t}_i$
- $\text c^{\text{L}}_{\text{rel}}(\text t_{i})$ is the relative lower bound (typically 0)
- $\text c^{\text{U}}_{\text{rel}}(\text t_{i})$ is the relative upper bound (typically 1)

With $\text c^{\text{L}}_{\text{rel}}(\text t_{i}) = 0$ and $\text c^{\text{U}}_{\text{rel}}(\text t_{i}) = 1$,
Equation $\eqref{eq:Storage_Bounds}$ simplifies to

$$ 0 \leq c(\text t_{i}) \leq \text C $$

The state of charge $c(\text{t}_i)$ decreases by a fraction of the prior state of charge. The belonging parameter
$ \dot{ \text c}_\text{rel, loss}(\text{t}_i)$ expresses the "loss fraction per hour". The storage balance from  $\text{t}_i$ to $\text t_{i+1}$ is

$$
\begin{align*}
    c(\text{t}_{i+1}) &= c(\text{t}_{i}) \cdot (1-\dot{\text{c}}_\text{rel,loss}(\text{t}_i) \cdot \Delta \text{t}_{i}) \\
    &\quad + p_{f_\text{in}}(\text{t}_i) \cdot \Delta \text{t}_i \cdot \eta_\text{in}(\text{t}_i) \\
    &\quad - \frac{p_{f_\text{out}}(\text{t}_i) \cdot \Delta \text{t}_i}{\eta_\text{out}(\text{t}_i)}
    \tag{3}
\end{align*}
$$

Where:

- $c(\text{t}_{i+1})$ is the state of charge at time $\text{t}_{i+1}$
- $c(\text{t}_{i})$ is the state of charge at time $\text{t}_{i}$
- $\dot{\text{c}}_\text{rel,loss}(\text{t}_i)$ is the relative loss rate (self-discharge) per hour
- $\Delta \text{t}_{i}$ is the time step duration in hours
- $p_{f_\text{in}}(\text{t}_i)$ is the input flow rate at time $\text{t}_i$
- $\eta_\text{in}(\text{t}_i)$ is the charging efficiency at time $\text{t}_i$
- $p_{f_\text{out}}(\text{t}_i)$ is the output flow rate at time $\text{t}_i$
- $\eta_\text{out}(\text{t}_i)$ is the discharging efficiency at time $\text{t}_i$
