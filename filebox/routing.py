from channels.routing import route
from filebox.consumers import box_add, box_message, box_disconnect


channel_routing = [
    route("websocket.connect", box_add),
    route("websocket.receive", box_message),
    route("websocket.disconnect", box_disconnect),
]
