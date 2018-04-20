from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import ptt

app = Flask(__name__)

line_bot_api = LineBotApi('4/Q8KZY2YlyxmdY3VY8e7DvM3V4U6hvR9D1kqX3sF/JMwGbfLTkqiyLZbCu2KHbGGYTEhJ5L3Zy3I132J4OtT6mJifdN4iNPBPHXSszB33xdCica5EnUOas9WVoJE2BtEbPQgmffXkOOv7mL/jPaxwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('2128d7d59327b4615609b84f37129ab0')

@app.route("/", methods=['GET'])
def yutreturn():
    return "Hello Yut"
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text == 'ราคาน้ำมัน':
        l = ptt.get_prices()
        s = ""
        for p in l:
            s += "%s %.2f บาท\n"%(p[0],p[1])

        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=s))

    else:
        ine_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text+'ค่ะ'))

if __name__ == "__main__":
    app.run()