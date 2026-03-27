while True:
    print("1-Додати  2-Показати  3-Пошук  4-Видалити  5-Вихід")
    c = input("Вибір: ")

    if c == "1":
        f = open("orders.txt", "a")

        num = input("Номер: ")
        name = input("Товар: ")
        qty = input("Кількість: ")
        price = input("Ціна: ")

        f.write(num + " " + name + " " + qty + " " + price + "\n")
        f.close()

    elif c == "2":
        f = open("orders.txt", "r")
        for line in f:
            print(line)
        f.close()

    elif c == "3":
        num = input("Номер: ")

        f = open("orders.txt", "r")
        for line in f:
            if line.startswith(num):
                print("Знайдено:", line)
        f.close()

    elif c == "4":
        num = input("Номер: ")

        f = open("orders.txt", "r")
        lines = f.readlines()
        f.close()

        f = open("orders.txt", "w")

        for line in lines:
            if not line.startswith(num):
                f.write(line)

        f.close()

    elif c == "5":
        break