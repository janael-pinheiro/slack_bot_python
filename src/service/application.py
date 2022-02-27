from flask import Flask, request
from waitress import serve
import logging
from datetime import datetime
from typing import Text, Dict

from src.bot.slack_bot import SlackClient

logging.basicConfig(
    format="%(asctime)s %(levelname)s %(message)s",
    level=logging.DEBUG,
    filename=f"application_{datetime.now()}.log")

app = Flask(__name__)


@app.route("/send_message", methods=["POST"])
def send_message_to_slack():
    request_data: Dict[str, str] = request.get_json()
    channel: str = request_data["channel"]
    message: Text = request_data["message"]
    if SlackClient().send_message(channel=channel, message=message):
        return f"Message sent sucessfully to channel {channel}."
    else:
        return "An error occurred while sending the message."


if __name__ == "__main__":
    serve(app, host="0.0.0.0", port=8080)
