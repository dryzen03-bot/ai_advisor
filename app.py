import streamlit as st

st.set_page_config(
    page_title="AI-советчик",
    page_icon="💡",
    layout="centered"
)

# ---------- Стили ----------
st.markdown("""
<style>
html, body, [class*="css"]  {
    font-family: 'Segoe UI', sans-serif;
}

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

.hero-title {
    font-size: 34px;
    font-weight: 700;
    margin-bottom: 8px;
}

.hero-subtitle {
    font-size: 16px;
    opacity: 0.95;
    line-height: 1.5;
}

.card {
    background: white;
    border-radius: 22px;
    padding: 24px;
    box-shadow: 0 8px 24px rgba(43, 55, 120, 0.08);
    margin-bottom: 18px;
}

.section-title {
    font-size: 18px;
    font-weight: 700;
    color: #2b2d42;
    margin-bottom: 10px;
}

.helper-text {
    color: #5f6475;
    font-size: 14px;
    margin-bottom: 12px;
}

.examples-box {
    background: #f7f8ff;
    border: 1px solid #e4e8ff;
    border-radius: 18px;
    padding: 18px;
    margin-top: 14px;
}

.example-chip {
    display: inline-block;
    background: white;
    border: 1px solid #d9def8;
    color: #4b4f67;
    border-radius: 999px;
    padding: 8px 12px;
    margin: 6px 6px 0 0;
    font-size: 14px;
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

# ---------- Заголовок ----------
st.markdown("""
<div class="hero-box">
    <div class="hero-title">💡 AI-советчик по Python</div>
    <div class="hero-subtitle">
        Задайте вопрос по заданию. Советчик подсказывает направление решения,
        напоминает синтаксис и помогает разобраться в теме, но не пишет готовый код.
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- Логика ответов ----------
def get_answer(q: str) -> str:
    q = q.lower()

    if "input" in q or "ввод" in q or "считать" in q:
        return """💡 Подсказка

Чтобы получить данные от пользователя, используется функция input().

Подумайте:
• сколько значений нужно считать
• нужно ли преобразовать их в число
• в какие переменные сохранить введённые данные"""

    elif "print" in q or "вывод" in q or "вывести" in q:
        return """💡 Подсказка

Для вывода данных используется функция print().

Проверьте:
• что именно нужно вывести
• нужно ли добавить поясняющий текст
• как объединить текст и переменные"""

    elif "if" in q or "услов" in q or "ветв" in q:
        return """💡 Подсказка

Условная конструкция нужна, когда программа должна выбрать одно из нескольких действий.

Алгоритм:
1. проверить условие
2. если оно истинно — выполнить одно действие
3. иначе — выполнить другое"""

    elif "for" in q or ("цикл" in q and "while" not in q):
        return """💡 Подсказка

Цикл for используется, когда количество повторений известно заранее.

Подумайте:
• сколько раз нужно повторить действие
• нужен ли range()
• что должно происходить внутри цикла"""

    elif "while" in q:
        return """💡 Подсказка

Цикл while выполняется до тех пор, пока условие истинно.

Важно:
• правильно задать условие
• изменять переменную внутри цикла
• следить, чтобы цикл не стал бесконечным"""

    elif "строк" in q or "split" in q or "upper" in q or "lower" in q or "символ" in q or "слово" in q:
        return """💡 Подсказка

При работе со строками нужно понять, что именно требуется:
• обработать всю строку
• разбить её на слова
• найти отдельные символы
• изменить регистр"""

    elif "спис" in q or "list" in q or "append" in q:
        return """💡 Подсказка

Список нужен для хранения нескольких значений.

Проверьте:
• как создаётся список
• как добавить новый элемент
• как обратиться к элементу по индексу
• нужен ли цикл для обработки всех элементов"""

    elif "двумер" in q or "матриц" in q or "таблиц" in q:
        return """💡 Подсказка

Двумерный список похож на таблицу: в нём есть строки и столбцы.

Подумайте:
• как обратиться к элементу по двум индексам
• нужен ли вложенный цикл
• что обрабатывается: строка, столбец или вся таблица"""

    elif "словар" in q or "dict" in q or "ключ" in q:
        return """💡 Подсказка

Словарь хранит данные в формате «ключ — значение».

Проверьте:
• какой ключ нужен
• какое значение ему соответствует
• как получить значение по ключу"""

    elif "кортеж" in q or "tuple" in q:
        return """💡 Подсказка

Кортеж похож на список, но его элементы нельзя изменять.

Подумайте:
• нужно ли просто сохранить набор значений
• будете ли вы потом менять элементы"""

    elif "функц" in q or "def" in q or "return" in q:
        return """💡 Подсказка

Функция помогает вынести отдельное действие в самостоятельный блок кода.

Подумайте:
• как назвать функцию
• нужны ли ей параметры
• должна ли она что-то возвращать через return"""

    elif "файл" in q or "open" in q or "read" in q or "write" in q:
        return """💡 Подсказка

Для работы с файлами используется open().

Сначала определите:
• нужно ли читать файл или записывать в него
• какой режим нужен: r, w или a
• нужно ли работать с текстом построчно"""

    elif "ошибк" in q:
        return """💡 Подсказка

Если в программе ошибка, проверьте:
• правильно ли написаны имена переменных
• не забыты ли двоеточия и скобки
• верные ли отступы
• подходит ли тип данных для операции"""

    else:
        return """🤖 Я не нашёл точного шаблонного ответа.

Попробуйте задать вопрос точнее.

Например:
• как использовать input
• как вывести переменную
• как сделать цикл for
• как объявить функцию
• как открыть файл"""

# ---------- Основная карточка ----------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">Введите вопрос</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="helper-text">Например: "как использовать input", "как сделать цикл for", "как открыть файл"</div>',
    unsafe_allow_html=True
)

question = st.text_input(
    label="Ваш вопрос",
    label_visibility="collapsed",
    placeholder="Напишите ваш вопрос здесь..."
)

if st.button("Получить подсказку", use_container_width=True):
    if question.strip() == "":
        st.warning("Введите вопрос.")
    else:
        answer = get_answer(question)
        st.markdown(f'<div class="answer-box">{answer}</div>', unsafe_allow_html=True)

st.markdown("""
<div class="examples-box">
    <div class="section-title" style="font-size:16px;">Примеры вопросов</div>
    <span class="example-chip">Как использовать input()?</span>
    <span class="example-chip">Как сделать условие if?</span>
    <span class="example-chip">Как работает цикл for?</span>
    <span class="example-chip">Как объявить функцию?</span>
    <span class="example-chip">Как открыть файл?</span>
    <span class="example-chip">Как добавить элемент в список?</span>
</div>
""", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# ---------- Нижняя заметка ----------
st.markdown("""
<div class="footer-note">
AI-советчик помогает понять направление решения. Итоговую программу студент пишет самостоятельно.
</div>
""", unsafe_allow_html=True)
