from random import uniform

it_max = 1000
v = [[0, 0, 0, 0, 0] for _ in range(10)]  # Initializing the velocity list
P = [[0, 0, 0, 0, 0] for _ in range(10)]  # Initializing the position list
Pbest = [[0, 0, 0, 0, 0] for _ in range(10)]  # Initializing the personal best list
gbest = [0, 0, 0, 0, 0]  # Initializing the global best

# Initialize particles (P) and Pbest with random values
for i in range(10):
    for j in range(5):
        randnum = uniform(-5, 5)
        P[i][j] = randnum
        Pbest[i][j] = randnum
        gbest[j] = randnum  # gbest is initialized with the first particle's position

# Fitness function (Rastrigin function)
def fitness(x):
    f = 0
    for z in range(4):
        f += 100 * ((x[z + 1] - x[z] ** 2) ** 2) + (x[z] - 1) ** 2
    return f

# Particle Swarm Optimization
for i in range(it_max):
    for j in range(10):
        fb = fitness(P[j])  # Fitness of the current particle
        pb = fitness(Pbest[j])  # Fitness of the personal best
        if fb < pb:  # If the current fitness is better, update Pbest
            Pbest[j] = P[j].copy()

    # Update global best
    gbest = Pbest[0]
    for k in range(1, 10):
        if fitness(Pbest[k]) < fitness(gbest):
            gbest = Pbest[k].copy()

    print(f"iteration {i} {fitness(gbest)}")

    # Update velocity and position
    for j in range(10):
        for k in range(5):
            v[j][k] += 2 * uniform(0, 1) * (Pbest[j][k] - P[j][k]) + 2 * uniform(0, 1) * (gbest[k] - P[j][k])
            P[j][k] = P[j][k] + v[j][k]  # Update position with new velocity

    print(gbest, fitness(gbest))
