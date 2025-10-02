from pathlib import Path

import google.generativeai as genai
from google.generativeai.types import GenerationConfig

from .config import read_config, userinput_selection
from .linting import rules
from .violations import examples


def write_sql_file(file_path, content) -> str:
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)


def read_sql_file(file_path: str) -> str:
    """Read the content of a SQL file and return it as a string."""
    path = Path(file_path)

    if path.suffix.lower() != ".sql":
        print("⚠️   Only .sql files are allowed")
        exit(1)

    elif not path.exists():
        print(f"⚠️   File not found: {file_path}")
        exit(1)

    else:
        return path.read_text(encoding="utf-8")


def ask_gemini(sql_query: str, question: str) -> str:
    """Send SQL query and a question to Gemini API and return the response text."""

    config = read_config()
    if config:
        api_key = config["api_key"]
        model = config["model"]
        sql_dialect = config["sql_dialect"]

    # Configure with API key
    genai.configure(api_key=api_key)

    # Pick a model
    selected_model = genai.GenerativeModel(model)

    # Build the prompt
    prompt = f"SQL Query (Important: Dialect is {sql_dialect}):\n{sql_query}\n\nQuestion:\n{question}"

    # Send to Gemini
    response = selected_model.generate_content(
        prompt, generation_config=GenerationConfig(temperature=0.5)
    )

    return response.text


def chat(file_path):
    
    sql_file = read_sql_file(file_path)
    
    conversation_history = []

    # adding the initial query at beginning of conversation to the history
    #Note: it can cause issues if user manually changes query during conversation
    conversation_history.append(f"User: This is the initial SQL query: {sql_file}")

    print("CONVERSATION START (hit `e` + `Enter` to exit):")
    print(file_path, "\n")
    

    while True:
        userinput = input("👨  You: ")

        # get latest file content
        sql_file = read_sql_file(file_path)

        if userinput == "e":
            print("👋  Exiting chat...")
            break

        conversation_history.append(f"User: {userinput}")

        response = ask_gemini(
            sql_query=sql_file,
            question=f"""
                Look at the provided SQL query and the conversation history to respond to the latest userinput. There are 3 possible output structures:
                - Option 1: If the user requests a modification of the SQL query, return the updated query beginning with 
                'MODIFIED QUERY: ' followed by the full query.
                - Option 2: If the user requests a modification of the SQL query, but you can't perform it, then explain why - nothing else.
                - Option 3: If the user does NOT request a modification, reply with a brief, direct answer and do NOT return the query.

                Conversation history:
                {conversation_history}
                """,
        )

        conversation_history.append(f"SQLAI: {response}")

        if response.startswith("MODIFIED QUERY: "):
            response_wo_prefix = response.removeprefix("MODIFIED QUERY: ")
            write_sql_file(file_path,response_wo_prefix)
            print(f"🤖  SQLAI: I updated the query.", "\n")
        else:
            print(f"🤖  SQLAI: {response}", "\n")


def run(file_path):

    sql_file = read_sql_file(file_path)

    choice = userinput_selection(
        options=[
            "fix",
            "format",
            "chat",
            "explain",
        ],
        prompt="Select an action",
    )

    if choice == "explain":
        print("👀  Checking the query ...")
        response = ask_gemini(
            sql_query=sql_file,
            question=f"""
            Give detailed explanation of what the SQL query does, structured in bullet points.
            The Answer should not exceed 500 characters.
            """,
        )
        print(response)
    elif choice == "fix":
        print("👀  Checking the query ...")
        response_1 = ask_gemini(
            sql_query=sql_file,
            question=f"""
                Check for the following violations in the provided SQL Query:
                
                {examples}

                If you don't spot any violations, then return `OK`, else list ALL violations you can find in short bullet points like this:
                - violation_1: more info
                - violation_2: more info
                _ ...
                """,
        )

        if response_1.strip() == "OK":
            print("✅  Nothing to fix")
        else:
            print(f"⚠️   {response_1}")

            print("🔧  Fixing the query ...")

            response_2 = ask_gemini(
                sql_query=sql_file,
                question=f"""
                Look at the SQL query and fix the following erros:
                {response_1}
                
                Return only the SQL query itself without enclosing it in ``` query ```, do not describe what you have changed.
                """,
            )

            write_sql_file(file_path, response_2)

            print("✅  Fixed")

    elif choice == "format":

        print("👀  Checking the query ...")

        response = ask_gemini(
            sql_query=sql_file,
            question=f"""
                Formatting the SQL query by enforcing the following rules:
                {rules}
                
                Return only the SQL query itself without enclosing it in ``` query ```, do not describe what you have changed.

                """,
        )

        write_sql_file(file_path, response)

        print("✅  Formatted")

    elif choice == "chat":

        chat(file_path)
