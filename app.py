import streamlit as st
from openai import OpenAI
import random

st.title("🔮 AI Tarot Reader")

# ไพ่ตัวอย่าง
cards = [
    "The Fool",
    "The Magician",
    "The High Priestess",
    "The Empress",
    "The Emperor",
    "The Lovers",
    "The Chariot",
    "Strength",
    "The Hermit",
    "Wheel of Fortune"
]

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

question = st.text_input("ถามคำถามเกี่ยวกับอนาคตของคุณ")

if st.button("สุ่มไพ่"):

    card = random.choice(cards)

    prompt = f"""
    ไพ่ที่ได้คือ {card}

    คำถามของผู้ใช้:
    {question}

    ช่วยทำนายดวงแบบไพ่ทาโรต์
    ตอบเป็นภาษาไทย
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    reading = response.choices[0].message.content

    st.subheader("ไพ่ของคุณ")
    st.write(card)

    st.subheader("คำทำนาย")
    st.write(reading)
