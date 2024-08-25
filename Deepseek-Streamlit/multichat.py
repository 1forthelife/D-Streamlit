#实现多轮可以反思的对话
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
    st.session_state.client = OpenAI(api_key="sk-9610cfbc5f504e2cb379cd21ecf0368f",
                                     base_url="https://api.deepseek.com/")
    st.session_state.messages = []

user_input = st.text_area('请学生输入想要问的问题')#显示这里每次会返回多个组件？这是为什么
st.session_state.messages.append({"role": "user", "content": user_input})
completion = st.session_state.client.chat.completions.create(
model="deepseek-chat",
messages=st.session_state.messages
)
answer = completion.choices[0].message.content
st.session_state.messages.append({"role": "assistant", "content": answer})
st.write(answer)
