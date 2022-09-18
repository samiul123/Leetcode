import collections
import queue


def findOrbits(associations):
    graph = collections.defaultdict(list)

    for assocation in associations:
        splitedAssociation = assocation.split(')')
        graph[splitedAssociation[0]].append(splitedAssociation[1])

    queue = [('SUN', 0)]
    planetLevel = []

    while queue:
        planet, level = queue.pop(0)
        planetLevel.append((planet,level))

        for adjPlanet in graph[planet]:
            queue.append((adjPlanet, level+1))

    print(planetLevel)


findOrbits(["SUN)B", "B)C", "C)D", "C)H", "B)F"])


