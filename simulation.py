import itertools
import argparse
from collections import Counter

from wand_quiz import wand_quiz, wand_cores, wand_flex, unique_woods
from sorting_quiz import sort_quiz, houses
from take_quiz import summarize_wand, summarize_house

# region Wands
wand_flex_list = wand_flex[1] + wand_flex[2] + wand_flex[3]


def create_answer_sheets_wands():
    last_question = wand_quiz[-1]
    ans = list(last_question.answers.keys())

    last_combos = itertools.combinations(ans, 2)
    # print(list(last_combos))

    question_combos = itertools.product(list(wand_quiz[0].answers.keys()), list(wand_quiz[1].answers.keys()), list(wand_quiz[2].answers.keys()), list(wand_quiz[3].answers.keys()))
    question_combos = itertools.product(question_combos, last_combos)

    combo_list = list(question_combos)

    return combo_list


def count_results_wands(combo_list):
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
        if temp_cores[0][1] == temp_cores[1][1]:
            results_cores["TIE"] += 1
        else:
            results_cores[temp_cores[0][0]] += 1

        # count woods
        temp_woods = Counter(wood_dict)
        temp_woods = temp_woods.most_common()
        if temp_woods[0][1] == temp_woods[1][1]:
            results_woods["TIE"] += 1
        else:
            results_woods[temp_woods[0][0]] += 1

    return results_flex, results_cores, results_woods


def print_results_wands(flex_result, core_result, wood_result, n):
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


def simulate_wands():
    combo_list = create_answer_sheets_wands()
    flex_result, core_result, wood_result = count_results_wands(combo_list)
    print_results_wands(flex_result, core_result, wood_result, len(combo_list))
# endregion


def create_answer_sheets_sorting():
    q1 = sort_quiz[0]
    ans1 = list(q1.answers.keys())
    q2 = sort_quiz[1]
    ans2 = list(q2.answers.keys())

    combos = itertools.product(ans1, ans2)
    combos = list(combos)

    for q in range(2, len(sort_quiz)):
        ans = list(sort_quiz[q].answers.keys())
        combos = itertools.product(combos, ans)
        combos = list(combos)
        combos = [c1 + (c2,) for c1, c2 in combos]

    combos = list(combos)

    return combos


def count_results_sorting(combo_list):
    results_houses = dict.fromkeys(["TIE"] + houses, 0)

    return results_houses


def simulate_sorting():
    combo_list = create_answer_sheets_sorting()
    houses_result = count_results_sorting(combo_list)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-q", "--quiz", help="choose quiz to simulate: wand or sorting", action="store")

    args = parser.parse_args()

    if args.quiz == "wand":
        simulate_wands()
    elif args.quiz == "sorting":
        simulate_sorting()
