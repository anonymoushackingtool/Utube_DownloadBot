from pyrogram import Client, Filters


@Client.on_message(Filters.command(["donate"]))
async def start(client, message):
    donatetxt = f"We will update as soon as possible"
    await message.reply_text(donatetxt)

    
