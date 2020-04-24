import pandas as pd
import markovify
import time

 
inp = pd.read_csv('abcnews-date-text.csv')
inp.head(3)

text_model = markovify.NewlineText(inp.headline_text, state_size = 2)

def temp_name():
    while True:
      for i in range(1):
        time.sleep(2)
        print(text_model.make_sentence())

temp_name() 