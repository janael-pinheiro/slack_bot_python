from typing import Text, Dict, Any
from slack import WebClient
import os
import logging


class Message(object):
    def __init__(self):
        self.__logger = logging.getLogger(__name__)

    def __get_template(self) -> Dict[str, Any]:
        return {
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

    def formatter(self, channel: str, message: Text) -> Dict[str, Any]:
        """Adds the channel and message to the template required by Slack.

        Parameters
        ----------
        channel : str
            the Slack channel to which the message will be sent
        message : Text
            message to be sent to Slack

        Returns
        ----------
            mapping with channel and message
        """
        message_template = self.__get_template()
        message_template["channel"] = channel
        message_template["blocks"][0]["text"]["text"] = message
        self.__logger.info("Formatted message.")
        return message_template


class SlackClient(object):
    def __init__(self) -> None:
        self.__client = WebClient(token=os.environ.get("SLACK_TOKEN"))
        self.__message = Message()
        self.__logger = logging.getLogger(__name__)

    def send_message(self, channel: str, message: Text) -> bool:
        """Send the message to Slack.

        Parameters
        ----------
        channel : str
            the Slack channel to which the message will be sent
        message : Text
            message to be sent to Slack

        Returns
        ----------
            true when the message was successfully sent, false otherwise.
        """
        self.formatted_message =\
            self.__message.formatter(channel=channel, message=message)

        try:
            self.__client.chat_postMessage(**self.formatted_message)
            self.__logger.info("Message sent successfully.")
            return True
        except Exception as e:
            self.__logger.exception(str(e))
            raise e
