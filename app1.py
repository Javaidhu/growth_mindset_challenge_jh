import streamlit as st

# 🎯 Set Page Configuration
st.set_page_config(page_title="Growth Mindset Challenge", page_icon="🌱", layout="wide")

# 🎉 App Title & Introduction
st.title("🌱 Growth Mindset Challenge")
st.markdown("### Embrace Challenges, Learn from Failure, and Grow! 💡")
st.write(
    "Welcome! This interactive challenge will help you develop a growth mindset. "
    "A growth mindset means believing that your abilities can improve with effort and learning. 🚀"
)

# 📚 Section 1: What is a Growth Mindset?
st.header("📚 What is a Growth Mindset?")
st.write(
    "A **growth mindset** is the belief that intelligence and abilities **can be developed over time**. "
    "Unlike a fixed mindset, which assumes that abilities are static, a growth mindset encourages:"
)
st.markdown("""
✔️ Embracing **challenges**  
✔️ Learning from **criticism**  
✔️ Persisting in the face of **setbacks**  
✔️ Finding inspiration in **others' success**  
""")

# 🧠 Section 2: Growth Mindset Quiz
st.header("🧠 Growth Mindset Quiz")
st.write("Take this short quiz to assess your mindset:")

# Quiz Questions
q1 = st.radio("1️⃣ When faced with a difficult task, I tend to:", 
              ["😟 Avoid it because I might fail", "💪 Give it a try and learn from the experience"])

q2 = st.radio("2️⃣ When I receive criticism, I usually:", 
              ["😡 Feel defensive and ignore it", "🤔 Reflect on it and see how I can improve"])

q3 = st.radio("3️⃣ I believe my intelligence and abilities are:", 
              ["🚫 Fixed and cannot change", "📈 Can improve with effort and practice"])

# 🏆 Quiz Results & Feedback
if st.button("📊 Submit Quiz"):
    score = sum([q1.endswith("experience"), q2.endswith("improve"), q3.endswith("practice")])

    st.subheader("🔎 Your Mindset Assessment:")
    if score == 3:
        st.success("🌟 **You have a strong growth mindset!** Keep challenging yourself and learning.")
    elif score == 2:
        st.warning("🚀 **You're on the right track!** Keep practicing growth-oriented thinking.")
    else:
        st.error("💡 **You might have a fixed mindset.** No worries—growth is possible with effort!")

# 🚀 Section 3: Tips to Develop a Growth Mindset
st.header("🚀 Tips for Building a Growth Mindset")
st.write("Here are some strategies to strengthen your mindset:")
st.markdown("""
🔹 **Embrace Challenges:** Step out of your comfort zone.  
🔹 **Learn from Criticism:** View feedback as a learning opportunity.  
🔹 **Persist Through Setbacks:** Mistakes are part of progress.  
🔹 **Celebrate Effort, Not Just Results:** Focus on learning, not just success.  
🔹 **Find Inspiration in Others:** Learn from those who have overcome obstacles.  
""")

# 📖 Section 4: Resources
st.header("📖 Recommended Resources")
st.write("Explore these resources to deepen your understanding of a growth mindset:")
st.markdown("""
📚 **Books:**  
- *Mindset: The New Psychology of Success* by Carol Dweck  
- *Grit: The Power of Passion and Perseverance* by Angela Duckworth  

🎥 **Videos:**  
- [The Power of Believing That You Can Improve](https://www.ted.com/talks/carol_dweck_the_power_of_believing_that_you_can_improve)  
- [Growth Mindset vs. Fixed Mindset](https://www.youtube.com/watch?v=M1CHPnZfFmU)  

📝 **Articles:**  
- [What Having a Growth Mindset Actually Means](https://hbr.org/2016/01/what-having-a-growth-mindset-actually-means)  
""")

# 🎯 Section 5: Daily Growth Challenge
st.header("💪 Daily Growth Mindset Challenge")
st.write("Choose a challenge for today to strengthen your mindset:")

challenges = [
    "📖 Learn something new today",
    "🗣️ Ask for feedback on a project",
    "✍️ Reflect on a recent failure and identify lessons learned",
    "🙌 Encourage someone else to take on a challenge"
]
selected_challenge = st.selectbox("Your challenge:", challenges)

if st.button("🚀 Start Challenge"):
    st.success(f"✅ Your challenge for today: **{selected_challenge}**. Good luck!")

# 📊 Section 6: Progress Tracker
st.header("📊 Growth Mindset Progress Tracker")
st.write("Track your mindset journey and improvement over time.")

progress = st.slider("On a scale of 1 to 10, how strong is your growth mindset today?", 1, 10, value=5)

if st.button("📈 Save Progress"):
    st.success(f"🌱 You rated your growth mindset as **{progress}/10** today. Keep growing!")

# 🎉 Ending Note
st.markdown("---")
st.markdown("### 🌟 Keep Learning, Keep Growing! 🌟")
st.write(
    "Developing a growth mindset is a lifelong journey. "
    "Keep challenging yourself, stay curious, and **never stop learning!** 🚀"
)
