class PID:
    def __init__(self, p = 1, i = 1, d = 1, sp = 10, memory = 10, x = 0):
        self.e_hist = []

        self.p = p
        self.i = i
        self.d = d

        self.sp = sp

        self.memory = memory

        self.x = x

    def integrate(self):
        riemann_sum = 0
        for e in self.e_hist:
            riemann_sum += e * dt
        return riemann_sum

    def e(self):
        return self.sp - self.x

    def update(self, dt = 0.1):
        u = 0
        u += self.p * self.e()
        u += self.i * self.integrate()
        if self.e_hist:
            u += self.d * (self.e() - self.e_hist[-1]) / dt
        self.e_hist.append(self.e())
        self.x += u * dt

c = PID(p=0.3, i=0.002, d=0.2, memory=1000)

for t in range(500):
    c.update()
    print(c.x)