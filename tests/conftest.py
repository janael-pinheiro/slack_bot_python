from pytest import fixture

from src.bot.slack_bot import Message, SlackClient


@fixture
def message_format_template():
    message_format = {
        "channel": None,
        "blocks": [{
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": None,
                }
            }
            ],
        }

    return message_format


@fixture
def message():
    return Message()


@fixture
def slack_client():
    return SlackClient()
