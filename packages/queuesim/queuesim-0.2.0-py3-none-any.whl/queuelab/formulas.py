def mm1_metrics(arrival_rate , service_rate):
    lam , mu  = arrival_rate , service_rate
    rho = lam/mu
    if rho>=1:
        raise ValueError("System is Unstable (p>=1)")

    L = rho/(1-rho)
    Lq = rho**2/(1-rho)
    W = 1/(mu-lam)
    Wq = rho / (mu-lam)
    P0 = 1-rho

    return {
        "Traffic Intensity ": rho ,
        "avg_customer_system ":L,
        "avg_customer_queue ":Lq,
        "avg_waiting_time_system ":W,
        "avg_waiting_queue ":Wq,
        "P0 ": P0,
    }


