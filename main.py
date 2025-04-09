import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from together import Together
from dotenv import load_dotenv

# تنظیم لاگر
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# بارگذاری متغیرهای محیطی از فایل .env
load_dotenv()

# دریافت توکن‌های مورد نیاز از متغیرهای محیطی
TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
TOGETHER_API_KEY = os.getenv('TOGETHER_API_KEY')

# پیکربندی Together API
client = Together(api_key=TOGETHER_API_KEY)

# پرامپت سیستم برای فرمت‌بندی کد
SYSTEM_PROMPT = """You are a helpful coding assistant specialized in Python. When providing code samples, always do the following:

1. Wrap the code in triple backticks, and immediately after the opening backticks, specify the language (e.g., `python`) to enable proper syntax highlighting.
2. Ensure the code is well-formatted, correctly indented, and free of unnecessary whitespace.
3. The code block should be self-contained so that users can copy and run it directly.
4. Include brief explanations if needed, but keep the code block separate from explanations.

For example, for a simple "Hello World" program, respond like this:
python
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """دستور شروع برای معرفی بات"""
    await update.message.reply_text(
        'سلام! من یک بات هوش مصنوعی برای کمک به کدنویسی هستم. '
        'سوال یا درخواست کد خود را بنویسید تا با استفاده از مدل Llama-4-Maverick-17B به شما کمک کنم.'
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """دستور راهنما"""
    await update.message.reply_text(
        'دستورات موجود:\n'
        '/start - شروع کار با بات\n'
        '/help - نمایش این پیام راهنما\n'
        'هر پیام دیگر به عنوان درخواست به مدل زبانی ارسال می‌شود.'
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """پردازش پیام‌های معمولی و ارسال به مدل زبانی"""
    user_message = update.message.text
    
    # نمایش وضعیت "در حال تایپ" در تلگرام
    await update.message.chat.send_action(action="typing")
    
    try:
        # ارسال درخواست به Together AI
        response = client.chat.completions.create(
            model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_message}
            ]
        )
        
        # دریافت پاسخ
        ai_response = response.choices[0].message.content
        
        # ارسال پاسخ به کاربر
        await update.message.reply_text(ai_response)
        
    except Exception as e:
        logging.error(f"خطا در ارتباط با Together API: {e}")
        await update.message.reply_text(
            'متأسفانه در پردازش درخواست شما مشکلی پیش آمد. لطفاً بعداً دوباره تلاش کنید.'
        )

def main() -> None:
    """راه‌اندازی بات"""
    # ساخت نمونه اپلیکیشن
    application = Application.builder().token(TELEGRAM_TOKEN).build()
    
    # اضافه کردن هندلرها
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    # شروع بات
    application.run_polling()
    
    logging.info("بات شروع به کار کرد.")

if __name__ == "__main__":
    main()