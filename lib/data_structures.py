spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]

def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"] > 5]

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        print(f'{food["name"]} ({food["cuisine"]}) | Heat Level: {"🌶" * food["heat_level"]}')

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)  # Reuse the get_spiciest_foods function
    print_spicy_foods(spiciest_foods)


def get_average_heat_level(spicy_foods):
    total_heat = sum([food["heat_level"] for food in spicy_foods])
    return total_heat // len(spicy_foods)

def create_spicy_food(spicy_foods, new_food):
    spicy_foods.append(new_food)
    return spicy_foods



# Example of how these functions would work:
print(get_names(spicy_foods))  # Output: ["Green Curry", "Buffalo Wings", "Mapo Tofu"]

print(get_spiciest_foods(spicy_foods))  # Output: [{'name': 'Green Curry', 'cuisine': 'Thai', 'heat_level': 9}, {'name': 'Mapo Tofu', 'cuisine': 'Sichuan', 'heat_level': 6}]

print_spicy_foods(spicy_foods)
# Output:
# Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶
# Buffalo Wings (American) | Heat Level: 🌶🌶🌶
# Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶

print(get_spicy_food_by_cuisine(spicy_foods, "American"))  # Output: {'name': 'Buffalo Wings', 'cuisine': 'American', 'heat_level': 3}

print_spiciest_foods(spicy_foods)
# Output:
# Green Curry (Thai) | Heat Level: 🌶🌶🌶🌶🌶🌶🌶🌶🌶
# Mapo Tofu (Sichuan) | Heat Level: 🌶🌶🌶🌶🌶🌶

print(get_average_heat_level(spicy_foods))  # Output: 6

create_spicy_food(spicy_foods, {'name': 'Griot', 'cuisine': 'Haitian', 'heat_level': 10})
print(spicy_foods)  
# Output: [{'name': 'Green Curry', 'cuisine': 'Thai', 'heat_level': 9}, {'name': 'Buffalo Wings', 'cuisine': 'American', 'heat_level': 3}, {'name': 'Mapo Tofu', 'cuisine': 'Sichuan', 'heat_level': 6}, {'name': 'Griot', 'cuisine': 'Haitian', 'heat_level': 10}]