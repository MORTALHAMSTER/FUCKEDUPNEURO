import tkinter as tk
import requests
import pyttsx3
import twitchio
import os

# Creating a window
root = tk.Tk ()
root.title("Example application with ChatGPT and voice acting")

# Creating a text field and a button
text_field = tk.Entry(root, width=50)
text_field.pack()
button = tk.Button(root, text="Send")

# Creating an object for voicing speech
engine = pyttsx3.init()

# Initializing the Twitch client
bot_nickname = "pasha_tech"
bot_oauth = "YOUR_BOT_OAUTH_TOKEN" # replace "YOUR_BOT_OAUTH_TOKEN" with your bot's OAuth token
bot = twitchio.Client(bot_nickname, oauth=bot_oauth)

# Function for sending a request to the ChatGPT API and receiving a response
def get_response(username, text):
url = "https://api.openai.com/v1/engines/davinci-codex/completions "
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer API_KEY" # replace "API_KEY" with your API key from ChatGPT
    }
    data = {
        "prompt": f"User {username} wrote in the chat: {text}\nAI will reply:",
"max_tokens": 50,
"temperature": 0.7
}
response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        result = response.json()["choices"][0]["text"]
else:
result = "Error processing request"
    
    # Displaying the response in the window
    response_label.config(text=result)
    
    # Voicing the response
    engine.say(result)
    engine.runAndWait()

# Message handler function in Twitch chat
async def on_message(channel, user, message):
if user.name != bot_nickname:
    
        # Sending a message for processing in ChatGPT
        get_response(user.name, message)
        
# Function for connecting to Twitch
async IRC chat def connect_to_twitch_chat():
    await bot.connect()
await bot.join(os.environ['CHANNEL_NAME']) # replace "CHANNEL_NAME" with the name of the channel the bot is connecting
to print(f"Bot {bot_nickname} has connected to the chat {os.environ['CHANNEL_NAME']}")

# Binding a function to a button
button.config(command=get_response)
button.pack()

# Creating a label to display the response
response_label = tk.Label(root, text="")
response_label.pack()

# Starting an endless loop of processing messages in a Twitch chat
bot.loop.create_task(connect_to_twitch_chat())
bot.loop.run_forever()

root.mainloop()
