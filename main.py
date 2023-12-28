# Программа для розыгрыша игрушек в магазине

# Создаем пустой список игрушек
toys = []

# Функция для добавления новых игрушек в список
def add_toy(name, weight):
    toy = {"name": name, "weight": weight}
    toys.append(toy)

# Функция для получения заданного веса игрушки
def get_toy(weight):
    # Создаем новый список игрушек с заданным весом
    selected_toys = [toy for toy in toys if toy["weight"] == weight]
    
    # Если есть игрушки с заданным весом, выбираем случайную
    if selected_toys:
        selected_toy = random.choice(selected_toys)
        return selected_toy["name"]
    else:
        return None

# Пример использования программы
if __name__ == "__main__":
    import random
    
    # Добавляем новые игрушки (вес указывается в граммах)
    add_toy("Мяч", 200)
    add_toy("Кукла", 500)
    add_toy("Машинка", 300)
    
    # Получаем игрушку с заданным весом (вес указывается в граммах)
    toy = get_toy(300)
    
    # Если есть игрушка с заданным весом, печатаем ее название
    if toy:
        print("Поздравляем, вы выиграли игрушку:", toy)
    else:
        print("К сожалению, сейчас нет игрушек с таким весом")