import streamlit as st
import google.generativeai as genai

# --- 核心設定 ---
# 這是你的專屬金鑰
API_KEY = "AIzaSyDz5AmxSMYFkmUV9XARr_lnbxBZrOWsglw"

st.set_page_config(page_title="五泰房屋 AI 測試")

st.title("🎬 五泰房屋 AI 連線測試")

# 1. 嘗試連線
try:
    genai.configure(api_key=API_KEY)
    # 我們試試看最保險的模型名稱
    model = genai.GenerativeModel('gemini-1.5-flash')
    st.success("✅ 程式碼加載成功！")
except Exception as e:
    st.error(f"❌ 初始化失敗：{e}")

# 2. 輸入測試
topic = st.text_input("影片主題", "五股大三房")

if st.button("🚀 點我測試連線"):
    with st.spinner('正在與 Google 大腦連線中...'):
        try:
            # 這是最關鍵的一行
            response = model.generate_content(f"請幫我寫一個關於『{topic}』的短影音標題")
            st.balloons() # 成功會噴氣球
            st.write("### AI 回應結果：")
            st.success(response.text)
        except Exception as e:
            st.error("❌ 連線失敗！")
            st.write("錯誤詳細原因：")
            st.code(str(e)) # 這會顯示真正的錯誤代碼
