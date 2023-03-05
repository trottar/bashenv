#! /usr/bin/python

#
# Description:
# ================================================================
# Time-stamp: "2023-03-05 04:52:44 trottar"
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
import os, sys

args = sys.argv

# Maximum number of tokens for model used
max_tokens = 2000

# Overlap in tokens if it exceeds maximum
overlap_size=100

openai.api_key = os.getenv('OPENAI_KEY')

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

if len(args) == 1:
    
    user_inp =  input('Please enter your prompt...')

    prompt_request = f"{user_inp}"
    
    # text-davinci-003
    '''
    prompt = convert_to_detokenized_text(prompt_request)

    response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=.5,
            max_tokens=summary_length,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
    )

    prompt_response = response["choices"][0]["text"].strip()
    '''

    # gpt-3.5-turbo
    messages = [{"role": "system", "content": "This is text summarization."}]    
    messages.append({"role": "user", "content": convert_to_detokenized_text(prompt_request)})

    response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=.5,
            max_tokens=max_tokens,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
    )

    prompt_response = response["choices"][0]["message"]['content'].strip()

    print("\n\n\n\n",prompt_response)

else:

    def run_gpt(user_inp):
        
        prompt_request = f"{user_inp}"

        # text-davinci-003
        '''
        prompt = convert_to_detokenized_text(prompt_request)

        response = openai.Completion.create(
                model="text-davinci-003",
                prompt=prompt,
                temperature=.5,
                max_tokens=summary_length,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
        )

        prompt_response = response["choices"][0]["text"].strip()
        '''

        # gpt-3.5-turbo
        messages = [{"role": "system", "content": "This is text summarization."}]    
        messages.append({"role": "user", "content": convert_to_detokenized_text(prompt_request)})

        response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=.5,
                max_tokens=max_tokens,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
        )

        prompt_response = response["choices"][0]["message"]['content'].strip()

        print("\n\n\n\n",prompt_response)

        return prompt_response
    
    # Define a function to handle button clicks
    def handle_button_click():
        # Get the user's input from the text box
        input_text = input_box.get("1.0", "end-1c")

        # Process the input (in this example, we just display it back to the user)
        output_text = run_gpt(input_text)

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
