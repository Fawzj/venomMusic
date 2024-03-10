import asyncio
from pyrogram import Client, filters
from strings.filters import command
from venomMusic.utils.decorators import AdminActual
from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardMarkup,
    ReplyKeyboardRemove,
    InputMediaPhoto,
    Message,
)
from venomMusic import (Apple, Resso, SoundCloud, Spotify, Telegram, YouTube, app)


REPLY_MESSAGE = "صلي علي النبي وتبسم ♥️✨"




REPLY_MESSAGE_BUTTONS = [
    [
        ("السورس"),
         ("صوره")
    ],
    
    [
        ("العكس"),
        ("احرف")
    ],
    [
        ("مطور السورس"),
        ("مطور البوت")
    ],
   
    [
        ("تويت"),
        ("صراحه")
    ],
    [
        ("الالعاب")
    ],
    [
        ("نكته"),
        ("كتابات")
    ],
    [
        ("اذكار")
    ],
    [
        ("زخارف"),
        ("انصحني")
    ],
    [
        ("يـوتيوب. 📽")
        
    ],
    [
        ("لو خيروك"),
        ("احساب العمر")
    ],    
    [
        ("اخفاء الازرار")
    ]
  
]



  

@app.on_message(filters.regex("^/start"), group=39)
async def cpanel(_, message: Message):             
        text = REPLY_MESSAGE
        reply_markup = ReplyKeyboardMarkup(REPLY_MESSAGE_BUTTONS, resize_keyboard=True, selective=True)
        await message.reply(
              text=text,
              reply_markup=reply_markup
        )

@app.on_message(filters.regex("اخفاء الازرار"))
async def down(client, message):
          m = await message.reply("**تم قفل الكيبورد بنجاح**", reply_markup= ReplyKeyboardRemove(selective=True))


@app.on_message(filters.regex("يـوتيوب. 📽"))
def reply_to_HEY(Client, message):
    message.reply_photo(
        photo=f"https://www7.0zz0.com/2024/02/28/05/415560079.jpg",
        caption=f"""**يتم استخدام هذا الامر لعرض تحميل من اليوتيوب**\n**استخدم الامر بهذا الشكل** `تنزيل` ** او ** `يوتيوب` ** كمثل تنزيل سوره الرحمن اضغط علي الامر لنسخ والاستخدام**""",
        reply_markup=InlineKeyboardMarkup(
            [
            [
                InlineKeyboardButton("𓏺𝗦𝗼𝘂𝗿𝗰𝗲ᯓ𝗩𝗘𝗡𝗢𝗠𖠛", url=f"https://t.me/K_o_c_3"),
            ]
         ]
     )
  )

