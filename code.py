import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import sys
from core.tokenkey import token

Client = discord.Client()
client = commands.Bot(command_prefix="$")

@client.event
async def on_ready():
    print("AltShop Bot is connected to Discord and Online!")
    await client.change_presence(game=discord.Game(name="By Slay >>", type=1))

@client.event
async def on_message(message):
    if message.content.upper().startswith("$VERIFY"):
        embed = discord.Embed(title="Welcome to the AltShop Discord:", description="This is the Discord Server for https://selly.gg/@Hackerable.", color=0x8000ff)
        embed.add_field(name="To Verify yourself:", value="React to this message with <:verify:430062882810757121> to access channels.")
        embed.set_thumbnail(url="https://imgur.com/uRRe1LC.png")
        await client.send_message(message.channel, embed=embed)
        await client.delete_message(message)
    if message.content.upper().startswith("$INFORMATION"):
        embed = discord.Embed(title="AltShop Discord Information", description="In this discord you can buy and sell alternate accounts, as well as leave feedback", color=0x8000ff)
        embed.add_field(name="Spotify Premium", value="Spotify Premium Accounts are priced at: 50pence / 70cents")
        embed.add_field(name="WWE Premium", value="WWE Premium Accounts are priced at: £1 / $1.40 ")
        embed.set_thumbnail(url="https://imgur.com/uRRe1LC.png")
        embed.set_footer(text="This is the list of current accounts. There will be more to be added.")
        await client.send_message(message.channel, embed=embed)
        await client.delete_message(message)
    if message.content.upper().startswith("$SELLYINFO"):
        embed = discord.Embed(title="AltShop Selly Information", description="", color=0x8000ff)
        embed.add_field(name="Selly Link:", value="https://selly.gg/@Hackerable")
        embed.add_field(name="Selly Admins:", value="@Violence#0004 (@Hackerable) | & | @Slay#0527 (@OverflowEIP)")
        embed.set_footer(text="Anyone else claiming to be an Admin on the Selly please report to us.")
        embed.set_thumbnail(url="https://imgur.com/uRRe1LC.png")
        await client.send_message(message.channel, embed=embed)
        await client.delete_message(message)
    if message.content.upper().startswith("$CHANNELINFO"):
        embed = discord.Embed(title="AltShop Discord Channel Information", description="", color=0x8000ff)
        embed.add_field(name="#information", value="The channel you are in right now. Displays all info about the AltShop.")
        embed.add_field(name="#news", value="Where all new stock of the AltShop is documented.")
        embed.add_field(name="#feedback", value="Leave feedback from previous purchases with us.")
        embed.add_field(name="#replacement-accs", value="If you are in need of a replacement ask the Administrators.")
        embed.add_field(name="#general", value="Talk about anything and everything. Don't break Discord TOS though.")
        embed.add_field(name="#marketplace", value="Buy and sell your own items within the Discord Server.")
        embed.set_thumbnail(url="https://imgur.com/uRRe1LC.png")
        embed.set_footer(text="This message will be edited if more channels are added and vice versa.")
        await client.send_message(message.channel, embed=embed)
        await client.delete_message(message)
    if message.content.upper().startswith("$NEWS"):
        embed = discord.Embed(title="AltShop Discord News", description="This is where the latest stock will be documented.", color=0x8000ff)
        embed.set_thumbnail(url="https/imgur.com/uRRe1LC.png")
        await client.send_message(message.channel, embed=embed)
        await client.delete_message(message)
    if message.content.upper().startswith("$FEEDBACK"):
        embed = discord.Embed(title="Leave your feedback here!", description="", color=0x8000ff)
        embed.add_field(name="Positive Feedback:", value="If we have fulfilled your needs, leave some positive feedback.")
        embed.add_field(name="Negative Feedback:", value="If we have failed to fulfill your needs, leave some negative feedback, and we can fix it.")
        embed.set_thumbnail(url="https://imgur.com/uRRe1LC.png")
        embed.set_footer(text="All forms of feedback are appreciated")
        await client.send_message(message.channel, embed=embed)
        await client.delete_message(message)
    if message.content.upper().startswith("$REPLACEMENTS"):
        embed = discord.Embed(title="AltShop Replacement Information:", description="You will only be in here if you are in need of a replacement account and have the 'Replacement' Role.", color=0x8000ff)
        embed.add_field(name="Requirements:", value="To be issued a replacement account you must have concrete evidence you are locked out/have been locked out of your purchased account.")
        embed.set_thumbnail(url="https://imgur.com/uRRe1LC.png")
        embed.set_footer(text="If you are here by mistake, contact @Slay#0527 or @Violence#0004 and we will remove the role from your account.")
        await client.send_message(message.channel, embed=embed)
        await client.delete_message(message)
    if message.content.upper().startswith("$MARKETPLACE"):
        embed = discord.Embed(tite="AltShop Discord Marketplace", description="Here you can buy and sell your own accounts.", color=0x8000ff)
        embed.add_field(name="Selling/Buying Format:", value="https://pastebin.com/SQYHVeW4")
        embed.set_thumbnail(url="https://imgur.com/uRRe1LC.png")
        await client.send_message(message.channel, embed=embed)
        await client.delete_message(message)
    if message.content.upper().startswith("$SPOTIFYSALES"):
        embed = discord.Embed(title="932x Spotify Premium Accounts:", description="We have stocked up on Spotify Premium, and are selling them for 50pence / 70 cents.", color=0x8000ff)
        embed.add_field(name="AltShop Selly Link", value="https://selly.gg/@Hackerable")
        embed.set_thumbnail(url="https://imgur.com/fICb174.png")
        embed.set_footer(text="This price may change. Keep an eye out for @.everyone's")
        await client.send_message(message.channel, embed=embed)
        await client.delete_message(message)
    if message.content.upper().startswith("$WWESALES"):
        embed = discord.Embed(title="129x WWE Premium Accounts", description="We have stocked up on WWE Premium Accounts, and are selling them for £1 / $1.40", color=0x8000ff)
        embed.add_field(name="AltShop Selly Link", value="https://selly.gg/@Hackerable")
        embed.set_thumbnail(url="https://imgur.com/BPZjb61.png")
        embed.set_footer(text="This price may change. Keep an eye out for @.everyone's.")
        await client.send_message(message.channel, embed=embed)
        await client.delete_message(message)
    if message.content.upper().startswith("$HMAVPNSALES"):
        embed = discord.Embed(title="11x HideMyAss VPN Accounts:", description="We have stocked up on HideMyAss VPN Accounts, and are selling them for £1.50 / $2.10", color=0x8000ff)
        embed.add_field(name="AltShop Selly Link:", value="https://selly.gg/@Hackerable")
        embed.set_thumbnail(url="https://imgur.com/110eUvs.png")
        embed.set_footer(text="This price may change. Keep an eye out for @.everyone's")
        await client.send_message(message.channel, embed=embed)
        await client.delete_message(message)
    if message.content.upper().startswith("$HBOLIVESALES"):
        embed = discord.Embed(title="179x HBOVideo Accounts:", description="We have stocked up on HBOVideo Accounts, and are selling them for £1 / $1.40", color=0x8000ff)
        embed.add_field(name="AltShop Selly Link:", value="https://selly.gg/@Hackerable")
        embed.set_thumbnail(url="https://imgur.com/mcxv8IY.png")
        embed.set_footer(text="This price may change. Keep an eye out for @.everyone's")
        await client.send_message(message.channel, embed=embed)
        await client.delete_message(message)


client.run(token, reconnect=True)
        
        
        
