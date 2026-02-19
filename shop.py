class Product:
                def __init__(self, name, price):
                        self.name=name
                        self.price=price
class Cart:
                def __init__(self):
                        self.products=[]
                def add_product(self, product):
                        self.products.append(product)

                def remove_product(self, product_name):
                      self.products = [product for product in self.products if product.name != product_name]
                      print(f"Товар {product_name} удален")
                def get_total(self):
                        return sum(product.price for product in self.products)
                def clear_cart(self):
                     self.products.clear()
                     print("Корзина очищена")
                def display(self):
                   if not self.products:
                     print("Корзина пуста")
                   else:
                     print("Корзина")
                   for product in self.products:
                     print(f"- {product.name}: ${product.price}")
                     print(f"Сумма: ${self.get_total()}")
class Shop:
       products={
                'ЯБЛОКО': 500,
                'Банан': 300,
                'хлеб':150,
                'Молоко':400}
       def show_products(self):
                print(" Товары в налчие")
                for name, price in self.products.items():
                        print(f"- {name}: ${price}")
       def get_product_by_name(self, name):
                if name in self.products:
                        return Product(name, self.products[name])
                else:
                        print("Товар не найден")
                        return None
class User:
       def __init__(self,name):
                self.name=name
                self.cart=Cart()
       





class StoreApp:
    def __init__(self):
        # Initialize the components
        self.shop = Shop()
        self.user = User("Покупатель")
        self.is_running = True

    def show_help(self):
        print("\n--- Доступные команды ---")
        print("1. list   - Показать товары в магазине")
        print("2. add    - Добавить товар (например: add ЯБЛОКО)")
        print("3. show   - Показать мою корзину")
        print("4. remove - Удалить товар (например: remove ЯБЛОКО)")
        print("5. clear  - Очистить корзину")
        print("6. exit   - Выйти из приложения")
 

    def process_command(self, command):
        # Разбиваем ввод на части (команда и аргумент)
        parts = command.strip().split(maxsplit=1)
        if not parts:
            return

        action = parts[0].lower()
        
        if action == "list":
            self.shop.show_products()

        elif action == "add":
            if len(parts) > 1:
                item_name = parts[1]
                product = self.shop.get_product_by_name(item_name)
                if product:
                    self.user.cart.add_product(product)
                    print(f"Добавлено: {item_name}")
            else:
                print("Укажите название товара после 'add'")

        elif action == "show":
            self.user.cart.display()

        elif action == "remove":
            if len(parts) > 1:
                self.user.cart.remove_product(parts[1])
            else:
                print("Укажите название товара для удаления")

        elif action == "clear":
            self.user.cart.clear_cart()

        elif action == "exit":
            self.exit()

        else:
            print("Неизвестная команда. Введите 'help' для списка команд.")

    def exit(self):
        print(f"До свидания, {self.user.name}!")
        self.is_running = False

    def start(self):
        print("Добро пожаловать в наш магазин!")
        self.show_help()
        
        while self.is_running:
            cmd = input("\nВведите команду: ")
            if cmd.lower() == "help":
                self.show_help()
            else:
                self.process_command(cmd)

# Запуск приложения
if __name__ == "__main__":
    app = StoreApp()
    app.start()
   