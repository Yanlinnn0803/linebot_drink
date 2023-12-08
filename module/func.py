from cProfile import label
from cgitb import text
from email import message
from email.mime import image
from pipes import Template
from turtle import title
from django.conf import settings
from django.template import base
from linebot import LineBotApi
from linebot.models import TextSendMessage, ImageSendMessage, StickerSendMessage, LocationSendMessage, QuickReply, QuickReplyButton, MessageAction,AudioSendMessage, VideoSendMessage
from linebot.models import TemplateSendMessage,ButtonsTemplate,MessageTemplateAction,URITemplateAction,PostbackTemplateAction,PostbackEvent,ConfirmTemplate,CarouselTemplate,CarouselColumn,ImageCarouselTemplate,ImageCarouselColumn,MessageImagemapAction,URIImagemapAction,BaseSize,ImagemapArea,ImagemapSendMessage,DatetimePickerTemplateAction
from linebot.models import BoxComponent,TextComponent,ImageComponent,ButtonComponent,IconComponent,SeparatorComponent,BubbleContainer,FlexSendMessage,URIAction
import datetime
from drinkbotapp.models import *
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

from numpy import size
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)

def sendText(event):
    try:
        message = TextSendMessage(text="hi")
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤"))

def sendImage(event):
    try:
        message = ImageSendMessage(
            original_content_url="https://i.imgur.com/LznHHnD.jpg",
            preview_image_url="https://i.imgur.com/LznHHnD.jpg"  
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤"))

def sendStick(event):
    try:
        message = StickerSendMessage(
            package_id=11538,
            sticker_id=51626497
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤"))

def sendMulti(event):
    try:
        message=[
            TextSendMessage(
                text="2008年於台灣高雄創立麻古茶坊🧉\n麻古茶坊果粒茶創始品牌\n以飽滿扎實的果肉口感席捲全台🤩\n開創茶飲界新風潮🍵\n隨後更推出無添加色素的『水晶粉圓』❤️\n搭配濃醇的拿鐵系列茶飲🥛更成為超人氣的話題飲品🍹\n經營多年的麻古茶坊😊以穩健的步伐持續在全台拓展門店👍\n2017帶著獨特鮮活口感的果粒茶於全台設立超過100家門市😎\n與喜愛鮮活生命體驗的健康愛好者😍分享麻古的果漾．輕生活體驗(๑•̀ㅂ•́)و✧"
            ),
            LocationSendMessage(
            title='麻古茶坊-中壢中原店',
            address='320桃園市中壢區中北路155號',
            latitude=24.957014022042976,
            longitude=121.23938690743806
            ),
            ImageSendMessage(
                original_content_url="https://i.imgur.com/knABVwE.jpg",
                preview_image_url="https://i.imgur.com/knABVwE.jpg"  
            )
        ]
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤"))

def sendPosition(event):
    try:
        message = LocationSendMessage(
            title='麻古茶坊-中壢中原店',
            address='320桃園市中壢區中北路155號',
            latitude=24.957014022042976,
            longitude=121.23938690743806
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤"))

def sendQuickreply(event):
    try:
        message = TextSendMessage(
            text='選擇最喜歡的飲料店',
            quick_reply=QuickReply(
                items=[
                    QuickReplyButton(
                        action=MessageAction(label='可不可',
                        text='可不可')
                    ),
                    QuickReplyButton(
                        action=MessageAction(label='清心',
                        text='清心')
                    ),
                    QuickReplyButton(
                        action=MessageAction(label='都可',
                        text='都可')
                    ),
                    QuickReplyButton(
                        action=MessageAction(label='50蘭',
                        text='50蘭')
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤"))

baseurl = "https://3d98-49-216-186-80.ngrok.io/static/"

def sendVoice(event):
    try:
        message = AudioSendMessage(
            original_content_url=baseurl + 'aaa777.mp4',
            duration=5000
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤"))

def sendVedio(event):
    try:
        message = VideoSendMessage(
            original_content_url=baseurl + 'aaa.mp4',
            preview_image_url=baseurl+'bo.jpeg'
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤"))
def sendButton(event):
    try:
        message = TemplateSendMessage(
            alt_text='按鈕樣板',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/4QfKuz1.png',
                title='按鈕樣板示範',
                text='請選擇：',
                actions=[
                    MessageTemplateAction(
                        label='文字訊息',
                        text='@購買披薩'
                    ),
                    URITemplateAction(
                        label='連結網頁',
                        uri='https://www.pizzahut.com.tw/?fm=hbgtoh'
                    ),
                    PostbackTemplateAction(
                        label='回應訊息',
                        data='action=buy'
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤！"))

def sendPizza(event):
    try:
        message = TextSendMessage(
            text='感謝您購買披薩，我們將盡快為您製作。'
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤！"))

def sendBack_buy(event,backdata):
    try:
        text1 = '感謝您購買披薩，\n'
        text1+='\n我們將盡快為您製作。'
        message = TextSendMessage(
            text=text1
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, 
        TextSendMessage(text="發生錯誤！"))

def sendConfirm(event):
    try:
        message = TemplateSendMessage(
            alt_text='確認樣板',
            template=ConfirmTemplate(
                text='你確定要購買這項商品嗎？',
                actions=[
                    MessageTemplateAction(
                        label="是",
                        text='@yes'
                    ),
                    MessageTemplateAction(
                        label='否',
                        text='@no'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤！"))

def sendYes(event):
    try:
        message = TextSendMessage(
            text='感謝您的購買，\n我們將盡快寄出商品。',
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤！"))


def sendCarousel(event):
    try:
        message = TemplateSendMessage(
            alt_text='轉盤樣板',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/4QfKuz1.png',
                        title='比薩啦',
                        text='吃吃吃吃吃吃',
                        actions=[
                            URITemplateAction(
                                label='哈辣墨西哥比薩',
                                uri='https://www.pizzahut.com.tw/menu/?parent_id=263&ppid=3306'
                            ),
                            URITemplateAction(
                                label='星級白醬海鮮',
                                uri='https://www.pizzahut.com.tw/menu/?parent_id=263&ppid=3035'
                            ),
                            URITemplateAction(
                                label='壽喜雪花牛',
                                uri='https://www.pizzahut.com.tw/menu/?parent_id=263&ppid=1752'
                            ),
                        ]
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://i.imgur.com/4QfKuz1.png',
                        title='比薩啦',
                        text='吃吃吃吃吃吃',
                        actions=[
                            URITemplateAction(
                                label='和風章魚燒',
                                uri='https://www.pizzahut.com.tw/menu/?parent_id=263&ppid=309'
                            ),
                            URITemplateAction(
                                label='海鮮',
                                uri='https://www.pizzahut.com.tw/menu/?parent_id=263&ppid=424'
                            ),
                            URITemplateAction(
                                label='超級總匯',
                                uri='https://www.pizzahut.com.tw/menu/?parent_id=263&ppid=421'
                            ),
                        ]
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤！"))

def sendBack_sell(event, backdata):
    try:
        message = TextSendMessage(
            text='點選的是賣'+backdata.get('item'),
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤！"))

def sendImgCarousel(event):
    try:
        message = TemplateSendMessage(
            alt_text='圖片轉盤樣板',
            template=ImageCarouselTemplate(
                columns=[
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/o27meg5.png',
                        action=MessageTemplateAction(
                            label='芝芝芒果果粒',
                            text='芝芝芒果果粒'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/MeqtB2m.png',
                        action=MessageTemplateAction(
                            label='芒果果粒波波',
                            text='芒果果粒波波'
                        )
                    ),
                    ImageCarouselColumn(
                        image_url='https://i.imgur.com/9IvV9al.png',
                        action=MessageTemplateAction(
                            label='楊枝甘露2.0',
                            text='楊枝甘露2.0'
                        )
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤！"))

def sendImgmap(event):
    try:
        image_url = "https://i.imgur.com/Yz2yzve.jpg"
        imgwidth = 1040
        imgheight = 300
        message = ImagemapSendMessage(
            base_url = image_url,
            alt_text = "圖片地圖範例",
            base_size=BaseSize(height=imgheight,width=imgwidth),
            actions=[
                MessageImagemapAction(
                    text='你點選了紅色區塊！',
                    area=ImagemapArea(
                        x=0,
                        y=0,
                        width=imgwidth*0.25,
                        height=imgheight
                    )
                ),
                URIImagemapAction(
                    link_uri='http://www.e-happy.com.tw',
                    area=ImagemapArea(
                        x=imgwidth*0.75,
                        y=0,
                        width=imgwidth*0.25,
                        height=imgheight

                    )
                ),
            ]
        )
        
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤！"))

def sendDatatime(event):
    try:
        message = TemplateSendMessage(
            alt_text='日期時間範例',
            template=ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/VxVB46z.jpg',
                title='日期時間示範',
                text='請選擇：',
                actions=[
                    DatetimePickerTemplateAction(
                        label='選取日期',
                        data='action=sell&mode=date',
                        mode='date',
                        initial="2022-05-20",
                        min='2022-01-01',
                        max='2022-12-31'
                    ),
                    DatetimePickerTemplateAction(
                        label='選取時間',
                        data='action=sell&mode=time',
                        mode='time',
                        initial="16:00",
                        min='00:00',
                        max='23:59'
                    ),
                    DatetimePickerTemplateAction(
                        label='選取日期時間',
                        data='action=sell&mode=datetime',
                        mode='datetime',
                        initial="2022-05-20T16:00",
                        min='2022-01-01T00:00',
                        max='2022-12-31T23:59'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤！"))

def sendData_sell(event, backdata):
    try:
        if backdata.get('mode') == 'date':
            dt='日期為：'+event.postback.params.get('date')
        elif backdata.get('mode') == 'time':
            dt='時間為：'+event.postback.params.get('time')
        elif backdata.get('mode') == 'datetime':
            dt=datetime.datetime.strptime(event.postback.params.get('datetime'),'%Y-%m-%dT%H:%M')
            dt=dt.strftime('{d}%Y-%m-%d,{t}%H:%M').format(d='日期為：',t='時間為：')
        message = TextSendMessage(
            text=dt
        )
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤！"))

def sendFlex(event):
    try:
        bubble = BubbleContainer(
            direction='ltr',
            header=BoxComponent(
                layout='vertical',
                contents=[
                    TextComponent(text='可愛飲料',weight='bold',size='xxl'),
                ]
            ),
            hero=ImageComponent(
                url='https://i.imgur.com/3sBRh08.jpg',
                size='full',
                aspect_ratio='792:555',
                aspect_mode='cover',
            ),
        
        body=BoxComponent(
            layout='vertical',
            contents=[
                TextComponent(text='評價',size='md'),
                BoxComponent(
                    layout='baseline',
                    margin='md',
                    contents=[
                        IconComponent(size='lg',url='https://i.imgur.com/GsWCrIx.png'),
                        TextComponent(text='25',size='sm',color='#999999',flex=0),
                        IconComponent(size='lg',url='https://i.imgur.com/sJPhtB3.png'),
                        TextComponent(text='14',size='sm',color='#999999',flex=0),
                    ]
                ),
                BoxComponent(
                    layout='vertical',
                    margin='lg',
                    contents=[
                        BoxComponent(
                            layout='baseline',
                            contents=[
                                TextComponent(text='營業地址',color='#aaaaaa',size='sm',flex=2),
                                TextComponent(text='台北市信義路14號',color='#666666',size='sm',flex=5),
                            ],
                        ),
                        SeparatorComponent(color='#0000FF'),
                        BoxComponent(
                            layout='baseline',
                            contents=[
                                TextComponent(text='營業時間：',color='#aaaaaa',size='sm',flex=2),
                                TextComponent(text='10:00-23:00',color='#666666',size='sm',flex=5),
                            ],
                        ),
                    ],
                ),
                BoxComponent(
                    layout='horizontal',
                    margin='xxl',
                    contents=[
                        ButtonComponent(
                            style='primary',
                            height='sm',
                            action=URIAction(label='電話聯絡',
                                uri='tel:0987654321'),
                        ),
                        ButtonComponent(
                            style='secondary',
                            height='sm',
                            action=URIAction(label='查看網頁',
                                uri='http://www.e-happy.com.tw')
                        )
                    ]
                )
            ],
            
        ),
            footer=BoxComponent(
                layout='vertical',
                contents=[
                    TextComponent(text='Copyright@happystudio 2022',
                    color='#888888',
                    size='sm',
                    align='center'),
                ]
            ),
        )
        message=FlexSendMessage(alt_text='彈性配置範例',contents=bubble)
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text="發生錯誤！"))

def sendOrderAndcreateHistory(event, uid, mtext):
    msg = ""
    #寄送郵件做備份
    content = MIMEMultipart()  
    content["subject"] = "訂單"  
    content["from"] = "richardkuo0721@gmail.com"  
    content["to"] = "richardkuo0721@gmail.com" 
    content.attach(MIMEText(mtext))  
    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login("richardkuo0721@gmail.com", "ekbslbcswynfeovx")  
            smtp.send_message(content)  
            print("Complete!")
        except Exception as e:
            print("Error message: ", e)
            msg = "發生錯誤"
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text=msg))
    #建置紀錄資料庫
    Client_History.objects.create(cUid = uid, cHistory = mtext)
    try:
        msg = "已傳送訂單！"
    except:
        msg = "發生錯誤"
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=msg))

def searchHistory(event, uid):
    try:
        msg = ""
        ClientInfo = Client_Info.objects.filter(cUid=uid)
        for client in ClientInfo:
            msg += client.cName + "的購買記錄\n"
        Historys = Client_History.objects.filter(cUid = uid)
        for History in Historys:
            if History != Historys.first():
                msg+= "\n"
            for i in range(20):
                msg+= "-"
            msg += '\n'
            timemsg = ""
            timecnt = 0
            for time in str(History.mdt):
                if time == ":":
                    timecnt += 1
                    if timecnt == 2:
                        break
                timemsg += time
            msg += "時間: " + timemsg + "\n紀錄: " + History.cHistory
    except:
        msg = "發生錯誤"
    line_bot_api.reply_message(event.reply_token,TextSendMessage(text=msg))