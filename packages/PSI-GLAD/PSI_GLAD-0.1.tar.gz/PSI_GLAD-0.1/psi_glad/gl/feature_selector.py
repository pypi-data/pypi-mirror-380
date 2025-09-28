import numpy as np
from abc import ABC, abstractmethod
from .base import GenLasso 
from sklearn.linear_model import LinearRegression, Lasso as skLasso, ElasticNet as skElasticNet
import cvxpy as cp

class FeatureSelector(ABC):
    def gen_data(n, p, true_beta, rho=1):
        '''
        Generate synthetic data for feature selection
        '''
        if rho == 1:
            X = np.random.normal(loc=0, scale=1, size=(n,p))
            mu = X @ true_beta
            y = mu + np.random.normal(loc=0, scale=1, size=(n,1))
            Sigma = np.identity(n)
        else:
            Sigma = np.identity(n)
            for i in range(n):
                for j in range(n):
                    if i == j:
                        continue
                    Sigma[i][j] = rho ** (abs(i - j))
            X = np.random.normal(loc=0, scale=1, size=(n,p))
            mu = X @ true_beta
            noise = np.random.multivariate_normal(mean=np.zeros(n), cov=Sigma).reshape(n, 1)
            y = mu + noise

        return X, y, mu, Sigma

    @abstractmethod
    def get_hyperparams(self):
        pass

    @abstractmethod
    def solve(self):
        pass

    def fit(self):
        self.solve()
        self.active_set = np.where(np.round(self.beta, 9) != 0)[0].tolist()
        return self.active_set
    
    def eval(self, X_val, y_val):
        '''
        Evaluate the model on validation data
        '''    
        y_pred = X_val @ self.beta
        residuals = y_val - y_pred
        mse = 1/2 * np.mean(residuals**2)
        return mse
    
    def is_empty(self):
        return len(self.active_set)==0

class VanillaLasso(GenLasso, FeatureSelector):
    """
    Vanilla Lasso feature selector.
    """
    def __init__(self, X, y, **kwargs):
        super().__init__()

        self.X = X
        self.y = y

        for key, value in kwargs.items():
            setattr(self, key, value)

        self.D = np.eye(X.shape[1])
        self.m, self.p = self.D.shape
        XTX = self.X.T.dot(self.X)

        self.A = np.zeros((self.p+2*self.m, self.p+2*self.m))
        self.A[:self.p, :self.p] = np.copy(XTX)

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
    
    def solve(self, method='sklearn'):
        if method == 'sklearn':
            lasso = skLasso(alpha = self.Lambda / self.X.shape[0], 
                        fit_intercept=False, tol = 1e-10, max_iter=1000000000)
            lasso.fit(self.X, self.y)
            self.beta = lasso.coef_.reshape(self.p, 1)
            self.xi_plus = np.maximum(self.beta, 0)  
            self.xi_minus = np.maximum(-self.beta, 0) 

        elif method == 'cvxpy':
            x = cp.Variable(self.A.shape[0])
            objective = cp.Minimize(0.5 * cp.quad_form(x, self.A) + self.Delta.T @ x)
            constraints = [self.P @ x <= 0]
            constraints.append(self.Q @ x == 0)

            prob = cp.Problem(objective, constraints)
            prob.solve(solver=cp.OSQP, eps_abs=1e-10, eps_rel=1e-10, max_iter=1000000, polish=True ,verbose=False)
            self.eps = x.value.reshape(-1,1)
            # self.u = prob.constraints[0].dual_value.reshape(-1,1)

            self.beta = self.eps[:self.p,:]
            self.xi_plus = self.eps[self.p:self.p+self.m, :]
            self.xi_minus = self.eps[self.p+self.m:, :]

        return self.beta, self.xi_plus, self.xi_minus
    
class ElasticNet(GenLasso, FeatureSelector):
    """
    Elastic Net feature selector.
    """
    def __init__(self, X, y, **kwargs):
        super().__init__()

        self.X = X
        self.y = y

        for key, value in kwargs.items():
            setattr(self, key, value)

        self.D = np.eye(X.shape[1])
        
        self.m, self.p = self.D.shape 
        XTX_Gamma = X.T.dot(X) + self.Gamma * np.eye(self.p)

        self.A = np.zeros((self.p+2*self.m, self.p+2*self.m))
        self.A[:self.p, :self.p] = XTX_Gamma

        delta1 = self.Lambda * np.vstack((np.zeros((self.p, 1)), np.ones((2*self.m, 1))))
        XTY = X.T.dot(y)
        delta2 = np.vstack((XTY, np.zeros((2*self.m, 1))))
        self.Delta = delta1 - delta2

        row_1 = np.hstack((np.zeros((self.m, self.p)), -np.eye(self.m), np.zeros((self.m, self.m))))
        row_2 = np.hstack((np.zeros((self.m, self.p)), np.zeros((self.m, self.m)), -np.eye(self.m)))
        self.P = np.vstack((row_1, row_2))

        self.Q = np.hstack((np.copy(self.D), -np.identity(self.m), np.identity(self.m)))

    def get_hyperparams(self):
        return {'Lambda': self.Lambda, 'Gamma': self.Gamma}
    
    def solve(self, method='sklearn'):
        if method == 'sklearn':
            elasticnet = skElasticNet(alpha=(self.Lambda+self.Gamma)/self.X.shape[0], 
                                    l1_ratio=self.Lambda/(self.Lambda+self.Gamma), 
                                    fit_intercept=False, tol = 1e-10, max_iter=1000000000)
            elasticnet.fit(self.X, self.y)
            self.beta = elasticnet.coef_.reshape(self.p, 1)
            self.xi_plus = np.maximum(self.beta, 0)  
            self.xi_minus = np.maximum(-self.beta, 0) 

        elif method == 'cvxpy':
            x = cp.Variable(self.A.shape[0])
            objective = cp.Minimize(0.5 * cp.quad_form(x, self.A) + self.Delta.T @ x)
            constraints = [self.P @ x <= 0]
            constraints.append(self.Q @ x == 0)

            prob = cp.Problem(objective, constraints)
            prob.solve(solver=cp.OSQP, eps_abs=1e-10, eps_rel=1e-10, max_iter=1000000, polish=True ,verbose=False)
            self.eps = x.value.reshape(-1,1)
            # self.u = prob.constraints[0].dual_value.reshape(-1,1)

            self.beta = self.eps[:self.p,:]
            self.xi_plus = self.eps[self.p:self.p+self.m, :]
            self.xi_minus = self.eps[self.p+self.m:, :]

        return self.beta, self.xi_plus, self.xi_minus
    
class NNLS(GenLasso, FeatureSelector):
    """
    Non-Negative Least Squares feature selector.
    """
    def __init__(self, X, y, **kwargs):
        super().__init__()

        self.X = X
        self.y = y

        self.p = self.X.shape[1]
        self.A = X.T.dot(X)
        self.Delta = -X.T.dot(y)
        self.P = -np.eye(self.p)

    def get_hyperparams(self):
        return {}
    
    def solve(self, method='sklearn'):
        if method == 'sklearn':
            nnls = LinearRegression(fit_intercept=False, tol=1e-10, positive=True)
            nnls.fit(self.X, self.y)
            self.beta = nnls.coef_.reshape(self.p, 1)
        elif method == 'cvxpy':
            x = cp.Variable(self.A.shape[0])
            objective = cp.Minimize(0.5 * cp.quad_form(x, self.A) + self.Delta.T @ x)
            constraints = [self.P @ x <= 0]

            prob = cp.Problem(objective, constraints)
            prob.solve(solver=cp.OSQP, eps_abs=1e-10, eps_rel=1e-10, max_iter=1000000, polish=True ,verbose=False)
            self.beta = x.value.reshape(-1,1)
            # self.u = prob.constraints[0].dual_value.reshape(-1,1)

        return self.beta