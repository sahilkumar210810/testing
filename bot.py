import os
import logging
import sys
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes, CallbackQueryHandler

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler('bot.log'),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)

# Get bot token from environment variable (AWS me yahi use hoga)
BOT_TOKEN = os.environ.get('BOT_TOKEN')
if not BOT_TOKEN:
    logger.error("BOT_TOKEN environment variable not set!")
    sys.exit(1)

# /start command handler
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    welcome_message = f"""
👋 Hello {user.first_name}! Welcome to AWS Test Bot!

🤖 **Bot Status:** 🟢 Running on AWS
📍 **Deployment:** AWS Cloud

📌 **Available Commands:**
/start - Start the bot
/help - Get help
/status - Check bot status
/aws - AWS info
/buttons - Test inline buttons
/echo <text> - Echo your message
    """
    
    await update.message.reply_text(welcome_message, parse_mode='Markdown')

# /status command - AWS deployment status
async def status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    import platform
    import datetime
    
    status_text = f"""
📊 **Bot Status Report**

🔹 **Deployment:** AWS Cloud
🔹 **Region:** {os.environ.get('AWS_REGION', 'Not specified')}
🔹 **Environment:** {os.environ.get('ENVIRONMENT', 'production')}
🔹 **Python Version:** {platform.python_version()}
🔹 **Platform:** {platform.platform()}
🔹 **Uptime:** Bot is running smoothly

✅ **All systems operational!**
    """
    
    await update.message.reply_text(status_text, parse_mode='Markdown')

# /aws command - AWS info
async def aws_info(update: Update, context: ContextTypes.DEFAULT_TYPE):
    aws_text = """
☁️ **AWS Deployment Info**

This bot is deployed on:
• **Compute:** AWS EC2 / Elastic Beanstalk
• **Configuration:** Environment variables se token
• **Auto-scaling:** Enabled
• **Monitoring:** CloudWatch logs

**Architecture:**
