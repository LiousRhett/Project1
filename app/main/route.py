from flask import current_app
from fastapi import Form, Request
from pydantic import BaseModel

from twilio.twiml.messaging_response import MessagingResponse

# from decouple import config
import requests
import json

from .. import client

from . import main

@main.get("/")
async def index():
    return {"msg": "working"}


class Item(BaseModel):
    Body: str
    Body: str


@main.post("/sms")
async def receive_sms(item: Item):
    # resp = MessagingResponse()
    print(item)
    # Add a message
    # resp.message("The Robots are coming! Head for the hills!")

    return ""


@main.post("/message")
async def reply(request: Request, Body: str = Form()):
    form_data = await request.form()
    whatsapp_number = form_data['From'].split("whatsapp:")[-1]

    # Check if the number is enrolled
    if whatsapp_number not in current_app.config["enrolled_numbers"]:
        message = client.messages.create(
            from_=f"whatsapp:{current_app.config['TWILIO_WHATSAPP_NUMBER']}",
            body="You are not enrolled in this service.",
            to=f"whatsapp:{whatsapp_number}"
        )
        return ""

    url = current_app.config["DIFY_URL"]
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f"Bearer {current_app.config['DIFY_API_KEY']}",
    }
    data = {
        'inputs': {},
        'query': Body,
        'response_mode': 'streaming',
        'conversation_id': current_app.config['CONVERSATION_IDS'].get(whatsapp_number, ''),
        'user': whatsapp_number,
    }
    response = requests.post(url, headers=headers, data=json.dumps(data), stream=True)
    answer = []
    for line in response.iter_lines():
        if line:
            decoded_line = line.decode('utf-8')
            if decoded_line.startswith('data: '):
                decoded_line = decoded_line[6:]
            try:
                json_line = json.loads(decoded_line)
                if "conversation_id" in json_line:
                    current_app.config["CONVERSATION_IDS"][whatsapp_number] = json_line["conversation_id"]
                if json_line["event"] == "agent_thought":
                    answer.append(json_line["thought"])
            except json.JSONDecodeError:
                print(json_line)
                continue

    merged_answer = ''.join(answer)

    try:
        # Split the message into smaller parts if it's too long
        message_parts = [merged_answer[i:i + 1590] for i in range(0, len(merged_answer), 1590)]

        for part in message_parts:
            message = client.messages.create(
                from_=f"whatsapp:{current_app.config['TWILIO_WHATSAPP_NUMBER']}",
                body=f"AI: {part}",
                to=f"whatsapp:{whatsapp_number}"
            )
            print(f"Message part sent to {whatsapp_number}: {message.body}")

        print(current_app.config['CONVERSATION_IDS'])
    except Exception as e:
        print(f"Error sending message to {whatsapp_number}: {e}")

    return ""
