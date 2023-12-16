from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from AnonX import app


def back_stats_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="TOPMARKUPGET",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl


def overallback_stats_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="GlobalStats",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl


def get_stats_markup(_, status):
    not_sudo = [
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"],
            callback_data="close",
        )
    ]
    sudo = [
        InlineKeyboardButton(
            text=_["G_7_Rr"],
            callback_data="bot_stats_sudo g",
        ),
        InlineKeyboardButton(
            text=_["CLOSEMENU_BUTTON"],
            callback_data="close",
        ),
    ]
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["G_7_Rr"],
                    callback_data="TOPMARKUPGET",
                )
            ],
            [
                InlineKeyboardButton(
                    text=_["G_7_Rr"],
                    url=f"https://t.me/{app.username}?start=stats",
                ),
                InlineKeyboardButton(
                    text=_["G_7_Rr"],
                    callback_data="TopOverall g",
                ),
            ],
            sudo if status else not_sudo,
        ]
    )
    return upl


def stats_buttons(_, status):
    not_sudo = [
        InlineKeyboardButton(
            text=_["G_7_Rr"],
            callback_data="TopOverall s",
        )
    ]
    sudo = [
        InlineKeyboardButton(
            text=_["G_7_Rr"],
            callback_data="bot_stats_sudo s",
        ),
        InlineKeyboardButton(
            text=_["G_7_Rr"],
            callback_data="TopOverall s",
        ),
    ]
    upl = InlineKeyboardMarkup(
        [
            sudo if status else not_sudo,
            [
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl


def back_stats_buttons(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="GETSTATS",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl


def top_ten_stats_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["G_7_Rr"],
                    callback_data="GetStatsNow Tracks",
                ),
                InlineKeyboardButton(
                    text=_["G_7_Rr"],
                    callback_data="GetStatsNow Chats",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["G_7_Rr"],
                    callback_data="GetStatsNow Users",
                ),
                InlineKeyboardButton(
                    text=_["G_7_Rr"],
                    callback_data="GetStatsNow Here",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data="GlobalStats",
                ),
                InlineKeyboardButton(
                    text=_["CLOSE_BUTTON"],
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl
