# web app: to building a sever
# Fcn of 
## heroku: can execute your web app code
## Github: only for code storage that can arrange version

from flask import Flask, request, abort # flask(for small project) /django(for large project with an image, like web) can be for python sever or build a website

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, StickerSendMessage
)

app = Flask(__name__)

# YOUR_CHANNEL_ACCESS_TOKEN權杖/利
line_bot_api = LineBotApi('2ZDlI+M1yYBZ7QhO5UqCIbeguyBViVzWelIm7aDY6+c/Dmxd3etQxmVLesRClSVBkcuGfSFFPMM9+wW9if4LI2jUMS711xR2fCwEht8kHK/69i9tglsrS/1lKJ2JQKWeXK6tFPPgqDVLPEWuQTlFagdB04t89/1O/w1cDnyilFU=')
# YOUR_CHANNEL_SECRET 
handler = WebhookHandler('cd6b252f9b8191ba35122e976024f118')



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
    # rule-based <----> AI - NLP, natural language processing
    msg = event.message.text
    r = 'do not understand'
    
    if '520' or 'sticker' in msg:
        sticker_message = StickerSendMessage(
            package_id='6370',
            sticker_id='11088020'
        )
        line_bot_api.reply_message(
        event.reply_token, 
        sticker_message)

        return    

    if msg in ['hi', 'Hi']:
        r = 'u good?'
    elif msg == 'eat':
        r = 'yes'
    elif msg == 'who':
        r = 'robot'
    elif 'reserve' in msg:
        r = 'want to reserve?'
    elif '5201314NanYuanFeiXue' in msg:
        r = '奧托覺得能與飛雪見面是一個特別而難得的緣分 特地挑了城裡稀有的音樂餐廳 希望當天整體氛圍對飛雪來說是好的 奧托記得當天與飛雪的約會非常的緊張 特別是飛雪簡訊告知奧托快到餐廳的時候 奧托在餐廳裡反覆地在座位與衛生間遊走 直到最後一次奧托走出衛生間那刻飛雪從餐廳門口走來並揮揮手 奧托也揮了揮手致意 飛雪向前走來穿的是米白色的毛衣搭上很淑女的針織衫外套 再配上金色的項鍊 鞋子是雪白色的皮鞋 不同於以往帽T的滑板少年風格 今天很讓奧托印象深刻 似乎飛雪也花了心思在今天呢 飛雪入座後 忙著解釋被耽擱的原因 其實奧托並不在意只是對她笑了笑 接著就看了菜單緊張的點了好多菜 吃飯時 奧托顧著說話都沒吃上幾口 轉眼間菜餚就堆滿了一桌 幸好飛雪貼心地幫奧托夾了一些菜 奧托才把眼前的菜吃了 奧托發現飛雪是很好的聆聽者 接著又滔滔不絕地說 飛雪注視著奧托也不時回應著他 時間流逝 最後還是剩下滿山的菜餚 飛雪說打包走 奧托肯定的點點頭 吃飽散步時 奧托還是口沫橫飛地說著 特別的是飛雪回應時 頭的面相總是與行進方向完美垂直 這點讓奧托覺得很不可思議 過了好一會兒 奧托覺得飛雪走累了 他們來到了噴水池邊做了下來 只是徐徐的風吹來讓飛雪覺得晚上的夜好冷 還不時地擔心鼻涕掉下來 因此一直發出奇怪的啜泣聲 但奧托似乎沒有發覺 讓飛雪鬆了一口氣 期間飛雪告訴奧托她喜歡去博物館 因此奧托就為下次見面訂了博物館行程 奧托很開心能與飛雪一起去博物館 時候不早了 奧托才緩緩地起身送飛雪坐車子回家 目送飛雪離去直到看不見車子 奧托滿心期待下次的見面 也開心地走回家了 這天奧托度過了滿好的一晚 希望飛雪也是'
    
    line_bot_api.reply_message(
        event.reply_token, 
        TextSendMessage(text=r)) # replied event.message.text is same to the user msg



if __name__ == "__main__":
    app.run()