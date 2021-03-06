import keyboards
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Weather π"),
            KeyboardButton(text="News"),
        ],
        [
            KeyboardButton(text="Vacation with Reddit π€‘"),
            KeyboardButton(text="Text translation π"),
        ],
        [
            KeyboardButton(text="TOP 20 films πΊ"),
            KeyboardButton(text="Rating of films π¦")
        ],
        [
            KeyboardButton(text="Subscriptionπ€"),
            KeyboardButton(text="Close the keyboard π"),
        ]
    ],
    resize_keyboard=True
)


translate_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Translation into Russian (β_β;)"),
            KeyboardButton(text="Translation into English (γ₯οΏ£ Β³οΏ£)γ₯")
        ],
        [
            KeyboardButton(text="Go back to the main menu π")
        ]
    ],
    resize_keyboard=True
)


weather_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Weather β"),
            KeyboardButton(text="Weather for 6 days π"),
        ],

        [
            KeyboardButton(text="Go back to the main menu π")
        ]

    ],
    resize_keyboard=True
)


news_back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Hi-tech news π€"),
            KeyboardButton(text="Latest hi-tech news π£"),
        ],
        [
            KeyboardButton(text="Go back to the main menuπ")
        ]
    ],
    resize_keyboard=True
)


top20_films = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Go back to the main menu π")
        ]
    ],
    resize_keyboard=True
)


film_search = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Rating of films π¦")
        ],
        [
            KeyboardButton(text="Go back to the main menu π")
        ]
    ],
    resize_keyboard=True
)


reddit_main = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Fresh memes πΈ")
        ],
        [
            KeyboardButton(text="Interesting posts π¨βπ»")
        ],
        [
            KeyboardButton(text="Go back to the main menu π")
        ]
    ],
    resize_keyboard=True
)


subscriber_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Subscribe π"),
            KeyboardButton(text="Unsubscribe π"),
        ],
        [
            KeyboardButton(text="Go back to the main menu π")
        ]
    ],
    resize_keyboard=True
)
