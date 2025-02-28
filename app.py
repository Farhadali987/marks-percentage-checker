import streamlit as st
import time

def calculate_result(marks, total_marks):
    if total_marks <= 0:
        return "Please enter valid marks and total marks.", "red"
    
    percentage = (marks / total_marks) * 100
    passing_percentage = 40  # پاس ہونے کا کرائٹیریا
    
    if percentage >= passing_percentage:
        return f'✅ You passed with a percentage of {percentage:.2f}%!', "black"
    else:
        return f'❌ You failed with a percentage of {percentage:.2f}%.', "red"

# Streamlit UI
st.markdown(
    """
    <style>
    body {
        background-color: #f0f2f6;
    }
    .info {
        margin-top: 20px;
        padding: 10px;
        border: 1px solid #ddd;
        border-radius: 5px;
        background-color: #f9f9f9;
        animation: fadeIn 2s;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    </style>
    """,
    unsafe_allow_html=True
)

title = "📊 Marks Percentage Checker"
st.title(title)

st.subheader("🎓 Enter Your Marks")
marks = st.number_input("Enter your marks:", min_value=0.0, format="%.2f")
total_marks = st.number_input("Enter total marks:", min_value=1.0, format="%.2f")

if st.button("Check Result"):
    result, color = calculate_result(marks, total_marks)
    st.markdown(f'<p style="color:{color}; font-size:20px; font-weight:bold; animation: fadeIn 1s;">{result}</p>', unsafe_allow_html=True)
    
    # Additional Info with Animation
    info_html = """
    <div class="info">
        My name is <b>Farhad Ali</b>, I am an <b>IT student</b> and learning <b>Latest Technologies</b> at <b>Sindh Governor House</b>.<br>
        I am <b>18 years old</b> and I am excited to learn and work in <b>Information Technology Industries</b>.
    </div>
    """
    time.sleep(1)  # Add delay for smooth animation
    st.markdown(info_html, unsafe_allow_html=True)
