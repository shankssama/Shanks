import html
import random
import time

from telegram import ChatPermissions, ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, Filters
from telegram.utils.helpers import escape_markdown

import YamatoRobot.modules.fun_strings as fun_strings
from YamatoRobot import REDLIONS, SPRYZONS, dispatcher
from YamatoRobot.modules.disable import (
    DisableAbleCommandHandler,
    DisableAbleMessageHandler,
)
from YamatoRobot.modules.helper_funcs.alternate import typing_action
from YamatoRobot.modules.helper_funcs.chat_status import is_user_admin
from YamatoRobot.modules.helper_funcs.extraction import extract_user

GIF_ID = "CgACAgQAAx0CSVUvGgAC7KpfWxMrgGyQs-GUUJgt-TSO8cOIDgACaAgAAlZD0VHT3Zynpr5nGxsE"


def runs(update: Update, context: CallbackContext):
    update.effective_message.reply_text(random.choice(fun_strings.RUN_STRINGS))


def sanitize(update: Update, context: CallbackContext):
    message = update.effective_message
    name = (
        message.reply_to_message.from_user.first_name
        if message.reply_to_message
        else message.from_user.first_name
    )
    reply_animation = (
        message.reply_to_message.reply_animation
        if message.reply_to_message
        else message.reply_animation
    )
    reply_animation(GIF_ID, caption=f"*Sanitizes {name}*")


def sanitize(update: Update, context: CallbackContext):
    message = update.effective_message
    name = (
        message.reply_to_message.from_user.first_name
        if message.reply_to_message
        else message.from_user.first_name
    )
    reply_animation = (
        message.reply_to_message.reply_animation
        if message.reply_to_message
        else message.reply_animation
    )
    reply_animation(random.choice(fun_strings.GIFS), caption=f"*Sanitizes {name}*")


def slap(update: Update, context: CallbackContext):
    bot, args = context.bot, context.args
    message = update.effective_message
    chat = update.effective_chat

    reply_text = (
        message.reply_to_message.reply_text
        if message.reply_to_message
        else message.reply_text
    )

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id == bot.id:
        temp = random.choice(fun_strings.SLAP_SHASA_TEMPLATES)

        if isinstance(temp, list):
            if temp[2] == "tmute":
                if is_user_admin(chat, message.from_user.id):
                    reply_text(temp[1])
                    return

                mutetime = int(time.time() + 60)
                bot.restrict_chat_member(
                    chat.id,
                    message.from_user.id,
                    until_date=mutetime,
                    permissions=ChatPermissions(can_send_messages=False),
                )
            reply_text(temp[0])
        else:
            reply_text(temp)
        return

    if user_id:

        slapped_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(slapped_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    temp = random.choice(fun_strings.SLAP_TEMPLATES)
    item = random.choice(fun_strings.ITEMS)
    hit = random.choice(fun_strings.HIT)
    throw = random.choice(fun_strings.THROW)

    if update.effective_user.id == 1415798813:
        temp = "@NeoTheKitty scratches {user2}"

    reply = temp.format(user1=user1, user2=user2, item=item, hits=hit, throws=throw)

    reply_text(reply, parse_mode=ParseMode.HTML)


def pat(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    message = update.effective_message

    reply_to = message.reply_to_message if message.reply_to_message else message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        patted_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(patted_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    pat_type = random.choice(("Text", "Gif", "Sticker"))
    if pat_type == "Gif":
        try:
            temp = random.choice(fun_strings.PAT_GIFS)
            reply_to.reply_animation(temp)
        except BadRequest:
            pat_type = "Text"

    if pat_type == "Sticker":
        try:
            temp = random.choice(fun_strings.PAT_STICKERS)
            reply_to.reply_sticker(temp)
        except BadRequest:
            pat_type = "Text"

    if pat_type == "Text":
        temp = random.choice(fun_strings.PAT_TEMPLATES)
        reply = temp.format(user1=user1, user2=user2)
        reply_to.reply_text(reply, parse_mode=ParseMode.HTML)


def roll(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(range(1, 7)))


def shout(update: Update, context: CallbackContext):
    args = context.args
    text = " ".join(args)
    result = []
    result.append(" ".join(list(text)))
    for pos, symbol in enumerate(text[1:]):
        result.append(symbol + " " + "  " * pos + symbol)
    result = list("\n".join(result))
    result[0] = text[0]
    result = "".join(result)
    msg = "```\n" + result + "```"
    return update.effective_message.reply_text(msg, parse_mode="MARKDOWN")


def toss(update: Update, context: CallbackContext):
    update.message.reply_text(random.choice(fun_strings.TOSS))


def shrug(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(r"¯\_(ツ)_/¯")


def bluetext(update: Update, context: CallbackContext):
    msg = update.effective_message
    reply_text = (
        msg.reply_to_message.reply_text if msg.reply_to_message else msg.reply_text
    )
    reply_text(
        "/BLUE /TEXT\n/MUST /CLICK\n/I /AM /A /STUPID /ANIMAL /THAT /IS /ATTRACTED /TO /COLORS"
    )


def rlg(update: Update, context: CallbackContext):
    eyes = random.choice(fun_strings.EYES)
    mouth = random.choice(fun_strings.MOUTHS)
    ears = random.choice(fun_strings.EARS)

    if len(eyes) == 2:
        repl = ears[0] + eyes[0] + mouth[0] + eyes[1] + ears[1]
    else:
        repl = ears[0] + eyes[0] + mouth[0] + eyes[0] + ears[1]
    update.message.reply_text(repl)


def decide(update: Update, context: CallbackContext):
    reply_text = (
        update.effective_message.reply_to_message.reply_text
        if update.effective_message.reply_to_message
        else update.effective_message.reply_text
    )
    reply_text(random.choice(fun_strings.DECIDE))


def eightball(update: Update, context: CallbackContext):
    reply_text = (
        update.effective_message.reply_to_message.reply_text
        if update.effective_message.reply_to_message
        else update.effective_message.reply_text
    )
    reply_text(random.choice(fun_strings.EIGHTBALL))


def table(update: Update, context: CallbackContext):
    reply_text = (
        update.effective_message.reply_to_message.reply_text
        if update.effective_message.reply_to_message
        else update.effective_message.reply_text
    )
    reply_text(random.choice(fun_strings.TABLE))


normiefont = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
weebyfont = [
    "卂",
    "乃",
    "匚",
    "刀",
    "乇",
    "下",
    "厶",
    "卄",
    "工",
    "丁",
    "长",
    "乚",
    "从",
    "𠘨",
    "口",
    "尸",
    "㔿",
    "尺",
    "丂",
    "丅",
    "凵",
    "リ",
    "山",
    "乂",
    "丫",
    "乙",
]


def weebify(update: Update, context: CallbackContext):
    args = context.args
    message = update.effective_message
    string = ""

    if message.reply_to_message:
        string = message.reply_to_message.text.lower().replace(" ", "  ")

    if args:
        string = "  ".join(args).lower()

    if not string:
        message.reply_text("Usage is `/weebify <text>`", parse_mode=ParseMode.MARKDOWN)
        return

    for normiecharacter in string:
        if normiecharacter in normiefont:
            weebycharacter = weebyfont[normiefont.index(normiecharacter)]
            string = string.replace(normiecharacter, weebycharacter)

    if message.reply_to_message:
        message.reply_to_message.reply_text(string)
    else:
        message.reply_text(string)


def flirt(update: Update, context: CallbackContext):
    reply_text = (
        update.effective_message.reply_to_message.reply_text
        if update.effective_message.reply_to_message
        else update.effective_message.reply_text
    )
    reply_text(random.choice(fun_strings.FLIRT_TEXT))


def romance(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    message = update.effective_message

    reply_to = message.reply_to_message or message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        romantic_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(romantic_user.first_name)

    else:
        user1 = bot.first_name
        user2 = curr_user

    romance_type = random.choice(("Text", "Gif", "Sticker"))
    if romance_type == "Gif":
        try:
            temp = random.choice(fun_strings.ROMANCE_GIFS)
            reply_to.reply_animation(temp)
        except BadRequest:
            romance_type = "Text"

    if romance_type == "Sticker":
        try:
            temp = random.choice(fun_strings.ROMANCE_STICKERS)
            reply_to.reply_sticker(temp)
        except BadRequest:
            romance_type = "Text"

    if romance_type == "Text":
        temp = random.choice(fun_strings.ROMANCE_TEMPLATES)
        reply = temp.format(user1=user1, user2=user2)
        reply_to.reply_text(reply, parse_mode=ParseMode.HTML)


@typing_action
def goodnight(update, context):
    message = update.effective_message
    first_name = update.effective_user.first_name
    reply = f"Good Night! {escape_markdown(first_name)}"
    message.reply_text(reply, parse_mode=ParseMode.MARKDOWN)


@typing_action
def goodmorning(update, context):
    message = update.effective_message
    first_name = update.effective_user.first_name
    reply = f"Good Morning! {escape_markdown(first_name)}"
    message.reply_text(reply, parse_mode=ParseMode.MARKDOWN)


def owo(update: Update, context: CallbackContext):
    bot = context.bot
    args = context.args
    message = update.effective_message

    reply_to = message.reply_to_message or message

    html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        owo_user = bot.get_chat(user_id)
        html.escape(owo_user.first_name)

    else:
        bot.first_name

    owo_type = random.choice(("Gif", "Sticker"))
    if owo_type == "Gif":
        try:
            temp = random.choice(fun_strings.OWO_GIFS)
            reply_to.reply_animation(temp)
        except BadRequest:
            owo_type = "Text"

    if owo_type == "Sticker":
        try:
            temp = random.choice(fun_strings.OWO_STICKERS)
            reply_to.reply_sticker(temp)
        except BadRequest:
            owo_type = "Text"


def gbun(update, context):
    user = update.effective_user
    chat = update.effective_chat

    if update.effective_message.chat.type == "private":
        return
    if int(user.id) in REDLIONS or int(user.id) in SPRYZONS:
        context.bot.sendMessage(chat.id, (random.choice(fun_strings.GBUN)))


def gbam(update, context):
    user = update.effective_user
    chat = update.effective_chat
    bot, args = context.bot, context.args
    message = update.effective_message

    curr_user = html.escape(message.from_user.first_name)
    user_id = extract_user(message, args)

    if user_id:
        gbam_user = bot.get_chat(user_id)
        user1 = curr_user
        user2 = html.escape(gbam_user.first_name)

    else:
        user1 = curr_user
        user2 = bot.first_name

    if update.effective_message.chat.type == "private":
        return
    if int(user.id) in REDLIONS or int(user.id) in SPRYZONS:
        gbamm = fun_strings.GBAM
        reason = random.choice(fun_strings.GBAM_REASON)
        gbam = gbamm.format(user1=user1, user2=user2, chatid=chat.id, reason=reason)
        context.bot.sendMessage(chat.id, gbam, parse_mode=ParseMode.HTML)


__help__ = """
 |• `/runs`*:* reply a random string from an array of replies
 |• `/slap`*:* slap a user, or get slapped if not a reply
 |• `/shrug`*:* get shrug XD
 |• `/table`*:* get flip/unflip :v
 |• `/decide`*:* Randomly answers yes/no/maybe
 |• `/toss`*:* Tosses A coin
 |• `/bluetext`*:* check urself :V
 |• `/roll`*:* Roll a dice
 |• `/rlg`*:* Join ears,nose,mouth and create an emo ;-;
 |• `/shout` <keyword>*:* write anything you want to give loud shout
 |• `/weebify` <text>*:* returns a weebified text
 |• `/sanitize`*:* always use this before /pat or any contact
 |• `/pat`*:* pats a user, or get patted
 |• `/8ball`*:* predicts using 8ball method 
*Play Game With Emojis:* 
 |• `/dice` 1 to 6 any value
 |• `/ball` 1 to 5 any value
 |• `/dart` 1 to 6 any value

 |• `/flirt` : chk out
 |• `/romance` : chk out
"""

SANITIZE_HANDLER = DisableAbleCommandHandler("sanitize", sanitize, run_async=True)
RUNS_HANDLER = DisableAbleCommandHandler("runs", runs, run_async=True)
SLAP_HANDLER = DisableAbleCommandHandler("slap", slap, run_async=True)
PAT_HANDLER = DisableAbleCommandHandler("pat", pat)
ROLL_HANDLER = DisableAbleCommandHandler("roll", roll, run_async=True)
TOSS_HANDLER = DisableAbleCommandHandler("toss", toss, run_async=True)
SHRUG_HANDLER = DisableAbleCommandHandler("shrug", shrug, run_async=True)
BLUETEXT_HANDLER = DisableAbleCommandHandler("bluetext", bluetext, run_async=True)
RLG_HANDLER = DisableAbleCommandHandler("rlg", rlg, run_async=True)
DECIDE_HANDLER = DisableAbleCommandHandler("decide", decide, run_async=True)
EIGHTBALL_HANDLER = DisableAbleCommandHandler("8ball", eightball, run_async=True)
TABLE_HANDLER = DisableAbleCommandHandler("table", table, run_async=True)
SHOUT_HANDLER = DisableAbleCommandHandler("shout", shout, run_async=True)
WEEBIFY_HANDLER = DisableAbleCommandHandler("weebify", weebify, run_async=True)
OWO_HANDLER = DisableAbleCommandHandler("owo", owo, run_async=True)
GDMORNING_HANDLER = DisableAbleMessageHandler(
    Filters.regex(r"(?i)(goodmorning|good morning)"),
    goodmorning,
    friendly="goodmorning",
    run_async=True,
)
GDNIGHT_HANDLER = DisableAbleMessageHandler(
    Filters.regex(r"(?i)(goodnight|good night)"),
    goodnight,
    friendly="goodnight",
    run_async=True,
)
FLIRT_HANDLER = DisableAbleCommandHandler("flirt", flirt, run_async=True)
ROMANCE_HANDLER = DisableAbleCommandHandler("romance", romance, run_async=True)
GBUN_HANDLER = DisableAbleCommandHandler("gbun", gbun, run_async=True)
GBAM_HANDLER = DisableAbleCommandHandler("gbam", gbam, run_async=True)

dispatcher.add_handler(WEEBIFY_HANDLER)
dispatcher.add_handler(SHOUT_HANDLER)
dispatcher.add_handler(SANITIZE_HANDLER)
dispatcher.add_handler(RUNS_HANDLER)
dispatcher.add_handler(SLAP_HANDLER)
dispatcher.add_handler(PAT_HANDLER)
dispatcher.add_handler(ROLL_HANDLER)
dispatcher.add_handler(TOSS_HANDLER)
dispatcher.add_handler(SHRUG_HANDLER)
dispatcher.add_handler(BLUETEXT_HANDLER)
dispatcher.add_handler(RLG_HANDLER)
dispatcher.add_handler(DECIDE_HANDLER)
dispatcher.add_handler(EIGHTBALL_HANDLER)
dispatcher.add_handler(TABLE_HANDLER)
dispatcher.add_handler(FLIRT_HANDLER)
dispatcher.add_handler(ROMANCE_HANDLER)
dispatcher.add_handler(OWO_HANDLER)
dispatcher.add_handler(GDMORNING_HANDLER)
dispatcher.add_handler(GDNIGHT_HANDLER)
dispatcher.add_handler(GBAM_HANDLER)
dispatcher.add_handler(GBUN_HANDLER)

__mod_name__ = "Fᴜɴ"
__command_list__ = [
    "runs",
    "slap",
    "roll",
    "toss",
    "shrug",
    "bluetext",
    "rlg",
    "decide",
    "table",
    "pat",
    "sanitize",
    "shout",
    "weebify",
    "8ball",
    "flirt",
    "romance",
    "owo",
    "gbun",
    "gbam",
]
__handlers__ = [
    RUNS_HANDLER,
    SLAP_HANDLER,
    PAT_HANDLER,
    ROLL_HANDLER,
    TOSS_HANDLER,
    SHRUG_HANDLER,
    BLUETEXT_HANDLER,
    RLG_HANDLER,
    DECIDE_HANDLER,
    TABLE_HANDLER,
    SANITIZE_HANDLER,
    SHOUT_HANDLER,
    WEEBIFY_HANDLER,
    EIGHTBALL_HANDLER,
    FLIRT_HANDLER,
    ROMANCE_HANDLER,
    OWO_HANDLER,
    GDMORNING_HANDLER,
    GDNIGHT_HANDLER,
    GBUN_HANDLER,
    GBAM_HANDLER,
]
