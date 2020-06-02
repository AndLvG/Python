import pymorphy2
from discord.ext import commands

TOKEN = "NzA5NzAzNTgwNzIxODcyODk2.XrpyDA.WUjTDTnD8zoxAKabhFQ9wJQHvEg"


class TranslatorBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='help_bot')
    async def help(self, ctx):
        message = 'Команды:\n"#!число" согласование числительных. Например <#!число кот 3>\n' \
                  '"#!живой" живой - не живой. Например <#!живой кот>\n' \
                  '"#!падеж" изменение по падежу (nomn, gent, datv, accs, ablt, loct) \n' \
                  '       и числу (single - один, plural - множественный)\n' \
                  '       Например <#!падеж кот ablt single>\n' \
                  '"#!начальная" перевести в начальную форму. Например <#!начальная котов>\n' \
                  '"#!анализ" морфологический анализ. Например <#!анализ кот>'
        await ctx.send(message)

    @commands.command(name='число')
    async def numerals(self, ctx, word, num):
        morph = pymorphy2.MorphAnalyzer()
        word_parse = morph.parse(word)[0].make_agree_with_number(int(num)).word
        await ctx.send(f'{num} {word_parse}')

    @commands.command(name='живой')
    async def alive(self, ctx, word):
        morph = pymorphy2.MorphAnalyzer()
        alive = morph.parse('Живое')[0]
        p = morph.parse(word)
        word_ = None
        for par in p:
            if 'NOUN' in par.tag:
                word_ = par
                break
        try:
            f = word_.tag.gender
            num = word_.tag.number
            if 'anim' in word_.tag:
                if 'plur' in word_.tag:
                    message = f'{word.capitalize()} {alive.inflect({num}).word}'
                else:
                    message = f'{word.capitalize()} {alive.inflect({f, num}).word}'
            else:
                if 'plur' in word_.tag:
                    message = f'{word.capitalize()} не {alive.inflect({num}).word}'
                else:
                    message = f'{word.capitalize()} не {alive.inflect({f, num}).word}'
        except Exception:
            message = 'Не существительное'
        await ctx.send(message)

    @commands.command(name='падеж')
    async def noun(self, ctx, word, case, number):
        morph = pymorphy2.MorphAnalyzer()
        word_parse = morph.parse(word)[0]
        if 'NOUN' in word_parse[1]:
            message = word_parse.inflect({case})[0] \
                if number == 'single' else \
                word_parse.inflect({case, 'plur'})[0]
        else:
            message = f'{word.capitalize()} не существительное'
        await ctx.send(message)

    @commands.command(name='начальная')
    async def infinitive(self, ctx, word):
        morph = pymorphy2.MorphAnalyzer()
        word_parse = morph.parse(word)[0]
        message = word_parse.normal_form
        await ctx.send(message)

    @commands.command(name='анализ')
    async def morph(self, ctx, word):
        morph = pymorphy2.MorphAnalyzer()
        message = morph.parse(word)[0].tag.cyr_repr
        await ctx.send(message)


bot = commands.Bot(command_prefix='#!')
bot.add_cog(TranslatorBot(bot))
bot.run(TOKEN)