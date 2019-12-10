import time
import random
import re
import numpy as np

from wand_quiz import wand_quiz, wand_cores, wand_flex
from sorting_quiz import houses, qtypes, tiebreaker, quiz_types


# region Wands
def summarize_wand(answers):
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
        q = wand_quiz[q_num - 1]
        a = answers[i]

        cores = q.get_core_scores(a)
        core[0] += cores[0]
        core[1] += cores[1]
        core[2] += cores[2]

        flex += q.get_flex_score(a)

        woods += q.get_woods(a)

    flex = flex / 6

    if flex <= 1:
        flexes = wand_flex[1]
    elif flex <= 2:
        flexes = wand_flex[2]
    else:
        flexes = wand_flex[3]

    flex_temp = flex % 1

    if flex_temp == 0 and flex != 0:
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


def print_answers_wand(flex, step, flexes, best, core, wood_dict, name):
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
    print("Potential flexibilities: {}".format(flexes))
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


def take_wand_quiz():
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

    for q in wand_quiz:
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
    print("Please return this questionnaire to an Ollivander's employee to begin the wand matching process.")
    print("\n")
    time.sleep(3)
    print("Your wand is waiting for you. Good luck.")
    input("\n\n")
    flex, step, flexes, best, core, wood_dict = summarize_wand(answers)
    print_answers_wand(flex, step, flexes, best, core, wood_dict, name)
# endregion


# region Sorting
def randomize_sort_quiz(n):
    random_quiz = []
    qtypes_rand = qtypes[0:-2]

    for q in qtypes_rand:
        questions = quiz_types[q]
        if n > len(questions):
            questions = random.shuffle()
        else:
            questions = random.sample(questions, n)

        random_quiz += questions

    random_quiz += quiz_types[qtypes[-2]]
    random_quiz += quiz_types[qtypes[-1]]

    return random_quiz


def summarize_house(answers, take_quiz, allow_ties=False, print_text=True):
    denial_msg = "Hmmm... I'm afraid not. You wouldn't do well there at all. \nBut never fear, I'll find the right place for you. Let me see...\n"

    for i in range(0, len(take_quiz)):
        q = take_quiz[i]
        answers[i] = q.get_house_score(answers[i])

    answers = np.array(answers)
    totals = answers.sum(axis=0)
    max_points = totals.max()

    qfinal = np.array(answers[-1])
    qfinal = qfinal.argmax()  # which house they picked

    maxes = np.where(totals == max_points)  # indices of max values
    if np.shape(maxes)[1] > 1:
        # check if their preferred house is in the tie
        if qfinal != 5 and bool(np.isin(qfinal, maxes)):
            # use their preference
            maxes = qfinal

        elif allow_ties:
            # for simulation purposes
            return "TIE"

        else:
            # ask tiebreaker
            if qfinal != 5 and print_text:
                print(denial_msg)
                time.sleep(3)

            tiebreaker.ask()
            ans = input("Answer: ")
            if print_text:
                print("\n[The Sorting Hat chuckles to itself.] Interesting, interesting...\n")

            ans = int(ans.strip())
            ans = tiebreaker.get_house_score(ans)
            ans = np.array(ans)

            totals = totals + ans
            max_points = totals.max()
            maxes = np.where(totals == max_points)

            if np.shape(maxes)[1] > 1:
                # break tie with biggest tiebreaker question value
                for i in range(0, np.shape(totals)[0]):
                    if not np.isin(i, maxes):
                        ans[i] = 0
                maxes = ans.argmax()

            else:
                maxes = maxes[0][0]

    else:
        if qfinal != 5 and not bool(np.isin(qfinal, maxes) and print_text):
            print(denial_msg)

        maxes = maxes[0][0]

    house = houses[maxes]
    return house.upper()


def start_sorting_quiz():
    announce = ["Better be", "Let's see how you like", "I'll put you in", "You will join", "I wish you luck in"]

    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    print("Ahhhh... another fine young mind for Hogwarts. Don't worry now, you're not hearing voices. I am the Sorting Hat.\n")
    time.sleep(4)
    print("I'm going to take a peek into your mind and decide which of our lovely houses you belong in, as I have done for every student before you for centuries.\n")
    time.sleep(5)
    print("Have no fear, this will take just a moment. I'll simply ask a few questions to guide your thoughts.\n")
    time.sleep(4)
    print("And remember: I can read your mind! So there's no hiding your true nature from me...\n\n")
    time.sleep(4)
    print("Now then, to business! Are you:")
    print("(1) Nervous (short quiz, 11 questions)")
    print("(2) Excited (long quiz, 23 questions)")
    print("(3) Committed (full quiz, 38 questions)")
    ans = input("Answer: ")
    print("\n\n")

    if ans == "1":
        # randomize short quiz
        take_quiz = randomize_sort_quiz(2)
    elif ans == "2":
        # randomize long quiz
        take_quiz = randomize_sort_quiz(5)
    else:
        # put together full quiz
        take_quiz = []
        for qtype in qtypes:
            take_quiz = take_quiz + quiz_types[qtype]

    answers = take_sorting_quiz(take_quiz)

    print()
    house = summarize_house(answers, take_quiz)
    print("Hmmmm... Right. Right, then. I see...\n")
    time.sleep(4)
    print("Very good, I know where to put you now. And you'll do quite well there, I think.\n")
    print("\n")
    time.sleep(2)
    suspense = random.choice(announce)
    print("{}...\n".format(suspense))
    time.sleep(2)
    print("{}!\n".format(house))
    time.sleep(1)
    print("[Your new housemates erupt into cheers and applause as you take off the Sorting Hat " +
          "and go to join them at their table.]")


def take_sorting_quiz(take_quiz):
    answers = []

    for q in take_quiz:
        q.ask()
        while True:
            ans = input("Answer: ")
            if ans == "exit":
                raise SystemExit(0)

            ans = re.sub(r'[^0-9]', '', ans)
            if ans == "":
                continue

            ans = int(ans)
            if ans > len(q.answers) or ans < 1:
                continue

            break

        answers.append(ans)
        print()

    return answers
# endregion


if __name__ == "__main__":
    # take_wand_quiz()
    start_sorting_quiz()