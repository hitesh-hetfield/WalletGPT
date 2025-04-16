from telegram import Update #envelope which sends all the information to the bot 
from telegram.ext import CommandHandler, ApplicationBuilder, ContextTypes
from blockchainConnect import isConnected, validAddress, getBalance
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN_BOT = os.getenv("TOKEN_BOT")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello send /balance <wallet address> to gett the wallet address")

async def get_balance(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if len(context.args) != 1:
        await update.message.reply_text("Invalid address length")
        return

    walletAddress = context.args[0]

    if not validAddress(walletAddress):
        await update.message.reply_text("Invalid wallet address")
        return    

    await update.message.reply_text(f"Fetching balance for address: {walletAddress}")

    if not isConnected():
        await update.message.reply_text("Web3 connection failed")
        return
    
    try:
        walletBalances = getBalance(walletAddress)
        await update.message.reply_text("\n".join(walletBalances))
    except Exception as e:
        await update.message.reply_text(f"Error: {str(e)}")
                                    


if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN_BOT).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("balance", get_balance))

    print("BOT is running...")
    app.run_polling()