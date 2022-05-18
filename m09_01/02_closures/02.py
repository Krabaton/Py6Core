# Closures

def taxer(base_tax):

    def calculate(money):
        nonlocal base_tax
        if money >= 10_000:
            base_tax = 1.5 * base_tax
        return money - base_tax * money

    return calculate


ukr = taxer(0.1)
swd = taxer(0.55)

m_u = ukr(5000)
m_s = swd(25000)

print(m_u, m_s)
