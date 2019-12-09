from question_classes import WandQuestion

wand_cores = ["Unicorn Hair", "Dragon Heartstring", "Phoenix Feather"]
wand_flex = {
	1: ["Hard", "Solid", "Rigid", "Brittle", "Unyielding", "Stiff"],
	2: ["Slightly Yielding", "Slightly Springy", "Fairly Bendy", "Reasonably Supple", "Very Flexible"],
	3: ["Quite Bendy", "Supple", "Pliant", "Swishy", "Surprisingly Swishy", "Whippy"]
}
unique_woods = ["Acacia", "Alder", "Apple", "Ash", "Aspen", "Beech", "Black Walnut", "Blackthorn",
				"Cedar", "Cypress", "Dogwood", "Ebony", "Elm", "English Oak", "Fir", "Hawthorn",
				"Hazel", "Holly", "Hornbeam", "Larch", "Laurel", "Mahogany", "Maple", "Pear", "Pine",
				"Poplar", "Redwood", "Rowan", "Silver Lime", "Spruce", "Sycamore", "Vine", "Walnut",
				"Willow", "Yew"]

quiz = []

q1 = WandQuestion("Which of these do you value most?",
	{
		1: "Power",
		2: "Uniqueness",
		3: "Loyalty",
		4: "Balance",
		5: "Independence",
		6: "Spontaneity"
	},
	{
		1: [0,1,0],
		2: [0,0,1],
		3: [1,0,0],
		4: [1,0,0],
		5: [0,0,1],
		6: [0,1,0]
	},
	[1,2,0,0,3,3],
	{
		1: ["Aspen", "Blackthorn", "Ebony", "Pear", "Rowan", "Yew"],
		2: ["Acacia", "Apple", "Blackthorn", "Cypress", "Ebony", "Holly", "Maple", "Silver Lime", "Vine", "Willow", "Yew"],
		3: ["Alder", "Ash", "Black Walnut", "English Oak", "Hornbeam", "Mahogany"],
		4: ["Beech", "Elm", "Fir", "Laurel", "Poplar", "Rowan", "Silver Lime", "Willow"],
		5: ["Black Walnut", "Cedar", "Cypress", "Ebony", "Hawthorn", "Maple", "Pine", "Redwood", "Sycamore"],
		6: ["Dogwood", "Hazel", "Larch", "Maple", "Redwood", "Spruce", "Sycamore", "Walnut"]
	}
)

quiz.append(q1)

q2 = WandQuestion("Do you like when things are easy, or do you prefer a challenge?",
	{1: "Easy", 2: "Challenge"},
	{
		1: [1,1,0],
		2: [0,0,1]
	},
	[2,1],
	{
		1: ["Alder", "Ash", "Cedar", "Dogwood", "English Oak", "Hazel", "Larch", "Laurel", "Pear", "Pine", "Poplar", "Rowan", "Silver Lime", "Sycamore", "Walnut", "Willow"],
		2: ["Acacia", "Apple", "Aspen", "Beech", "Black Walnut", "Blackthorn", "Cypress", "Ebony", "Elm", "Fir", "Hawthorn", "Holly", "Hornbeam", "Maple", "Redwood", "Spruce", "Vine", "Yew"]
	}
)

quiz.append(q2)

q3 = WandQuestion("Do you follow the rules?",
	{
		1: "Most of the time.",
		2: "If it's convenient.",
		3: "If they make sense and are fair.",
		4: "Rules are made to be broken."
	},
	{
		1: [1,0,0],
		2: [0,1,0],
		3: [1,0,0],
		4: [0,1,1]
	},
	[0,2,1,3],
	{
		1: ["Alder", "Acacia", "Blackthorn", "Elm", "English Oak", "Fir", "Laurel", "Pear", "Vine", "Willow"],
		2: ["Aspen", "Hawthorn", "Hazel", "Maple", "Pine", "Sycamore", "Vine"],
		3: ["Apple", "Beech", "Black Walnut", "Cedar", "Cypress", "Ebony", "Holly", "Poplar", "Rowan"],
		4: ["Dogwood", "Mahogany", "Redwood", "Silver lime", "Spruce", "Walnut", "Yew"]
	}
)

quiz.append(q3)

q4 = WandQuestion("Which of these would you rather be known for?",
	{
		1: "Strength",
		2: "Honor",
		3: "Knowledge",
		4: "Courage",
		5: "Justice",
		6: "Morality",
		7: "Creativity"
	},
	{
		1: [0,1,0],
		2: [1,1,0],
		3: [0,0,1],
		4: [0,1,1],
		5: [1,0,0],
		6: [1,0,0],
		7: [0,0,1]
	},
	[1,0,2,1,0,0,3],
	{
		1: ["Acacia", "Aspen", "Blackthorn", "Elm", "English Oak", "Fir", "Hawthorn", "Mahogany", "Spruce", "Walnut", "Yew"],
		2: ["Aspen", "Elm", "Holly", "Hornbeam", "Laurel", "Rowan"],
		3: ["Acacia", "Beech", "Cedar", "Pine", "Silver Lime", "Sycamore"],
		4: ["Ash", "Blackthorn", "Cypress", "Dogwood", "English Oak", "Hazel", "Larch", "Maple", "Yew"],
		5: ["Black Walnut", "Larch", "Mahogany", "Rowan"],
		6: ["Alder", "Apple", "Ash", "Cypress", "Ebony", "Holly", "Hornbeam", "Pear", "Poplar", "Rowan"],
		7: ["Dogwood", "Larch", "Pine", "Redwood", "Silver Lime", "Sycamore", "Vine", "Walnut", "Willow"]
	}
)

quiz.append(q4)

q5 = WandQuestion("Which two words describe you best? (Enter answer like: 1, 2)",
	{
		1: "Stubborn",
		2: "Helpful",
		3: "Mischievous",
		4: "Wise",
		5: "Perceptive",
		6: "Sincere",
		7: "Dignified",
		8: "Intimidating",
		9: "Emotional"
	},
	{
		1: [0,0,1],
		2: [1,0,0],
		3: [0,1,1],
		4: [1,0,1],
		5: [0,1,1],
		6: [1,0,0],
		7: [0,0,1],
		8: [0,1,0],
		9: [1,1,0]
	},
	[0,2,3,2,1,0,0,1,3],
	{
		1: ["Ash", "Dogwood", "English Oak", "Fir", "Hornbeam", "Larch", "Spruce", "Vine"],
		2: ["Alder", "Apple", "Cypress", "Mahogany", "Rowan", "Willow"],
		3: ["Dogwood", "Hazel", "Maple", "Redwood", "Sycamore", "Walnut"],
		4: ["Beech", "Black Walnut", "Cedar", "Fir", "Silver Lime"],
		5: ["Black Walnut", "Cedar", "Hazel", "Silver Lime", "Vine"],
		6: ["Apple", "Black Walnut", "Cypress", "Ebony", "Hornbeam", "Laurel", "Mahogany", "Poplar", "Rowan", "Yew"],
		7: ["Acacia", "Aspen", "Beech", "Elm", "Pear", "Pine"],
		8: ["Aspen", "Blackthorn", "Elm", "Fir", "Mahogany", "Pine", "Spruce", "Yew"],
		9: ["Ash", "English Oak", "Hawthorn", "Hazel", "Holly", "Larch", "Maple", "Walnut", "Willow"]
	}
)

quiz.append(q5)