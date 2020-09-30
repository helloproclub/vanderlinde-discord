import discord
from discord.ext import commands
import asyncio
import vanderlinde

client = commands.Bot(command_prefix = commands.when_mentioned_or('.'))
client.remove_command('help')
#Event
#Displaying if bot ready
@client.event
async def on_ready():
    print('Bot is ready.')
#Available
@client.event
async def on_command_error(ctx,error):
    if isinstance(error,commands.CommandNotFound):
        await ctx.send('Perintah tidak ada')

@client.event
async def my_background_task():
        await client.wait_until_ready()
        channel = client.get_channel() # channel ID goes here
        text = vanderlinde.count_registration_list()
        while not client.is_closed():
            await channel.send(text)
            await asyncio.sleep(3600) # task runs every 1 hour

#Commands
#Bot latency
@client.command()
async def ping(ctx):
    await ctx.send('Pong! {} ms'.format(round(client.latency * 1000)))

#Help list
@client.command(aliases=['commands'],pass_context=True)
@commands.has_permissions(administrator=True)
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
    embed.add_field(name='.reject <id> <message>', value = 'Rejecting registration', inline=False)
    embed.add_field(name='.invlink <numerator> <satuan waktu>', value = 'Creating invite link just .invilink or seconds = 0 will create permanent invite link', inline=False)

    await author.send(embed=embed)

#Registration list
@client.command(aliases=['registration'])
@commands.has_permissions(administrator=True)
async def registration_list(ctx):
    text = vanderlinde.get_user_by_status('0')
    await ctx.send(text)

#Accepted list
@client.command(aliases=['accepted'])
@commands.has_permissions(administrator=True)
async def accepted_list(ctx):
    text = vanderlinde.get_user_by_status('1')
    await ctx.send(text)

#Rejected list
@client.command(aliases=['rejected'])
@commands.has_permissions(administrator=True)
async def rejected_list(ctx):
    text = vanderlinde.get_user_by_status('2')
    await ctx.send(text)

#Registration detail
@client.command(aliases=['detail'])
@commands.has_permissions(administrator=True)
async def registration_detail(ctx, nim = '0'):
    if(nim == '0'):
        await ctx.send('Masukan id dengan benar')
    else:
        text =vanderlinde.get_user_by_nim(nim)
        print(text)
        await ctx.send(text)

#Accepted
@client.command(aliases=['accept'])
@commands.has_permissions(administrator=True)
async def accept_registration(ctx, nim = '0'):
    if(nim == '0'):
        await ctx.send('mohon isi detail nim')
    else:
        print('oke')
        link = await ctx.channel.create_invite(max_uses = 1)
        await ctx.send(vanderlinde.accept_user_by_nim(nim,link))

#Rejected
@client.command(aliases=['reject'])
@commands.has_permissions(administrator=True)
async def reject_registration(ctx, nim = '0', *,message = ''):
    if(nim == "0" or message != ''):
        await ctx.send('mohon isi detail nim atau pesan')
    else:
        print('oke')
        await ctx.send(vanderlinde.decline_user_by_nim(nim,message))

#Say
@client.command(aliases=['say'])
async def bot_say(ctx, *, word):
    author = ctx.message.author
    await ctx.send(f'{author.mention} says {word}')

#Create invite link
@commands.has_permissions(administrator=True)
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

client.loop.create_task(my_background_task())
client.run('')