from discord.ext import commands # Bot Commands Frameworkをインポート
import os

prefix=os.environ['DISCORD_BOT_PREFIX']
tokun=os.environ['DISCORD_BOT_TOKEN']
# クラスの定義。ClientのサブクラスであるBotクラスを継承。
class MyBot(commands.Bot):

    # Botの準備完了時に呼び出されるイベント
    async def on_ready(self):
        print('-----')
        print(self.user.name)
        print(self.user.id)
        print('-----')


# MyBotのインスタンス化及び起動処理。
if __name__ == '__main__':
    bot = MyBot(command_prefix=prefix) # command_prefixはコマンドの最初の文字として使うもの。 e.g. !ping
    bot.run(tokun) # Botのトークン
