f = open("data.txt", "w")

for i in range(3):
    text = input("Введіть рядок: ")
    f.write(text + "\n")

f.close()