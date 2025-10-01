import numpy as np
from sklearn.linear_model import LinearRegression
from scipy.sparse import csc_matrix, eye, diags
from scipy.sparse.linalg import spsolve


def remove_background(signal, background):
    shape = list(background.shape) + [1] * (len(signal.shape) - len(background.shape))
    return signal - np.reshape(background, shape=shape)


def estimate_baseline(signal):
    corrected_signal = arPLS_fitting(signal)
    baseline = signal - corrected_signal
    return baseline


def arPLS_fitting(input_array,lam = 100, repeat = 15):
    orig_array=np.array(input_array) 
    size=orig_array.shape[0]
    w=np.ones(size)
    for i in range(1,repeat+1):
        corrected = background_estimator_aPLS(orig_array, w, lam)
        d=orig_array-corrected
        dssn=np.abs(d[d<0].sum())
        if(dssn<0.001*(abs(orig_array)).sum() or i==repeat):
            if(i==repeat): print('baseline cannot be determined..')
            break
        w[d>=0]=0 # d>0 -> part of a peak, ignore it
        w[d<0]=np.exp(i*np.abs(d[d<0])/dssn)
        w[0]=np.exp(i*(d[d<0]).max()/dssn) 
        w[-1]=w[0]
    return orig_array-corrected


def background_estimator_aPLS(input_array,w,lam):
    array=np.matrix(input_array)
    size=array.size
    # i=np.arange(0,m)
    E=eye(size,format='csc')
    D=E[1:]-E[:-1] # numpy.diff() errors with sparse matrix .. might give errors
    W=diags(w,0,shape=(size,size))
    A=csc_matrix(W+(lam*D.T*D))
    B=csc_matrix(W*array.T)
    background=spsolve(A,B)
    return np.array(background)
