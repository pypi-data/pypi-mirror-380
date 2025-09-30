import re
from enum import IntEnum
from inspect import isclass
from typing import Coroutine

from pyrogram.filters import chat, private
from pyrogram.handlers import CallbackQueryHandler, MessageHandler
from pyrogram.types import (
    Message,
    User,
    ReplyKeyboardMarkup,
    CallbackQuery,
    KeyboardButton,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from xync_schema import models
from xync_schema.enums import SynonymType, Party, Slip, AbuserType, NameType

from pyro_client.client.file import FileClient


async def cbank(txt: str) -> list[tuple[int, str]]:
    return await models.Pm.filter(norm__startswith=txt[0], bank=True).values_list("id", "norm")


async def cppo(txt: str) -> list[tuple[int, str]]:
    opts = re.findall(r"\d+", txt) or [1, 2, 3, 5, 10]
    return [(o, str(o)) for o in opts]


async def btns(typ: SynonymType.__class__, txt: str = None) -> InlineKeyboardMarkup | None:
    if lst := synopts[typ]:
        if isinstance(lst, list):
            kb = [[InlineKeyboardButton(n, f"st:{typ.name}:{i}")] for i, n in enumerate(lst)]
        elif isclass(lst) and issubclass(lst, IntEnum):
            kb = [[InlineKeyboardButton(i.name, f"st:{typ.name}:{i.value}")] for i in lst]
        else:
            kb = [[InlineKeyboardButton(n, f"st:{typ.name}:{i}")] for i, n in await lst(txt)]
        return InlineKeyboardMarkup(kb)
    else:
        return lst


def get_val(typ: SynonymType.__class__, val: str) -> tuple[SynonymType | int | bool, str]:
    if isinstance(val, str) and val.isnumeric():
        val = int(val)
    if isclass(lst := synopts[typ]) and issubclass(lst, IntEnum):
        return (v := lst(val)), v.name
    elif isinstance(lst, list):
        return val, lst[val]
    return val, val


synopts: dict[SynonymType, list[str] | IntEnum | None | Coroutine] = {
    SynonymType.name: ["not_slavic", "slavic"],
    SynonymType.ppo: cppo,
    SynonymType.from_party: Party,
    SynonymType.to_party: Party,
    SynonymType.slip_req: Slip,
    SynonymType.slip_send: Slip,
    SynonymType.abuser: AbuserType,
    SynonymType.scale: ["1", "10", "100", "1000"],
    SynonymType.slavic: NameType,
    SynonymType.mtl_like: None,
    SynonymType.bank: cbank,
    SynonymType.bank_side: ["except", "only"],
}


class FillerClient(FileClient): ...


async def cond_start_handler(bot: FillerClient, msg: Message, *args, **kwargs):
    me: User = msg.from_user
    cond = await models.Cond.filter(parsed__isnull=True).order_by("-created_at").first().prefetch_related("parsed")
    rm = ReplyKeyboardMarkup(
        [
            [KeyboardButton("ppo"), KeyboardButton("abuser")],
            [KeyboardButton("from_party"), KeyboardButton("to_party")],
            [KeyboardButton("slip_send"), KeyboardButton("slip_req")],
            [KeyboardButton("name"), KeyboardButton("slavic")],
            [KeyboardButton("scale"), KeyboardButton("mtl_like")],
            [KeyboardButton("bank"), KeyboardButton("bank_side")],
        ]
    )
    bot.add_handler(MessageHandler(got_synonym, chat(me.id) & private))
    bot.storage.session.state |= {me.id: {"synonym": {"id": cond.id}}}

    return await msg.reply_text(await wrap_cond(cond.raw_txt), reply_markup=rm)


async def wrap_cond(txt: str):
    rs = {syn.txt: f'`{syn.txt}`||{syn.typ.name}="{syn.val}"||' for syn in await models.Synonym.all() if syn.txt in txt}
    [txt := txt.replace(o, n) for o, n in rs.items()]
    return txt


async def got_synonym(bot: FillerClient, msg: Message):
    if not (msg.text in {st.name for st in SynonymType} and (typ := SynonymType[msg.text])):
        return await msg.reply_text(
            f'Нет раздела "{msg.text}", не пиши текст сам, выдели кусок из моего сообщения,'
            f"ответь на него, выбери кнопку раздела"
        )
    if not msg.quote:
        return await msg.reply_text(f"Вы забыли выделить кусок текста для {msg.text}")
    me: User = msg.from_user
    ((state, cidd),) = bot.storage.session.state.get(me.id, {None: {}}).items()
    if state == "synonym":
        if typ := SynonymType[msg.text]:
            bot.storage.session.state[me.id][state] |= {typ: msg.quote.text}
            # bot.rm_handler(me.id)
            await models.Synonym.update_or_create({"typ": typ}, txt=msg.quote.text)
            bot.add_handler(CallbackQueryHandler(got_synonym_val, chat(me.id) & private))
            if rm := await btns(typ, msg.quote.text):
                return await msg.reply_text("Уточните", reply_to_message_id=msg.id, reply_markup=rm)
            return await syn_result(bot, msg, f"st:{typ.name}:1")
    elif state:
        ...
    return await msg.reply_text("Не туда попал")


async def got_synonym_val(bot: FillerClient, cbq: CallbackQuery):
    return await syn_result(bot, cbq.message, cbq.data)


async def syn_result(bot: FillerClient, msg: Message, data: str):
    t, st, sv = data.split(":")
    if t == "st":
        typ = SynonymType[st]
        cid = bot.storage.session.state[msg.chat.id]["synonym"]["id"]
        txt = bot.storage.session.state[msg.chat.id]["synonym"][typ]
        val, hval = get_val(typ, sv)
        syn, _ = await models.Synonym.update_or_create({"val": val}, typ=typ, txt=txt)
        await models.CondParsed.update_or_create({typ.name: val}, cond_id=cid)
        await msg.reply_text(
            f'Текст "{txt}" определен как синоним для `{typ.name}` со значением {hval}',
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Готово! Давай новый", f"cond:complete:{cid}"),
                        # , InlineKeyboardButton('Хватит! Я устал', f'cond:complete:{cid}')
                    ]
                ]
            ),
        )
        await wrap_cond(await models.Cond.get(id=cid).values_list("raw_txt", flat=True))
        # await bot.edit_message_text(bot.me.id, msg.reply_to_message.reply_to_message_id, wrapped_txt)
        await msg.reply_to_message.delete()
        await msg.delete()
        await msg.delete()

    elif t == "cond":
        await models.CondParsed.update_or_create({"parsed": True}, cond_id=int(sv))
        await cond_start_handler(bot, msg)
    else:
        await msg.reply_text("Где я?")
