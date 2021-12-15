
from queue import PriorityQueue

# pre-amble
q_rates = PriorityQueue()
q_months = PriorityQueue()

rates = [1, 2, 0.5, 5, 2.75, 4]
months = [2, 6, 7, 4, 2, 1]
d_rates = []

for k in range(len(rates)):
    q_rates.put((-rates[k], rates[k]))
    q_months.put((-months[k], months[k]))

for k in range(len(rates)):
    d_rates.append((q_rates.get()[1], q_months.get()[1]))

print(d_rates)


