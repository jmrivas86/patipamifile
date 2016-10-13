from channels import Group
from channels.auth import channel_session_user_from_http


# Connected to websocket.connect
@channel_session_user_from_http
def box_add(message):
    Group("box").add(message.reply_channel)


# Connected to websocket.receive
@channel_session_user_from_http
def box_message(message):
    Group("box").send({
        "text": message.content['text'],
    })


# Connected to websocket.disconnect
@channel_session_user_from_http
def box_disconnect(message):
    Group("box").discard(message.reply_channel)
