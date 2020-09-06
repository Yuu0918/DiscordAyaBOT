import discord

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith("!r ayanami"):
        if client.user != message.author:
            import random
            r = 'はい、大丈夫ですよ？','そんなに話し掛けられてしまうと、お仕事がちゃんとできないです…','お茶にいたしましょうか？','ごきげんよう。特型駆逐艦、綾波と申します。','や～りま～した～','この海域は、譲れません！','綾波が、守ります！','はぁ…癒されます…感謝ですね…','綾波が一番だなんて…嬉しいです…司令官のおかげですね'
            await message.channel.send(random.choice(r))
    if message.content.startswith("!updata"):
        if client.user != message.author:
            updata=discord.Embed(title='前回の綾波BOTのアップデート情報', description='前回のアップデート(ver.0.0.1α→0.0.1β)', color=0x00ff40)
            updata.set_author(name='綾波BOT', icon_url='https://github.com/Yuu0918/test/blob/master/ayanami.png?raw=true')
            updata.add_field(name='アップデート！', value='!INMGRKを追加したよ！これでいつでも淫夢語録を覚えられるね！\r!topを追加したよ！これでいちいち画像検索をしなくて済むね！\r!kancolleを追加したよ！これでやるまでに回りくどいサイトに行く必要がなくなるね！\rこのBOTが24時間に対応したよ！いつまでもこのBOTとあらんことを。', inline=False)
            updata.add_field(name='これで安心！', value='多くの誤字脱字を削除したよ！読みにくい文字はすべて潰した(はず...)だよ！', inline=False)
            updata.add_field(name='えっ何？俺とBOT開発がしたいって？(難聴)', value='Pythonがわかる人もわからない人も開発チームに参加してくれるのは大歓迎！\rチームに入りなくなったらいつでもYuu_0918にDMしてね！', inline=False)
            updata.set_footer(text='AYANAMIBOT ver.0.0.1β')
            await message.channel.send(embed=updata)
    if message.content.startswith("!nextupdata"):
        if client.user != message.author:
            nextupdata=discord.Embed(title="次回の綾波BOTのアップデート予定", description="日時未定 (ver.0.0.1β→0.0.1γ)\r日時が変更になる可能性がございます。あらかじめご了承ください。", color=0xff6c26)
            nextupdata.set_author(name="綾波BOT", icon_url="https://github.com/Yuu0918/test/blob/master/ayanami.png?raw=true")
            nextupdata.add_field(name='追加予定', value='未定', inline=False)
            nextupdata.add_field(name='削除予定', value='未定', inline=False)
            nextupdata.add_field(name='バグ削除予定', value='なし', inline=False)
            nextupdata.set_footer(text='AYANAMIBOT ver.0.0.1β')
            await message.channel.send(embed=nextupdata)
    if message.content.startswith("!help"):
        if client.user != message.author:
            help = discord.Embed(title = '綾波BOTの使い方', description = 'Yuu_0918が勉強用に作ったBOTです\r詳しい使い方はYuu_0918に聞いてください...', color=0x189c1f)
            help.set_author(name = '綾波BOT', icon_url = 'https://github.com/Yuu0918/test/blob/master/ayanami.png?raw=true')
            help.add_field(name='!help', value='ヘルプを表示します。', inline=False)
            help.add_field(name='!update', value='前回のアップデート内容を表示します', inline=False)
            help.add_field(name='!nextupdate', value='次回のアップデートの日付と内容を表示します', inline=False)
            help.add_field(name='!r ayanami', value='綾波のセリフをランダムで発言します', inline=False)
            help.add_field(name='!kancolle', value='艦これのURLを表示します', inline=False)
            help.add_field(name='!top', value='トプ画を配布します', inline=False)
            help.add_field(name='機能募集！', value='このBOTに追加してほしい機能を募集しております\rありましたらYuu_0918にいってください。可能な限り実装していきます。', inline=False)
            help.set_footer(text='AYANAMIBOT ver.0.0.1β')
            await message.channel.send(embed=help)
    if message.content.startswith("!top"):
        if message.author != client.user:
            top = 'photo/ayanami.jpeg'
            await message.channel.send(top)
    if message.content.startswith("!kancolle"):
        kan = "http://www.dmm.com/netgame/social/-/gadgets/=/app_id=854854/ \rおかえりなさい！提督。"
            await message.channel.send(kan)

client.run("TOKEN")
