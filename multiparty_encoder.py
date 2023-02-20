import requests
import json
from requests_toolbelt import MultipartEncoder

# 设置请求地址
url = "云小微申请的AppKey"

# 设置请求头
headers = {
    "AppKey": "云小微申请的AppKey",
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW',
}

# 设置对应参数
# json.dumps 作用是把python格式解码为json格式
payload = json.dumps({
    "header": {
    },
    "payload": {
        "audioMeta": {
            # 音频格式
            "format": "mp3",
            # 采样率
            "sampleRate": "48K",
            # 音频通道数
            "channel": 2,
            # 语言类型
            "lang": "en-US"
        },
        # 语言片在语言流中的漂移
        "offset": 0,
        # 是否加标点
        "needPunc": True,
        # 是否开启文字转数字  一二三-----> 123.txt
        "transNum": True,
        # 是否调运云端vad 由云端结束语音 无需发送finished
        "useCloudVad": True,
        # 云端vad静音阈值 建议500 单位ms
        "vadThreshold": 500,
        "finished": True
    }
})

data = MultipartEncoder(
    fields={
        "audio": ("filename", open(r"语音文件", "rb"), "audio/mp3"),
        "metadata": ("metadata", payload, "application/json;charset=utf-8")
    }, boundary="----WebKitFormBoundary7MA4YWxkTrZu0gW"
)

# print("-----------------------------")
r = requests.post(url, data=data, headers=headers)
print(r.text)
print(json.loads(r.text)["payload"]["text"])

