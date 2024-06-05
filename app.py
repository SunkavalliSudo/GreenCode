import time
from codecarbon import track_emissions


@track_emissions(project_name="xyz")
def count_sunset_buildings_optimized(buildings):
    count = 0
    max_height = 0

    # Traverse the buildings from right to left
    for height in reversed(buildings):
        if height > max_height:
            count += 1
            max_height = height

    return count


# Example usage
buildings = [3, 7, 8, 3, 6, 14, 7, 8, 10, 13, 9, 4]



start_time = time.time()
count = count_sunset_buildings_optimized(buildings * 50)
end_time = time.time()
worst_time = end_time - start_time

print("Optimized Algorithm Result:", count , "time taken to execute:", worst_time)