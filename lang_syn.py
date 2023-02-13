# 导入所需要的包
import requests
import json
import base64

# 请求地址  /ai/tts
url = 'https://gwgray.tvs.qq.com/ai/tts'

# 设置请求头 注意是content-type 而不是content_type
headers = {
    "AppKey": "在云小微申请的AppKey",
    "Content-Type": "application/json"
}

data = json.dumps({
    "header": {
    },
    "payload": {
        # 合成的文本
        "text": "合成的文本 请使用 UTF-8 字符集文字长度不能超过 300",
        # 发声人
        "voiceName": "libai",
        # 合成方式, 流式合成:stream
        "synthetic_method": "stream",
        # 合成采用的模型, 标准模型:level_1, 高质模型:level_3, 默认:level_1,
        "model": "level_1",
        # 语气风格, 默认:0,悲伤:1,开心:2, 默认:0
        # "style": 2,
        # 一段文本合成语音, 可能会产生多个语音包, 合成的第一个响应包里会体现是否数据下发完成,  如果还有后续数据, 请逐渐增加 index, 来完成后续数据的请求, 直到完成为止
        "index": 0,
        # 语言类型, 中文: zh-CN, 英文: en-US, 默认: zh-CN
        # "lang": "zh-CN",
        #  音频格式: pcm/wav/opus/mp3, 默认: mp3
        # "format": "mp3",
        #  采样率: 16K/24K, 默认: 16K
        # "sampleRate": "16k",
        # speed: int // 音速(0, 100], 默认: 50
        # volume: int // 音量(0, 100], 默认: 50
        # pitch: int // 音调(0, 100], 默认: 50
        # needPhoneDuration: string // 是否需要音素时长
        # "yes", "no"，默认: "no"
    }
})

# 获取接口响应的base64
r = requests.post(url, data, headers=headers)
print("base64连接为: data:audio/mpeg;base64," + json.loads(r.text)["payload"]["dataBase64"])
# 打开/新建一个文件
file = open("文件名", "w")
# 写入文件
print(json.loads(r.text)["payload"]["dataBase64"], file=file)
file.close()


# 定义一个函数将Base64转化为MP3
def invert(txt, file):
    with open(txt, "r") as fileObj:
        base64_data = fileObj.read()
        ori_mp3_data = base64.b64decode(base64_data)
        fout = open(file, "wb")
        fout.write(ori_mp3_data)
        fout.close()


invert("文件名", "文件名")
