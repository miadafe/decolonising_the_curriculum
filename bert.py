from sentence_similarity import sentence_similarity
from transformers import BertModel, BertTokenizer, PreTrainedTokenizer
import torch
import numpy as np

corpus = ['', '', '']
def addDeweyToCorp():
    # prev dewey.txt
    with open("new_ddc.txt", "r", encoding="utf-8") as f:
         deweypara = f.read().splitlines()
    for i in range(len(deweypara)):
        corpus[0] = corpus[0] + deweypara[i] + " "

def addLeedsToCorp():
    # prev leeds.txt
    with open("new_lu.txt", "r", encoding="utf-8") as f:
         leedspara = f.read().splitlines()
    for i in range(len(leedspara)):
        corpus[1] = corpus[1] + leedspara[i] + " "

def addUniToCorp():
    # prev universal.txt
    with open("new_udc.txt", "r", encoding="utf-8") as f:
         unipara = f.read().splitlines()
    for i in range(len(unipara)):
        corpus[2] = corpus[2] + unipara[i] + " "

addDeweyToCorp()
addLeedsToCorp()
addUniToCorp()

# Load the pre-trained BERT model and tokenizer
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertModel.from_pretrained('bert-base-uncased')

paragraph1 = corpus[0]
paragraph2 = corpus[1]
paragraph3 = corpus[2]

# Tokenize the paragraphs and add the special [CLS] token and [SEP] tokens
tokens1 = tokenizer.tokenize(paragraph1)
tokens2 = tokenizer.tokenize(paragraph2)
tokens3 = tokenizer.tokenize(paragraph3)

tokens1 = ['[CLS]'] + tokens1 + ['[SEP]']
tokens2 = ['[CLS]'] + tokens2 + ['[SEP]']
tokens3 = ['[CLS]'] + tokens3 + ['[SEP]']

# Convert the tokens to their corresponding IDs
token_ids1 = tokenizer.convert_tokens_to_ids(tokens1)
token_ids2 = tokenizer.convert_tokens_to_ids(tokens2)
token_ids3 = tokenizer.convert_tokens_to_ids(tokens3)

# Combine the token IDs for both paragraphs into a single tensor
max_seq_length = 128
padded_token_ids = token_ids1[:max_seq_length-1] + [0] * (max_seq_length - len(token_ids1))
padded_token_ids += token_ids2[:max_seq_length-1] + [0] * (max_seq_length - len(token_ids2))
padded_token_ids += token_ids3[:max_seq_length-1] + [0] * (max_seq_length - len(token_ids3))

input_ids = torch.tensor([padded_token_ids])

# Generate BERT embeddings for the paragraphs
with torch.no_grad():
    outputs = model(input_ids)
    embedding1 = outputs[0][0][0].numpy()  # Extract the embedding for the [CLS] token of paragraph 1
    embedding2 = outputs[0][0][max_seq_length].numpy()  # Extract the embedding for the [CLS] token of paragraph 2
    embedding3 = outputs[0][0][2*max_seq_length].numpy()

# Compute the Euclidean distance between the embeddings
distance1 = np.linalg.norm(embedding1 - embedding2)
distance2 = np.linalg.norm(embedding2 - embedding3)
distance3 = np.linalg.norm(embedding1 - embedding3)
print(f"The Euclidean distance between 1 and 2 is {distance1:.2f}") #13.98
print(f"The Euclidean distance between 2 and 3 is {distance2:.2f}") #15.26
print(f"The Euclidean distance between 1 and 3 is {distance3:.2f}") #12.01
