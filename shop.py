lass Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class Cart:
    def __init__(self):
        self.items = []

    def add_product(self, product):
        self.items.append(product)
        print(f"Товар '{product.name}' добавлен.")

    def delete(self, name):
        for pro in self.items:
            if pro.name.lower() == name.lower():
                self.items.remove(pro)
                print("Удалено.")
                return
        print("Товар не найден в корзине.")

    def get_total(self):
        return sum(pro.price for pro in self.items)

    def show(self):
        if not self.items:
            print('Корзина пуста')
        else:
            for product in self.items:
                print(product.name, "   ", product.price)
            print("Итого:", self.get_total())


    def clear(self):
        self.items.clear()
        print('Корзина очищена.')

class Shop:
    def __init__(self):
        self.goods = [
            Product('Banan', 1000),
            Product('Apple', 500),
            Product('Bread', 200),
            Product('Milk', 650)
        ]

    def show_products(self):
        print("\n--- Ассортимент магазина ---")
        for product in self.products:

            print(product.name, "  ", product.price)


    def get_pro_by_name(self, name):
        for product in self.goods:
            if product.name.lower() == name.lower():
                return product
        return None

class User:
    def __init__(self, name):
        self.name = name
        self.cart = Cart()
        self.history = []

    def add_history(self, action):
        self.history.append(action)

class StoreApp:
    def __init__(self):
        self.shop = Shop()
        self.is_running = False
        self.user = None

    def show_help(self):
        print("\nКоманды:")
        print("1 - Список товаров")
        print("2 - Добавить в корзину")
        print("3 - Просмотр корзины")
        print("4 - Удалить из корзины")
        print("5 - Справка")
        print("6 - Оформить заказ")
        print("7 - Выход")

    def start(self):
        name = input("Введите ваше имя: ")
        self.user = User(name)
        print(f"Добро пожаловать, {self.user.name}!")
        self.is_running = True
        self.show_help()
        
        while self.is_running:
            self.main_loop()

    def main_loop(self):
        command = input("Выберите действие: ")
        if not command: return
        self.user.add_history(command)
        self.process_command(command)

    def process_command(self, cmd):
        if cmd == '1':
            self.shop.show_products()
        elif cmd == '2':
            name = input("Введите название товара: ")
            product = self.shop.get_pro_by_name(name)
            if product:
                self.user.cart.add_product(product)
            else:
                print("Этого товара сейчас нет в наличии.")
        elif cmd == '3':
            self.user.cart.show()
        elif cmd == '4':
            name = input("Что удалить? ")
            self.user.cart.delete(name)
        elif cmd == '5':
            self.show_help()
        elif cmd == '6':
            total = self.user.cart.get_total()
            if total > 0:
                print("Заказ оформлен. Спасибо за покупку!")
                self.user.cart.clear()
            else:
                print("Ваша корзина пуста.")
        elif cmd == '7':
            self.exit_app()
        else:
            print("Ошибка. Введите '5' для справки.")

    def exit_app(self):
        print(f"До свидания, {self.user.name}!")
        self.is_running = False

if __name__ == '__main__':
    app = StoreApp()
    app.start()
      
