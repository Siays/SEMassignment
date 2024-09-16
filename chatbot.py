import streamlit as st
import database_interaction
from faq import FAQ

# fetch collection form fire store
category_docs = database_interaction.fetch_all_data_from_collection('Category')
main_question_docs = database_interaction.fetch_all_data_from_collection('MainQuestion')
sub_question_docs = database_interaction.fetch_all_data_from_collection('SubQuestion')
answer_docs = database_interaction.fetch_all_data_from_collection('Answer')

# create FAQ object
faq = FAQ(category_docs, main_question_docs, sub_question_docs, answer_docs)

# initial question asked by the chatbot.
INITIAL_QUESTION = ("Hello! Welcome to the FOCS Frequently Asked Questions (<b>FAQ</b>) Chatbot!<br/>Please select a "
                    "category that your inquiry belongs to:")

# please select msg used by the chatbot.
PLEASE_SELECT_MSG = "Please select from the following questions."


# Reset conversation state
def reset_conversation():
    st.session_state['step'] = 1
    st.session_state['current_question'] = INITIAL_QUESTION
    st.session_state['current_selection_id'] = None


# Update conversation state
def update_state(current_question, current_selection_id):
    st.session_state['current_question'] = current_question
    st.session_state['current_selection_id'] = current_selection_id
    st.session_state['step'] += 1


# Function to generate JavaScript for closing the tab
def close_tab():
    st.markdown(
        """
        <script>
        window.close();
        </script>
        """,
        unsafe_allow_html=True
    )


def main():
    # Custom CSS to style the markdown content
    custom_css = """
    <style>
    .markdown-text {
        color: black; /* Change text color */
        width: 50%;
        margin-bottom: 1rem;
    }
    </style>
    """

    # Inject custom CSS
    st.markdown(custom_css, unsafe_allow_html=True)

    # Initialize session state if it's the first time the app is loaded
    if 'step' not in st.session_state:
        reset_conversation()

    # Display chat-like interface
    st.title("FAQ Chatbot")

    # Initial conversation steps (step 1 to 3)
    if st.session_state['step'] < 4:
        # Get the current question and display it.
        question = st.session_state['current_question']
        if st.session_state['step'] != 1:
            st.markdown(f"<div class='markdown-text'><b>You:</b> {question}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='markdown-text'><b>Chatbot:</b> {PLEASE_SELECT_MSG}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='markdown-text'><b>Chatbot:</b> <br/>{question}</div>", unsafe_allow_html=True)

        # Display pills as buttons for the next set of questions
        if st.session_state['step'] == 1:
            categories = faq.get_categories()
            for category in categories:
                st.button(category.category_name, on_click=update_state, args=[category.category_name, category.id])
        elif st.session_state['step'] == 2:
            next_questions = faq.get_main_questions(st.session_state['current_selection_id'])
            for q in next_questions:
                st.button(q.question, on_click=update_state, args=[q.question, q.id])
        else:
            next_questions = faq.get_sub_questions(st.session_state['current_selection_id'])
            for q in next_questions:
                st.button(q.question, on_click=update_state, args=[q.question, q.id])
    else:
        # End of conversation (step 4)
        st.markdown(f"<div class='markdown-text'><b>Chatbot:</b> <br/>{faq.get_answer(st.session_state['current_selection_id']).content}</div>"
                    , unsafe_allow_html=True)
        st.link_button("More Info", f"{faq.get_answer(st.session_state['current_selection_id']).link}")

        st.markdown("<div class='markdown-text'><b>Chatbot:</b> <br/>You have reached the end of the conversation.</div>", unsafe_allow_html=True)
        st.button("Ask Another Question", on_click=reset_conversation)


if __name__ == "__main__":
    main()
