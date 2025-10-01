import random
import matplotlib.pyplot as plt

class MM1:
    def __init__(self, arrival_rate, service_rate, max_customers=1000):
        self.lam = arrival_rate
        self.mu = service_rate
        self.max_customers = max_customers
        self.queue_lengths = []
        self.wait_times = []

    def simulate(self):
        t = 0
        server_busy_until = 0
        queue = 0

        for _ in range(self.max_customers):
            # Generate next arrival
            inter_arrival = random.expovariate(self.lam)
            t += inter_arrival

            # If server is free
            if t >= server_busy_until:
                wait_time = 0
                service_time = random.expovariate(self.mu)
                server_busy_until = t + service_time
                queue = 0
            else:
                # Server busy -> customer waits
                wait_time = server_busy_until - t
                service_time = random.expovariate(self.mu)
                server_busy_until += service_time
                queue += 1

            self.wait_times.append(wait_time)
            self.queue_lengths.append(queue)

        return {
            "avg_wait_time": sum(self.wait_times) / len(self.wait_times),
            "avg_queue_length": sum(self.queue_lengths) / len(self.queue_lengths),
        }

    def plot_queue_length(self):
        plt.plot(self.queue_lengths)
        plt.xlabel("Customer Index")
        plt.ylabel("Queue Length")
        plt.title("M/M/1 Queue Simulation")
        plt.show()
