import streamlit as st
import random

tarot_cards = [
"The Fool","The Magician","The High Priestess","The Empress","The Emperor",
"The Hierophant","The Lovers","The Chariot","Strength","The Hermit",
"Wheel of Fortune","Justice","The Hanged Man","Death","Temperance",
"The Devil","The Tower","The Star","The Moon","The Sun","Judgement","The World",

"Ace of Wands","Two of Wands","Three of Wands","Four of Wands","Five of Wands",
"Six of Wands","Seven of Wands","Eight of Wands","Nine of Wands","Ten of Wands",
"Page of Wands","Knight of Wands","Queen of Wands","King of Wands",

"Ace of Cups","Two of Cups","Three of Cups","Four of Cups","Five of Cups",
"Six of Cups","Seven of Cups","Eight of Cups","Nine of Cups","Ten of Cups",
"Page of Cups","Knight of Cups","Queen of Cups","King of Cups",

"Ace of Swords","Two of Swords","Three of Swords","Four of Swords","Five of Swords",
"Six of Swords","Seven of Swords","Eight of Swords","Nine of Swords","Ten of Swords",
"Page of Swords","Knight of Swords","Queen of Swords","King of Swords",

"Ace of Pentacles","Two of Pentacles","Three of Pentacles","Four of Pentacles",
"Five of Pentacles","Six of Pentacles","Seven of Pentacles","Eight of Pentacles",
"Nine of Pentacles","Ten of Pentacles","Page of Pentacles","Knight of Pentacles",
"Queen of Pentacles","King of Pentacles"
]

st.set_page_config(page_title="AI Tarot Reader", page_icon="🔮")

st.title("🔮 AI Tarot Reader")
st.write("พิมพ์คำถาม แล้วสุ่มไพ่")

question = st.text_input("คำถามของคุณ")

category = st.selectbox(
"หมวดคำถาม",
["ทั่วไป","ความรัก","การงาน","การเงิน"]
)

if category in ["ความรัก","การงาน"]:
    num_cards = 5
else:
    num_cards = 3

if st.button("สุ่มไพ่"):
    if question == "":
        st.warning("กรุณาพิมพ์คำถามก่อน")
    else:
        cards = random.sample(tarot_cards, num_cards)

        st.subheader("ไพ่ที่ได้")

        cols = st.columns(num_cards)

        for i,card in enumerate(cards):
            with cols[i]:
                st.info(card)

        st.subheader("คำทำนาย")

        st.write(f"""
คำถาม: {question}

ไพ่ที่ได้: {', '.join(cards)}

คำทำนาย:
สถานการณ์นี้กำลังมีการเปลี่ยนแปลง ไพ่แนะนำให้ใช้สติและพิจารณาทางเลือกให้รอบคอบ
""")
