from dataclasses import dataclass, field
from string import Template

from aiogram import types, Bot
from aiogram.utils import markdown as m



@dataclass
class SendingData:
    uid: str
    text: str | Template
    url: str
    btn_title: str
    photo: str | None = None

    kb: types.InlineKeyboardMarkup = field(init=False)
    count: int = field(init=False)

    async def get_text(self, bot: Bot, user_id: int, name: str = None):
        if isinstance(self.text, str):
            return self.text
        else:
            if name is None:
                chat_member = await bot.get_chat_member(user_id, user_id)
                name = chat_member.user.first_name
            name = m.quote_html(name)
            return self.text.substitute(name=name)

    def __post_init__(self):
        self.kb = types.InlineKeyboardMarkup()
        self.kb.add(types.InlineKeyboardButton(self.btn_title, url=self.url))
        self.count = 0


bf_sending = SendingData("sending_24_april",
                         Template(f'💎ФИНАНСОВАЯ НЕЗАВИСИМОСТЬ УЖЕ СЕГОДНЯ ⬇️\n\n🔮Зеркальная дата 24.04.2024 в такой день энергия финансов на самом высоком уровне, только сегодня мы можем кардинально изменить твою жизнь! ️\n\nЭтот день принесет тебе новые возможности, новые предложения, деньги будут буквально на каждом шагу после прохождения практики у @your_gurusoul️\n\nНапиши слово " ФИНАНСЫ" ️\n\nНе упусти возможность изменить жизнь ✈️🌴'),
                         url="https://t.me/your_gurusoul",
                         btn_title="Написать"
                         )
