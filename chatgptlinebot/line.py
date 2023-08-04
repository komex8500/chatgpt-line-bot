from django.conf import settings
import os

from linebot import LineBotApi, WebhookHandler
from linebot.models.send_messages import TextSendMessage

handler = WebhookHandler(settings.LINE_CHANNEL_SECRET)
line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)


def get_room(event):
    return event.source.user_id


def get_msg(event):
    return event.message.text.strip()


def reply_text(event, *messages, **kwargs):
    line_bot_api.reply_message(
        event.reply_token,
        messages=[TextSendMessage(text=message, **kwargs)
                  for message in messages],
    )
