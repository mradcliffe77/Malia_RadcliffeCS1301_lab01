#Quiz
import streamlit as st
st.set_page_config(initial_sidebar_state="expanded")
st.title("🍽️ GT Dining Match Quiz") 

st.write("Answer a few questions and I'll match you with your best GT dining option!")  # basic

st.image("nave.png", caption="North Avenue Dining Hall (Nav)"), use_container_width=True) 
st.image("willage.png", caption="Willage Dining Hall", use_container_width=True)
st.image("student_center.png", caption="Student Center Options", use_container_width=True) 

st.divider()  

# Scores for each outcome
scores = {
    "Nav Dining Hall": 0,
    "Willage Dining Hall": 0,
    "Student Center Panda Express": 0,
    "Student Center Chick-fil-A": 0,
    "Prefer to Cook in Dorm": 0
}

st.subheader("Question 1: What's your #1 priority?") 
priority = st.radio(  
    "Choose one:",
    ["Speed", "Variety", "Healthier options", "Comfort food", "Saving money"]
)

if priority == "Speed":
    scores["Student Center Panda Express"] += 2
    scores["Student Center Chick-fil-A"] += 2
elif priority == "Variety":
    scores["Nav Dining Hall"] += 2
    scores["Willage Dining Hall"] += 2
elif priority == "Healthier options":
    scores["Prefer to Cook in Dorm"] += 2
    scores["Willage Dining Hall"] += 1
elif priority == "Comfort food":
    scores["Student Center Chick-fil-A"] += 2
    scores["Nav Dining Hall"] += 1
else:  
    scores["Prefer to Cook in Dorm"] += 2
    scores["Nav Dining Hall"] += 1

st.subheader("Question 2: Which foods sound good right now? (pick 2–4)")
foods = st.multiselect(  
    "Select all that apply:",
    ["Fried chicken", "Orange chicken / rice bowls", "Salad / light meals", "Pizza / burgers", "Home-style meal prep"]
)

#scoring for choices
if "Fried chicken" in foods:
    scores["Student Center Chick-fil-A"] += 2
if "Orange chicken / rice bowls" in foods:
    scores["Student Center Panda Express"] += 2
if "Salad / light meals" in foods:
    scores["Willage Dining Hall"] += 2
if "Pizza / burgers" in foods:
    scores["Nav Dining Hall"] += 2
if "Home-style meal prep" in foods:
    scores["Prefer to Cook in Dorm"] += 2

st.subheader("Question 3: How busy is your day today?")
busyness = st.slider("0 = chill day, 10 = chaotic day", 0, 10, 5)  

if busyness >= 8:
    scores["Student Center Panda Express"] += 2
    scores["Student Center Chick-fil-A"] += 2
elif 4 <= busyness <= 7:
    scores["Nav Dining Hall"] += 1
    scores["Willage Dining Hall"] += 1
else:
    scores["Prefer to Cook in Dorm"] += 2

st.subheader("Question 4: How far are you willing to walk?")
walk = st.selectbox( 
    "Pick one:",
    ["I want it super close", "I'll walk a bit", "I'll walk anywhere if it's worth it"]
)

if walk == "I want it super close":
    scores["Student Center Panda Express"] += 1
    scores["Student Center Chick-fil-A"] += 1
elif walk == "I'll walk a bit":
    scores["Nav Dining Hall"] += 1
    scores["Willage Dining Hall"] += 1
else:
    scores["Willage Dining Hall"] += 2

st.subheader("Question 5: How many times per week do you realistically eat on campus, realistically?")
meals = st.number_input("Enter a number (0–21):", min_value=0, max_value=21, value=10)  #NEW

if meals >= 14:
    scores["Nav Dining Hall"] += 2
    scores["Willage Dining Hall"] += 2
elif 7 <= meals <= 13:
    scores["Student Center Panda Express"] += 1
    scores["Student Center Chick-fil-A"] += 1
else:
    scores["Prefer to Cook in Dorm"] += 2

st.divider() 

# Displaying Results
st.subheader("Your Results")


progress = 1.0  
st.progress(progress)


sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
best_choice, best_score = sorted_scores[0]
backup_choice, backup_score = sorted_scores[1]

st.metric("Top Match", best_choice)
st.metric("Backup Match", backup_choice)


st.write("### Why you got this match:")
if best_choice == "Nav Dining Hall":
    st.write("- You seem to like variety and classic dining hall options.")
    st.write("- Nav is a solid all-around choice when you want options.")
elif best_choice == "Willage Dining Hall":
    st.write("- You leaned toward lighter/healthier choices and variety.")
    st.write("- Willage is great when you want a balanced meal.")
elif best_choice == "Student Center Panda Express":
    st.write("- Speed + bold flavors = Panda energy.")
    st.write("- Great when you need quick fuel between classes.")
elif best_choice == "Student Center Chick-fil-A":
    st.write("- Comfort food + convenience vibes.")
    st.write("- Perfect when you need a guaranteed favorite fast.")
else:
    st.write("- You value saving money, control over ingredients, or meal prep.")
    st.write("- Cooking in your dorm fits your style best.")


col1, col2 = st.columns(2)

with col1:
    if st.button("Celebrate my results 🎉"):  
        st.balloons()  
        st.success("Congrats on finding your dining destiny!")  

with col2:
    if st.button("GT just needs better dining halls 😅"):  
        st.warning("Your feedback has been forwarded directly to... nobody.")
        st.write("But spiritually, everyone student at GT heard you on that one.")
        st.snow()
