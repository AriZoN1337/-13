class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' открыт!")

# Далее твой код из 13.2:

r1 = Restaurant("Суши Мастер", "Японская")
r2 = Restaurant("Пельмени и Блины", "Русская")
r3 = Restaurant("Пиццерия", "Итальянская")

r1.describe_restaurant()
print()
r2.describe_restaurant()
print()
r3.describe_restaurant()

