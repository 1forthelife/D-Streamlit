import streamlit as st
import openai

# 设置页面配置
st.set_page_config(
    page_title="LLM Chat App",
    page_icon="💬",
    layout="centered",
)

# 应用标题
st.title("LLM Chat App")

# 输入API参数
st.sidebar.header("API Configuration")
api_base_url = st.sidebar.text_input("API Base URL", "https://api.deepseek.com/v1")
api_key = st.sidebar.text_input("API Key", type="password")
model_name = st.sidebar.text_input("Model Name", "deepseek-chat")

# 设置OpenAI API密钥和base URL
openai.api_key = api_key
openai.api_base = api_base_url

# 聊天记录
if "messages" not in st.session_state:
    st.session_state.messages = []


# 显示聊天记录
def display_chat(messages):
    for i, message in enumerate(messages):
        role = message["role"]
        content = message["content"]
        if role == "user":
            st.markdown(f"**I:** {content}", unsafe_allow_html=True)
        else:
            st.markdown(f"**AI:** {content}", unsafe_allow_html=True)


# 发送消息并获取响应
def send_message(user_input):
    if user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})

        # 调用OpenAI API
        try:
            response = openai.ChatCompletion.create(
                model=model_name,
                messages=st.session_state.messages,
            )

            response_message = response["choices"][0]["message"]["content"]
            st.session_state.messages.append({"role": "assistant", "content": response_message})

            # 刷新页面以显示对话结果
            st.rerun()

        except openai.error.OpenAIError as e:
            st.error(f"OpenAI API Error: {e}")


# 显示聊天记录
display_chat(st.session_state.messages)

# 输入区域
if api_key and api_base_url and model_name:
    user_input = st.text_input("You:")
    if st.button("Send"):
        send_message(user_input)
else:
    st.warning("Please enter your API Base URL, API Key, and Model Name in the sidebar.")
