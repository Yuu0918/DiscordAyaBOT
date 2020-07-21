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
            await client.send_message(message.channel,random.choice(r))
    if message.content.startswith("!updata"):
        if client.user != message.author:
            updata=discord.Embed(title='前回の綾波BOTのアップデート情報', description='前回のアップデート(ver.0.0.1α→0.0.1β)', color=0x00ff40)
            updata.set_author(name='綾波BOT', icon_url='https://github.com/Yuu0918/test/blob/master/ayanami.png?raw=true')
            updata.add_field(name='アップデート！', value='!INMGRKを追加したよ！これでいつでも淫夢語録を覚えられるね！\r!topを追加したよ！これでいちいち画像検索をしなくて済むね！\r!kancolleを追加したよ！これでやるまでに回りくどいサイトに行く必要がなくなるね！\rこのBOTが24時間に対応したよ！いつまでもこのBOTとあらんことを。', inline=False)
            updata.add_field(name='これで安心！', value='多くの誤字脱字を削除したよ！読みにくい文字はすべて潰した(はず...)だよ！', inline=False)
            updata.add_field(name='えっ何？俺とBOT開発がしたいって？(難聴)', value='Pythonがわかる人もわからない人も開発チームに参加してくれるのは大歓迎！\rチームに入りなくなったらいつでもYuu_0918にDMしてね！', inline=False)
            updata.set_footer(text='AYANAMIBOT ver.0.0.1β')
            await client.send_message(message.channel, embed=updata)
    if message.content.startswith("!nextupdata"):
        if client.user != message.author:
            nextupdata=discord.Embed(title="次回の綾波BOTのアップデート予定", description="日時未定 (ver.0.0.1β→0.0.1γ)\r日時が変更になる可能性がございます。あらかじめご了承ください。", color=0xff6c26)
            nextupdata.set_author(name="綾波BOT", icon_url="https://github.com/Yuu0918/test/blob/master/ayanami.png?raw=true")
            nextupdata.add_field(name='追加予定', value='未定', inline=False)
            nextupdata.add_field(name='削除予定', value='未定', inline=False)
            nextupdata.add_field(name='バグ削除予定', value='なし', inline=False)
            nextupdata.set_footer(text='AYANAMIBOT ver.0.0.1β')
            await client.send_message(message.channel, embed=nextupdata)
    if message.content.startswith("!help"):
        if client.user != message.author:
            help = discord.Embed(title = '綾波BOTの使い方', description = 'Yuu_0918が勉強用に作ったBOTです\r詳しい使い方はYuu_0918に聞いてください...', color=0x189c1f)
            help.set_author(name = '綾波BOT', icon_url = 'https://github.com/Yuu0918/test/blob/master/ayanami.png?raw=true')
            help.add_field(name='!help', value='ヘルプを表示します。', inline=False)
            help.add_field(name='!update', value='前回のアップデート内容を表示します', inline=False)
            help.add_field(name='!nextupdate', value='次回のアップデートの日付と内容を表示します', inline=False)
            help.add_field(name='!INMGRK', value='淫夢語録をランダムで表示します', inline=False)
            help.add_field(name='!TNOK', value='谷岡が免許を取り上げに来ます', inline=False)
            help.add_field(name='!r ayanami', value='綾波のセリフをランダムで発言します', inline=False)
            help.add_field(name='!kusa', value='代理で草をはやします※', inline=False)
            help.add_field(name='!kancolle', value='艦これのURLを表示します', inline=False)
            help.add_field(name='!top', value='トプ画を配布します', inline=False)
            help.add_field(name='!YTR', value='オッハー！と返事します(たまに違うあいさつの可能性も微レ存...?)※', inline=False)
            help.add_field(name='面白かったねー！', value='綾波の頭が爆発します', inline=False)
            help.add_field(name='機能募集！', value='このBOTに追加してほしい機能を募集しております\rありましたらYuu_0918にいってください。可能な限り実装していきます。', inline=False)
            help.add_field(name='注意', value='※ この機能はまだ実装されてないので打つだけ無駄です。\r※2 次回のVer.では消される可能性がありますご了承ください。\r※3 コマンドの連打などで再起不能な状態に陥ったりした場合は特定して後ろから鉈で刺しに行きます。', inline=True)
            help.set_footer(text='AYANAMIBOT ver.0.0.1β')
            await client.send_message(message.channel, embed=help)
    if message.content.startswith("!TNOK"):
        if client.user != message.author:
            tnok = discord.Embed(title='不幸な追突', description='おいゴルァ！降りろ免許持ってんのかてめぇ。\r免許見せろよ、あくしろよ.', colour=0x000000)
            tnok.set_author(name = 'TNOK', icon_url = 'https://github.com/Yuu0918/test/blob/master/4623012-0b35b1cd-d787-4133-9351-75659d6b3b48-large.png?raw=true')
            await client.send_message(message.channel, embed=tnok)
    if message.content.startswith("!top"):
        if message.author != client.user:
            top = 'photo/ayanami.jpeg'
            await client.send_file(message.channel, top)
    if message.content.startswith("面白かったねー！"):
        pan = " パーン☆┗(^o^)┛ってなりましたね、頭が。" + message.author.name + "さんから「面白かったね」っていうのが聞こえた瞬間に 何がなんだか分かんなくなっちゃって もう、 嬉しくて感動で"
        await client.send_message(message.channel,pan)
    if message.content.startswith("!kancolle"):
        kan = "http://www.dmm.com/netgame/social/-/gadgets/=/app_id=854854/ \rおかえりなさい！提督。"
        await client.send_message(message.channel,kan)
    if message.content.startswith("!INMGRK"):
        if message.author != client.user:
            import random
            INMGRK = '警察だ！（インパルス板倉）','こ↑こ↓','金！暴力！SEX！','36、普通だな！','センセンシャル','ただいまおもみもものサービスをさせて頂いてますので……','誰だよ、お前の彼か？','あーつまんね','なんてことを・・・(憤怒)','すいません許してください！何でもしますから！','もう始まってる！','えっ、そんなん関係無いでしょ（正論）','見たい、見たい、院長がイクとこ見たい！','30分で、5万','マジすか(棒読み)','私には理解に苦しむね(ペチペチ)','違うだろ！いい加減にしろ！','なんか芸術的','人間の屑がこの野郎','For iPhone?','豚ァ！','見ろよコレぇ……この無残な姿をよぉ！','やったぜ。','やはりヤバい','許してもらえるわけがな～い','何だこのオッサン！？','なんか足んねえよなぁ？','がわﾞいﾞいﾞなﾞぁﾞだいﾞぢぐんﾞ','コラ！何勃↑起↓している！','だ↑ま→れ↓','お金タダでいいから（親切）','お前もう生きて帰れねぇな？','ドジョウと俺のさ、子供ができたらどうする？ドジョウと俺と・・・え？総理大臣の誕生か？','もう許せるぞオイ！','えぇ…','工事してると思ったら自分の工事してるのか','いなりが入ってないやん!','14万！？うせやろ！？','やっぱ…中野くんの料理を…最高やな！','Hな介護をしてください!（大声）','よっしゃ！早く終わらせて、帰ってオナニーでもするか','乳首感じるんでしたよね？','あ、やべえ!こんなことしてる場合じゃねぇ！早く戻んなきゃ','ファッ！？','そうだよ（便乗）','あくしろよ','ほらほらほらほらほら','やりますねぇ！','ん？今なんでもするって言ったよね？','ｱｰｲｷｿ','暴れるなよ…暴れんなよ…','オォン!アォン!','硬くなってんぜ。','ｶﾝﾉﾐﾎ','見とけよ見とけよ～','まずいですよ!','ダイナモ感覚！ダイナモ感覚！YO！YO！YO！YEAH！','終わり！閉廷！以上！皆解散！','ちゃんと二本咥え入れろ～？','つっかえ！','なんか芸術的','なんか足んねぇよなぁ','流行らせコラ！','ぼくひで','また君か壊れるなぁ','ラグビーってなんだよ(哲学)','今日は逆さ吊り、鞭攻めをしよう（提案）','おう、考えてやるよ（返すとは言っていない）','お前精神状態おかしいよ…','小生やだ！','3人はどういう集まりなんだっけ？','お前ノンケかよぉ！？（驚愕）','おまんこぉ～＾','いっぱいいっぱい裕次郎...','太いシーチキンが欲しい・・・','ちゃんちゃちゃちゃんちゃん！FOO⤴︎','ﾊﾟｲﾊﾟｲﾊﾟｰｲﾊﾟﾊﾟｲﾆ"ﾁｰｯﾁｯﾁｯﾁｯﾁｯﾁｯﾁｯｽﾞｵｫ','ふ・ざ・け・ん・な、ヤ・メ・ロ・バ・カ！','ポイテーロ！','多分変態だと思うんですけど(名推理)','三人に勝てるわけないだろ！','ドロヘドロ！','何だお前！？(素)','ちんぽであります！','ちんぽであります！(あきつ丸)',
            await client.send_message(message.channel,random.choice(INMGRK))

client.run("TOKEN")
