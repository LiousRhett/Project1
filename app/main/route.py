from flask import Flask, request, current_app

from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse

from . import main

# 预设关键词和回复
responses = {
    "hello": "Hi! How can I assist you?",
    "help": "Sure, here is what I can do: ...",
    "bye": "Goodbye! Have a great day!"
}

client = Client(current_app.config['ACCOUNT_SID'], current_app.config['AUTH_TOKEN'])

# 接收和回复 WhatsApp 消息
@main.route("/webhook", methods=["POST"])
def webhook():
    # 获取用户消息
    incoming_msg = request.form.get("Body", "").lower()


    sender = request.form.get("From")
    response_msg = "Sorry, I didn't understand that."

    # 匹配关键词
    for keyword, reply in responses.items():
        if keyword in incoming_msg:
            response_msg = reply
            break

    # 生成 Twilio 响应
    resp = MessagingResponse()
    resp.message(response_msg)
    return str(resp)
