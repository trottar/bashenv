#! /usr/bin/python

#
# Description:
# ================================================================
# Time-stamp: "2023-03-10 19:28:09 trottar"
# ================================================================
#
# Author:  Richard L. Trotta III <trotta@cua.edu>
#
# Copyright (c) trottar
#
import tkinter as tk
import nltk
nltk.download('punkt')
from nltk.tokenize import word_tokenize
import openai
import json
import readline
import re
import os, sys

args = sys.argv

prompt_type = sys.argv[1]

# Debug flag
DEBUG = False

# Maximum number of tokens for model used
max_tokens = 1500

# Overlap in tokens if it exceeds maximum
overlap_size = 100

openai.api_key = os.getenv('OPENAI_KEY')

# Open the JSON file and load the data into a dictionary
with open('prompts.json', 'r') as file:
    promptJSON = json.load(file)

for tmp in promptJSON:
    if prompt_type in tmp["name"]:
        promptDict = tmp
    
def break_up_input(tokens, chunk_size, overlap_size):
    if len(tokens) <= chunk_size:
        yield tokens
    else:
        chunk = tokens[:chunk_size]
        yield chunk
        yield from break_up_input(tokens[chunk_size-overlap_size:], chunk_size, overlap_size)

def convert_to_detokenized_text(tokenized_text):
    prompt_text = " ".join(tokenized_text)
    prompt_text = prompt_text.replace(" 's", "'s")
    return prompt_text

def chat(messages):
        # gpt-3.5-turbo
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=.5,
            max_tokens=max_tokens,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )

        if DEBUG == True:
            api_usage = response['usage']
            print(f"\n\nTotal tokens comsumed: {api_usage}\n\n")

        messages.append({'role': response.choices[0].message.role, 'content': response.choices[0].message.content})
    
        return messages

def convert_to_readable_code(text):
    '''
    Finds code snippets and colors it yellow
    '''
    
    
    # Find the first and second occurrence of ```
    first_occur = re.search('```', text)
    second_occur = None
    if first_occur:
        second_occur = re.search('```', text[first_occur.end():])
    if second_occur:
        start1 = first_occur.start()
        end1 = first_occur.end()
        start2 = second_occur.start() + end1
        end2 = second_occur.end() + end1
        new_text = text[:start1] + '\033[33m\n\033[7m' + text[end1:start2] + '\033[0m\n\033[0m\033[32m' + text[end2:] + '\033[0m\n'
    else:
        new_text = text


    return new_text
    
if len(args) == 2:

    prompt_request = promptDict["prompt"]
    
    messages = []
    messages.append({"role": "system", "content": convert_to_detokenized_text(prompt_request)})
    messages = chat(messages)
    print('\033[36m{0}\033[0m: \033[32m{1}\033[0m\n'.format(messages[-1]['role'].strip(), convert_to_readable_code(messages[-1]['content'].strip())))

    # Keep track of the last user input
    last_user_input = ""
    
    # Loop through the conversation
    while True:

        user_inp =  input('Please enter your prompt...')
        
        if user_inp == "\033[A":
            user_inp = last_user_input
            print(user_inp)
        else:
            last_user_input = user_inp
            
        if user_inp[0:3] == "bye":
            break
        if user_inp == "":
            continue

        prompt_request = f"My first request is '{user_inp}'"

        messages.append({"role": "user", "content": convert_to_detokenized_text(prompt_request)})
        messages = chat(messages)
        print('\033[36m{0}\033[0m: \033[32m{1}\033[0m\n'.format(messages[-1]['role'].strip(), convert_to_readable_code(messages[-1]['content'].strip())))
    

else:
    
    # Define a function to handle button clicks
    def handle_button_click():
        # Get the user's input from the text box
        user_inp = input_box.get("1.0", "end-1c")

        prompt_request = promptDict["prompt"]
        
        messages = []
        messages.append({"role": "system", "content": convert_to_detokenized_text(prompt_request)})
        messages = chat(messages)
        print('\033[36m{0}\033[0m: \033[32m{1}\033[0m\n'.format(messages[-1]['role'].strip(), convert_to_readable_code(messages[-1]['content'].strip())))

        # Loop through the conversation
        prompt_request = f"My first request is '{user_inp}'"
        
        messages.append({"role": "user", "content": convert_to_detokenized_text(prompt_request)})
        messages = chat(messages)
        print('\033[36m{0}\033[0m: \033[32m{1}\033[0m\n'.format(messages[-1]['role'].strip(), convert_to_readable_code(messages[-1]['content'].strip())))
        
        # Process the input (in this example, we just display it back to the user)
        output_text = '{0}: {1}\n'.format(messages[-1]['role'].strip(), messages[-1]['content'].strip())

        # Display the output in the output label
        output_label.config(text=output_text)

    # Create a Tkinter window
    window = tk.Tk()

    # Set the window title
    window.title('ChatGPT')
    
    # Set the window size
    window.geometry('500x300')
    window.resizable(True, True)

    # Create a frame for the input box
    input_frame = tk.Frame(window)
    input_frame.pack(expand=True, fill='both')

    # Create a label for the input box
    input_label = tk.Label(input_frame, text='Please enter your prompt...')
    input_label.pack(side='top')

    # Create an entry box for the user's input
    input_box = tk.Text(input_frame, width=50, height=5, wrap='word')
    input_box.pack(side='top', expand=True, fill='both')

    # Create a button to submit the input
    submit_button = tk.Button(window, text='Submit', command=handle_button_click)
    submit_button.pack()

    # Create a label for the output
    output_label = tk.Label(window, text='', wraplength=450)
    output_label.pack(expand=True, fill='both')

    # Run the Tkinter event loop
    window.mainloop()
