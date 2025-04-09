# DeepCoder Telegram Chat Bot

## توضیحات فارسی

### درباره مدل DeepCoder (DeepCoder) یک مدل زبانی هوش مصنوعی اوپن‌سورس (Open-Source) جدید با ۱۴ میلیارد پارامتر است که برای استدلال (Reasoning) و تولید کد (Code Generation) بهینه‌سازی شده است. این مدل با استفاده از روش تقویتی توزیع‌شده (Distributed RL) روی مدل پایه Deepseek-R1-Distilled-Qwen-14B (Deepseek-R1-Distilled-Qwen-14B) فاین‌تیون (Fine-Tuned) شده است.

#### ویژگی‌های کلیدی:
- **عملکرد برجسته**: در بنچمارک LiveCodeBench به دقت ۶۰.۶٪ Pass@1 رسیده است که ۸٪ بهتر از مدل پایه عمل می‌کند.
- **رقابتی با مدل‌های انحصاری**: عملکرد مشابه با مدل‌های انحصاری مانند o3-mini-2025-01-031 (Low) و o1-2024-12-17 دارد.
- **کاملاً اوپن‌سورس**: تمام دیتاست، کدها، لاگ‌های آموزشی و بهینه‌سازی‌های سیستمی که برای آموزش مدل استفاده شده است، به صورت اوپن‌سورس منتشر شده‌اند.

### درباره بات تلگرام
این بات تلگرام به کاربران امکان می‌دهد تا با استفاده از مدل زبانی Llama-4-Maverick-17B-128E-Instruct-FP8 برای نوشتن، تصحیح و بهبود کد کمک بگیرند. بات به گونه‌ای طراحی شده که کدها را به صورت خوانا و قالب‌بندی شده در تلگرام نمایش می‌دهد.

#### قابلیت‌ها:
- تولید کد براساس توضیحات و درخواست‌های کاربر
- دیباگ و عیب‌یابی کد
- بهینه‌سازی کدهای موجود
- پاسخگویی به سوالات برنامه‌نویسی
- نمایش کد در قالب‌بندی مناسب در محیط تلگرام

### نصب و راه‌اندازی

#### پیش‌نیازها:
- Python 3.8 یا بالاتر
- دسترسی به API تلگرام (توکن بات)
- دسترسی به Together AI API

#### مراحل نصب:
1. مخزن را کلون کنید:
```
git clone https://github.com/yourusername/deepcoder-telegram-bot.git
cd deepcoder-telegram-bot
```

2. وابستگی‌ها را نصب کنید:
```
pip install -r requirements.txt
```

3. فایل `.env` را با اطلاعات مربوط به توکن‌های خود پیکربندی کنید:
```
TELEGRAM_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
TOGETHER_API_KEY=YOUR_TOGETHER_API_KEY
```

4. بات را اجرا کنید:
```
python telegram_bot.py
```

#### دستورات بات:
- `/start` - شروع کار با بات
- `/help` - نمایش پیام راهنما
- هر پیام دیگر به عنوان درخواست به مدل زبانی ارسال می‌شود

---

## English Description

### About DeepCoder Model
DeepCoder is a new open-source language model with 14 billion parameters optimized for code reasoning and generation. This model has been fine-tuned using distributed Reinforcement Learning (RL) on the base model Deepseek-R1-Distilled-Qwen-14B.

#### Key Features:
- **Outstanding Performance**: Achieved 60.6% Pass@1 accuracy on the LiveCodeBench benchmark, performing 8% better than the base model.
- **Competitive with Proprietary Models**: Performs similarly to proprietary models like o3-mini-2025-01-031 (Low) and o1-2024-12-17.
- **Fully Open-Source**: All datasets, codes, training logs, and system optimizations used for training the model are released as open-source.

### About the Telegram Bot
This Telegram bot allows users to leverage the Llama-4-Maverick-17B-128E-Instruct-FP8 language model for writing, correcting, and improving code. The bot is designed to display code in a readable and well-formatted manner in Telegram.

#### Capabilities:
- Generate code based on user descriptions and requests
- Debug and troubleshoot code
- Optimize existing code
- Answer programming questions
- Display code in proper formatting in the Telegram environment

### Installation and Setup

#### Prerequisites:
- Python 3.8 or higher
- Access to Telegram API (bot token)
- Access to Together AI API

#### Installation Steps:
1. Clone the repository:
```
git clone https://github.com/yourusername/deepcoder-telegram-bot.git
cd deepcoder-telegram-bot
```

2. Install dependencies:
```
pip install -r requirements.txt
```

3. Configure the `.env` file with your token information:
```
TELEGRAM_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
TOGETHER_API_KEY=YOUR_TOGETHER_API_KEY
```

4. Run the bot:
```
python telegram_bot.py
```

#### Bot Commands:
- `/start` - Start using the bot
- `/help` - Display help message
- Any other message is sent as a request to the language model
