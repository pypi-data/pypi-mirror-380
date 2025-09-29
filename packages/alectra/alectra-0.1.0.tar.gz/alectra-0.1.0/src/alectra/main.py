import os
import pandas as pd
import re
import string
import numpy as np
import onnxruntime as ort
from alectra.tools import tokenizer 

module_dir = os.path.dirname(__file__) 
model_path = os.path.join(module_dir, "models", "ALECTrA-ver-002.onnx")

ort_session = ort.InferenceSession(model_path)

#Importing the two dataset from drive with pandas
data_path = os.path.join(module_dir, "data", "data.csv")
train_evdata = pd.read_csv(data_path)

# Seperating the word input data (X) from the emotional value output data (Y)
TrainX = np.array(train_evdata.drop(['EV'], axis=1).values).tolist()
TrainY = np.array(train_evdata['EV'].values).tolist()

key_list = [0., 0.025, 0.05, 0.075, 0.1, 0.125, 0.15,  0.175, 0.2, 0.225, 0.25,  0.275,
 0.3, 0.325, 0.35, 0.375, 0.4, 0.5, 0.525, 0.55, 0.575, 0.6, 0.625, 0.65,
 0.675, 0.7, 0.725, 0.75,  0.775, 0.8]

lexicon = {}
key = {}

for x, y in zip(TrainX, TrainY):
  lexicon[x[0]] = y

index = -1

for entry in key_list:
  index += 1
  key[index] = entry


def sentence_parse(sentence):
  sentence = sentence.lower()
  sentence = re.sub(f"[{re.escape(string.punctuation)}]", "", sentence)
  sentence = re.sub(r"\s+", " ", sentence).strip()
  words = []
  temp_word = ''
  for character in sentence:
        if character == ' ':
         words.append(temp_word)
         temp_word = ''
        else:
         temp_word = temp_word + character
  index = len(words)
  return words

def get_word_tensor(word):
  encodings = tokenizer(word)
  input = encodings['input_ids']
  mask = encodings['attention_mask']
  return [input, mask]

"""
Lexical Rules

Subject - When encountered with a specific subject, perform a lexical...
adaptation...depends on the subject matter
Adverbs -
Negations - flip the sentiment of the nearest word with an EV != 0 ...
every two negations cancel
Unknown Words - run through Transformer, add to Lexicon

"""

def ALECTrA(sentence):
  # Special Word Types (SWTs)
  subjects_map = {'movies': [0.4, 0.45],  'movie': [0.4, 0.45]} #class A subjects
  subjects_map_b = {} #class B subjects (non-universal adverbs)
  adverbs = ['very', 'immensly', 'definitely']
  negations = ['not', 'never']

  words = sentence_parse(sentence)
  tot_ev = 0
  length = len(words) + 1

  adverb = False
  negation = False
  subject = False
  unknown = False

  for word in words:
    ev = 0
    pointer = [0,0]

   

    if word in adverbs:
      adverb = True

    elif word in negations:
      if negation:
        negation = False
      else:
        negation = True
  
    if word in adverbs or negations:
      ev = 0.5
      tot_ev += ev
      continue

    elif word in subjects_map:
      pointer = subjects_map[word]
      mag = abs(pointer[0] - 0.5)
      if pointer[0] < 0.5:
        ev = 0.5 + mag
      elif pointer[0] > 0.5:
        ev = 0.5 - mag
      subject = True

    if word not in lexicon:
      inputs = get_word_tensor(word)

      #Expected input is a tuple of two (1, 128) tensors 
      input_data = {
        'input_ids': inputs[0],
        'attention_mask': inputs[1]
      }
      outputs = ort_session.run(None, input_data)
      logits = outputs[0]
      predicted_class_id = np.argmax(logits, axis=-1)[0]
      print(predicted_class_id)

      pred_ev = key[predicted_class_id]
      lexicon[word] = pred_ev
      print(f'added {word} to lexicon with value {pred_ev}')
      if not adverb and not negation and not subject:
        tot_ev += pred_ev
        continue 


  

    if subject and lexicon[word] == pointer[0] or lexicon[word] == pointer[1] :
        tot_ev += ev
        subject = False

    elif adverb and lexicon[word] != 0.5:
         if lexicon[word] < 0.5:
             ev = lexicon[word] - 0.05
         elif lexicon[word] > 0.5:
             ev = lexicon[word] + 0.05
         tot_ev += ev
         adverb = False

    elif negation and lexicon[word] != 0.5:
      mag = abs(lexicon[word] - 0.5)
      if lexicon[word] < 0.5:
        ev = 0.5 + mag
      elif lexicon[word] > 0.5:
        ev = 0.5 - mag
      tot_ev += ev

    else:
      ev = lexicon[word]
      tot_ev += ev
  return round(tot_ev / length, 2)


