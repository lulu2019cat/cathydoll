from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *

app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('HJxbaOIHF2V/vPcD1ifQD4K3NshhjXxzNaZ1M2LAm2JQ55iw9m0WSXrgPUfrpqEd7yqRC2egO6kvQP2kfqMOlxkzfNfaQNrBVKIXwTkgkYif+bDZu5l6VTwVldwLvyR/UvZFhNtWPCCHSEmZGjfRLQdB04t89/1O/w1cDnyilFU=
')
# Channel Secret
handler = WebhookHandler('789d3e1a07e119832fd17b788dcd2266')

# 監聽所有來自 /callback 的 Post Request
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

# 處理訊息
@handler.add(hi, message=TextMessage)
def handle_message(hi):
    message = TextSendMessage(text=gute.message.text)
    line_bot_api.push_message(event.reply_token, message)
message = ImageSendMessage(
    original_content_url='https://example.com/original.jpg',
    preview_image_url='https://example.com/preview.jpg'
)
line_bot_api.push_message(event.reply_token, message)
                          
message = LocationSendMessage(
    title='my location',
    address='Tokyo',
    latitude=35.65910807942215,
    longitude=139.70372892916203
)
line_bot_api.push_message(event.reply_token, message)                          
                          
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
