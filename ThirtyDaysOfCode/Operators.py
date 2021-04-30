# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    return round(meal_cost + meal_cost * (tip_percent / 100) + meal_cost * (tax_percent / 100))

if __name__ == '__main__':
    meal_cost = float(input())

    tip_percent = float(input())

    tax_percent = float(input())

    print(solve(meal_cost, tip_percent, tax_percent))
