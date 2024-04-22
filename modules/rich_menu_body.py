rich_menu = {
    'index':{
        'body': {
            'size': {'width': 2500, 'height': 1100},
            'selected': 'true',
            'name': 'richmenu-a',
            'chatBarText': 'Index',
            'areas': [
                {'bounds': {'x': 66, 'y': 200, 'width': 700, 'height': 700}, 'action': {'type': 'postback','label': 'a','data': 'change-to-query_system'}},
                {'bounds': {'x': 900, 'y': 200, 'width': 700, 'height': 700}, 'action': {'type': 'postback','label': 'b','data': 'change-to-recommendation_system'}},
                {'bounds': {'x': 1733, 'y': 200, 'width': 700, 'height': 700}, 'action': {'type': 'postback','label': 'c','data': 'change-to-contact_us'}}
                ]
            },
        'IMG-source': '/Users/MiNG/Documents/SideProj/nccu_food_linebot/LineBotTest/img/rich_menus/banner/Richmenu0-2500x1100.png'
        
    },
    'query_system':{
        'body': {
            'size': {'width': 2500, 'height': 1100},
            'selected': 'true',
            'name': 'richmenu-b',
            'chatBarText': '查詢系統',
            'areas': [
                {'bounds': {'x': 0, 'y': 0, 'width': 833, 'height': 220}, 'action': {'type': 'postback','label': 'a','data': 'set-default'}},
                {'bounds': {'x': 834, 'y': 0, 'width': 834, 'height': 220}, 'action': {'type': 'postback','label': 'b','data': 'change-to-recommendation_system'}},
                {'bounds': {'x': 1668, 'y': 0, 'width': 833, 'height': 220}, 'action': {'type': 'postback','label': 'c','data': 'change-to-contact_us'}},
                {'bounds': {'x': 0, 'y': 220, 'width': 1250, 'height': 800}, 'action': {'type': 'message', 'text': '查詢 0dfgfdgdfgdfgdfgdf'}},
                {'bounds': {'x': 1251, 'y': 220, 'width': 1250, 'height': 800}, 'action': {'type': 'message', 'text': '查詢 xfbxcbxbcvbcvb'}}
                ]   
            },
        'IMG-source': '/Users/MiNG/Documents/SideProj/nccu_food_linebot/LineBotTest/img/rich_menus/banner/Richmenu1-2500x1100.png'
    },
    'recommendation_system':{
        'body': {
            'size': {'width': 2500, 'height': 1100},
            'selected': 'true',
            'size': {'width': 2500, 'height': 1100},
            'selected': 'true',
            'name': '推薦系統',
            'chatBarText': '推薦系統',
            'areas': [
                {'bounds': {'x': 0, 'y': 0, 'width': 833, 'height': 220}, 'action': {'type': 'postback','label': 'a','data': 'change-to-query_system'}},
                {'bounds': {'x': 834, 'y': 0, 'width': 834, 'height': 220}, 'action': {'type': 'postback','label': 'b','data': 'set-default'}},
                {'bounds': {'x': 1668, 'y': 0, 'width': 833, 'height': 220}, 'action': {'type': 'postback','label': 'c','data': 'change-to-contact_us'}},
                {'bounds': {'x': 0, 'y': 220, 'width': 1250, 'height': 800}, 'action': {'type': 'message', 'text': '推薦 0'}},
                {'bounds': {'x': 1251, 'y': 220, 'width': 1250, 'height': 800}, 'action': {'type': 'message', 'text': '推薦 1'}}
                ]
            },
        'IMG-source': '/Users/MiNG/Documents/SideProj/nccu_food_linebot/LineBotTest/img/rich_menus/banner/Richmenu2-2500x1100.png'
    },
    'contact_us':{
        'body': {
            'size': {'width': 2500, 'height': 1100},
            'selected': 'true',
            'name': '查詢系統',
            'chatBarText': '聯絡我們',
            'areas': [
                {'bounds': {'x': 0, 'y': 0, 'width': 833, 'height': 220}, 'action': {'type': 'postback','label': 'a','data': 'change-to-query_system'}},
                {'bounds': {'x': 834, 'y': 0, 'width': 834, 'height': 220}, 'action': {'type': 'postback','label': 'b','data': 'change-to-recommendation_system'}},
                {'bounds': {'x': 1668, 'y': 0, 'width': 833, 'height': 220}, 'action': {'type': 'postback','label': 'c','data': 'set-default'}},
                {'bounds': {'x': 0, 'y': 220, 'width': 1250, 'height': 800}, 'action': {'type': 'message', 'text': '聯絡 0'}},
                {'bounds': {'x': 1251, 'y': 220, 'width': 1250, 'height': 800}, 'action': {'type': 'message', 'text': '聯絡 1'}}
                ]
            },
        'IMG-source': '/Users/MiNG/Documents/SideProj/nccu_food_linebot/LineBotTest/img/rich_menus/banner/Richmenu3-2500x1100.png'
    }
}
