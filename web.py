import streamlit as st
import functions

todos = functions.read()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write(todos)


st.title("My Todo App")
st.write("This app is to improve your productivity")

for index, i in enumerate(todos):
    check = st.checkbox(i, key=i)
    if check:
        todos.pop(index)
        functions.write(todos)
        del st.session_state[i]
        st.rerun()

st.text_input(label='', placeholder="Add new todo", on_change=add_todo,
              key='new_todo')
