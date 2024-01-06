import streamlit as st
from pew.prompts.sqlite_prompt_library import SQLitePromptLibrary
from pew.prompts.prompt import Prompt

# Initialize SQLitePromptLibrary
library = SQLitePromptLibrary("prompts.db")

# App title
st.title("Prompt Library Management")

# Function to display main menu options and handle user selection
def main():
    activities = ["Create", "Edit", "Delete", "View"]
    choice = st.sidebar.selectbox("Select Activity", activities)

    if choice == "Create":
        create_prompt()
    elif choice == "Edit":
        edit_prompt()
    elif choice == "Delete":
        delete_prompt()
    elif choice == "View":
        view_prompts()

# Function to handle prompt entry creation
def create_prompt():
    st.subheader("Create a new prompt")
    prompt_name = st.text_input("Enter prompt name")
    prompt_contents = st.text_area("Enter prompt details")
    prompt_description = st.text_area("Enter prompt description")
    categories = st.text_input("Enter categories (comma-separated)")

    if st.button("Add Prompt"):
        categories = categories.split(',')
        prompt_obj = Prompt(prompt_name, prompt_contents, prompt_description)
        library.add_prompt(prompt_obj, categories)
        st.success(f"Prompt '{prompt_name}' successfully created.")

# Function to handle prompt entry updates
def edit_prompt():
    st.subheader("Edit an existing prompt")
    all_prompts = library.list_prompt_names()
    prompt_name = st.selectbox("Select the prompt to edit", all_prompts)

    if prompt_name:
        prompt = library.get_prompt_by_name(prompt_name)
        new_contents = st.text_area("Modify Prompt Contents", prompt.contents)
        new_description = st.text_input("Modify Prompt Description", prompt.description)
        new_categories = st.text_input("Modify Categories (comma-separated)", ', '.join(library.get_prompt_categories(prompt_name)))

    if st.button("Update Prompt"):
        new_categories = new_categories.split(',')
        library.add_prompt(Prompt(prompt_name, new_contents, new_description), new_categories)
        st.success(f"Prompt '{prompt_name}' successfully updated.")

# Function to handle prompt entry deletion
def delete_prompt():
    st.subheader("Delete an existing prompt")
    all_prompts = library.list_prompt_names()
    prompt_name = st.selectbox("Select the prompt to delete", all_prompts)

    if st.button("Delete Prompt"):
        library.delete_prompt(prompt_name)
        st.success(f"Prompt '{prompt_name}' successfully deleted.")

# Function to handle viewing all prompts
def view_prompts():
    st.subheader("All Prompts")
    all_prompts = library.list_prompt_names()
    for prompt_name in all_prompts:
        st.text(prompt_name)

main()
