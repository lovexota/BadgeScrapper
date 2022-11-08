import discum, time

staff_emoji = "Staff"
partner_emoji = "Parceiro"
hypesquad_emoji = "HypeSquad"
bughunter_emoji = "BugHunter"
bughunter2_emoji = "BugHunterGold"
early_emoji = "Pig"
dev_emoji = "Dev"
moderator_emoji = "Mod"

# ---------------------------

print(f"""\n\n╔═╗╔═╗──────────╔═══╗
║║╚╝║║──────────║╔═╗║
║╔╗╔╗╠══╦══╦╦══╗║╚══╦══╦═╦══╦══╦══╦═╗
║║║║║║╔╗║╔╗╠╣╔═╝╚══╗║╔═╣╔╣╔╗║╔╗║║═╣╔╝
║║║║║║╔╗║╚╝║║╚═╗║╚═╝║╚═╣║║╔╗║╚╝║║═╣║
╚╝╚╝╚╩╝╚╩═╗╠╩══╝╚═══╩══╩╝╚╝╚╣╔═╩══╩╝
────────╔═╝║────────────────║║
────────╚══╝────────────────╚╝\n""")

# ---------------------------

token = input("\nDiscord token ?\n")
guild_id = input("\nServer id ? \n")
channel_id = input("\nChannel id ? \n")

print("----- Iniciando Scraping... -----")
bot = discum.Client(token= token, log=True)

bot.gateway.fetchMembers(guild_id, channel_id, keep=['public_flags','username','discriminator','premium_since'],startIndex=0, method='overlap')
@bot.gateway.command
def memberTest(resp):
    if bot.gateway.finishedMemberFetching(guild_id):
        lenmembersfetched = len(bot.gateway.session.guild(guild_id).members)
        print(str(lenmembersfetched)+' membros encontrados!')
        bot.gateway.removeCommand(memberTest)
        bot.gateway.close()

bot.gateway.run()


def __get_badges(flags) -> list[str]:
    
        BADGES = {
            1 << 0:  staff_emoji,
            1 << 1:  partner_emoji,
            1 << 2:  hypesquad_emoji,
            1 << 3:  bughunter_emoji,
            1 << 9:  early_emoji,
            1 << 14: bughunter2_emoji,
            1 << 17: dev_emoji,
            1 << 18: moderator_emoji
        }

        badges = []

        for badge_flag, badge_name in BADGES.items():
            if flags & badge_flag == badge_flag:
                badges.append(badge_name)

        return badges

with open('result.txt', 'w', encoding="utf-8") as file :
    for memberID in bot.gateway.session.guild(guild_id).members:
        id = str(memberID)
        temp = bot.gateway.session.guild(guild_id).members[memberID].get('public_flags')
        user = str(bot.gateway.session.guild(guild_id).members[memberID].get('username'))
        disc = str(bot.gateway.session.guild(guild_id).members[memberID].get('discriminator'))
        username = f'{user}#{disc}'
        creation_date = str(time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(((int(id) >> 22) + 1420070400000) / 1000)))
        if temp != None:
            z = __get_badges(temp)
            if len(z) != 0:
                badges = ', '.join(z)
                print(f'ID: <@{id}> | Username: {username} | Badges: {badges} | Data de criação: {creation_date}')
                file.write(f'<@{id}> | {username} | {creation_date} | {badges}\n')