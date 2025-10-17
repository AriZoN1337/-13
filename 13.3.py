class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating=0):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = rating  # начальный рейтинг

    def describe_restaurant(self):
        print(f"Название ресторана: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")

    def open_restaurant(self):
        print(f"Ресторан '{self.restaurant_name}' открыт!")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг ресторана '{self.restaurant_name}' обновлен до {self.rating}")

# Пример использования
r = Restaurant("Кафе Приятель", "Кофейня", rating=4.5)
r.describe_restaurant()
r.update_rating(4.8)
r.describe_restaurant()
