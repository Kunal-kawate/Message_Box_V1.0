# Message_Box_V1.0

Welcome to Message_Box_V1.0, a Python web application developed using Streamlit, imaplib, and the email module. This project allows users to share their thoughts, messages, and stories in a unique way by sending them to a designated email address. The messages are then displayed on the web application by reading from the recipient's email inbox.

![Alt text](https://github.com/Kunal-kawate/Message_Box_V1.0/blob/main/ScreenShot.png)

## Features

- **Streamlit for GUI**: Utilizes the Streamlit framework to provide a simple and intuitive user interface.
- **Email Storage**: Uses `imaplib` and `email` modules to store user messages as emails.
- **Automatic Email Sending**: When a user clicks the "Save" button, their message is automatically sent to a designated system email.
- **Email Reading**: Reads and displays messages from the receiver's email inbox, making them visible to all visitors on the site.

## How It Works

1. **Write a Message**: Users can input their messages, thoughts, or stories into the web application.
2. **Save the Message**: Upon clicking the "Save" button, the message is sent to a designated system email.
3. **Display Messages**: A Python function reads the emails from the receiver's inbox, extracts the message bodies, and displays them on the web application.
4. **Shared Platform**: All visitors can view the collective messages, creating a shared space for thoughts and memories.

## Installation

To run this project locally, follow these steps:

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/Kunal-kawate/Message_Box_V1.0.git
    cd Message_Box_V1.0
    ```

2. **Install Dependencies**:
    Make sure you have Python installed, then install the required libraries:
    ```bash
    pip install streamlit
    ```

3. **Set Up Email Configuration**:
    Create a file named `config.py` and add your email configuration:
    ```python
    'email01' : st.secrets['EMAIL01'],
    'email02' : st.secrets['EMAIL02'],
    'pass01' : st.secrets['PASS01'],
    'pass02' : st.secrets['PASS02'],
    ```

4. **Run the Application**:
    ```bash
    streamlit run app.py
    ```

## Usage

- Navigate to the local URL provided by Streamlit after running the application.
- Write your message in the provided input box.
- Click on the "Save" button to send your message to the designated email.
- The message will appear on the web page, visible to all users after being read from the receiver's email.

## Contributing

If you would like to contribute to this project, feel free to fork the repository and submit a pull request. Any contributions, such as bug fixes, feature enhancements, or optimizations, are welcome.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

## Acknowledgments

- [Streamlit](https://www.streamlit.io/) for providing the web application framework.
- Python's [imaplib](https://docs.python.org/3/library/imaplib.html) and [email](https://docs.python.org/3/library/email.html) modules for email handling.

## Contact

If you have any questions, feel free to contact me at kunalkawate424@gmail.com
