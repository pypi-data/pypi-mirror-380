import numpy as np

class PhaseSpace:
    """
    Hamiltonian-inspired phase space calculator.
    """

    def __init__(self, all_e, all_ig, mask, m=1.0, k=1.0):
        all_e = np.array(all_e, dtype=float)
        all_ig = np.array(all_ig, dtype=float)
        mask = np.array(mask, dtype=bool)

        if np.any(mask):
            self._q = all_ig[mask].mean() - all_e[mask].mean()
            self._p = all_ig[mask].mean()
        else:
            self._q, self._p = 0.0, 0.0

        self.m = m
        self.k = k

    @property
    def position(self): return self._q
    @property
    def momentum(self): return self._p
    @property
    def kinetic(self): return (self._p**2) / (2*self.m)
    @property
    def potential(self): return self.k * (self._q**2)
    @property
    def energy(self): return self.kinetic + self.potential
    @property
    def lagrangian(self): return self.kinetic - self.potential
    @property
    def dq_dt(self): return self._p / self.m
    @property
    def dp_dt(self): return -2 * self.k * self._q

    def _derivatives(self, q, p):
        dqdt = p / self.m
        dpdt = -2 * self.k * q
        return dqdt, dpdt

    def trajectory(self, t_max=10.0, dt=0.01, method="rk4"):
        steps = int(t_max / dt)
        times = np.linspace(0, t_max, steps+1)
        qs, ps = [self._q], [self._p]
        q, p = self._q, self._p

        for _ in range(steps):
            if method == "euler":
                dq, dp = self._derivatives(q, p)
                q += dq*dt; p += dp*dt
            else:  # RK4
                k1q, k1p = self._derivatives(q, p)
                k2q, k2p = self._derivatives(q+0.5*dt*k1q, p+0.5*dt*k1p)
                k3q, k3p = self._derivatives(q+0.5*dt*k2q, p+0.5*dt*k2p)
                k4q, k4p = self._derivatives(q+dt*k3q, p+dt*k3p)
                q += (dt/6.0)*(k1q+2*k2q+2*k3q+k4q)
                p += (dt/6.0)*(k1p+2*k2p+2*k3p+k4p)
            qs.append(q); ps.append(p)

        return times, np.array(qs), np.array(ps)

    def __repr__(self):
        return (f"PhaseSpace(q={self._q:.4f}, p={self._p:.4f}, "
                f"H={self.energy:.4f}, T={self.kinetic:.4f}, V={self.potential:.4f})")
