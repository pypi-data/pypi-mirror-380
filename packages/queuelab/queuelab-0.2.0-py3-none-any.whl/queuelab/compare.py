import random
import matplotlib.pyplot as plt


# --------------------------
# M/M/1 Simulation Class
# --------------------------
class MM1:
    def __init__(self, arrival_rate, service_rate, max_customers=10000):
        self.lam = arrival_rate
        self.mu = service_rate
        self.max_customers = max_customers

    def simulate(self):
        arrival_time = 0
        service_end = 0
        total_wait = 0
        total_queue_length = 0
        customers = 0

        for _ in range(self.max_customers):
            # Next arrival time
            inter_arrival = random.expovariate(self.lam)
            arrival_time += inter_arrival

            # Service time
            service_time = random.expovariate(self.mu)

            # If server is free
            if arrival_time > service_end:
                service_start = arrival_time
            else:
                service_start = service_end

            service_end = service_start + service_time
            wait = service_start - arrival_time

            total_wait += wait
            total_queue_length += max(0, service_start - arrival_time)
            customers += 1

        avg_wait_time = total_wait / customers
        avg_queue_length = total_queue_length / customers

        return {"avg_wait_time": avg_wait_time, "avg_queue_length": avg_queue_length}


# --------------------------
# Theoretical M/M/1 Metrics
# --------------------------
def mm1_metrics(arrival_rate, service_rate):
    lam, mu = arrival_rate, service_rate
    rho = lam / mu
    if rho >= 1:
        raise ValueError("System is Unstable (ρ ≥ 1)")

    L = rho / (1 - rho)       # Avg customers in system
    Lq = rho**2 / (1 - rho)   # Avg customers in queue
    W = 1 / (mu - lam)        # Avg wait in system
    Wq = rho / (mu - lam)     # Avg wait in queue
    P0 = 1 - rho              # Probability system is empty

    return {
        "traffic_intensity": rho,
        "avg_customer_system": L,
        "avg_customer_queue": Lq,
        "avg_wait_time_system": W,
        "avg_wait_time_queue": Wq,
        "P0": P0,
    }


# --------------------------
# Compare Simulation vs Theory
# --------------------------
def compare_mm1(arrival_rate, service_rate, max_customers=10000):
    # Simulation
    sim = MM1(arrival_rate, service_rate, max_customers)
    sim_results = sim.simulate()

    # Theoretical
    math_results = mm1_metrics(arrival_rate, service_rate)

    print("\nComparison of M/M/1 Results")
    print("=" * 50)
    print(f"{'Metric':<25} {'Simulation':<15} {'Theory':<15}")
    print("-" * 50)
    print(
        f"{'Avg wait time (W)':<25} {sim_results['avg_wait_time']:<15.4f} {math_results['avg_wait_time_system']:<15.4f}"
    )
    print(
        f"{'Avg queue length (Lq)':<25} {sim_results['avg_queue_length']:<15.4f} {math_results['avg_customer_queue']:<15.4f}"
    )
    print("=" * 50)

    # Plot comparison
    labels = ['W (wait time)', 'Lq (queue length)']
    sim_vals = [sim_results['avg_wait_time'], sim_results['avg_queue_length']]
    math_vals = [math_results['avg_wait_time_system'], math_results['avg_customer_queue']]

    x = range(len(labels))
    plt.bar([i - 0.2 for i in x], sim_vals, width=0.4, label='Simulation')
    plt.bar([i + 0.2 for i in x], math_vals, width=0.4, label='Theoretical')

    plt.xticks(x, labels)
    plt.ylabel("Values")
    plt.title("M/M/1 Queue: Simulation vs Theoretical")
    plt.legend()
    plt.show()

    return {"simulation": sim_results, "theoretical": math_results}
