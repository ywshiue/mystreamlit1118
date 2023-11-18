import streamlit as st
import os
import pandas as pd
import re
import openpyxl

st.title(':blue[薛家聚餐-投票調查]')
# 建立一個勾選題
options_1=['老爸','老媽','10','老哥','小歐','陳柏偉','15']
options_2=['1/7(日)','1/14(日)','1/21(日)','Others']
options_3=['高麗肉(韓式燒烤)','西式','日式','Others']


st.write('#### **你是誰?**')
answer_1=st.selectbox('請選擇你的身分:',options_1)

st.write('#### **你哪時有空:**')
answer_2=st.selectbox('請選擇一個時間:',options_2)

if answer_2=='Others':
    answer_2=st.text_input('請填寫其他時間:')
    
st.write('#### **你想吃哪家餐廳:**')
answer_3=st.selectbox('請選擇一家餐廳:',options_3)

if answer_3=='Others':
    answer_3=st.text_input('請填寫其他餐廳:')
    
if os.path.exists('answers.xlsx'):
    df_old=pd.read_excel('answers.xlsx')
else:
    df_old=pd.DataFrame()
    
#增加按鈕
if st.button('送出'):
    if answer_1:
        df_new=pd.DataFrame({'身分':[answer_1],'時間':[answer_2],'餐廳':[answer_3]})
        df=pd.concat([df_old,df_new],ignore_index=True)
        df.to_excel('answers.xlsx',index=False)
        st.success('投票結果已送出，感謝您的回覆!')
        
