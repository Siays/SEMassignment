class Category:
    def __init__(self, id, category_name):
        self.id = id
        self.category_name = category_name

    def __repr__(self):
        return f"Category(id='{self.id}', category_name='{self.category_name}')"


class MainQuestion:
    def __init__(self, id, question, category_id):
        self.id = id
        self.question = question
        self.category_id = category_id

    def __repr__(self):
        return f"MainQuestion(id='{self.id}', question='{self.question}', category_id='{self.category_id}')"


class SubQuestion:
    def __init__(self, id, question, main_question_id):
        self.id = id
        self.question = question
        self.main_question_id = main_question_id

    def __repr__(self):
        return f"SubQuestion(id='{self.id}', question='{self.question}', main_question_id='{self.main_question_id}')"


class Answer:
    def __init__(self, id, content, link, sub_question_id):
        self.id = id
        self.content = content
        self.link = link
        self.sub_question_id = sub_question_id

    def __repr__(self):
        return f"Answer(id='{self.id}', content='{self.content}', link='{self.link}', sub_question_id='{self.sub_question_id}')"

class FAQ:
    def __init__(self, category_docs, main_question_docs, sub_question_docs, answer_docs):
        self.id = id
        categories = []
        main_questions = []
        sub_questions = []
        answers = []

        for doc in category_docs:
            category = Category(
                id=doc.id,
                category_name=doc.get('categoryName')
            )
            categories.append(category)

        for doc in main_question_docs:
            main_question = MainQuestion(
                id=doc.id,
                question=doc.get('question'),
                category_id=doc.get('categoryID')
            )
            main_questions.append(main_question)

        for doc in sub_question_docs:
            sub_question = SubQuestion(
                id=doc.id,
                question=doc.get('question'),
                main_question_id=doc.get('mqID')
            )
            sub_questions.append(sub_question)

        for doc in answer_docs:
            answer = Answer(
                id=doc.id,
                content=doc.get('content'),
                link=doc.get('link'),
                sub_question_id=doc.get('subqID')
            )
            answers.append(answer)

        self.categories = categories
        self.main_questions = main_questions
        self.sub_questions = sub_questions
        self.answers = answers

    def get_categories(self):
        return self.categories

    def get_main_questions(self,category_id):
        filtered_main_questions = [main_question for main_question in self.main_questions if
                                   getattr(main_question, 'category_id', None) == category_id]
        return filtered_main_questions

    def get_sub_questions(self,main_question_id):
        filtered_sub_questions = [sub_question for sub_question in self.sub_questions if
                                  getattr(sub_question, 'main_question_id', None) == main_question_id]
        return filtered_sub_questions

    def get_answer(self,sub_question_id):
        for answer in self.answers:
            if getattr(answer, 'sub_question_id', None) == sub_question_id:
                return answer
        return None


