from typing import Union

from pyrogram.types import InlineKeyboardButton
from config import SUPPORT_GROUP


def setting_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="جودة الصوت", callback_data="AQ"
            ),
            InlineKeyboardButton(
                text="جودة الفيديو", callback_data="VQ"
            ),
        ],
        [
            InlineKeyboardButton(
                text="المصادقه", callback_data="AU"
            ),
            InlineKeyboardButton(
                text="وضع التنظيف", callback_data="CM"
            ),
        ],
        [
            InlineKeyboardButton(
                text="⌞𝗦𝗼𝘂𝗥𝗰𝗲 𝗧𝗲𝘁𝗼⌝", url=f"https://t.me/G_7_Rr",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons


def audio_quality_markup(
    _,
    low: Union[bool, str] = None,
    medium: Union[bool, str] = None,
    high: Union[bool, str] = None,
):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["G_7_Rr"].format("➻")
                if low == True
                else _["G_7_Rr"].format(""),
                callback_data="LQA",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["G_7_Rr"].format("➻")
                if medium == True
                else _["G_7_Rr"].format(""),
                callback_data="MQA",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["G_7_Rr"].format("➻")
                if high == True
                else _["G_7_Rr"].format(""),
                callback_data="HQA",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons


def video_quality_markup(
    _,
    low: Union[bool, str] = None,
    medium: Union[bool, str] = None,
    high: Union[bool, str] = None,
):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["G_7_Rr"].format("➻")
                if low == True
                else _["G_7_Rr"].format(""),
                callback_data="LQV",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["G_7_Rr"].format("➻")
                if medium == True
                else _["G_7_Rr"].format(""),
                callback_data="MQV",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["G_7_Rr"].format("➻")
                if high == True
                else _["G_7_Rr"].format(""),
                callback_data="HQV",
            )
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons


def cleanmode_settings_markup(
    _,
    status: Union[bool, str] = None,
    dels: Union[bool, str] = None,
    sug: Union[bool, str] = None,
):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["G_7_Rr"], callback_data="CMANSWER"
            ),
            InlineKeyboardButton(
                text=_["G_7_Rr"] if status == True else _["G_7_Rr"],
                callback_data="CLEANMODE",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["G_7_Rr"], callback_data="COMMANDANSWER"
            ),
            InlineKeyboardButton(
                text=_["G_7_Rr"] if dels == True else _["G_7_Rr"],
                callback_data="COMMANDELMODE",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons


def auth_users_markup(_, status: Union[bool, str] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["G_7_Rr"], callback_data="AUTHANSWER"
            ),
            InlineKeyboardButton(
                text=_["ST_B_16"] if status == True else _["G_7_Rr"],
                callback_data="AUTH",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["G_7_Rr"], callback_data="AUTHLIST"
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons


def playmode_users_markup(
    _,
    Direct: Union[bool, str] = None,
    Group: Union[bool, str] = None,
    Playtype: Union[bool, str] = None,
):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["G_7_Rr"], callback_data="SEARCHANSWER"
            ),
            InlineKeyboardButton(
                text=_["G_7_Rr"] if Direct == True else _["G_7_Rr"],
                callback_data="MODECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["G_7_Rr"], callback_data="AUTHANSWER"
            ),
            InlineKeyboardButton(
                text=_["G_7_Rr"] if Group == True else _["G_7_Rr"],
                callback_data="CHANNELMODECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["G_7_Rr"], callback_data="PLAYTYPEANSWER"
            ),
            InlineKeyboardButton(
                text=_["G_7_Rr"]
                if Playtype == True
                else _["G_7_Rr"],
                callback_data="PLAYTYPECHANGE",
            ),
        ],
        [
            InlineKeyboardButton(
                text=_["BACK_BUTTON"],
                callback_data="settingsback_helper",
            ),
            InlineKeyboardButton(
                text=_["CLOSE_BUTTON"], callback_data="close"
            ),
        ],
    ]
    return buttons
