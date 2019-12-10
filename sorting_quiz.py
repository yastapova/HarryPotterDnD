from question_classes import SortingQuestion

houses = ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]
qtypes = ["Innate", "Overt", "Situational", "Multi", "Fundamental", "Final"]

sort_quiz = []
quiz_types = {}

for t in qtypes:
    quiz_types[t] = []

q1 = SortingQuestion(
    "Dawn or Dusk?",
    {
        1: "Dawn",
        2: "Dusk"
    },
    {
        1: [1, 1, 0, 0],
        2: [0, 0, 1, 1]
    },
    "Innate"
)
sort_quiz.append(q1)

q2 = SortingQuestion("Forest or River?",
    {
        1: "Forest",
        2: "River"
    },
    {
        1: [1, 0, 1, 0],
        2: [0, 1, 0, 1]
    },
    "Innate"
)
sort_quiz.append(q2)

q3 = SortingQuestion("Moon or Stars?",
    {
        1: "Moon",
        2: "Stars"
    },
    {
        1: [1, 0, 1, 0],
        2: [0, 1, 0, 1]
    },
    "Innate"
)
sort_quiz.append(q3)

q4 = SortingQuestion("Which of the following would you most hate people to call you?",
    {
        1: "Ordinary",
        2: "Ignorant",
        3: "Cowardly",
        4: "Selfish"
    },
    {
        1: [1, 1, 0, 2],
        2: [0, 2, 0, 1],
        3: [2, 0, 1, 0],
        4: [0, 0, 2, 0]
    },
    "Overt"
)
sort_quiz.append(q4)

q5 = SortingQuestion("After you have died, what would you most like people to do when they hear your name?",
    {
        1: "Miss you, but smile",
        2: "Ask for more stories about your adventures",
        3: "Think with admiration of your achievements",
        4: "I don't care what people think of me after I'm dead, it's what they think of me while I'm alive that counts"
    },
    {
        1: [0, 0, 2, 0],
        2: [2, 1, 1, 0],
        3: [0, 2, 0, 1],
        4: [1, 0, 0, 2]
    },
    "Overt"
)
sort_quiz.append(q5)

q6 = SortingQuestion("How would you like to be known to history?",
    {
        1: "The Wise",
        2: "The Good",
        3: "The Great",
        4: "The Bold"
    },
    {
        1: [0, 2, 0, 1],
        2: [1, 0, 2, 0],
        3: [0, 1, 0, 2],
        4: [2, 0, 1, 0]
    },
    "Overt"
)
sort_quiz.append(q6)

q7 = SortingQuestion("Given the choice, would you rather invent a potion that would guarantee you:",
    {
        1: "Love",
        2: "Glory",
        3: "Wisdom",
        4: "Power"
    },
    {
        1: [0, 0, 1, 0],
        2: [1, 0, 0, 0],
        3: [0, 1, 0, 0],
        4: [0, 0, 0, 1]
    },
    "Overt"
)
sort_quiz.append(q7)

q8 = SortingQuestion("Once every century, the Flutterby bush produces flowers that adapt their scent \n" +
                     "to attract the unwary. If it lured you, it would smell of:",
    {
        1: "A crackling log fire",
        2: "The sea",
        3: "Fresh parchment",
        4: "Home"
    },
    {
        1: [1, 0, 0, 0],
        2: [0, 0, 0, 1],
        3: [0, 1, 0, 0],
        4: [0, 0, 1, 0]
    },
    "Innate"
)
sort_quiz.append(q8)

q9 = SortingQuestion("Four goblets are placed before you. Which would you choose to drink?",
    {
        1: "The foaming, frothing, silvery liquid that sparkles as though containing ground diamonds.",
        2: "The smooth, thick, richly purple drink that gives off a delicious smell of chocolate and plums.",
        3: "The golden liquid so bright that it hurts the eye, and which makes sunspots dance all around the room.",
        4: "The mysterious black liquid that gleams like ink, and gives off fumes that make you see strange visions."
    },
    {
        1: [0, 1, 0, 0],
        2: [0, 0, 1, 0],
        3: [1, 0, 0, 0],
        4: [0, 0, 0, 1]
    },
    "Innate"
)
sort_quiz.append(q9)

q10 = SortingQuestion("What kind of instrument most pleases your ear?",
    {
        1: "Violin",
        2: "Trumpet",
        3: "Piano",
        4: "Drum"
    },
    {
        1: [0, 0, 0, 1],
        2: [0, 0, 1, 0],
        3: [0, 1, 0, 0],
        4: [1, 0, 0, 0]
    },
    "Innate"
)
sort_quiz.append(q10)

q11 = SortingQuestion("You enter an enchanted garden. What would you be most curious to examine first?",
    {
        1: "The silver leafed tree bearing golden apples",
        2: "The fat red toadstools that appear to be talking to each other",
        3: "The bubbling pool, in the depths of which something luminous is swirling",
        4: "The statue of an old wizard with a strangely twinkling eye"
    },
    {
        1: [0, 2, 0, 1],
        2: [1, 0, 2, 0],
        3: [0, 1, 0, 2],
        4: [2, 0, 1, 0]
    },
    "Innate"
)
sort_quiz.append(q11)

q12 = SortingQuestion("Four boxes are placed before you. Which would you try and open?",
    {
        1: "The small tortoiseshell box, embellished with gold, inside \nwhich some small creature seems to be squeaking.",
        2: "The gleaming jet black box with a silver lock and key, \nmarked with a mysterious rune that you know to be the mark of Merlin.",
        3: "The ornate golden casket, standing on clawed feet, whose \ninscription warns that both secret knowledge and unbearable temptation lie within.",
        4: "The small pewter box, unassuming and plain, with a scratched \nmessage upon it that reads 'I open only for the worthy.'"
    },
    {
        1: [1, 0, 2, 0],
        2: [0, 1, 0, 2],
        3: [0, 2, 0, 1],
        4: [2, 0, 1, 0]
    },
    "Innate"
)
sort_quiz.append(q12)

q13 = SortingQuestion("A troll has gone beserk in the Headmaster's study at Hogwarts. It is about to smash, \n" +
                      "crush and tear several irreplaceable items and treasures. In which order would you rescue \n" +
                      "these objects from the troll's club, if you could?",
    {
        1: "1. a nearly perfected cure for dragon pox; 2. student records going back 1000 years; 3. a mysterious handwritten book full of strange runes",
        2: "1. student records; 2. mysterious book; 3. nearly perfected cure",
        3: "1. mysterious book; 2. nearly perfected cure; 3. student records",
        4: "1. nearly perfected cure; 2. mysterious book; 3. student records",
        5: "1. student records; 2. nearly perfected cure; 3. mysterious book",
        6: "1. mysterious book; 2. student records; 3. nearly perfected cure"
    },
    {
        1: [1, 0, 2, 0],
        2: [0, 1, 0, 2],
        3: [2, 2, 0, 1],
        4: [2, 0, 1, 0],
        5: [0, 0, 2, 0],
        6: [0, 2, 0, 2]
    },
    "Multi"
)
sort_quiz.append(q13)

q14 = SortingQuestion("Which of the following do you find most difficult to deal with?",
    {
        1: "Hunger",
        2: "Cold",
        3: "Loneliness",
        4: "Boredom",
        5: "Being ignored"
    },
    {
        1: [0, 1, 1, 0],
        2: [0, 0, 1, 1],
        3: [1, 1, 1, 0],
        4: [1, 0, 0, 1],
        5: [1, 1, 0, 1]
    },
    "Multi"
)
sort_quiz.append(q14)

q15 = SortingQuestion("Would you rather be:",
    {
        1: "Envied",
        2: "Imitated",
        3: "Trusted",
        4: "Praised",
        5: "Liked",
        6: "Feared"
    },
    {
        1: [0, 1, 0, 2],
        2: [0, 2, 1, 0],
        3: [1, 0, 2, 0],
        4: [2, 0, 0, 1],
        5: [1, 0, 2, 0],
        6: [0, 1, 0, 2]
    },
    "Multi"
)
sort_quiz.append(q15)

q16 = SortingQuestion("If you could have any power, which would you choose?",
    {
        1: "Read minds",
        2: "Invisibility",
        3: "Superhuman strength",
        4: "Speak to animals",
        5: "Change the past",
        6: "Change your appearance at will"
    },
    {
        1: [0, 2, 0, 2],
        2: [1, 0, 2, 1],
        3: [2, 0, 1, 0],
        4: [0, 1, 2, 0],
        5: [2, 0, 0, 2],
        6: [1, 2, 0, 1]
    },
    "Multi"
)
sort_quiz.append(q16)

q17 = SortingQuestion("What are you most looking forward to learning at Hogwarts?",
    {
        1: "Apparition and Disapparition (being able to materialize and dematerialize at will)",
        2: "Transfiguration (turning one object into another object)",
        3: "Flying on a broomstick",
        4: "Hexes and jinxes",
        5: "All about magical creatures, and how to befriend/care for them",
        6: "Secrets about the castle",
        7: "Every area of magic I can",
        8: "Herbology (the study of magical plants)",
        9: "Nothing! I'm excited about having fun with my friends instead!"
    },
    {
        1: [0, 1, 1, 0],
        2: [0, 2, 0, 1],
        3: [2, 0, 1, 0],
        4: [1, 0, 0, 2],
        5: [1, 0, 2, 0],
        6: [2, 0, 0, 1],
        7: [0, 2, 0, 2],
        8: [0, 1, 2, 0],
        9: [2, 0, 1, 0]
    },
    "Multi"
)
sort_quiz.append(q17)

q18 = SortingQuestion("You and two friends need to cross a bridge guarded by a river troll who insists \n" +
                      "on fighting one of you before he will let all of you pass. Do you:",
    {
        1: "Attempt to confuse the troll into letting all three of you pass without fighting",
        2: "Suggest drawing lots to decide which of you will fight",
        3: "Use tactics to trick him or take him by surprise",
        4: "Volunteer to fight"
    },
    {
        1: [0, 2, 0, 1],
        2: [0, 0, 2, 0],
        3: [0, 1, 0, 2],
        4: [2, 0, 1, 0]
    },
    "Situational"
)
sort_quiz.append(q18)

q19 = SortingQuestion("One of your house mates has cheated in a Hogwarts exam by using a Self-Spelling Quill. \n" +
                      "Now he has come top of the class in Charms, beating you into second place. \n" +
                      "Professor Flitwick is suspicious of what happened. He draws you to one side after his lesson\n" +
                      "and asks you whether or not your classmate used a forbidden quill. What do you do?",
    {
        1: "Lie and say you don't know (but hope that somebody else tells Professor Flitwick the truth).",
        2: "Tell Professor Flitwick that he ought to ask your classmate (and resolve to tell your \nclassmate that if he doesn't tell the truth, you will).",
        3: "Tell Professor Flitwick the truth. If your classmate is prepared to win by cheating, he \ndeserves to be found out. Also, as you are both in the same house, any points he \nloses will be regained by you, for coming first in his place.",
        4: "You would not wait to be asked to tell Professor Flitwick the truth. If you knew that \nsomebody was using a forbidden quill, you would tell the teacher before the exam started."
    },
    {
        1: [2, 1, 0, 0],
        2: [1, 0, 2, 0],
        3: [0, 2, 0, 1],
        4: [0, 0, 1, 2]
    },
    "Situational"
)
sort_quiz.append(q19)

q20 = SortingQuestion("A Muggle confronts you and says that they are sure you are a witch or wizard. Do you:",
    {
        1: "Ask what makes them think so?",
        2: "Agree, and ask whether they'd like a free sample of a jinx?",
        3: "Agree, and walk away, leaving them to wonder whether you are bluffing?",
        4: "Tell them that you are worried about their mental health, and offer to call a doctor."
    },
    {
        1: [0, 2, 1, 0],
        2: [2, 0, 0, 1],
        3: [1, 0, 2, 0],
        4: [0, 1, 0, 2]
    },
    "Situational"
)
sort_quiz.append(q20)

q21 = SortingQuestion("Which nightmare would disturb you the most?",
    {
        1: "Standing on top of something very high and realizing suddenly that there are \nno hand- or footholds, nor any barrier to stop you falling.",
        2: "An eye at the keyhole of the dark, windowless room in which you are locked.",
        3: "Waking up to find that neither your friends nor your family have any idea who you are.",
        4: "Being forced to speak in such a silly voice that hardly anyone can understand you, and everyone laughs at you."
    },
    {
        1: [0, 2, 0, 1],
        2: [2, 0, 1, 0],
        3: [1, 0, 2, 0],
        4: [1, 1, 0, 2]
    },
    "Innate"
)
sort_quiz.append(q21)

q22 = SortingQuestion("Which road tempts you the most?",
    {
        1: "The wide, sunny, grassy lane",
        2: "The narrow, dark, lantern-lit alley",
        3: "The twisting, leaf-strewn path through woods",
        4: "The cobbled street lined with ancient buildings"
    },
    {
        1: [0, 0, 1, 0],
        2: [0, 0, 0, 1],
        3: [1, 0, 0, 0],
        4: [0, 1, 0, 0]
    },
    "Innate"
)
sort_quiz.append(q22)

q23 = SortingQuestion("Late at night, walking alone down the street, you hear a peculiar cry \n" +
                      "that you believe to have a magical source. Do you:",
    {
        1: "Proceed with caution, keeping one hand on your concealed wand and an eye out for any disturbance?",
        2: "Draw your wand and try to discover the source of the noise?",
        3: "Draw your wand and stand your ground?",
        4: "Withdraw into the shadows to await developments, while mentally reviewing the \nmost appropriate defensive and offensive spells, should trouble occur?"
    },
    {
        1: [0, 0, 2, 1],
        2: [2, 0, 1, 0],
        3: [1, 2, 0, 0],
        4: [0, 1, 0, 2]
    },
    "Situational"
)
sort_quiz.append(q23)

q24 = SortingQuestion("Magic is:",
    {
        1: "A weapon",
        2: "An art",
        3: "A treasure",
        4: "A gift"
    },
    {
        1: [5, 0, 0, 0],
        2: [0, 5, 0, 0],
        3: [0, 0, 0, 5],
        4: [0, 0, 5, 0]
    },
    "Fundamental"
)
sort_quiz.append(q24)

q25 = SortingQuestion("What do you value more?",
    {
        1: "Comfort",
        2: "Freedom",
        3: "Control",
        4: "Possibility",
        5: "Excitement",
        6: "Understanding",
        7: "Harmony",
        8: "Legacy"
    },
    {
        1: [0, 0, 5, 2],
        2: [5, 2, 0, 0],
        3: [0, 0, 2, 5],
        4: [2, 5, 0, 0],
        5: [5, 2, 0, 0],
        6: [0, 5, 2, 0],
        7: [0, 0, 5, 2],
        8: [2, 0, 0, 5]
    },
    "Fundamental"
)
sort_quiz.append(q25)

q26 = SortingQuestion("What do you like to do after a bad day?",
    {
        1: "Go to the Three Broomsticks with my friends.",
        2: "A group activity like Quidditch or Gobstones.",
        3: "Something distracting and involved (like writing or jogging).",
        4: "Relax for the evening — good food, a movie or a book."
    },
    {
        1: [0, 1, 0, 2],
        2: [2, 0, 1, 0],
        3: [0, 0, 2, 1],
        4: [1, 2, 0, 0]
    },
    "Innate"
)
sort_quiz.append(q26)

q27 = SortingQuestion("What is your ideal day?",
    {
        1: "I accomplish something important.",
        2: "I make someone else's day.",
        3: "I finish everything I planned to.",
        4: "I just sit around with my peeps."
    },
    {
        1: [1, 0, 0, 2],
        2: [0, 0, 2, 1],
        3: [0, 2, 1, 0],
        4: [2, 1, 0, 0]
    },
    "Overt"
)
sort_quiz.append(q27)

q28 = SortingQuestion("Your troubled friend confides in you. How do you console them?",
    {
        1: "Offer solutions.",
        2: "Hug ‘em.",
        3: "Tea, food, beer, chocolate — whatever applies.",
        4: "Encourage them to talk it through and understand it better."
    },
    {
        1: [0, 1, 0, 2],
        2: [1, 0, 2, 0],
        3: [2, 0, 1, 0],
        4: [0, 2, 0, 1]
    },
    "Situational"
)
sort_quiz.append(q28)

q29 = SortingQuestion("How do you plan for the future?",
    {
        1: "I'll see how it goes, do what I love.",
        2: "I don't plan very far into future, I live in the present.",
        3: "I've have goals in sight and work towards them.",
        4: "I make a careful plan for everything."
    },
    {
        1: [1, 2, 0, 0],
        2: [2, 0, 1, 0],
        3: [0, 0, 2, 1],
        4: [0, 1, 0, 2]
    },
    "Overt"
)
sort_quiz.append(q29)

q30 = SortingQuestion("How do you resolve conflicts with your friends?",
    {
        1: "I don't really have enough conflicts to see a pattern.",
        2: "If someone comes to me, I'll try to find a compromise or change my behaviour if I'm doing something wrong.",
        3: "It's important to deal with conflicts proactively — if there's a problem I'm direct and seek a solution.",
        4: "I always get my way and often see the best solution."
    },
    {
        1: [0, 1, 2, 0],
        2: [0, 2, 1, 0],
        3: [2, 0, 0, 1],
        4: [1, 0, 0, 2]
    },
    "Overt"
)
sort_quiz.append(q30)

q31 = SortingQuestion("How did you spend your first ride on the Hogwarts Express?",
    {
        1: "Divided my attention between my spellbooks and the window.",
        2: "Spent plenty of time watching the scenery pass. Might have chatted to some of the kids in my compartment.",
        3: "I went around to the different compartments to see if I knew anyone, and met a few new people.",
        4: "Tried to impress everyone with the magic I could already do."
    },
    {
        1: [0, 2, 0, 1],
        2: [0, 1, 2, 0],
        3: [2, 0, 1, 0],
        4: [1, 0, 0, 2]
    },
    "Situational"
)
sort_quiz.append(q31)

q32 = SortingQuestion("What role do you play in your social circle?",
    {
        1: "We don't really have roles — at least, I don't.",
        2: "Captain or Firstmate.",
        3: "Team player or I try, anyway.",
        4: "Who cares?"
    },
    {
        1: [0, 1, 2, 0],
        2: [1, 0, 0, 2],
        3: [2, 0, 1, 0],
        4: [0, 2, 0, 1]
    },
    "Overt"
)
sort_quiz.append(q32)

q33 = SortingQuestion("Your friend is being bullied. What do you do?",
    {
        1: "Kick some bully arse.",
        2: "Talk to my friend, be supportive.",
        3: "Report it to the authorities, get some results.",
        4: "Allow them to handle it -- they will come to me if they need help."
    },
    {
        1: [2, 0, 0, 1],
        2: [0, 1, 2, 0],
        3: [0, 0, 1, 2],
        4: [1, 2, 0, 0]
    },
    "Situational"
)
sort_quiz.append(q33)

q34 = SortingQuestion("What do you need from your career?",
    {
        1: "To make a positive impact on people's lives.",
        2: "To be challenged and stimulated every day.",
        3: "To be surrounded by people or to collaborate.",
        4: "To be busy and feel that I'm achieving things."
    },
    {
        1: [1, 0, 2, 0],
        2: [0, 2, 0, 1],
        3: [2, 0, 1, 0],
        4: [0, 1, 0, 2]
    },
    "Overt"
)
sort_quiz.append(q34)

q35 = SortingQuestion("What do you think children need most in early years?",
    {
        1: "Discipline and Routine",
        2: "Cookies and Cuddles",
        3: "Books and Music",
        4: "Friends and Playdates"
    },
    {
        1: [0, 0, 0, 1],
        2: [0, 0, 1, 0],
        3: [0, 1, 0, 0],
        4: [1, 0, 0, 0]
    },
    "Overt"
)
sort_quiz.append(q35)

q36 = SortingQuestion("How do you prepare for exams?",
    {
        1: "Should be okay, I have the general idea.",
        2: "Pulling all nighters, cue cards, the works.",
        3: "I’ve been working hard all year because I need to do well.",
        4: "I focus on the information. I can’t think about the test: it’s just me and the data."
    },
    {
        1: [1, 0, 0, 0],
        2: [0, 0, 0, 1],
        3: [0, 0, 1, 0],
        4: [0, 1, 0, 0]
    },
    "Overt"
)
sort_quiz.append(q36)

q37 = SortingQuestion("Who do you see in your future?",
    {
        1: "Partner and/or kids, and lots of friends, I hope.",
        2: "Me, when it comes down to it.",
        3: "I’m a career person, so, colleagues, a boss (unless I’m the boss), etc.",
        4: "There’ll be people, I don’t think about it much."
    },
    {
        1: [0, 0, 1, 0],
        2: [0, 1, 0, 0],
        3: [0, 0, 0, 1],
        4: [1, 0, 0, 0]
    },
    "Overt"
)
sort_quiz.append(q37)

q38 = SortingQuestion("What house do you think you belong in?",
    {
        1: "Gryffindor",
        2: "Ravenclaw",
        3: "Hufflepuff",
        4: "Slytherin",
        5: "I'm not sure"
    },
    {
        1: [2, 0, 0, 0],
        2: [0, 2, 0, 0],
        3: [0, 0, 2, 0],
        4: [0, 0, 0, 2],
        5: [0, 0, 0, 0]
    },
    "Final"
)
sort_quiz.append(q38)

for q in sort_quiz:
    quiz_types[q.qtype].append(q)

tiebreaker = SortingQuestion("One last question... How is a raven like a writing desk?",
    {
        1: "Um... I don't know?",
        2: "What kind of question is that? That doesn't make any sense!",
        3: "Are you seriously basing something as important and permanent as my house sorting on a stupid riddle?",
        4: "...Hmm... I give up, what's the answer?"
    },
    {
        1: [1, 2, 3, 0],
        2: [3, 0, 2, 1],
        3: [2, 1, 0, 3],
        4: [0, 3, 1, 2]
    },
    "Final"
)
