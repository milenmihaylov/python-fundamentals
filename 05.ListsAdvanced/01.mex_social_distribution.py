population = [int(x) for x in input().split(', ')]
minimum_wealth = int(input())

equal_distribution = False
for _ in range(len(population) + 1):
    wealthiest = max(population)
    poorest = min(population)
    if poorest < minimum_wealth:
        wealth_distribution = minimum_wealth - poorest
        population[population.index(poorest)] += wealth_distribution
        population[population.index(wealthiest)] -= wealth_distribution
        equal_distribution = False
    else:
        equal_distribution = True
        break

if equal_distribution:
    print(population)
else:
    print('No equal distribution possible')
