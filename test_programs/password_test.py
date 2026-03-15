import random
num_emount = int(input("цифры"))
letters_emount = int(input("буквы"))
sim_emount = int(input("символы"))
password = []
for i in range(num_emount):
    password.append(random.choice([0],[1],[2],[3],[4],[5],[6],[7],[8],[9]))
print(password)