import time

from wand_quiz import quiz, wand_cores, wand_flex

def summarize_answers(answers):
	questions = [1,2,3,4,5,5]
	temp = answers[4].split(',')
	temp = [x.strip() for x in temp]
	answers = answers[0:4]
	answers.append(temp[0])
	answers.append(temp[1])

	answers = [int(a) for a in answers]

	core = [0,0,0]
	flex = 0
	woods = []

	for i in range(0, len(questions)):
		q_num = questions[i]
		q = quiz[q_num - 1]
		a = answers[i]

		cores = q.get_core_scores(a)
		core[0] += cores[0]
		core[1] += cores[1]
		core[2] += cores[2]

		flex += q.get_flex_score(a)

		woods += q.get_woods(a)

	flex = flex / 6

	if(flex <= 1):
		flexes = wand_flex[1]
	elif(flex <= 2):
		flexes = wand_flex[2]
	else:
		flexes = wand_flex[3]

	flex_temp = flex % 1

	if(flex_temp == 0 and flex != 0):
		flex_temp = flex - 0.0001
		flex_temp = flex_temp % 1

	step = 1 / len(flexes)
	flex_temp = flex_temp / step
	flex_temp = round(flex_temp) - 1
	best = flexes[flex_temp]

	flexes = ", ".join(flexes)

	wood_dict = {}
	for w in woods:
		if w in wood_dict:
			wood_dict[w] += 1
		else:
			wood_dict[w] = 1

	return(flex, step, flexes, best, core, wood_dict)


def print_answers(flex, step, flexes, best, core, wood_dict):
	wood_print = sorted(wood_dict, key=wood_dict.get, reverse=True)

	print("\n\n\n")
	print("-------------------------------------------")
	print("Results: {}".format(name))
	print("-------------------------------------------")
	print()
	print("---------------------")
	print("Flexibility")
	print("---------------------")
	print("Score: {}".format(flex))
	print("Step: {}".format(step))
	print("Potential flexibilites: {}".format(flexes))
	print("Best Fit: {}".format(best))
	print()
	print("---------------------")
	print("Core")
	print("---------------------")
	print("Unicorn Hair: {}".format(core[0]))
	print("Dragon Heartstring: {}".format(core[1]))
	print("Phoenix Feather: {}".format(core[2]))
	print()
	print("---------------------")
	print("Wood")
	print("---------------------")
	for w in wood_print:
		print("{}: {}".format(w, wood_dict[w]))


if __name__ == "__main__":
	answers = []

	print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	print("Welcome to Ollivander's Wand Shop, Diagon Alley branch!\n\n")
	print("Please fill out this preliminary questionnaire to help us find the wand that is your best match.\n\n")
	print("Be sure to answer these questions truthfully, otherwise it may take a long time to find a suitable wand.\n")
	print("You cannot fool a wand by lying about your true nature.\n\n\n\n\n")
	print()
	print("Date: August 12th, 2017")
	name = input("Name: ")
	print()

	for q in quiz:
		q.ask()
		ans = input("Answer: ")
		answers.append(ans)
		print()

	print("\n\n")
	print("(As you answer the last question on the sheet, all the words disappear and seem to sink into the paper.")
	print("After a brief pause, new words swim to the surface and slowly reveal themselves.)")
	print("\n\n")
	time.sleep(7)
	print("Thank you, {}.".format(name))
	time.sleep(3)
	print("\n")
	print("Please return this questionaire to an Ollivander's employee to begin the wand matching process.")
	print("\n")
	time.sleep(3)
	print("Your wand is waiting for you. Good luck.")
	input("\n\n")
	flex, step, flexes, best, core, wood_dict = summarize_answers(answers)
	print_answers(flex, step, flexes, best, core, wood_dict)