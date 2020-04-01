import asyncio
import random
import os

import discord
from discord import Member, Guild, guild, reaction


client = discord.Client()


token = int(os.environ.get('token')

            
@client.event
async def on_ready():
    print('{} ist ready, Diggah!'.format(client.user.name))
    client.loop.create_task(status_task()

                            
antworten = ['Jo', 'Nö', 'Du bist einfach zu dumm, da kann ich keine Antwort nennen.', 'Woher soll ich das wissen?',
             'Nur, wenn Du ganz fest dran glaubst...', 'Was, worum gehts? War grad meinen Darm entleeren.',
             'Guck mal, ein Einhorn!',
             'Was hat ein Rabe gemeinsam? Genau, beide Beine sind gleich lang, besonders das Rechte']


smalltalk = ['Ja ich weiß, ist nicht ganz so aktuell, aber Gott halt will kein Whatsapp, \r\n'
             'er hat zu viel Angst um seine Daten.',
             'Ah, er hat zurück geschrieben: \r\n'
             '`Die Möhre im Bettchen wieder flotter machen! Jetzt unter www.kaufdirbilligpenispumpen.de` \r\n'
             'huch, war die falsche']


)


async def status_task():
    while True:
        await client.change_presence(activity=discord.Game('von Jesus a.k.a. Finn'), status=discord.Status.online)
        await asyncio.sleep(5)
        await client.change_presence(activity=discord.Game('!inkompetenz'), status=discord.Status.online)
        await asyncio.sleep(3)
        await client.change_presence(activity=discord.Game('für Optionen...'), status=discord.Status.online)
        await asyncio.sleep(3)


@client.event
async def on_message(message):
    if message.author.bot:
        return
    if '!inkompetenz' in message.content:
        kanye = message.author.name
        embed = discord.Embed(title='Zu inkompetent mich zu bedienen?',
                              description='Leude, {} ist mal wieder für alles zu dumm :joy: !'.format(kanye),
                              color=0xf1c40f)
        embed.add_field(name='!inkompetenz', value='Zeigt, wie geil ich programmiert bin!',
                        inline=False)
        embed.add_field(name='!ausweisbidde + Name', value='Zeigt intimste Geheimnisse der gewünschten Person!',
                        inline=False)
        embed.add_field(name='!steinigung + Name + Grund',
                        value='Lässt die Gerechtigkeit siegen! (oder Ardalan)',
                        inline=False)
        embed.add_field(name='!prophet + Frage', value='Ich frage den Herrn nach einer Antwort...',
                        inline=False)
        embed.add_field(name='!randommeme', value='Spielt ein Random Meme ab!',
                        inline=False)
        embed.set_footer(text='Es könnte auch sein, dass es noch mehr Funktionen gibt, \r\n'
                              'aber Finn es mal wieder verpennt hat, die hier dazu zu schreiben...')
        await message.channel.send(embed=embed)
    if message.content.startswith('!ausweisbidde'):
        args = message.content.split(' ')
        if len(args) == 2:
            member: Member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
            if member:
                embed = discord.Embed(title='Ausweis von {}'.format(member.name),
                                      description='Dies ist definitiv der offizielle Ausweis von {}'.format(
                                          member.mention),
                                      color=0x1ecc01)
                embed.add_field(name='Server beigetreten', value=member.joined_at.strftime('%d/%m/%Y, %H:%M:%S'),
                                inline=True)
                embed.add_field(name='Discord beigetreten', value=member.created_at.strftime('%d/%m/%Y, %H:%M:%S'),
                                inline=True)
                rollen = ''
                for role in member.roles:
                    if not role.is_default():
                        rollen += '{} \r\n'.format(role.mention)
                if rollen:
                    embed.add_field(name='Rollen', value=rollen, inline=True)
                embed.set_thumbnail(url=member.avatar_url)
                embed.set_footer(text='Angaben wie immer ohne Gewähr...')
                mess = await message.channel.send(embed=embed)
    if message.content.startswith('!steinigung'):
        args = message.content.split(' ')
        if len(args) >= 3:
            member: Member = discord.utils.find(lambda m: args[1] in m.name, message.guild.members)
            grund = ' '.join(args[2:])
            kläger = message.author.name
            if member:
                if grund:
                    embed = discord.Embed(title='Steinigung von {}'.format(member.name),
                                          description='Gesteinigt wird die Sünderin {0} für seine Taten!'.format(
                                              member.mention),
                                          color=0xe01c1c)
                    embed.add_field(name='Sünde', value=grund,
                                    inline=True)
                    embed.add_field(name='Kläger', value=kläger,
                                    inline=True)
                    embed.set_thumbnail(url=member.avatar_url)
                    embed.set_footer(text='Steinigung nur für männliche Mitglieder. \r\n'
                                          'Du bist weiblich? Kauf Dir jetzt einen Bart für nur 14,99€')
                    mess = await message.channel.send(embed=embed)
                    await mess.add_reaction(':steinigung:691001406391582760')
                    await mess.add_reaction(':Bart:691005071546253372')
    if message.content.startswith('!prophet'):
        args = message.content.split(' ')
        if len(args) >= 2:
            frage = ' '.join(args[1:])
            mess = await message.channel.send('Warte, ich schreib Gott kurz ne E-Mail...')
            await asyncio.sleep(5)
            await mess.edit(content='{}'.format(random.choice(smalltalk)))
            await asyncio.sleep(10)
            await mess.edit(content='Hier stehts: Gottes Antwort auf die Frage `{0}` lautet: \r\n'
                                    ' `{1}`'.format(frage, random.choice(antworten)))
    if message.content.startswith('grün'):
        mess = await message.channel.send('nee blau', tts=True)
        await asyncio.sleep(2)
        await mess.edit(content='obwohl doch orange')
        await asyncio.sleep(2)
        await mess.edit(content='oder rot?')
        await asyncio.sleep(2)
        await mess.edit(content='Naja, ich bleib bei Ypsilion')
        await mess.add_reaction('😂')
    if 'jehova' in message.content:
        sunder = message.author.name
        embed = discord.Embed(title='Steinigung von {}'.format(sunder),
                              description='Gesteinigt wird die Sünderin {0} für seine Taten!'.format(sunder),
                              color=0xe01c1c)
        embed.add_field(name='Sünde', value='hat Jehova gesagt',
                        inline=True)
        embed.add_field(name='Kläger', value='Gott persönlich',
                        inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.set_footer(text='Steinigung nur für männliche Mitglieder. \r\n'
                              'Du bist weiblich? Kauf Dir jetzt einen Bart für nur 14,99€')
        mess = await message.channel.send(embed=embed)
        await mess.add_reaction(':steinigung:691001406391582760')
        await mess.add_reaction(':Bart:691005071546253372')
    if 'Jehova' in message.content:
        sunder = message.author.name
        embed = discord.Embed(title='Steinigung von {}'.format(sunder),
                              description='Gesteinigt wird die Sünderin {0} für seine Taten!'.format(sunder),
                              color=0xe01c1c)
        embed.add_field(name='Sünde', value='hat Jehova gesagt',
                        inline=True)
        embed.add_field(name='Kläger', value='Gott persönlich',
                        inline=True)
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.set_footer(text='Steinigung nur für männliche Mitglieder. \r\n'
                              'Du bist weiblich? Kauf Dir jetzt einen Bart für nur 14,99€')
        mess = await message.channel.send(embed=embed)
        await mess.add_reaction(':steinigung:691001406391582760')
        await mess.add_reaction(':Bart:691005071546253372')
    if message.content.startswith('lol'):
        role = discord.utils.get(message.guild.roles, name='Gotteslästerer')
        await message.author.add_roles(role)
        await message.author.edit(voice_channel=None)
    if message.content.startswith('!randommeme'):
        await message.channel.send('!play {}'.format(random.choice(memes)))
    if message.content.startswith('$thumb'):
            channel = message.channel
            await channel.send('Send me that 👍 reaction, mate')

            def check(reaction, user):
                return str(reaction.emoji) == '👍'

            try:
                reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
            except asyncio.TimeoutError:
                return
            else:
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout=60.0, check=check)
                except asyncio.TimeoutError:
                    return
                else:
                    await channel.send('Lol')



client.run(token)
