# Employee Wellness Feedback BOT 

A chatbot for conversing with employees.

1) Asks basic questions regarding work culture and job satisfaction.
2) Accepts both MCQ and open ended responses
3) Stores responses in SQLite database



Tech stack :
Python 
RASA
Sqlite


## Running the assistant

1. Train the model:

``rasa train``

2. Open a second terminal window and start the action server:

``rasa run actions``

3. Return to the first terminal window and start the assistant on the command line:

``rasa shell``

