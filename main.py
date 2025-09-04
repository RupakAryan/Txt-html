import os
import requests
import subprocess
import txthtml
from pyromod import listen
from vars import API_ID, API_HASH, BOT_TOKEN, CREDIT
from pyrogram import Client, filters
from pyrogram.types import Message

# Initialize the bot
bot = Client(
    "bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

@bot.on_message(filters.command(["start"]))
async def txt_handler(bot: Client, message: Message):
    def categorize_urls(urls):
    categorized_videos = []
    categorized_pdfs = []
    categorized_others = []

    for url in urls:
        # yaha url ko directly use karna hai, video_url variable galat tha
        new_url = f"https://anonymouspwplayer-b99f57957198.herokuapp.com/pw?url={url}&token=your_working_token"
        categorized_videos.append(new_url)

    return categorized_videos, categorized_pdfs, categorized_others

           
    with open(file_path, "r") as f:
        file_content = f.read()

    urls = txthtml.extract_names_and_urls(file_content)

    videos, pdfs, others = txthtml.categorize_urls(urls)

    html_content = txthtml.generate_html(file_name, videos, pdfs, others)
    html_file_path = file_path.replace(".txt", ".html")
    with open(html_file_path, "w") as f:
        f.write(html_content)

    await message.reply_document(document=html_file_path, caption=f"✅ 𝐒𝐮𝐜𝐜𝐞𝐬𝐬𝐟𝐮𝐥𝐥𝐲 𝐃𝐨𝐧𝐞!\n<blockquote><b>`{file_name}`</b></blockquote>\n❖** Open in Chrome.**❖\n\n🌟**Extracted By : {CREDIT}**")

    os.remove(file_path)
    os.remove(html_file_path)

# Run the bot
if __name__ == "__main__":
    print("Bot is running...")
    bot.run()
