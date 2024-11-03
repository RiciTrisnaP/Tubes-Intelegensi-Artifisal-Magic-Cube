import random

def ordered_crossover(parent1, parent2):
    children = [None, None]

    for i in range(2):
        child = [None] * len(parent1)
        
        start, end = sorted(random.sample(range(len(parent1)), 2))

        if i == 0:
            child[start:end] = parent1[start:end]
        else:
            child[start:end] = parent2[start:end]

        current_pos = end 
        source_parent = parent2 if i == 0 else parent1
        for elem in source_parent:
            if elem not in child:
                if current_pos >= len(parent1):
                    current_pos = 0
                child[current_pos] = elem
                current_pos += 1

        children[i] = child 

    return children

# Example usage
parent1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
parent2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]

children = ordered_crossover(parent1, parent2)
print("Parent 1:", parent1)
print("Parent 2:", parent2)
print("Children:")
for i, child in enumerate(children):
    print(f"Child {i + 1}:", child)
