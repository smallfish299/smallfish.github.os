import requests
import json
from requests_toolbelt import MultipartEncoder

# 设置请求地址
url = "https://gw.tvs.qq.com/ai/asr"

# 设置请求头
headers = {
    "AppKey": "fa344ca04d8611eb93763d03417560a2",
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
        "audio": ("filename", open(r"C:\Users\29965\Desktop\音频文件\音频文件\答案3.wav", "rb"), "audio/mp3"),
        "metadata": ("metadata", payload, "application/json;charset=utf-8")
    }, boundary="----WebKitFormBoundary7MA4YWxkTrZu0gW"
)

# print("-----------------------------")
r = requests.post(url, data=data, headers=headers)
print(r.text)
print(json.loads(r.text)["payload"]["text"])

