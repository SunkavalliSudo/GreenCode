import time

from codecarbon import track_emissions


@track_emissions(project_name="mediumCode")
def count_sunset_buildings_worst(buildings):
    count = 0
    n = len(buildings)
    for i in range(n):
        can_see_sunset = True
        for j in range(i + 1, n):
            if buildings[j] >= buildings[i]:
                can_see_sunset = False
                break
        if can_see_sunset:
            count += 1

    return count


# Example usage
buildings = [3, 7, 8, 3, 6, 14, 7, 8, 10, 13, 9, 4]
start_time = time.time()
count = count_sunset_buildings_worst(buildings * 200)
end_time = time.time()
worst_time = end_time - start_time

print("Optimized Algorithm Result:", count, "time taken to execute:", worst_time)