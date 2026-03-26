import streamlit as st
import google.generativeai as genai

# 設定網頁標題
st.set_page_config(page_title="五泰房屋 AI 文案產生器")

# 從後台秘密設定讀取 API Key
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
except:
    st.error("❌ 尚未設定 API Key，請至 Streamlit 後台設定 Secrets。")

st.title("🎬 短影音文案產生器")
st.info("專為 Reels / TikTok / YT Shorts 設計")

# 輸入框
topic = st.text_input("1. 影片主題", placeholder="例如：五股社會住宅申請教學")
points = st.text_area("2. 影片重點", placeholder="免仲介費、有補助、阿泰小五推薦")
tone = st.selectbox("3. 選擇語氣", ["親切鄰家", "專業權威", "活潑有趣"])

# 按鈕執行
if st.button("🚀 產生文案"):
    if topic:
        model = genai.GenerativeModel('gemini-1.5-flash')
        prompt = f"你是一位房地產社群專家，請針對主題『{topic}』與重點『{points}』，以『{tone}』的語氣，寫出 3 個吸睛標題與一段適合 Reels 的短影音文案，內容要包含適當的 Emoji。"
        
        with st.spinner('AI 正在幫你動腦中...'):
            response = model.generate_content(prompt)
            st.success("✨ 文案生成完畢！")
            st.markdown(response.text)
    else:
        st.warning("請輸入影片主題喔！")