import streamlit as st
from openai import OpenAI

st.set_page_config(
    page_title="AI-советчик по Python",
    page_icon="💡",
    layout="centered"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(180deg, #f4f7ff 0%, #eef2ff 100%);
}
.block-container {
    max-width: 820px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}
.hero-box {
    background: linear-gradient(135deg, #6d5dfc 0%, #8b7cff 100%);
    color: white;
    padding: 28px 30px;
    border-radius: 24px;
    box-shadow: 0 10px 30px rgba(93, 80, 255, 0.25);
    margin-bottom: 22px;
}
.card {
    background: white;
    border-radius: 22px;
    padding: 24px;
    box-shadow: 0 8px 24px rgba(43, 55, 120, 0.08);
    margin-bottom: 18px;
}
.answer-box {
    background: #eef4ff;
    border-left: 6px solid #6d5dfc;
    padding: 18px;
    border-radius: 16px;
    color: #23304d;
    white-space: pre-line;
    line-height: 1.6;
    margin-top: 10px;
}
.footer-note {
    text-align: center;
    color: #6c7287;
    font-size: 13px;
    margin-top: 16px;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="hero-box">
    <h1>💡 AI-советчик по Python</h1>
    <p>Задайте вопрос по заданию. Советчик помогает понять направление решения, но не пишет готовый код.</p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="card">', unsafe_allow_html=True)

question = st.text_input(
    "Введите ваш вопрос",
    placeholder="Например: как использовать input()?"
)

if st.button("Получить подсказку", use_container_width=True):
    if not question.strip():
        st.warning("Введите вопрос.")
    else:
        try:
            client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

            system_prompt = """
Ты — AI-советчик по Python для студентов.

Твоя задача — помогать понять задачу, но не решать её за студента.

Правила:
1. Не давай полный готовый код.
2. Не давай решение, которое можно сразу отправить в Stepik.
3. Объясняй идею, алгоритм, синтаксис и типичные ошибки.
4. Можно давать:
   - наводящие вопросы,
   - пошаговый алгоритм без готового кода,
   - объяснение синтаксиса,
   - разбор ошибки.
5. Если студент просит "реши", "напиши код", "сделай за меня",
   вежливо откажись и дай только подсказку.

Пиши понятно, кратко и по-русски.
"""

            with st.spinner("AI-советчик думает..."):
                response = client.responses.create(
                    model="gpt-5-mini",
                    instructions=system_prompt,
                    input=question
                )

            answer = response.output_text
            st.markdown(f'<div class="answer-box">{answer}</div>', unsafe_allow_html=True)

        except Exception as e:
            error_text = str(e)

            if "insufficient_quota" in error_text or "429" in error_text:
                st.error("AI-советчик временно недоступен: не настроен или исчерпан API-баланс.")
            else:
                st.error(f"Ошибка: {e}")

st.markdown('</div>', unsafe_allow_html=True)

st.markdown("""
<div class="footer-note">
AI-советчик помогает понять направление решения. Итоговую программу студент пишет самостоятельно.
</div>
""", unsafe_allow_html=True)
