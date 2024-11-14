gym_cost, trainer_cost, budget = map(int, input().split())

if gym_cost > budget:
    print(0)
elif gym_cost + trainer_cost <= budget:
    print(2)
else:
    print(1)
