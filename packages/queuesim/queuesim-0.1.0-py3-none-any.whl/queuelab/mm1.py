import random
import matplotlib.pyplot as plt

class MM1:
    def __init__(self, arrival_rate , service_rate , max_customers = 1000):
        self.lam = arrival_rate
        self.mu = service_rate
        self.max_customers = max_customers
        self.queue_lengths = []
        self.wait_times = []

    def simulate(self):
        t = 0
        server_busy_until = 0

        for _ in range(self.max_customers):
            inter_arrival = random.expovariate(self.lam)
            t += inter_arrival

            if t>= server_busy_until :
                wait_time = 0
                service_time = random.expovariate(self.mu)
                server_busy_until = t + service_time

            else:
                wait_time = server_busy_until - t
                service_time = random.expovariate(self.mu)
                server_busy_until +=service_time

                self.wait_times.append(wait_time)
                self.queue_lengths.append(len(self.queue_lengths))

                return{
                    "avg waiting time ": sum(self.wait_times) / len(self.wait_times),
                "avg queue length ": sum(self.queue_lengths)/len(self.queue_lengths),

                }

    def plot_queue_length(self):
        plt.plot(self.queue_lengths)
        plt.xlabel("Customer Index")
        plt.ylabel("Queue Length")
        plt.title("M/M/1 Queue Simulation")
        plt.show()
