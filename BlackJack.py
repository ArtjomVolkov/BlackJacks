import random
igrok = 0
bot = 0
koloda = [2, 3, 4, 6, 7, 8, 9, 10, 11]
print("Поиграем в BlackJack? Если хотите играть нажмите Enter, если хотите выйти, то закройте всё!")
print("В колоде есть 6,7,8,9,10,(Валет=2),(Дама=3),(Король=4),(Туз=11)")
a=input()
popitka=0
while True:
	if igrok == 21:
		print("Больше карт не надо, у вас 21")
		print("Вы автоматически победили бота, так как у вас 21.")
		exit(0)
	if igrok>21:
		print("Вы проиграли, так как набрали больше 21")
		print("Попытайте свою попытку в другой раз.")
		popitka+=1
		print()
		print("Было потрачено", popitka, "попытка/ок")
		print()
		exit(0)
	variant = input("Будете ли вы брать карту?Введите 1(да) или введите 2(нет) =>")
	if variant == "1":
		kart = random.choice(koloda)
		print("Вы взяли карту выпало:", kart)
		igrok += kart
		print("Сейчас у вас ", igrok)
	if variant == "2":
		print("У вас ", igrok, "очков.")
		print()
		print("Ход бота")
		while True:
			if bot<15:
				print("Бот берет карту")
				kart = random.choice(koloda)
				print("Боту выпало", kart, "очков.")
				bot += kart
				print("У бота ", bot, "очков.")
				print()
				exit(0)
			if bot>21:
				print("Бот проиграл.Так как у него", bot, "очков, а у вас ", igrok)
				print("Нажмите Enter, чтобы закрыть")
				popitka+=1
				print()
				print("Было потрачено", popitka, "попытка/ок")
				print()
				exit(0)
			if bot>igrok:
				print("Бот победил.Так как у него", bot, "очков, а у вас ", igrok)
				print("Не растраивайтесь. Попробуйте ещё раз.")
				print("Нажмите Enter, чтобы закрыть")
				popitka+=1
				print()
				print("Было потрачено", popitka, "попытка/ок")
				print()
				exit(0)
			if bot == igrok:
				print("Вы набрали равное количество очков и у вас ничья")
				print("Нажмите Enter, чтобы закрыть")
				popitka+=1
				print()
				print("Было потрачено", popitka, "попытка/ок.")
				print()
				exit(0)
print("Всего было потрачено", popitka, "попытка/ок")
