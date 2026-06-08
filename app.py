import streamlit as st
import random

st.set_page_config(page_title="English Tutor", page_icon="📘")

st.title("📘 English AI Tutor (Offline Version)")
st.write("Learn English step by step — no internet AI needed.")

# ---------------- SESSION ----------------
if "score" not in st.session_state:
    st.session_state.score = 0

# ---------------- VOCAB ----------------
words = {
    "happy": "delighted / joyful / excited",
    "angry": "furious / irritated",
    "smart": "intelligent / brilliant",
    "big": "enormous / massive",
    "important": "crucial / essential"
}

# ---------------- MODE ----------------
mode = st.selectbox("Choose Mode", [
    "📚 Vocabulary",
    "✍️ Sentence Practice",
    "📖 Dictionary",
    "🧪 Quiz"
])

# ---------------- VOCAB ----------------
if mode == "📚 Vocabulary":
    word = random.choice(list(words.keys()))
    st.subheader(f"Word: {word}")
    st.success(words[word])

    sentence = st.text_input("Use this word in a sentence:")

    if st.button("Check"):
        if word in sentence.lower():
            st.success("Good job 👍")
            st.session_state.score += 1
        else:
            st.warning("Try using the word correctly.")

# ---------------- SENTENCE PRACTICE ----------------
elif mode == "✍️ Sentence Practice":
    prompts = [
        "I am very happy",
        "She is very angry",
        "This is a big house"
    ]

    q = random.choice(prompts)
    st.write("Rewrite this sentence:")
    st.info(q)

    ans = st.text_input("Your answer:")

    if st.button("Check Answer"):
        if len(ans.split()) > 5:
            st.success("Good improvement 👍")
            st.session_state.score += 1
        else:
            st.warning("Make your sentence longer.")

# ---------------- DICTIONARY ----------------
elif mode == "📖 Dictionary":
    word = st.text_input("Search word:")

    dictionary = {
        "delighted": "very happy",
        "furious": "very angry",
        "enormous": "very big",
        "crucial": "very important"
    }

    if word:
        meaning = dictionary.get(word.lower())
        if meaning:
            st.success(meaning)
        else:
            st.warning("Word not found.")

# ---------------- QUIZ ----------------
elif mode == "🧪 Quiz":
    q = "What is a better word for 'happy'?"
    st.write(q)

    answer = st.text_input("Your answer:")

    if st.button("Submit"):
        if answer.lower() in ["delighted", "joyful", "excited"]:
            st.success("Correct 🎉")
            st.session_state.score += 1
        else:
            st.error("Try: delighted / joyful / excited")

st.divider()
st.write("⭐ Score:", st.session_state.score)
