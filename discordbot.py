from discord.ext import commands # Bot Commands Frameworkをインポート
import os
import traceback # エラー表示のためにインポート
import r
import discord

prefix=os.environ['DISCORD_BOT_PREFIX']
tokun=os.environ['DISCORD_BOT_TOKEN']

# 読み込むコグの名前を格納しておく。
INITIAL_EXTENSIONS = [
    'cogs.stay',
    'cogs.eval',
    'cogs.game'
]

# クラスの定義。ClientのサブクラスであるBotクラスを継承。
class MyBot(commands.Bot):

    # MyBotのコンストラクタ。
    def __init__(self, command_prefix):
        # スーパークラスのコンストラクタに値を渡して実行。
        super().__init__(command_prefix)

        # INITIAL_COGSに格納されている名前から、コグを読み込む。
        # エラーが発生した場合は、エラー内容を表示。
        for cog in INITIAL_EXTENSIONS:
            try:
                self.load_extension(cog)
            except Exception:
                traceback.print_exc()

    # Botの準備完了時に呼び出されるイベント
    async def on_ready(self):
        print('-----')
        print(self.user.name)
        print(self.user.id)
        print('-----')
        conn=r.connect()
        ky=conn.keys()
        p="人狼参加者"
        count=0
        for i in ky:
            i=str(i)
            if i == p:
                count+=1
        if count==0:
            ps=conn.sadd(p,"0")
            if p==True:
                print("正常起動")
            else:
                print("異常発生")
        else:
            print(ky)
        await self.change_presence(status=discord.Status.idle,activity=discord.Game(name=f'人狼げーむ')) 
        

# MyBotのインスタンス化及び起動処理。
if __name__ == '__main__':
    bot = MyBot(command_prefix=prefix) # command_prefixはコマンドの最初の文字として使うもの。 e.g. !ping
    bot.run(tokun) # Botのトークン
