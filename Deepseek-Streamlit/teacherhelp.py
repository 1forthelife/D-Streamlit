#庞老师的代码运行
import streamlit as st
from openai import OpenAI

# 设置页面配置
st.set_page_config(
    page_title="物理教学技能训练反馈助手",
    page_icon="💬",
    layout="centered",
)

# 应用标题
st.title("物理教学技能训练反馈助手")


if 'client' not in st.session_state:
    st.session_state.client = OpenAI(api_key="sk-be93207081af4f60a4a84f073e409bd8",
                                     base_url="https://api.deepseek.com/")
    st.session_state.messages = []

user_input = st.text_area('请同学输入你想问的问题')

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    response = st.session_state.client.chat.completions.create(
        model="deepseek-chat",
        messages=st.session_state.messages
    )

    gen_text = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": gen_text})

    st.write(gen_text)