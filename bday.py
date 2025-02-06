import streamlit as st
import time

# Set Page Config
st.set_page_config(page_title="🎉 Dev's Special Birthday Wish!", layout="centered")

# Main Birthday Wish Message
st.markdown("<h1 style='text-align: center; color: #ff4500; font-size: 40px;'>🎉 Happy Birthday, Dev! 🎂</h1>", unsafe_allow_html=True)

# Display Your Photo Together (Replace 'us.jpg' with your actual file)
st.image("us.jpg", caption="💖 Forever Together 💖", use_column_width=True)

# Personalized Heartfelt Message
st.markdown(
    """
    <h2 style='text-align: center; color: #cc0000; font-size: 26px;'>Dear Dev,</h2>
    <p style='text-align: center; font-size: 20px; color: #FFFFFF; font-weight: bold;'>
    From the moment we met, my days have been brighter and my heart fuller.  
    You are my joy, my love, and my greatest adventure.  
    On this special day, I wish you boundless happiness, success, and all the love in the world. 💖  
    <br><br>
    Happy Birthday, my love! 🥰🎁🎈
    </p>
    """,
    unsafe_allow_html=True,
)

# Background Music (Audio) without Controls
st.markdown(
    """
    <audio autoplay loop>
        <source src="https://pixabay.com/music/upbeat-happy-birthday-song-background-music-295823/">
    </audio>
    """,
    unsafe_allow_html=True
)

# Centering the "Surprise" Button
col1, col2, col3 = st.columns([1, 1, 1])  # Adjust width for centering

with col2:
    surprise = st.button("Click for a Surprise 🎊", key="surprise_button")  # Centered Button

# Trigger Effects on Button Click
if surprise:
    st.balloons()  # 🎈 Balloons Effect
    st.snow()  # ❄️ Confetti Effect

    st.markdown("<h2 style='text-align: center; color: #ff9900;'>🎂 Here's a Cake Just for You! 🍰</h2>", unsafe_allow_html=True)
    st.image("https://gifdb.com/images/high/cute-birthday-cake-cupcake-nzme2j0fakd24oyh.gif", use_column_width=True)  # Cake GIF

    time.sleep(2)  # Delay for fun!

    st.markdown("<h2 style='text-align: center; color: #ff0000;'>🕯️ Make a Wish & Blow the Candles! 🕯️</h2>", unsafe_allow_html=True)
    st.image("https://i.pinimg.com/originals/35/27/e2/3527e257d5b858e307c08caa0ec4491b.gif", use_column_width=True)  # Candles GIF

    st.success("🎉 Dev, I hope this made your day extra special! 💕")

# Space Before Love Note
st.markdown("<br>", unsafe_allow_html=True)  # Space
st.markdown("<h2 style='text-align: center; color: #cc0000; font-size: 26px;'>💌 A Special Love Note 💌</h2>", unsafe_allow_html=True)

# Centering the "Reveal the Letter" Button
col1, col2, col3 = st.columns([1, 1, 1])  # Adjust width for centering

with col2:
    reveal_note = st.button("💖 Click to Reveal the Letter 💌")  # Centered Button

if reveal_note:
    time.sleep(1)  # Small delay for suspense
    st.markdown(
        """
        <div style='border: 3px solid #cc0000; padding: 20px; border-radius: 15px; background-color: #fff5f8;'>
        <h3 style='text-align: center; color: #cc0000;'>My Dearest Dev,</h3>
        <p style='font-size: 20px; color: #222; text-align: center;'>
        Every day with you is a gift, and today is the most special of them all.  
        You make my world brighter, my heart fuller, and my life richer.  
        <br><br>
        On this birthday, I want you to know that my love for you grows with every passing moment.  
        You are not just my partner—you are my happiness, my safe place, and my forever.  
        <br><br>
        No matter where life takes us, I promise to always stand by your side.  
        <br><br>
        Happy Birthday, my love. Here’s to us, always. 💕
        </p>
        <h3 style='text-align: center; color: #ff3366;'>Forever Yours ❤️</h3>
        </div>
        """,
        unsafe_allow_html=True,
    )