# -*- coding: utf-8 -*-
"""
Created on Fri Apr 22 21:06:00 2022

@author: Zhou N
"""

import streamlit as st
import numpy as np 
import pandas as pd 
from PIL import Image

st.set_page_config(page_title = "渝管家智能健康管理系统",layout="wide")
image = Image.open('image.png')



with st.sidebar:
    st.header('基本信息')
    st.image(image)
with st.sidebar:
    name=st.text_input('姓名')
    age=st.number_input('年龄')
    gender=st.selectbox('sex',options=('男','女'))
    if gender=='男':
        sex=1
    else:
        sex=0
    national=st.text_input('民族')
    high=st.number_input('身高(cm)')
    weight=st.number_input('体重(g)')

col1, col2= st.columns([2,1])
with col1:
    st.subheader('未来5年心脑血管病趋势预测')  
    vessels=[[1,3],[2,3.7],[2.5,4],[4.7,4.1],[5,5.4]
             ]
    line_data = pd.DataFrame(
    vessels,
    columns=['心脏病风险', '卒中风险'],
    )
    
    st.line_chart(line_data,use_container_width=True,height=240)
    
    import matplotlib.pyplot as plt
    import matplotlib as mpl
    
    mpl.rcParams["font.sans-serif"]=["SimHei"]
    mpl.rcParams["axes.unicode_minus"]=False
    
    st.subheader('癌前病变风险评估') 
    
    x = ('黏膜白斑','腺瘤性肠息肉','慢性萎缩性胃炎','乳腺囊性增生','肝硬化')
    y = (5,10,37,8,50)
    chart_data= pd.DataFrame(
        y,index=x,columns=['风险程度'])
    st.bar_chart(chart_data,use_container_width=True,height=240)
    
with col2:
    st.subheader('健康建议')  
    st.write('1.随着年龄的增长，您的心脑血管疾病风险呈上升趋势，除了定期体检外，保持良好的生活习惯也能够起到积极作用')
    st.write('2.幽门螺旋杆菌阳性合并慢性萎缩性胃炎是您需要高度重视的健康风险信号，除了对慢性萎缩性胃炎积极治疗外，针对幽门螺旋杆菌的三联抗菌疗法也需要尽快开始')
    st.write('3.肥胖与饮酒导致您的肝硬化风险较高，您需要从改变生活习惯开始，配合以适当的保肝护肝药物逆转这一趋势')
    
    
    
    
