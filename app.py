import streamlit as st

# Set page config
st.set_page_config(page_title="Doctor Chatbot", layout="centered")

# Title
st.title("🩺 Virtual Doctor Chatbot")

# Define list of specialties
specialties = {
    "General Physician": "Welcome to the General Doctor! How can I help you today?",
    "Dentist": "Hello! I'm your Dental Assistant. What's troubling your teeth?",
    "Gynaecologist": "Hi there! I'm the Gynaecology expert. How can I assist you?",
    "Orthopedic": "Hey! Orthopedic care at your service. Describe your joint or bone issue."
}

# Initialize session state for selected doctor
if "selected_doctor" not in st.session_state:
    st.session_state.selected_doctor = None

# Sidebar with doctor selection
with st.sidebar:
    st.header("Choose Your Doctor")
    for doctor in specialties:
        if st.button(doctor):
            st.session_state.selected_doctor = doctor

# Main chatbot interface
if st.session_state.selected_doctor:
    st.subheader(f"👨‍⚕️ You are now chatting with: {st.session_state.selected_doctor}")
    st.info(specialties[st.session_state.selected_doctor])

    user_input = st.text_input("💬 Your Message:", key="user_input")

    if user_input:
        # Placeholder for chatbot logic
        st.write(f"🤖 {st.session_state.selected_doctor} says: *This is a dummy reply to:* `{user_input}`")
        # Here you can plug in your model or logic per doctor type

    if st.button("🔁 Back to Doctor List"):
        st.session_state.selected_doctor = None
else:
    st.markdown("### 👇 Select a doctor from the left panel to begin your consultation.")

