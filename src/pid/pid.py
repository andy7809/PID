class PID:
    def __init__(self, p, i, d, sp, memory, x):
        self.e_hist = []

        self.p = p
        self.i = i
        self.d = d

        self.sp = sp

        self.memory = memory

        self.x = x

    def update(self, dt = 0.1):
        def integrate(self):
            riemann_sum = 0
            for e in self.e_hist:
                riemann_sum += e * dt
            return riemann_sum

        def e(self):
            return self.sp - self.x

        u = 0
        u += self.p * e(self)
        u += self.i * integrate(self)

        if self.e_hist:
            u += self.d * (e(self) - self.e_hist[-1]) / dt
        self.e_hist.append(e(self))
        self.x += u * dt