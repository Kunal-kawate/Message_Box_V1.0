import streamlit as st
import random
# ------------------Mail- Modules---------------
import imaplib
import email
from email.header import decode_header

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# -----------------------------------------------

# VS environment path D:\Final_Proejcts\QR_Gen\.venv\Scripts\python.exe -m 

# ------------------CodeBox for Environment Variables ----------------------
headers = {
    'email01' : st.secrets['EMAIL01'],
    'email02' : st.secrets['EMAIL02'],
    'pass01' : st.secrets['PASS01'],
    'pass02' : st.secrets['PASS02'],
    'content-type': 'application/json'
}

# -----------------------------------------------

def display_message_in_box(message,random_num_Text):
    if random_num_Text == 0:
        st.info(message)
    elif random_num_Text == 1:
        st.success(message)
    elif random_num_Text == 2:
        st.warning(message)
    elif random_num_Text == 3:
        st.error(message)


def read_existed_mails():
    username = headers["email02"]   #"kunalkawate242@gmail.com"
    password = headers["pass02"] 
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)

    # Select the mailbox you want to use
    mail.select("inbox")

    # The subject you are searching for
    search_subject = "MSG"

    # Search for emails with the specific subject
    status, messages = mail.search(None, '(SUBJECT "{}")'.format(search_subject))

    # Check if any emails were found
    if messages[0]:
        messages = messages[0].split()
        for num in messages:
            res, msg = mail.fetch(num, "(RFC822)")
            for response in msg:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    subject, encoding = decode_header(msg["Subject"])[0]
                    if msg.is_multipart():
                        for part in msg.walk():
                            content_type = part.get_content_type()
                            content_disposition = str(part.get("Content-Disposition"))
                            try:
                                body = part.get_payload(decode=True).decode()
                            except:
                                pass
                            if content_type == "text/plain" and "attachment" not in content_disposition:
                                random_num_Text = random.randint(0,3)
                                display_message_in_box(body,random_num_Text )
                                
    else:
        print(f"No emails found with subject: {search_subject}")
    mail.logout()

def send_email(subject, body, to_email):
    # Email account credentials
    from_email = headers["email01"] #"kunalkawate424@gmail.com"
    password = headers["pass01"] 

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    # Create server object with SSL option
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(from_email, password)

    # Send the email
    server.sendmail(from_email, to_email, msg.as_string())
    
    # Terminate the SMTP session and close the connection
    server.quit()

def main():
    st.set_page_config(layout="centered")
    st.title("Kunya.Thing ")
    st.sidebar.title("About")
    st.sidebar.write("""
Welcome to my special corner of the web! 🌟 Here, friends, family, and well-wishers can share their thoughts, memories, and funny incidents about me. 💬 Whether it's a cherished moment we've shared, a hilarious story that makes you laugh every time 😂, or simply a heartfelt message ❤️, this is your space to express it.
""")
    st.sidebar.write('**Your identity remains a secret, so feel free to share without any worries!** 🤫✨')
    st.write("From Memories to Moments: Your Stories Here ⬇️")


    # ----------read and print existed data-------------------
    read_existed_mails()
    # ----------------end------------------------------------

    # Text input at the bottom
    user_input = st.text_input("Write anything! | wait 5 sec. to save msg", key="input", placeholder="Type your message here...")

    col1, col2 = st.columns([1, 5])
    
    with col1:
        send_button = st.button("Save")
    
    with col2:
        re_fresh_button = st.button("Refresh")

    if send_button and user_input:
        subject = "MSG"
        body = user_input
        to_email = "kunalkawate242@gmail.com"
        send_email(subject, body, to_email)
        

    if re_fresh_button:
        st.session_state.clear()

if __name__ == "__main__":
    main()
