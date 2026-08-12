# DUP Equations — Reference Sheet

**Status:** Working reference for implementation in `packages/theory-sim`. All equations
are implemented; cross-reference the code for exact semantics.

## 1. Pressure field

**DUP pressure** (pressure from particle flux speed):

$$P = \rho v^2$$

**Wave form** (resonance branch):

$$P(x,t) = A_0\, e^{i(2\pi f t + \phi(x))}, \qquad f = 7.83\ \mathrm{Hz}\ \text{(Schumann fundamental)}$$

## 2. Force laws

**DUP force** (pressure-gradient force, replaces Newtonian gravity):

$$\mathbf{F} = -\nabla P \cdot V$$

**Newtonian gravity** (kept for comparison):

$$F = \frac{G m_1 m_2}{r^2}$$

**DEC (Dynamic Electrostatic Containment) collection force:**

$$\mathbf{F} = q(\mathbf{E} + \mathbf{v} \times \mathbf{B}) = -q\nabla V$$

## 3. Orbital models (the falsifiable fork)

| Model | Law | Solar-system RMS error |
|---|---|---|
| Kepler/Newton | $v = \sqrt{GM/r}$ | 0.42 % |
| DUP | $v = k/r$ (fitted $k \approx 1.06\times10^{16}\ \mathrm{m^2/s}$) | 135 % |

**Conclusion (data-driven):** the simple `1/r` law is falsified at planetary scale.
Open test: galaxy rotation curves (flat $v \approx \mathrm{const}$).

## 4. IPS sensor equations

**Interferometric phase shift:**

$$\Delta\phi = \frac{2\pi}{\lambda}\, n\, L$$

**Energy density (sphere core):**

$$u = \tfrac{1}{2}\varepsilon_0 E^2 + \frac{1}{2\mu_0} B^2$$

**Entropy reclaim rate:**

$$\eta_S = \frac{E_{\text{recovered}}}{E_{\text{waste}}} \qquad (\text{spec band } 40\text{--}60\%)$$

**Capacitor:**

$$U_C = \tfrac{1}{2} C V^2, \qquad \tau = R_{\mathrm{ESR}} C \ (< 5\ \mathrm{ns})$$

**Color visualization (Wien):**

$$\lambda_{\mathrm{peak}} = \frac{b}{T}$$

## 5. Implementation map

| Equation | File | Function |
|---|---|---|
| $P = \rho v^2$ | `theory_sim/dup_physics.py` | `dup_pressure` |
| $\mathbf{F} = -\nabla P$ | `theory_sim/dup_physics.py` | `pressure_gradient_force` |
| $v = \sqrt{GM/r}$ vs $v = k/r$ | `theory_sim/dup_physics.py` | `kepler_orbital_speed`, `dup_orbital_speed`, `compare_orbital_models` |
| $P(x,t) = A_0 e^{i(2\pi f t + \phi)}$ | `theory_sim/resonance.py` | `pressure_wave`, `superposition` |
| $\Delta\phi = 2\pi n L/\lambda$ | `sensor/ips_model.py` | `phase_shift` |
| $\mathbf{F} = q(\mathbf{E}+\mathbf{v}\times\mathbf{B})$ | `sensor/ips_model.py` | `lorentz_force` |
| $\eta_S$ | `sensor/ips_model.py` | `entropy_reclaim_rate` |
| $U_C = \tfrac12 CV^2$, $\tau = R C$ | `sensor/ips_model.py` | `capacitor_energy`, `capacitor_response_time` |
| $\lambda_{\mathrm{peak}} = b/T$ | `sensor/ips_model.py` | `wien_peak_wavelength` |
