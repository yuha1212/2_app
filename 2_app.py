import streamlit as st
import random

# セッション状態を使ってクイズの値を保持
if "exponent" not in st.session_state:
    st.session_state.exponent = None
    st.session_state.number = None

st.title("🔢 これは 2 の何乗？クイズ")

# 「問題を出す」ボタン
if st.button("🎲 新しい問題を出す"):
    st.session_state.exponent = random.randint(1, 10)
    st.session_state.number = 2 ** st.session_state.exponent

# 問題が表示される
if st.session_state.number is not None:
    st.write(f"この数は 2 の何乗でしょう？ 👉 **{st.session_state.number}**")

    user_input = st.text_input("あなたの答え（例：5）", key="answer_input")

    if user_input:
        try:
            guess = int(user_input)
            correct = st.session_state.exponent
            if guess == correct:
                st.success("✅ 正解です！")
            else:
                st.error(f"❌ 不正解です。正しくは 2 の {correct} 乗です。")
        except ValueError:
            st.warning("⚠️ 数字を入力してください。")
else:
    st.write("上のボタンを押して、問題を出しましょう！")
