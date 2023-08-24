import numpy as np
import pandas as pd
from numpy import dot
from numpy.linalg import norm
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
from streamlit_chat import message


embedding_data = pd.read_pickle('/Users/hana/Documents/GitHub/NLP_project/embedding_vector.pkl')
model = SentenceTransformer('sentence-transformers/xlm-r-100langs-bert-base-nli-stsb-mean-tokens')

#함수설정
def cos_sim(A, B):
  return dot(A, B)/(norm(A)*norm(B))

def return_answer(question) :
    embedding = model.encode(question)
    embedding_data['score'] = embedding_data.apply(lambda x: cos_sim(x['embedding'], embedding), axis=1)
    score_max = embedding_data.loc[embedding_data['score'].idxmax()]
    return score_max

def make_label2_Q(row):
    if row['label'] == 2:
        return row['Q'].replace(" ","").split(',')
    else:
        return 0
    
#데이터 생성
embedding_data['label2_Q'] = embedding_data.apply(lambda row: make_label2_Q(row), axis=1)

#stremlit
st.header("BITAmin Chatbot 💬🤖")
 
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
    score_max = return_answer(user_input)
    if (score_max['label'] == 2) and any(user_input.find(word) != -1 for word in score_max['label2_Q']) :
        found_words = [word for word in score_max['label2_Q'] if user_input.find(word) != -1]
        answer = found_words[0] +'에 대한 비타민 세션 자료입니다!\n' + score_max['A']

        for word in found_words:
            answer += '\n\n' + word + '에 대해 더 알고 싶으시면 아래 링크를 클릭하세요!' + '\n https://www.google.com/search?q=' + word

    elif (score_max['label'] == 1):
        answer = score_max['A']

    elif (score_max['label'] == 3):
        answer = score_max['Q'] + '에 해당되는 발표자료입니다.\n' + score_max['A']
    
    else:
        answer = '요청하신 주제에 해당되는 발표자료가 아닐 수 있지만... 👉🏻👈🏻 한번 클릭해주시면 감사하겠습니다 🙂🫶🏻\n' + score_max['A']
 
    st.session_state.past.append(user_input)
    st.session_state.generated.append(answer)
 
if st.session_state['generated']:
    for i in range(len(st.session_state['generated'])-1, -1, -1):
        message(st.session_state['past'][i], is_user=True, key=str(i) + '_user')
        message(st.session_state["generated"][i], key=str(i))