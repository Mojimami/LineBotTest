from modules.accessTokenAndKey import access_token, secret
from modules.rich_menu_body import rich_menu
from linebot.exceptions import LineBotApiError
from linebot import LineBotApi
import requests
import json

line_bot_api = LineBotApi(access_token)

rickMenu_list = list(rich_menu.keys())


def create_rich_menu(label):
    headers = {'Authorization': 'Bearer ' + access_token, 'Content-Type': 'application/json'}
    
    req = requests.request('POST', 'https://api.line.me/v2/bot/richmenu', headers=headers, data=json.dumps(rich_menu[label]['body']).encode('utf-8'))
    rich_menu_id = json.loads(req.text)['richMenuId']
    return rich_menu_id


def rich_menu_image(label,rich_menu_id):
    with open(rich_menu[label]['IMG-source'], 'rb') as f:
        line_bot_api.set_rich_menu_image(rich_menu_id, 'image/jpeg', f)

def assign_rich_menu_to_all(rich_menu_id):
    try:
        headers = {'Authorization': 'Bearer ' + access_token}
        req = requests.post('https://api.line.me/v2/bot/user/all/richmenu/' + rich_menu_id, headers=headers)
        return True
    except LineBotApiError as e:
        print(f"Failed to assign rich menu to All users: {e}")
        return False
        
    
def assign_rich_menu(user_id, rich_menu_id):
    try:
        line_bot_api.link_rich_menu_to_user(user_id, rich_menu_id)
        print(f"Successfully assigned rich menu {rich_menu_id} to user {user_id}")
        return True
    except LineBotApiError as e:
        print(f"Failed to assign rich menu to user: {e}")
        return False
    
def initialize_rich_menu():
    for label in rickMenu_list:
        rich_menu_id = create_rich_menu(label)
        rich_menu_image(label,rich_menu_id)
        rich_menu[label]['id']  = rich_menu_id
   
    line_bot_api.set_default_rich_menu(rich_menu["index"]['id'])
    assign_rich_menu_to_all(rich_menu["index"]['id'])
    return True
            

