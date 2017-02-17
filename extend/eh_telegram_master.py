import config

from plugins.eh_telegram_master import TelegramChannel, db


class TelegramExChannel(TelegramChannel):
    def process_msg(self, msg):
        if self._flag('linked_only', False):
            chat_uid = '%s.%s' % (msg.channel_id, msg.origin['uid'])
            tg_chats = db.get_chat_assoc(slave_uid=chat_uid)
            if len(tg_chats) == 0:
                return
        super().process_msg(msg)

    def polling_from_tg(self):
        webhook_url = self._flag('webhook_url', '')
        if webhook_url != '':
            token = getattr(config, self.channel_id)['token']
            self.bot.start_webhook('0.0.0.0', 5000, token)
            if not webhook_url.endswith('/'):
                webhook_url += '/'
            webhook_url += token
            self.bot.bot.setWebhook(webhook_url=webhook_url)
        else:
            self.bot.start_polling(timeout=10)
