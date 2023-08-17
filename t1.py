import numpy as np
import pandas as pd
from numpy import dot
from numpy.linalg import norm
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
from streamlit_chat import message


td2 = pd.read_pickle('/Users/dhl/Desktop/BChat/td2.pkl')
model = SentenceTransformer('sentence-transformers/xlm-r-100langs-bert-base-nli-stsb-mean-tokens')

def cos_sim(A, B):
  return dot(A, B)/(norm(A)*norm(B))

def return_answer(question) :
    embedding = model.encode(question)
    td2['score'] = td2.apply(lambda x: cos_sim(x['embedding'], embedding), axis=1)
    return td2.loc[td2['score'].idxmax()]['A']

# API_URL = "https://api-inference.huggingface.co/models/facebook/blenderbot-400M-distill"
# API_TOKEN = "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"
# headers = {"Authorization": f"Bearer {API_TOKEN}"}



st.header("Bcha (Demo)")
 
if 'generated' not in st.session_state:
    st.session_state['generated'] = []
 
if 'past' not in st.session_state:
    st.session_state['past'] = []
 
# def query(payload):
# 	response = requests.post(API_URL, headers=headers, json=payload)
# 	return response.json()
 
 
with st.form('form', clear_on_submit=True):
    user_input = st.text_input('You: ', '', key='input')
    submitted = st.form_submit_button('Send')
 
# if submitted and user_input:
#     output = query({
#         "inputs": {
#             "past_user_inputs": st.session_state.past,
#             "generated_responses": st.session_state.generated,
#             "text": user_input,
#         },
#         "parameters": {"repetition_penalty": 1.33},
#     })

if submitted and user_input:
    answer = return_answer(user_input)
 
    st.session_state.past.append(user_input)
    st.session_state.generated.append(answer)
 
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))

