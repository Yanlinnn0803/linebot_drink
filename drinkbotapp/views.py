from ast import parse
from asyncio import events
from email import message
from re import S
from turtle import back
from django.shortcuts import render
from module import func

# Create your views here.
from django.conf import settings
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt

from linebot import LineBotApi, WebhookParser
from linebot.exceptions import InvalidSignatureError, LineBotApiError
from linebot.models import MessageEvent, TextSendMessage,TextMessage
from urllib.parse import parse_qsl
from linebot.models import *

from drinkbotapp.models import *

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
 

@csrf_exempt
def callback(request):
    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')

        try:
            events = parser.parse(body, signature)
        except InvalidSignatureError:
            return HttpResponseForbidden()
        except LineBotApiError:
            return HttpResponseBadRequest()
        
        for event in events:
            if isinstance(event, MessageEvent):
                #line_bot_api.reply_message(event.reply_token,TextSendMessage(text=event.message.text))
                mtext=event.message.text
                uid=event.source.user_id
                profile=line_bot_api.get_profile(uid)       
                name=profile.display_name
                iceLevel = ["去冰", "微冰", "少冰", "正常"]

                #個人資料建置
                if Client_Info.objects.filter(cUid=uid).exists()==False:
                    Client_Info.objects.create(cName = name, cUid = uid)
                #查看菜單 期間限定 關於我們
                if mtext == "關於我們":
                    func.sendMulti(event)
                elif mtext == "期間限定":
                    func.sendImgCarousel(event)
                elif mtext == "查看菜單":
                    func.sendImage(event)
                elif mtext == "查看記錄":
                    func.searchHistory(event, uid)
                # 下訂單及建立訂購紀錄
                else:
                    for ice in iceLevel:
                        if mtext.find(ice) != -1:
                            func.sendOrderAndcreateHistory(event, uid, mtext)
                    
        return HttpResponse()
    else: 
        return HttpResponseBadRequest()

                # if mtext == "@傳送文字":
                #     func.sendText(event)
                # elif mtext == "@傳送圖片":
                #     func.sendImage(event)
                # elif mtext == "@傳送貼圖":
                #     func.sendStick(event)
                # elif mtext == "@多項傳送":
                #     func.sendMulti(event)
                # elif mtext == "@傳送位置":
                #     func.sendPosition(event)
                # elif mtext == "@快速選單":
                #     func.sendQuickreply(event)
                # elif mtext == "@高歌離席":
                #     func.sendVoice(event)
                # elif mtext == "@高歌離席2":
                # func.sendVedio(event)
                # if isinstance(event, PostbackEvent):
                # backdata = dict(parse_qsl(event.postback.data))
                # if backdata.get('action') == 'buy':
                #     func.sendBack_buy(event,backdata)
                # elif backdata.get('action') == 'sell':
                #     func.sendBack_sell(event,backdata)