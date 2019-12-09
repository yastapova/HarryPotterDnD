class Question:
	def __init__(self, question, answers):
		self.question = question
		self.answers = answers

	def ask(self):
		print(self.question)
		for k in self.answers:
			print("({}) {}".format(k, self.answers[k]))


class WandQuestion(Question):
	def __init__(self, question, answers, core_scores, flex_scores, woods):
		self.core_scores = core_scores
		self.flex_scores = flex_scores
		self.woods = woods
		super().__init__(question, answers)

	def get_core_scores(self, answer):
		return self.core_scores[answer]

	def get_flex_score(self, answer):
		return self.flex_scores[answer - 1]

	def get_woods(self, answer):
		return self.woods[answer]
