import telebot
from time import strftime
tb = telebot.TeleBot('YOUR_TELE_TOKEN')	#create a new Telegram Bot object
channel_id = 'YOUR_TELE_ID'
# Upon calling this function, TeleBot starts polling the Telegram servers for new messages.
# - interval: int (default 0) - The interval between polling requests
# - timeout: integer (default 20) - Timeout in seconds for long polling.
# - allowed_updates: List of Strings (default None) - List of update types to request 
string = strftime('%M')
if string == '33': #create excel file on set date
    time = strftime("%d/%m/%Y %I:%M %p")
    # Send a text message
    tb.send_message(channel_id, text='Hello, guys!!')
    tb.send_message(channel_id, text='now is ' + time)
    print("send chat")
    # Send a document
    #tb.send_document(channel_id, document=open('/your/file/path', 'rb'))
    print("send file")

tb.infinity_polling()