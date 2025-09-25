import streamlit as st
from nltk.chat.util import Chat, reflections

# -----------------------------
# Chatbot conversation patterns
# -----------------------------
pairs = [
    # Greetings
    [r"hi|hello|hey", ["Hello! Welcome to Ceramic Pro India, How can I help you ?"]],
    [r"(i am|i'm|new) customer", ["🚗 Welcome! 🎉 As a new customer, would you like to know about our services or company background?"]],
    [r"(regular|existing)", ["🏁 Welcome back! 🙌 Would you like to know about new offers, aftercare, or warranty details?"]],
    [r"(vvip|vip)", ["🌟🏎️ Welcome VVIP! We truly value you. Do you want exclusive partnership info, premium services, or priority support?"]],

    # About Company
    [r"what is ceramic pro|about company", [
        "🛡 Ceramic Pro is a global leader in nanoceramic protective coatings, developed by Nanoshine Group Ltd. "
        "Founded around 2010, we now operate in 80+ countries with 5,000+ certified installers worldwide. 🏎️"
    ]],

    # Services
    [r"services|what services do you provide", [
        "We provide a wide range of services:\n"
        "🚗 Automotive\n🛡 Paint Protection Film\n🌞 Window Tint\n🏎 Motorsports\n⛵ Marine\n🏭 Industrial\n🏢 Dealerships\n🤝 Partnerships"
    ]],

    [r"(i choose|i'm intrested in|i was looking for)automotive", ["🚗 Our automotive services include advanced protective coatings that enhance gloss and protect against UV, dirt, and scratches."]],
    [r"(i choose|i'm intrested in|i was looking for) paint protection film|ppf", ["🛡 KAVACA Paint Protection Film protects your car from scratches, rock chips, and damage. It’s self-healing and high-gloss. 🏎️"]],
    [r"(i choose|i'm intrested in|i was looking for)window tint", ["🌞 Ceramic IR Window Films block UV and infrared heat, keeping your vehicle cool and stylish. 🚘"]],
    [r"(i choose|i'm intrested in|i was looking for)motorsports", ["🏎 For motorsports, we provide durable coatings and films to protect high-performance vehicles under extreme conditions."]],
    [r"(i choose|i'm intrested in|i was looking for)marine", ["⛵ Marine coatings protect boats and yachts from saltwater, UV rays, and harsh environments."]],
    [r"(i choose|i'm intrested in|i was looking for)industrial", ["🏭 Industrial-grade coatings enhance durability of machinery, structures, and surfaces exposed to harsh conditions."]],
    [r"(i choose|i'm intrested in|i was looking for)dealerships", ["🏢 Dealership programs include training, certifications, and support tools like Shop Manager software."]],
    [r"(i choose|i'm intrested in|i was looking for)partnerships", ["🤝 We collaborate globally with partners for elite dealership networks, distribution, and training."]],

    # Product details
    [r"coating|ceramic pro 9h", ["Ceramic Pro 9H is our flagship nanoceramic coating, offering hardness, hydrophobicity, UV resistance, and chemical protection. 🚗"]],
    [r"aftercare|maintenance", ["🧴 We provide boosters and gloss enhancers to maintain shine and hydrophobic performance."]],
    [r"warranty", ["📜 Our warranty requires annual inspections and proper maintenance. Details vary by package, so always check terms carefully. 🏎️"]],

    # Exit
    [r"bye|exit|quit", ["🏁 Thank you for visiting Ceramic Pro Showroom. Have a great day! ✨"]],
    [r"thank you| thanks", ["Ur most welcome, we Value our customers, providing them Good Services is our 1st priority "]]
]

chatbot = Chat(pairs, reflections)

# -----------------------------
# Streamlit UI
# -----------------------------
st.set_page_config(page_title="Ceramic Pro ChatBot", page_icon="🏎️", layout="centered")

st.title("CERAMIC PRO INDIA")
st.write("Welcome to Ceramic Pro Customer Service Chat! 💬")

# Sports car image banner
st.image("C:\my projects\Ceramic pro.png", caption="Ceramic Pro - Protecting What You Love 🏎️", use_container_width=True)

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "collecting_info" not in st.session_state:
    st.session_state.collecting_info = None
if "customer_details" not in st.session_state:
    st.session_state.customer_details = {"name": None, "phone": None, "email": None}

# Chat input
user_input = st.text_input("You: ", "")

if user_input:
    response = None

    # Check if user agrees to service
    if any(word in user_input.lower() for word in ["yes", "agree", "book", "i want", "interested"]):
        st.session_state.collecting_info = "name"
        response = "Great choice! 🏎️ Please provide your **full name** for further processing."
    
    # Collecting details step by step
    elif st.session_state.collecting_info == "name":
        st.session_state.customer_details["name"] = user_input
        st.session_state.collecting_info = "phone"
        response = f"Thanks {user_input}! 🙌 Now, please share your **phone number**."
    
    elif st.session_state.collecting_info == "phone":
        st.session_state.customer_details["phone"] = user_input
        st.session_state.collecting_info = "email"
        response = "Perfect! 📱 Now, could you provide your **email address**?"
    
    elif st.session_state.collecting_info == "email":
        st.session_state.customer_details["email"] = user_input
        st.session_state.collecting_info = None
        details = st.session_state.customer_details
        response = (f"✅ Thank you {details['name']}! We’ve received your details:\n"
                    f"- Phone: {details['phone']}\n"
                    f"- Email: {details['email']}\n\n"
                    "Our team will reach out to you shortly 📧📱. Have a great day! ✨")

    # Normal chatbot conversation
    else:
        response = chatbot.respond(user_input.lower())
        if not response:
            response = "Sorry, I didn’t quite get that. Can you please rephrase? 🙂"
    
    # Save to history
    st.session_state.chat_history.append(("You", user_input))
    st.session_state.chat_history.append(("Bot", response))

# Display chat history
for sender, message in st.session_state.chat_history:
    if sender == "You":
        st.markdown(f"**🧑‍💻 {sender}:** {message}")
    else:
        st.markdown(f"**🤖 {sender}:** {message}")



