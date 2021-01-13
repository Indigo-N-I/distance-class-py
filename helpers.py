### Helper functions ###
import scipy as sp
import numpy as np

"""
TODO: function to find closest
"""
def closest():
    pass

def shift(data: np.ndarray):
    minimum = np.min(data)
    return (data + minimum, minimum)


def gamma_mle(data: np.ndarray, iterations = 4: int):
    '''
    data: numpy array of the data that is to be fitted to a gamma distribution
    interations: number of times the loop is to run, 4 tends to be sufficint

    returns a
    '''
    #using Gamma(shape,scale) not Gamma(shape, rate)
    alpha = [0,0] # 0 is k, 1 is theta
    x = np.asarray([0,0]) #0 is np.log(np.mean(x)) 1 is np.mean(np.log(x))

    x[0] = np.log(np.mean(data))
    x[1] = np.mean(np.log(data))

    alpha[0]= .5/(x[0] - x[1])

    k = alpha[0]
    for i in range(iterations):
        digamma = sp.special.digamma(k)
        digamma_prime = sp.special.polygamma(1, k)
        k = 1/ (1/k + (x[1] - x[0] + np.log(k) - digamma)/(k**2*(1/k - digamma_prime)))
        ##print("itermidiary step:", k)

    alpha[0] = k
    alpha[1] = np.exp(x[0])/alphas[0]
    return alpha
