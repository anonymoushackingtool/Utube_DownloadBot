from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Currently only supports Youtube Single  videos(No playlist),Just Send Youtube Url.\n\nlike:http://www.youtube.com/watch?v=6Ojs-T8936g\nOr\nhttps://youtu.be/6Ojs-T8936g\n\nYou can also use ```@vid``` in inline mode to search youtube videos.\nExample: Type \" ```@vid silenceandroidgamer``` \"."
    await message.reply_text(
    text = helptxt,
    disable_web_page_preview=True)
