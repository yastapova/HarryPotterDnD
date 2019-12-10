import itertools
from collections import Counter

from wand_quiz import wand_quiz, wand_cores, wand_flex, unique_woods
from take_quiz import summarize_wand

wand_flex_list = wand_flex[1] + wand_flex[2] + wand_flex[3]


def create_answer_sheets():
    last_question = wand_quiz[-1]
    ans = list(last_question.answers.keys())

    last_combos = itertools.combinations(ans, 2)
    # print(list(last_combos))

    question_combos = itertools.product(list(wand_quiz[0].answers.keys()), list(wand_quiz[1].answers.keys()), list(wand_quiz[2].answers.keys()), list(wand_quiz[3].answers.keys()))
    question_combos = itertools.product(question_combos, last_combos)

    combo_list = list(question_combos)

    return(combo_list)


def count_results(combo_list):
    results_flex = dict.fromkeys(wand_flex_list, 0)
    results_cores = dict.fromkeys(["TIE", "Unicorn Hair", "Dragon Heartstring", "Phoenix Feather"], 0)
    results_woods = dict.fromkeys(["TIE"] + unique_woods, 0)

    combo_list = [([str(a) for a in x], [str(b) for b in y]) for x, y in combo_list]
    combo_list = [x + [",".join(y)] for x, y in combo_list]

    for combo in combo_list:
        flex, step, flexes, best, core, wood_dict = summarize_wand(combo)

        # count flexibilities
        results_flex[best] += 1

        # count cores
        temp_cores = dict(zip(wand_cores, core))
        temp_cores = Counter(temp_cores)
        temp_cores = temp_cores.most_common()
        if(temp_cores[0][1] == temp_cores[1][1]):
            results_cores["TIE"] += 1
        else:
            results_cores[temp_cores[0][0]] += 1

        # count woods
        temp_woods = Counter(wood_dict)
        temp_woods = temp_woods.most_common()
        if(temp_woods[0][1] == temp_woods[1][1]):
            results_woods["TIE"] += 1
        else:
            results_woods[temp_woods[0][0]] += 1

    return(results_flex, results_cores, results_woods)


def print_results(flex_result, core_result, wood_result, n):
    print("\nSIMULATION RESULTS\n")
    print("-------------------------------------------")
    print("Wand Core Results")
    print("-------------------------------------------")
    print("TIEs: {0}, {1:2.2f}%".format(core_result["TIE"], core_result["TIE"] / n * 100))
    for k in [key for key in core_result.keys() if key not in ["TIE"]]:
        print("{0}: {1}, {2:2.2f}%".format(k, core_result[k], core_result[k] / n * 100))

    print("\n-------------------------------------------")
    print("Flexibility Results")
    print("-------------------------------------------")
    for k in [key for key in flex_result.keys()]:
        print("{0}: {1}, {2:2.2f}%".format(k, flex_result[k], flex_result[k] / n * 100))

    print("\n-------------------------------------------")
    print("Wood Results")
    print("-------------------------------------------")
    print("TIEs: {0}, {1:2.2f}%".format(wood_result["TIE"], wood_result["TIE"] / n * 100))
    for k in [key for key in wood_result.keys() if key not in ["TIE"]]:
        print("{0}: {1}, {2:2.2f}%".format(k, wood_result[k], wood_result[k] / n * 100))


combo_list = create_answer_sheets()
flex_result, core_result, wood_result = count_results(combo_list)
print_results(flex_result, core_result, wood_result, len(combo_list))
