import streamlit as st
import google.generativeai as genai

# 1. 網頁基本設定
st.set_page_config(page_title="五泰房屋 AI 文案產生器", page_icon="🎬")

# 2. 安全讀取 API Key
try:
    API_KEY = st.secrets["GEMINI_API_KEY"]
    genai.configure(api_key=API_KEY)
except:
    st.error("❌ 尚未在 Secrets 設定 API Key")

st.title("🎬 短影音文案產生器")
st.caption("專為 Reels / TikTok / YT Shorts 設計")

# 3. 輸入介面
topic = st.text_input("1. 影片主題", placeholder="例如：1580萬入主大三房")
points = st.text_area("2. 影片重點", placeholder="走路就上學、龍居鄉大三房")
tone = st.selectbox("3. 選擇語氣", ["活潑有趣", "專業權威", "親切鄰家"])

# 4. 執行邏輯 (重點修正區)
if st.button("🚀 產生文案"):
    if not topic:
        st.warning("請先輸入主題喔！")
    else:
        with st.spinner('AI 正在嘗試多個模型版本以確保連線...'):
            # 這裡我們換成最通用的名稱，並加上錯誤處理
            success = False
            # 依序測試可能的模型名稱
            for model_name in ['gemini-1.5-flash-latest', 'gemini-1.5-pro-latest', 'gemini-pro']:
                try:
                    model = genai.GenerativeModel(model_name)
                    prompt = f"你是一位房地產專家，請針對主題『{topic}』與重點『{points}』，以『{tone}』的語氣，寫出3個吸睛標題、前3秒鉤子文案與一段短影音說明，包含適當的 Emoji。"
                    response = model.generate_content(prompt)
                    
                    st.success(f"✨ 使用模型 {model_name} 生成成功！")
                    st.markdown("---")
                    st.markdown(response.text)
                    success = True
                    break # 只要成功一個就停止測試
                except Exception as e:
                    continue # 失敗就試下一個
            
            if not success:
                st.error("❌ 目前所有模型版本皆無法連線，請檢查您的 API Key 是否正確或是否有權限。")

st.divider()
st.caption("© 2026 住商不動產五泰房屋")
