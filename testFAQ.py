import database_interaction
from faq import FAQ

#fetch collection form fire store
category_docs = database_interaction.fetch_all_data_from_collection('Category')
main_question_docs = database_interaction.fetch_all_data_from_collection('MainQuestion')
sub_question_docs = database_interaction.fetch_all_data_from_collection('SubQuestion')
answer_docs = database_interaction.fetch_all_data_from_collection('Answer')

#create FAQ object
faq = FAQ(category_docs, main_question_docs, sub_question_docs, answer_docs)

#call FAQ object method
categories = faq.get_categories()
print(categories[0])
main_questions = faq.get_main_questions(categories[0].id)
print(main_questions[0])
sub_questions = faq.get_sub_questions(main_questions[0].id)
print(sub_questions[0])
answer = faq.get_answer(sub_questions[0].id)
print(answer)