from flask import Flask, request
#https://github.com/line/line-bot-sdk-python
from linebot import LineBotApi, WebhookHandler
from linebot.models import FlexSendMessage, TextSendMessage
import threading
from action import action
token='rkVS9PMWauGedQ7CmvhmupHJ02nhJ0egkEmXEOnvKzjx4fiU+o0YKlfPsL/uopop3HCoWWq5S6rXCs0KwYljOQCTcv98e9FSNT/O+h2yJpK/Qve8/PHFypPlsZhkYmSKaly4NzylGMdUY3OTCS4o4gdB04t89/1O/w1cDnyilFU='
app = Flask(__name__)
true=True
line_bot = LineBotApi(token)
# LINE 聊天機器人的基本資料
loc1=["基隆市","台北市","新北市","桃園市","新竹市","新竹縣","苗栗縣","台中市","彰化縣","雲林縣","南投縣","嘉義市","嘉義縣","台南市","高雄市","屏東縣","台東縣","花蓮縣","宜蘭縣","連江縣","金門縣","澎湖縣"]
loc2={"基隆市":"2d7ad0763322f8f204948bab69b8437cc74e2cb1fddc0b11261dc6666360749e",
    "台北市":"6b221b26e046a442e03dc46fbe91d5874c6461afde61187dd4126bddeea1e2aa",
    "新北市":"5f5c20be14aba17192a3bb3a57511db1ebf2cbdd439af51cd03fa623d67e2de1",
    "桃園市":"efbf308224729b20c95ff9150f731657639bc63cce74c8c098357587b7bbc9c4",
    "新竹市":"9d98eb3f97a83330c0599a7548c3c7b47163615858673cfee2406e208ce20604",
    "新竹縣":"57a7b26fe9f26d76db41f36fb9bc87e0deca14bde2053885dad839edf0e26fc3",
    "苗栗縣":"b994c89cc0ff3b6b56814e2730a58c821d2585ce6d3f190ea6a8c502c82268c2",
    "台中市":"8e095973cc14ab3966eab1a0c6a1b04f5291e61049bff4cb42a510b3881afec9",
    "彰化縣":"50f0afa948f93e0309ee2f37a6d34beaf66a79e423e4dec6b9bc063ce8d993c8",
    "雲林縣":"ea62fd1222f79ea36b16907f723f715e9e5640c8f1dbe52360334dde168f3410",
    "南投縣":"d8b83853a6cc59e5bb3fe1e512cc4be8a3e5c1842889f42c5272bc1b14c2abb9",
    "嘉義市":"083ec430bd75b8e34579f93ce7c6c033e47d58eca20302a4ede6e3914cd1150a",
    "嘉義縣":"715bc33c482ab5cf9fa7ee48fefbf5547d8ac5da7025db275d5b43d4d000785a",
    "台南市":"cb9a4442e9bf7da0ece89bd21a5161210e79cccc0ec2647b3565977e7a278c31",
    "高雄市":"48697cc4c9743031df643ebe553fc08fd83bf2e96d7c7f58c0db435d5888131f",
    "屏東縣":"2303e8481a2d2f9b32e5343dc3661a921123f3ccdd277563e4b6d7771d53a244",
    "台東縣":"081fa0de6091622e509eef3a5b3346083026cfb067ee1df44c55c15919096639",
    "花蓮縣":"6e37fc12427c24cb9ae8e50a596754434e8244b28c1a3d25b8122fb3a0dca2f6",
    "宜蘭縣":"509a0202845cfc5a9b7e8c39e61323b593893292803d99c5fa3fe0f572f2ddff",
    "連江縣":"1fec843e21c6886161e8680edfcc424b2bd7c0a2c7cbe8996fa5473d580c8e7c",
    "金門縣":"e0c8bf85249767181baf1c831c322a7b5a7e8df91ea86434ad6b1a1ba47f6ef8",
    "澎湖縣":"952e360e0b0a5052fd0f5bd4fd190b928c930897dd3860dc5f5628af71e79ea5"}
keyword=['開始','說明','北台灣','中台灣','南台灣','東台灣','離島']
@app.route("/", methods=['POST'])

def verify():
    data = request.get_json()
    if len(data["events"]) == 0:
        print("webhook驗證通知")
        pass
    elif data['events'][0]['type']=='message':
        t=data['events'][0]['message']['text']
        if t in loc1 and t not in keyword:
            loc=loc2[t]
            A1=threading.Thread(target=action,args=(loc,))
            A1.start()
            A1.join
            ans=action(loc)
            # ans=loc
            line_bot.reply_message(data['events'][0]['replyToken'],TextSendMessage(alt_text='123',text=ans))
    return "OK", 200
if __name__ == "__main__":
    app.run(port=2000)