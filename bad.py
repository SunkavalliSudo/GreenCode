import time

from codecarbon import track_emissions


@track_emissions(project_name="bad")
def count_buildings_with_sunset_view(buildings):
    count = 0

    # Iterate through each building from left to right
    for i in range(len(buildings)):
        can_see_sunset = True
        # Check if this building is taller than all buildings to its right
        for j in range(i + 1, len(buildings)):
            if buildings[i] <= buildings[j]:
                can_see_sunset = False
                break
        if can_see_sunset:
            count += 1

    return count


# Example usage:
buildings = [3, 7, 8, 3, 6, 14, 7, 8, 10, 13, 9, 4]
print(count_buildings_with_sunset_view(buildings * 1000))