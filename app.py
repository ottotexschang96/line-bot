# web app: to building a sever

from flask import Flask, request, abort # flask(for small project) /django(for large project with an image, like web) can be for python sever or build a website

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

line_bot_api = LineBotApi('2ZDlI+M1yYBZ7QhO5UqCIbeguyBViVzWelIm7aDY6+c/Dmxd3etQxmVLesRClSVBkcuGfSFFPMM9+wW9if4LI2jUMS711xR2fCwEht8kHK/69i9tglsrS/1lKJ2JQKWeXK6tFPPgqDVLPEWuQTlFagdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('cd6b252f9b8191ba35122e976024f118')
# YOUR_CHANNEL_ACCESS_TOKEN權杖/利
# YOUR_CHANNEL_SECRET 

# The following is the code for receving the msg from line
# if user input www.line-bot.com/callback
@app.route("/callback", methods=['POST'])

# callback will run the following
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
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'

# the above will trigger the following to reply the msg from line
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)) # event.message.text is the user msg


if __name__ == "__main__":
    app.run()