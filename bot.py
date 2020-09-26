import discord
from discord.ext import commands

client = commands.Bot(command_prefix = commands.when_mentioned_or('.'))
client.remove_command('help')
#Event
#Displaying if bot ready
@client.event
async def on_ready():
    print('Bot is ready.')

@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandNotFound):
        await ctx.send('Perintah tidak ada')
#Commands
#Bot latency
@client.command()
async def ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms')

#bot call
@client.command(aliases=['vanderlinde'])
async def Vanderlinde(ctx):
    await ctx.send('Gunakan !help untuk melihat commands list')

#Help list
@client.command(aliases=['commands'],pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        colour = discord.Colour.red()
    )

    embed.set_author(name='Help')
    embed.add_field(name='.help', value = 'Bot commands list', inline=False)
    embed.add_field(name='.ping', value = 'Bot latency!', inline=False)
    embed.add_field(name='.registration', value = 'Returns registration list', inline=False)
    embed.add_field(name='.accepted', value = 'Returns accepted list', inline=False)
    embed.add_field(name='.rejected', value = 'Returns rejected list', inline=False)
    embed.add_field(name='.detail <id>', value = 'Registration detail!', inline=False)
    embed.add_field(name='.accept <id>', value = 'Accepting registration', inline=False)
    embed.add_field(name='.reject <id>', value = 'Rejecting registration', inline=False)
    embed.add_field(name='.invlink <numerator> <satuan waktu>', value = 'Creating invite link just .invilink or seconds = 0 will create permanent invite link', inline=False)

    await author.send(embed=embed)
    
#Registration list
@client.command(aliases=['registration'])
async def registration_list(ctx):
    await ctx.send('Vanderlinde')

#Accepted list
@client.command(aliases=['accepted'])
async def accepted_list(ctx):
    await ctx.send('Accepted')

#Rejected list
@client.command(aliases=['rejected'])
async def rejected_list(ctx):
    await ctx.send('Rejected')

#Registration detail
@client.command(aliases=['detail'])
async def registration_detail(ctx, id = "0"):
    if(id == "0"):
        await ctx.send('mohon isi detail id')
    else:
        await ctx.send('yo wassap mafren')

#Accepted
@client.command(aliases=['accept'])
async def accept_registration(ctx, id = "0"):
    if(id == "0"):
        await ctx.send('mohon isi detail id')
    else:
        await ctx.send('aye aye aye aye')

#Rejected
@client.command(aliases=['reject'])
async def reject_registration(ctx, id = "0"):
    if(id == "0"):
        await ctx.send('mohon isi detail id')
    else:
        await ctx.send('muda muda muda muda')

#Say
@client.command(aliases=['say'])
async def bot_say(ctx, *, word):
    author = ctx.message.author
    await ctx.send(f'{author.mention} says {word}')

@client.command(aliases=['invlink'])
async def create_invite(ctx, numerator = 0 , waktu = "detik"):
    if(waktu == "detik" and 0 < numerator < 86400):
        link = await ctx.channel.create_invite(max_age = numerator)
    elif(waktu == "menit" and 0 < numerator <= 1440):
        link = await ctx.channel.create_invite(max_age = numerator * 60)
    elif(waktu == "jam" and 0 < numerator <= 24):
        link = await ctx.channel.create_invite(max_age = numerator * 3600)
    elif(waktu == "hari" and 0 < numerator <= 1):
        link = await ctx.channel.create_invite(max_age = numerator * 86400)
    await ctx.send(link)

client.run('TOKEN')