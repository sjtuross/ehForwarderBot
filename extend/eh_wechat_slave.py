import itchat
import logging
import mimetypes
import os

from channel import MsgType
from plugins.eh_wechat_slave import WeChatChannel


class WechatExChannel(WeChatChannel):
    def __init__(self, queue, mutex):
        super(WeChatChannel, self).__init__(queue, mutex)
        self.itchat = itchat.new_instance()
        itchat.set_logging(loggingLevel=logging.getLogger().level, showOnCmd=False)
        self.itchat_msg_register()
        mimetypes.init(files=["mimetypes"])
        self.logger.info("EWS Inited!!!\n---")

    def poll(self):
        self.reauth()
        super().poll()

    def send_message(self, msg):
        if self._flag('gif_as_video', False) and msg.type == MsgType.Image and msg.mime == 'image/gif':
            path = msg.path.rsplit('.', 1)[0]
            if os.path.isfile(path):
                try:
                    os.remove(msg.path)
                except FileNotFoundError:
                    pass
                msg.type = MsgType.Video
                msg.path = path
        super().send_message(msg)
