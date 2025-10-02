import numpy as np

def bass_cumulative_fraction(t,p,q):
    return (1 - np.exp(-(p+q)*t)) / (1 + (q/p)*np.exp(-(p+q)*t))

def bass_sales_fraction(t,p,q):
    return ( (p+q)**2 / p ) * np.exp(-(p+q)*t) / ( (1 + (q/p)*np.exp(-(p+q)*t))**2 )

def bass_sales(t,p,q,m):
    return ( m*(p+q)**2 / p ) * np.exp(-(p+q)*t) / ( (1 + (q/p)*np.exp(-(p+q)*t))**2 )

def bass_sales_generations(t,p,q,m,tau_i):
    ## m,tau_i need to be lists,
    ## first entry in tau_i should be 0

    N = len(m)
    gen_sales = np.zeros((len(t),N))
    Fi = np.zeros((len(t),N))

    for n in range(N):
        ti = t - tau_i[n]
        ti[ti < 0] = 0
        Fi[:,n] = bass_cumulative_fraction(ti,p,q)

        for k in range(n+1):
            Gk = m[k] * np.prod([ Fi[:,i] for i in range(k,n+1)],axis = 0)
            gen_sales[:,n] += Gk

        if n < N-1:
            ti = t - tau_i[n+1]
            ti[ti < 0] = 0
            gen_sales[:,n] *= (1 - bass_cumulative_fraction(ti,p,q))

    return gen_sales

def fit_bass_model_generations(counts,p0,q0,m0,tau0):

    t = np.arange(counts.shape[0])
    gen = len(m0)

    def loss_function(params):
        p = params[0]
        q = params[1]
        m = params[2:2+gen]
        tau_i = params[2+gen:]
        pred_sales = bass_sales_generations(t,p,q,m,tau_i)
        return np.sum((counts - pred_sales)**2)
    
    from scipy.optimize import minimize
    # x0 = [x for xs in [[p0],[q0],m0] for x in xs]
    # res = minimize(loss_function, x0=x0, args = (tau0))

    # return {'p': res.x[0], 'q': res.x[1], 'm': res.x[2:2+gen]}
    
    
    x0 = [x for xs in [[p0],[q0],m0,tau0] for x in xs]
    res = minimize(loss_function, x0=x0)
    return {'p': res.x[0], 'q': res.x[1], 'm': res.x[2:2+gen], 'tau': res.x[2+gen:]}

