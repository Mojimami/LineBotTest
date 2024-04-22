from modules.accessTokenAndKey import access_token, secret
from modules.rich_menu_func import initialize_rich_menu, assign_rich_menu, assign_rich_menu_to_all, rich_menu
from modules.rich_menu_body import rich_menu
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, PostbackEvent
import json

app = Flask(__name__)
# Channel Access Token and Channel Secret from LINE Developer Console
CHANNEL_ACCESS_TOKEN = access_token
CHANNEL_SECRET = secret

# Initialize LineBot SDK
line_bot_api = LineBotApi(CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(CHANNEL_SECRET)


# Define Flask route for receiving webhook events from LineBot
@app.route("/callback", methods=['POST'])
def callback():
    assign_rich_menu_to_all(rich_menu['index']['id'])
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


# Handle text messages
@handler.add(MessageEvent, message=TextMessage)
def handle_text_message(event):
    message_text = event.message.text
    reply_text = "You said: " + message_text
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=reply_text))
    
# Handle postback
@handler.add(PostbackEvent) 
def handle_postback(event):
    action = event.postback.data
    user_id = event.source.user_id
    
    if action.startswith("change-to-"):
        rich_menu_name = action.split("-")[-1]
        rich_menu_id = rich_menu[rich_menu_name]['id']
        assign_rich_menu(user_id, rich_menu_id)
    
    elif action == 'set-default':
        rich_menu_id = line_bot_api.get_default_rich_menu()
        assign_rich_menu(user_id, rich_menu_id)
        


if __name__ == "__main__":
    initialize_rich_menu()

    app.run(port=5002)
