from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings


from linebot import LineBotApi, WebhookParser
from linebot.models import MessageEvent, TextMessage

from .line import handler, reply_text, get_msg
from .message_queue import MessageQueue

import requests

line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
parser = WebhookParser(settings.LINE_CHANNEL_SECRET)


@csrf_exempt
def callback(request):

    if request.method == 'POST':
        signature = request.META['HTTP_X_LINE_SIGNATURE']
        body = request.body.decode('utf-8')
        handler.handle(body, signature)

    return HttpResponse()


@handler.add(MessageEvent, message=TextMessage)
def route(event):
    if MessageQueue.handle(event):
        return

    msg = get_msg(event)
    api_endpoint = "https://api.openai.com/v1/chat/completions"

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {settings.CHATGPT_API_KEY}"
    }

    data = {
        "model": "gpt-3.5-turbo",
        "max_tokens": 200,
        "messages": [
            {
                "role": "system",
                "content": "You are a helpful assistant."
            },
            {
                "role": "user",
                "content": msg
            }
        ]
    }

    response = requests.post(api_endpoint, json=data, headers=headers)
    if response.status_code == 200:
        reply_text(event, response.json()["choices"][0]["message"]["content"])
    else:
        print("呼叫API時發生錯誤：")
        print(response.json())
        return None
