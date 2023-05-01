import os
import openai

from hidden import APIKEY

openai.api_key = APIKEY

response = openai.Completion.create(model="text-davinci-003", prompt="Say this is a test", temperature=0, max_tokens=7)
