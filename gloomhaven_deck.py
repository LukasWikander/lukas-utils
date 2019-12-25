import random

dictOfCards = {'-2': 1, '-1': 5, '0': 5, '+1': 5, '+2': 1, '2x': 1, 'Miss': 1,'Curse': 0,'Blessing': 0}

print(dictOfCards)

while True:
	remainingCards = []
	for k, v in dictOfCards.items():
		for i in range(v):
			remainingCards.append(k)

	random.shuffle(remainingCards)
	pendingShuffle = False
	print("Deck shuffled")
	print("Input (c)urse to add a curse")
	print("Input (b)less to add a blessing")

	for card in remainingCards:
		print('')
		inp = input("Draw a card?")
		if inp.lower() == 'c' or inp.lower() == 'curse':
			dictOfCards['Curse'] = dictOfCards['Curse'] + 1
			print("Curse added to deck")
			pendingShuffle = True
		elif inp.lower() == 'b' or inp.lower() == 'bless':
			dictOfCards['Blessing'] = dictOfCards['Blessing'] + 1
			print("Blessing added to deck")
			pendingShuffle = True
		else:	
			print(card)
			if card == '2x' or card == 'Miss':
				pendingShuffle = True
			elif card == 'Curse':
				dictOfCards['Curse'] = dictOfCards['Curse'] - 1
				print('')
				print("Curse removed from deck")
			elif card == 'Blessing':
				dictOfCards['Blessing'] = dictOfCards['Blessing'] - 1
				print('')
				print("Blessing removed from deck")
		
		if pendingShuffle:
			inp = ''
			while inp.lower() != 'y' and inp.lower() != 'n':
				print('')
				inp = input("Shuffle deck? [y/n]")
				if inp.lower() == 'y':
					pendingShuffle = False
					break
				elif inp.lower() == 'n':
					break
				else:
					print("Only yes or no are acceptable")
			if not pendingShuffle:
				break


