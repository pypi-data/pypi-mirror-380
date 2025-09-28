from .da.otda import OTDA
from .cv.model import HoldOutCV, KFoldCV
from .gl.feature_selector import VanillaLasso, ElasticNet, NNLS
from .gl.change_point_detector import FusedLasso

import numpy as np
from .utils import intersect

def divide_and_conquer(a, b, gl_ins, cv_ins, da_ins, zmin, zmax, unit, pm_mat):
    if cv_ins is None:
        gl_class = type(gl_ins)
        hyperparams = gl_ins.get_hyperparams()
        da_class = type(da_ins)
        ns, nt = da_ins.ns, da_ins.nt
        Xs, Xt = da_ins.Xs, da_ins.Xt
        X = np.vstack((Xs, Xt))
        
        list_intervals = []
        list_M = []
        z = zmin
        while z < zmax:
            yz = a + b * z
            ys, yt = yz[0:ns, :], yz[ns:, :]
            da_model = da_class(np.hstack((Xs, ys)), np.hstack((Xt, yt)))
            Tz, _ = da_model.fit()
            interval_da = da_model.get_interval(a, b)

            # Select the interval containing the data point that we are currently conget_intervaldering.
            for i in interval_da:
                if i[0] <= z <= i[1]:
                    interval_da = [i]
                    break

            if interval_da[0][1] < z:
                z = interval_da[0][1] - 1e-6

            Omega_z = np.hstack((np.zeros((ns + nt, ns)), np.vstack((ns * Tz, np.identity(nt)))))
            a_tilde, b_tilde = Omega_z @ a, Omega_z @ b 
            
            if pm_mat is not None:
                a_tilde, b_tilde = pm_mat @ a_tilde, pm_mat @ b_tilde  
            else:
                Xz_tilde = Omega_z @ X
            
            while z < interval_da[0][1]:
                yz = a + b * z
                yz_tilde = Omega_z @ yz
                
                if pm_mat is not None:
                    yz_tilde = pm_mat @ yz_tilde
                    hyperparams['D'] = np.kron((np.diag([-1] * nt, k=0) + np.diag([1] * (nt - 1), k=1))[:-1], 
                                        1/(unit+1) * np.ones((1, unit+1)))
                    gl_model = gl_class(yz_tilde, **hyperparams)
                else:
                    gl_model = gl_class(Xz_tilde, yz_tilde, **hyperparams)
                M_v = gl_model.fit()
                
                if gl_model.is_empty():
                    z += 5e-4
                    continue
            
                interval_gl = gl_model.get_interval(a_tilde, b_tilde)            
                interval_z = intersect(interval_da, interval_gl)
                # with open('debug.txt', 'a') as f:
                #     f.write(f'{z}\t\t{interval_z}\n')
                list_intervals += interval_z
                list_M += [M_v]
                z = interval_z[0][1] + 5e-4

                if z > zmax:
                    break
        
        return list_intervals, list_M
    else:
        gl_class = type(gl_ins)
        hyperparams = gl_ins.get_hyperparams()
        cv_class = type(cv_ins)
        da_class = type(da_ins)
        ns, nt = da_ins.ns, da_ins.nt
        Xs, Xt = da_ins.Xs, da_ins.Xt
        X = np.vstack((Xs, Xt))
        
        list_intervals = []
        list_M = []
        z = zmin

        while z < zmax:
            yz = a + b * z
            ys, yt = yz[0:ns, :], yz[ns:, :]
            da_model = da_class(np.hstack((Xs, ys)), np.hstack((Xt, yt)))
            Tz, _ = da_model.fit()
            # da_model.check_KKT()
            interval_da = da_model.get_interval(a, b)

            # Select the interval containing the data point that we are currently conget_intervaldering.
            for i in interval_da:
                if i[0] <= z <= i[1]:
                    interval_da = [i]
                    break
            
            if interval_da[0][1] < z:
                z = interval_da[0][1] - 1e-6

            Omega_z = np.hstack((np.zeros((ns + nt, ns)), np.vstack((ns * Tz, np.identity(nt)))))
            a_tilde, b_tilde = Omega_z @ a, Omega_z @ b 
            Xz_tilde = Omega_z @ X
            while z < interval_da[0][1]:
                yz = a + b * z
                yz_tilde = Omega_z @ yz
                cv_model = cv_class(train_val_pairs=cv_ins.train_val_pairs)
                best_Lambda, _ = cv_model.fit(Xz_tilde, yz_tilde, gl_class, cv_ins.list_lambda)
                interval_cv = cv_model.get_interval(a_tilde, b_tilde)
                for i in interval_cv:
                    if i[0] <= z <= i[1]:
                        interval_cv = [i]
                        break

                interval_cv = intersect(interval_da, interval_cv)
                hyperparams['Lambda'] = best_Lambda

                if interval_cv[0][1] < z:
                    z = interval_cv[0][1] - 1e-6

                while z < interval_cv[0][1]:
                    yz = a + b * z
                    yz_tilde = Omega_z @ yz

                    gl_model = gl_class(Xz_tilde, yz_tilde, **hyperparams)
                    M_v = gl_model.fit()
                    # gl_model.check_KKT()
                    
                    if gl_model.is_empty():   
                        z += 5e-4
                        continue
                
                    interval_gl = gl_model.get_interval(a_tilde, b_tilde)
                    interval_z = intersect(interval_cv, interval_gl)
                    list_intervals += interval_z
                    list_M += [M_v]
                    z = interval_z[0][1] + 5e-4

                    if z > zmax:
                        break
                
                if z > zmax:
                    break
                
        return list_intervals, list_M

def fit(a, b, gl_ins, cv_ins=None, da_ins=None, zmin=-20, zmax=20, 
        unit=None, pm_mat=None):
    
    list_intervals, list_M = divide_and_conquer(a, b, gl_ins, cv_ins, da_ins, zmin, zmax, unit, pm_mat)
    
    Z = []
    M_obs = gl_ins.active_set

    for i in range(len(list_intervals)):
        if np.array_equal(list_M[i], M_obs):
            Z.append(list_intervals[i])
    return Z