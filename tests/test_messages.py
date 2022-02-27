from pytest import mark
import pytest


@mark.parametrize(
    "channel, message_text",
    [("#messages", "Hello, world!"), ("#test", "just a test message")])
def test_message_formatter_add_channel_and_message(
        message_format_template,
        message,
        channel,
        message_text):
    message_format_template["channel"] = channel
    message_format_template["blocks"][0]["text"]["text"] = message_text
    expected_format_message = message_format_template
    formated_message = message.formatter(channel=channel, message=message_text)

    assert formated_message == expected_format_message


@mark.parametrize(
    "channel, message_text", 
    [("#messages", "Raul seixas"), ("#project", "Fall out boy")])
def test_send_message_to_the_channel(
        slack_client,
        channel,
        message_text):
    assert slack_client.send_message(channel=channel, message=message_text)


def test_given_invalid_channel_name_raises_exception(slack_client):
    with pytest.raises(Exception):
        slack_client.send_message(channel="#invalid_channel", message="")
