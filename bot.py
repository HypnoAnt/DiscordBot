#Bot.py
import discord
import asyncio
import chess as cs
import chess.svg
import os
from cairosvg import svg2png
from discord.ext import commands
from discord import FFmpegPCMAudio
from discord import FFmpegPCMAudio
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')
MARK = os.getenv('MARK')

intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix = '.' , intents = intents )
board = cs.Board()
rook = cs.svg.board(board)
f = open("Test.svg","a")
f.write(rook)
f.close()



@client.event
async def on_ready():
    print("Bot ONLINE")
    print("-----------------------")

@client.command()
async def hello(ctx):
    await ctx.send("I am the ServerManager")

@client.command(pass_content = True)
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('OhhHiMarkCut.mp3')
        player = voice.play(source)
    else:
        await ctx.send("Join a voice channel")

@client.command(pass_content = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("I left")

@client.command(pass_content = True)
async def gavgav(ctx):
    await ctx.send(file=discord.File('gavgav.png'))

@client.command(pass_content = True)
async def chess(ctx,arg1="",arg2=""):
    if arg1 == "move":
        if board.parse_san(arg2) in board.legal_moves:
            board.push_san(arg2)
            if board.is_stalemate() or board.is_insufficient_material() or board.is_seventyfive_moves()  or board.is_repetition(3):
                await ctx.send("DRAW")
            if board.is_checkmate():
                await ctx.send("Checkmate")
    if arg1 == "reset":
        board.reset()
    boardImage = cs.svg.board(board)
    svg2png(bytestring=boardImage,write_to='output.png')
    await ctx.send(file=discord.File("output.png"))
    os.remove("output.png")


@client.event
async def on_voice_state_update(member,before,after):
    if member.name == MARK:
        channel = member.voice.channel
        if before.channel is None or before.channel is not after.channel:
            voice = await channel.connect()
            source = FFmpegPCMAudio('OhhHiMarkCut.mp3')
            player = voice.play(source)
            await asyncio.sleep(1)
            await voice.disconnect()

client.run(TOKEN)