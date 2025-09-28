from abc import ABC
import numpy as np
# import scipy.sparse as sp
# import scipy.sparse.linalg as spla
from ..utils import solve_linear_inequalities

class GenLasso(ABC):
    def __init__(self):
        '''
        Initialize the QP-based Generalized Lasso
        '''
        self.A = None
        self.Delta = None
        self.P = None
        self.Q = None
        self.D = None
        self.u = None

    def get_interval(self, a, b):
        '''
        Get the interval of z such that the active set and I set remains unchanged
        when the response vector y changes as y = a + bz. 
        '''
        if self.Q is not None: # Vanilla Lasso, Elastic Net, Fused Lasso
            if self.u is not None:
                I = np.where(self.u <= 1e-6)[0].tolist()
            else:
                xi = np.vstack((self.xi_plus, self.xi_minus))
                I = np.where(xi >= 1e-9)[0].tolist()
            Ic = [i for i in range(2*self.m) if i not in I]
            PI = np.copy(self.P[I, :])
            PIc = np.copy(self.P[Ic, :])
            
            # y = a + bz
            # [delta] = g0 + g1z
            g0 = np.vstack((-self.X.T @ a, self.Lambda * np.ones((2*self.m, 1))))
            g1 = np.vstack((-self.X.T @ b, np.zeros((2*self.m, 1))))

            self.G = np.vstack((np.hstack((self.A, PIc.T, self.Q.T)), 
                            np.hstack((PIc, np.zeros((len(Ic), len(Ic))), np.zeros((len(Ic), self.m)))), 
                            np.hstack((self.Q, np.zeros((self.m, len(Ic)+self.m))))))
            self.G = np.linalg.inv(self.G)

            self.vec1 = np.vstack((g0, np.zeros((len(Ic)+self.m, 1))))
            self.vec2 = np.vstack((g1, np.zeros((len(Ic)+self.m, 1))))

            h0 = - self.G[:(self.p+2*self.m+len(Ic)), :] @ self.vec1
            h1 = - self.G[:(self.p+2*self.m+len(Ic)), :] @ self.vec2

            temp = np.vstack((np.hstack((-PI, np.zeros((len(I), len(Ic))))),       
                            np.hstack((np.zeros((len(Ic), self.p+2*self.m)), np.identity(len(Ic))))))

            psi = temp @ h0
            phi = temp @ h1

            # sparse = sp.csc_matrix(self.mat2)

            # # Factorize sparse A
            # lu = spla.splu(sparse)

            # # Solve A X = I → gives full inverse
            # I = np.eye(self.mat2.shape[0])
            # self.mat2 = lu.solve(I)
        
        else: # Non-negative Least Squares
            I = np.where(self.beta > 1e-6)[0].tolist()
            Ic = [i for i in range(len(self.beta)) if i not in I]
            PI = np.copy(self.P[I, :])
            PIc = np.copy(self.P[Ic, :])

            # y = a + bz
            # [delta] = g0 + g1z
            g0 = np.vstack((-self.X.T @ a))
            g1 = np.vstack((-self.X.T @ b))

            self.G = np.vstack((np.hstack((self.A, PIc.T)), 
                            np.hstack((PIc, np.zeros((len(Ic), len(Ic)))))))
            self.G = np.linalg.inv(self.G)

            temp = np.vstack((np.hstack((-PI, np.zeros((len(I), len(Ic))))),       
                            np.hstack((np.zeros((len(Ic), self.P.shape[1])), np.identity(len(Ic))))))

            self.vec1 = np.vstack((g0, np.zeros((len(Ic), 1))))
            self.vec2 = np.vstack((g1, np.zeros((len(Ic), 1))))

            h0 = - self.G @ self.vec1
            h1 = - self.G @ self.vec2

            psi = temp @ h0
            phi = temp @ h1

        # Solve the inequalities: p + qz <= 0
        return solve_linear_inequalities(-psi, -phi)