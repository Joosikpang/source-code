import discord
import asyncio

client = discord.Client()

token = "비공개"

@client.event
async def on_ready():

    print(client.user.name)
    print("봇 시작 완료")
    game = discord.Game("!명령어")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "!주식빵":
        await message.channel.send("잘생김!ㅋㅋ")

    if message.content == "!명령어":
        await message.channel.send("!주식빵, !식빵이, !유튜브 채널, !니얼굴, !엔젤탱, !연두색필통, !주빵식, !공포, !깃허브, !버전, !파이썬, !임베드. 더 추가 할 예정 입니다")

    if message.content == "!식빵이":
        await message.channel.send("부르셨습니까? (!명령어) 를 쳐보세요")

    if message.content == "!유튜브 채널":
        await message.channel.send("https://www.youtube.com/channel/UCQE0eMpssVivw3niNRZJsaw 개발자 유튜브 채널 입니다. 구독 해주시면 감사하겠습니다")

    if message.content == "!니얼굴":
        await message.channel.send("????? 미쳤습니까 휴먼")

    if message.content == "!엔젤탱":
        await message.channel.send("병아리: https://www.youtube.com/channel/UC6jXEHo58cbzIUZDDmGyRSg")

    if message.content == "!연두색필통":
        await message.channel.send("필통: https://www.youtube.com/channel/UCz7DEfvHpcjhr2CutmvEhDg")

    if message.content == "!주빵식":
        await message.channel.send("주빵식임!")

    if message.content == "!공포":
        await message.channel.send("ㅎㅎㅎ 놀자~ ㅎㅎㅎ~~!!!")

    if message.content == "!코딩":
        await message.channel.send("이 봇은 유튜브 주식빵에 의해서 만들어졌습니다. 파이썬 운영채제로 만들어 졌습니다. [코드는 깃허브를 참고해 주세요.]")

    if message.content == "!파이썬":
        await message.channel.send("파이썬은 귀도 반로섬이 취미로 만든 프로그램언어 입니다.")

    if message.content == "!깃허브":
        await message.channel.send("https://github.com/Joosikpang/source-code")

    if message.content == "!버전":
        await message.channel.send("버전: 0.02 v")

    if message.content == "!임베드":
        embed = discord.Embed(title="안녕하세요!", description="써 주셔서 감사합니다", color=0x00f00)
        embed.add_field(name="개발자 구독해주세요", value="싫으면 엔젤탱, 연두색필통",inline=True)
        embed.add_field(name="개발자 구독해주세요(2스택)", value="싫으면 엔젤탱, 연두색필통(2스택)",inline=True)
        embed.add_field(name="근데요", value="주식빵은 천재에요",inline=True)
        embed.set_footer(text="구독자 100명을 원합니다")
        await message.channel.send(embed=embed)

    if message.content == "!종료":
        await message.channel.send("프로세스를 즉시 종료합니다.")
client.run(token)
