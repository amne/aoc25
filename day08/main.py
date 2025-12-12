def vec3_dist(a,b):
    return ((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)**0.5

def compute_all_distances(junctions):
    distances = []
    for i in range(len(junctions)):
        for j in range(i + 1, len(junctions)):
            dist = vec3_dist(junctions[i], junctions[j])
            distances.append((i, j, dist))
    distances.sort(key=lambda x: x[2])
    return distances

def circuits_p1(junctions):
    distances = compute_all_distances(junctions)
    print("Distances done", len(distances))
    # print(distances)
    circuits = [[c] for c in range(len(junctions))]
    connections = 1000
    # while shortest is not None and connections > 0:
    while connections > 0:
        connections -= 1
        shortest = distances.pop(0)
        extended_circuit = False
        circuits_to_merge = []
        for i in range(len(circuits)):
            if shortest[0] in circuits[i]:
                circuits_to_merge.append(i)
            if shortest[1] in circuits[i]:
                circuits_to_merge.append(i)
        circuits_to_merge = list(set(circuits_to_merge))
        # if len == 1 then both are in the same circuit
        if len(circuits_to_merge) == 1:
            # connections += 1
            continue
        if len(circuits_to_merge) == 2:
            circuits[circuits_to_merge[0]] += circuits[circuits_to_merge[1]]
            circuits = circuits[:circuits_to_merge[1]] + circuits[circuits_to_merge[1]+1:]
        # print("Connections left:", connections)
        # circuits = sorted(circuits, key=lambda x: len(x), reverse=True)
        # print("Final circuits:", circuits)
        # shortest = shortest_distance_p1(distances, circuits)
    # print(", ".join([str(len(c)) for c in circuits]))
    circuits = sorted(circuits, key=lambda x: len(x), reverse=True)
    # print("Final circuits:", circuits)
    # print(", ".join([str(len(c)) for c in circuits]))
    print(len(circuits[0])*len(circuits[1])*len(circuits[2]))

def main():
    vec3_string = []
    # with open("input.txt") as f:
    with open("biginput.txt") as f:
        for line in f:
            vec3_string.append(line.strip().split(","))
    junctions = [(float(x), float(y), float(z)) for x, y, z in vec3_string]
    # [print(j) for j in junctions]
    circuits_p1(junctions)


if __name__ == "__main__":
    main()
