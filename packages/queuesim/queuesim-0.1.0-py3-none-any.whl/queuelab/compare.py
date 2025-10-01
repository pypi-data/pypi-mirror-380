import matplotlib.pyplot as plt
from .mm1 import MM1
from .formulas import mm1_metrics

def compare_mm1(arrival_rate , service_rate , max_customers = 10000):
    #Simulation
    sim = MM1(arrival_rate , service_rate,max_customers)
    sim_results = sim.simulate()

    #Theoretical Records

    math_results = mm1_metrics(arrival_rate,service_rate)

    print("\n Comparison of M/M/1 Results")
    print("=" * 40)
    print(f"{'Metric':<25} {'Simulation':<15} {'Theory':<15}")
    print("-" * 40)
    print(
        f"{'Avg wait time (W)':<25} {sim_results['avg_wait_time']:<15.4f} {math_results['avg_wait_time_system']:<15.4f}")
    print(
        f"{'Avg queue length (Lq)':<25} {sim_results['avg_queue_length']:<15.4f} {math_results['avg_customers_queue']:<15.4f}")
    print("=" * 40)

    labels = ['W (wait time)', 'Lq (queue length)']
    sim_vals = [sim_results['avg_wait_time'], sim_results['avg_queue_length']]
    math_vals = [math_results['avg_wait_time_system'], math_results['avg_customers_queue']]

    x = range(len(labels))
    plt.bar([i-0.2 for i in x],sim_vals , width=0.4 , label = 'Simulation')
    plt.bar([i + 0.2 for i in x], math_vals, width=0.4, label='Theoretical')

    plt.xticks(x,labels)
    plt.ylabel("Values")
    plt.title("M/M/1 Queue : Simulation Data vs Theoretical Data")
    plt.legend()
    plt.show()

    return {"simulation" : sim_results , "Theoretical" : math_results}
