from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

openai.api_key = os.getenv("OPENAI_API_KEY")

from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def get_ai_reply(user_msg):
    return "Hello This is  my WhatsApp chatbot working successfully!"
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful WhatsApp assistant."},
                {"role": "user", "content": user_msg}
            ]
        )
        return response.choices[0].message.content

    except Exception as e:
        print("Error:", e)
        return "⚠️ Bot error, check server."
@app.route("/whatsapp", methods=["POST"])
def whatsapp():
    incoming_msg = request.form.get("Body")
    reply = get_ai_reply(incoming_msg)

    resp = MessagingResponse()
    msg = resp.message()
    msg.body(reply)

    return str(resp)

if __name__ == "__main__":
    app.run(port=5000, debug=True)