from aiogram import Bot,Dispatcher,F
from aiogram.filters import CommandStart,Command
from aiogram.types import Message
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
import asyncio

dp=Dispatcher()

@dp.message(CommandStart())
async def start_handler(msg:Message):
    await msg.answer("Assalomu Alaykum botga xush kelibsiz",reply_markup=inline_menu)

@dp.message(Command("fanlar"))
async def fanlar_handler(msg:Message):
    await msg.answer("Maktab Fanlari Haqida va ",reply_markup=inline_fanlar)

inline_fanlar=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Matematika",callback_data="matematika")],[InlineKeyboardButton(text="Informatika",callback_data="informatika")],
        [InlineKeyboardButton(text="Kimyo",callback_data="kimyo")],[InlineKeyboardButton(text="Biologiya",callback_data="biologiya")],
        [InlineKeyboardButton(text="Geografiya",callback_data="geografiya")],[InlineKeyboardButton(text="Ona tili va Adabiyot",callback_data="adabiyot")],
        [InlineKeyboardButton(text="Tarix",callback_data="tarix")],[InlineKeyboardButton(text="Tarbiya",callback_data="tarbiya")],
        [InlineKeyboardButton(text="Huquq asoslari",callback_data="huquq")],[InlineKeyboardButton(text="Chet tili",callback_data="tili")],
        [InlineKeyboardButton(text="Tasviriy san’at va Musiqa",callback_data="sanat")],[InlineKeyboardButton(text="Jismoniy tarbiya",callback_data="tarbiya")],
        [InlineKeyboardButton(text="Texnologiya",callback_data="texnologiya")]
    ]
)  

@dp.callback_query(F.data=='matematika')
async def btn(call:CallbackQuery):
    await call.message.answer("Dunyoni sonlar va shakllar orqali tushunish, mantiqiy izchillik va muammolarni yechish qobiliyatini rivojlantirish uchun.")
    await call.answer()

@dp.callback_query(F.data=='informatika')
async def btn(call:CallbackQuery):
    await call.message.answer("Texnologiyalar bilan ishlash, dasturlash asoslari va raqamli dunyoda xavfsiz harakatlanishni o'rganish uchun.")
    await call.answer()

@dp.callback_query(F.data=='Fizika')
async def btn(call:CallbackQuery):
    await call.message.answer("Tabiat qonunlari (tortishish, yorug'lik, energiya) va texnika qanday ishlashini tushunish uchun.")
    await call.answer()

@dp.callback_query(F.data=='kimyo')
async def btn(call:CallbackQuery):
    await call.message.answer("Moddalarning tarkibi, ularning o'zgarishi va kundalik hayotdagi (dori-darmon, oziq-ovqat) ahamiyatini bilish uchun.")
    await call.answer()

@dp.callback_query(F.data=='biologiya')
async def btn(call:CallbackQuery):
    await call.message.answer("Tirik organizmlar, inson tanasi va tabiatdagi hayot muvozanatini anglash uchun.")
    await call.answer()

@dp.callback_query(F.data=='geografiya')
async def btn(call:CallbackQuery):
    await call.message.answer("Yer sayyorasining tuzilishi, iqlim, davlatlar va iqtisodiy resurslarni o'rganish uchun.")
    await call.answer()

@dp.callback_query(F.data=='adabiyot')
async def btn(call:CallbackQuery):
    await call.message.answer("O'z fikrini to'g'ri bayon qilish, savodxonlikni oshirish va ma'naviy dunyoni boyitish uchun.")
    await call.answer()

@dp.callback_query(F.data=='tarix')
async def btn(call:CallbackQuery):
    await call.message.answer("O'tmishdagi xatolardan xulosa chiqarish, ajdodlar merosini bilish va kelajakni bashorat qilish uchun.")
    await call.answer()

@dp.callback_query(F.data=='tarbiya')
async def btn(call:CallbackQuery):
    await call.message.answer("Jamiyatda o'zini tutish, odob-axloq qoidalari va qadriyatlarni shakllantirish uchun.")
    await call.answer()

@dp.callback_query(F.data=='huquq')
async def btn(call:CallbackQuery):
    await call.message.answer("Davlat qonunlarini bilish, o'z haq-huquqlarini himoya qila olish uchun.")
    await call.answer()

@dp.callback_query(F.data=='tili')
async def btn(call:CallbackQuery):
    await call.message.answer("Dunyo hamjamiyatiga chiqish, zamonaviy axborotlardan foydalanish va xalqaro muloqot uchun.")
    await call.answer()

@dp.callback_query(F.data=='sanat')
async def btn(call:CallbackQuery):
    await call.message.answer("Ijodiy qobiliyatni rivojlantirish, go'zallikni his qilish va estetik zavq olish uchun.")
    await call.answer()

@dp.callback_query(F.data=='tarbiya')
async def btn(call:CallbackQuery):
    await call.message.answer("Sog'lom turmush tarzi, jismoniy chidamlilik va intizomni shakllantirish uchun.")
    await call.answer()

@dp.callback_query(F.data=='texnologiya')
async def btn(call:CallbackQuery):
    await call.message.answer("Amaliy ko'nikmalar (hunar o'rganish), loyihalash va mehnatsevarlikni o'rganish uchun.")
    await call.answer()

inline_menu=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Inline Tugma",callback_data="inline_tugma")],[InlineKeyboardButton(text="Hech Narsa qilmaydigan tugma",callback_data="tugma")],
        [InlineKeyboardButton(text="Yangiliklar",callback_data="yangilik")],[InlineKeyboardButton(text="Aloqa",callback_data="aloqa")],
    ]
)  

@dp.callback_query(F.data=='inline_tugma')
async def btn(call:CallbackQuery):
    await call.message.answer("Salom, bu inline tugma!")
    await call.answer()

@dp.callback_query(F.data=='tugma')
async def btn(call:CallbackQuery):
    await call.message.answer("Salom, bu odiy tugma!")
    await call.answer()

@dp.callback_query(F.data=='yangilik')
async def btn(call:CallbackQuery):
    await call.message.answer("Bu kunning yangiliklari")
    await call.answer()

@dp.callback_query(F.data=='aloqa')
async def btn(call:CallbackQuery):
    await call.message.answer("Biz bilan bog'laning: example@gmail.com")
    await call.answer()

@dp.message(Command("soroq"))
async def fanlar_handler(msg:Message):
    await msg.answer("Sizga bot yoqdimi?",reply_markup=inline_soroq)

inline_soroq=InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Ha",callback_data="ha")],[InlineKeyboardButton(text="Yo'q",callback_data="yoq")]
    ]
)  

@dp.callback_query(F.data=='ha')
async def btn(call:CallbackQuery):
    await call.message.answer("Rahmat!")
    await call.answer()

@dp.callback_query(F.data=='yoq')
async def btn(call:CallbackQuery):
    await call.message.answer("Xo'p, keyingi safar yaxshiroq bo'lamiz!")
    await call.answer()

async def main():
    bot=Bot(token="8628393530:AAEmRLHTFzLIbQvNsW4dH0xO-SuuTN9n9mk")
    
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())