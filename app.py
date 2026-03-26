import streamlit as st
import google.generativeai as genai

st.title("API 測試工具")

# 直接手寫貼上你的 API Key (測試完記得刪除)
api_key = st.text_input("請貼上你的 API Key 進行測試：", type="password")

if st.button("測試連線"):
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-1.5-flash')
        response = model.generate_content("你好")
        st.success(f"連線成功！AI 回應：{response.text}")
    except Exception as e:
        st.error(f"連線失敗，錯誤原因：{e}")
