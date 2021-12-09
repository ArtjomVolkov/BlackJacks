import random
user = 0
bot = 0
koloda = [2, 3, 4, 6, 7, 8, 9, 10, 11]
print("Поиграем в BlackJack? Если хотите играть нажмите Enter, если хотите выйти, то закройте всё!")
print("В колоде есть 6,7,8,9,10,(Валет=2),(Дама=3),(Король=4),(Туз=11)")
a=input()
while True:
	if user == 21:
		print("Больше карт не надо, у вас 21")
		print("Вы автоматически победили бота, так как у вас 21.")
		break
	if user>21:
		print("Вы проиграли, так как набрали больше 21")
		print("Попытайте свою попытку в другой раз.")
		break
	variant = input("Будете ли вы брать карту?Введите 1(да) или введите 2(нет) =>")
	if variant == "1":
		kart = random.choice(koloda)
		print("Вы взяли карту выпало:", kart)
		user += kart
		print("Сейчас у вас ", user)
	if variant == "2":
		print("У вас ", user, "очков.")
		print()
		print("Ход бота")
		while True:
			if bot<15:
				print("Бот берет карту")
				kart = random.choice(koloda)
				print("Боту выпало", kart, "очков.")
				bot += kart
				print("У бота ", bot, "очков.")
			if bot>21:
				print("Бот проиграл.Так как у него", bot, "очков, а у вас ", user)
				print("Нажмите Enter, чтобы закрыть")
				exit(0)
			if bot>user:
				print("Бот победил.Так как у него", bot, "очков, а у вас ", user)
				print("Не растраивайтесь. Попробуйте ещё раз.")
				print("Нажмите Enter, чтобы закрыть")
				exit(0)
			if bot == user:
				print("Вы набрали равное количество очков и у вас ничья")
				print("Нажмите Enter, чтобы закрыть")
				exit(0)
