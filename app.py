# -*- coding: utf-8 -*-
"""
Created on Sat Aug 18 01:00:17 2018

@author: linzino
"""


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

app = Flask(__name__)

line_bot_api = LineBotApi('ezzuSg71I5IQMdkrssu9o4IOzxYzbH5oYaWadU0UGlWG+e4jQLaethLWfYgpCey87fcFBp3N9xSQcHHpeuWyImwYadQ9dRiV69cEuWAmQkxnzz9GgGwqL+1TOvCqZCWV6jkanOvFLjjqV4rg1jvIdwdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('01f92b404bae1ef79ba774cb40547fdb')



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
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))
 

if __name__ == '__main__':
    app.run(debug=True)