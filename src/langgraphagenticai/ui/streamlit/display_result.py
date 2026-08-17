import streamlit as st


class DisplayResultStreamlit:
    def __init__(self, usecase, graph, user_message):
        self.usecase = usecase
        self.graph = graph
        self.user_message = user_message

    def display_result_on_ui(self):
        with st.chat_message("user"):
            st.markdown(self.user_message)

        response = self.graph.invoke({"messages": [("user", self.user_message)]})
        ai_message = response["messages"][-1].content

        with st.chat_message("assistant"):
            st.markdown(ai_message)
