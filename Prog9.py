

with open("USPopulation.txt", "r") as pop:
    population = pop.readlines()
    population = [[int(i.strip()), x] for x, i in enumerate(population, start=1950)]
    pop_change = []
    for x in population[1::]:
        pop_change.append([x[0]-population[population.index(x) - 1][0]]+[population[population.index(x)-1][1]]+[x[1]])
    print(pop_change)
    print(f"Year with Most Population Growth: {max(pop_change)[1]} to {max(pop_change)[2]}")
    print(f"Year with Least Population Growth: {min(pop_change)[1]} to {min(pop_change)[2]}")
    print(f"Avg Population Change: {sum([x[0] for x in pop_change])/len(pop_change):.0f} People")