import numpy as np
from abc import ABC, abstractmethod
from .base import GenLasso
import cvxpy as cp

class ChangePointDetector(ABC):
    def gen_data(n, delta, list_change_points):
        true_y = np.zeros(n)
    
        if len(list_change_points)==1:
            true_y[list_change_points[0]:] += delta
        elif len(list_change_points)>1:
            segments = [(start, end) for start, end in zip(list_change_points[:-1], list_change_points[1:])]
            sign = 1
            for segment in segments:
                start = segment[0]
                end = segment[1]
                true_y[start:end] += sign * delta
                sign = 1 - sign
        
        y = true_y + np.random.normal(0, 1, n)
        return y.reshape(-1,1), true_y.reshape(-1,1), np.eye(n)

    @abstractmethod
    def __init__(self):
        pass

    def get_hyperparams(self):
        pass

    @abstractmethod
    def solve(self):
        pass

    def fit(self):
        self.solve()
        temp = self.D @ self.beta
        self.active_set = (np.where(np.round(temp, 9) != 0)[0] + 1).tolist()
        self.active_set = [0] + self.active_set + [self.m - 1]  # Add boundaries to change points
        return self.active_set
    
    def is_empty(self):
        return len(self.active_set)==2
    
class FusedLasso(GenLasso, ChangePointDetector):
    """
    Fused Lasso change point detector.
    """
    def __init__(self, y, **kwargs):
        super().__init__

        self.X = np.eye(y.shape[0])
        self.y = y

        for key, value in kwargs.items():
            setattr(self, key, value)

        if self.D is None:
            self.D = (np.diag([-1] * y.shape[0], k=0) + np.diag([1] * (y.shape[0] - 1), k=1))[:-1]

        self.m, self.p = self.D.shape
        XTX = self.X.T.dot(self.X)

        self.A = np.zeros((self.p+2*self.m, self.p+2*self.m))
        self.A[:self.p, :self.p] = XTX

        delta1 = self.Lambda * np.vstack((np.zeros((self.p, 1)), np.ones((2*self.m, 1))))
        XTY = self.X.T.dot(y)
        delta2 = np.vstack((XTY, np.zeros((2*self.m, 1))))
        self.Delta = delta1 - delta2

        row_1 = np.hstack((np.zeros((self.m, self.p)), -np.eye(self.m), np.zeros((self.m, self.m))))
        row_2 = np.hstack((np.zeros((self.m, self.p)), np.zeros((self.m, self.m)), -np.eye(self.m)))
        self.P = np.vstack((row_1, row_2))
        self.Q = np.hstack((np.copy(self.D), -np.identity(self.m), np.identity(self.m)))

    def get_hyperparams(self):
        return {'Lambda': self.Lambda}
    
    def solve(self):
        x = cp.Variable(self.A.shape[0])
        objective = cp.Minimize(0.5 * cp.quad_form(x, self.A) + self.Delta.T @ x)
        constraints = [self.P @ x <= 0]
        constraints.append(self.Q @ x == 0)

        prob = cp.Problem(objective, constraints)
        prob.solve(solver=cp.OSQP, eps_abs=1e-10, eps_rel=1e-10, max_iter=1000000, polish=True ,verbose=False)
        self.eps = x.value.reshape(-1,1)
        self.u = prob.constraints[0].dual_value.reshape(-1,1)

        self.beta = self.eps[:self.p,:]
        self.xi_plus = self.eps[self.p:self.p+self.m, :]
        self.xi_minus = self.eps[self.p+self.m:, :]
        return self.beta, self.xi_plus, self.xi_minus