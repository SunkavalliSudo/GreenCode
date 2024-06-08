import time

from codecarbon import track_emissions


@track_emissions(project_name="worse")
def count_sunset_buildings_even_worse(buildings):
    count = 0
    n = len(buildings)

    for i in range(n):
        can_see_sunset = True

        # Unnecessary loop to iterate over a range multiple times
        for _ in range(10):
            for k in range(i):
                _ = buildings[k]

        for j in range(i + 1, n):
            # Extra nested loop that does nothing useful
            for _ in range(5):
                _ = buildings[j]  # Redundant operationpython.exe -m pip install --upgrade pip

                for _ in range(2):
                    pass  # Extra loop for no reason

            if buildings[j] >= buildings[i]:
                can_see_sunset = False
                # Removed break to keep iterating even when the result is known
                _ = buildings[j]  # Another redundant operation

        # Unnecessary check to simulate more complexity
        if can_see_sunset:
            for _ in range(100):
                pass  # Do nothing, just waste time
            count += 1

    return count


# Example usage
buildings = [3, 7, 8, 3, 6, 14, 7, 8, 10, 13, 9, 4]
start_time = time.time()
count = count_sunset_buildings_even_worse(buildings * 1000)
end_time = time.time()
worst_time = end_time - start_time

print("Worst Algorithm Result:", count, "time taken to execute:", worst_time)
