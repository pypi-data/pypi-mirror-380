class Pi:
    def __init__(self, coefficient=1, denominator=1):
        self.coefficient = coefficient
        self.denominator = denominator
    
    def __repr__(self):
        return f"{self.coefficient} * π / {self.denominator}"
    
    def evall(self, iterations=10000):
        pi_val = 0
        for k in range(iterations):
            pi_val += (-1)**k / (2*k + 1)
        return 4 * pi_val * self.coefficient / self.denominator
    
    def evaln(self, terms=5000):
        pi_val = 3
        for i in range(1, terms+1):
            term = 4 / ((2*i)*(2*i+1)*(2*i+2))
            if i % 2 == 0:
                pi_val -= term
            else:
                pi_val += term
        return pi_val * self.coefficient / self.denominator
    
    def eval_symbolic(self):
        return self

def pif(method="leibniz", iterations=10000):
    p = Pi()
    if method.lower() == "leibniz":
        return p.evall(iterations)
    elif method.lower() == "nilakantha":
        return p.evaln(iterations)
    else:
        raise ValueError("method must be 'leibniz' or 'nilakantha'")

pi_default = Pi()
pi_half = Pi(1,2)