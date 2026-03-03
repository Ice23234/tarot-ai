import streamlit as st
from openai import OpenAI

st.title("🔮 AI Tarot Reader")

# รับ API key จาก Streamlit secrets
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

question = st.text_input("ถามคำถามเกี่ยวกับอนาคตของคุณ")

if st.button("ทำนาย"):

    prompt = f"""
    ผู้ใช้ถามว่า: {question}

    กรุณาทำนายดวงแบบไพ่ทาโรต์
    ตอบเป็นภาษาไทย
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    answer = response.choices[0].message.content

    st.write("🔮 คำทำนาย")
    st.write(answer)
