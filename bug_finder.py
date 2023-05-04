import glob
import os
import subprocess
import sys
import argparse
import openai
# test 2

# Replace with your OpenAI API key
openai.api_key = os.environ["OPENAI_API_KEY"]

def find_bugs_in_code(code):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that finds bugs in Python code."},
            {"role": "user", "content": f"Find bugs in the following Python code:\n{code}"}
        ]
    )

    assistant_message = response.choices[0].message['content']
    return assistant_message.strip()

def get_modified_files():
    output = subprocess.check_output(["git", "diff", "--name-only", "HEAD^", "HEAD"])
    return output.decode("utf-8").strip().split("\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Find bugs in Python files using OpenAI's GPT-3")
    parser.add_argument("files", metavar="FILE", nargs="+", help="Python files to analyze")
    args = parser.parse_args()
    modified_files = get_modified_files()

    for file in modified_files:
        if file.endswith(".py"):
            with open(file, "r") as f:
                code = f.read()
                print(f"Checking file: {file}")
                bugs = find_bugs_in_code(code)
                if bugs:
                    print("Bugs found:")
                    print(bugs)
                else:
                    print("No bugs found.")
