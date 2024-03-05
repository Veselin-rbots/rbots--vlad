from collections import deque

n = int(input())

stations = deque([])

for _ in range(n):
    stations.append(input())

tank_petrol = 0


for big_circle_iteration in range(n):
    is_valid = True
    for small_circle_iteration in range(n):
        current_station = stations.popleft()
        stations.append(current_station)
        petrol, distance_to_next_station = current_station.split()
        petrol = int(petrol)
        distance_to_next_station = int(distance_to_next_station)
        tank_petrol += petrol

        if tank_petrol >= distance_to_next_station:
            tank_petrol -= distance_to_next_station
        else:
            is_valid = False
            break
    if is_valid:
        print(big_circle_iteration)
        break