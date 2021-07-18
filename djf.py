import discord
import asyncio

client = discord.Client()

token = "비공개"

@client.event
async def on_ready():

    print(client.user.name)
    print("봇 시작 완료")
    game = discord.Game("저에게 !명령어 이라고 쳐보세요!")
    await client.change_presence(status=discord.Status.online, activity=game)

@client.event
async def on_message(message):
    if message.content == "!주식빵":
        await message.channel.send("잘생김!ㅋㅋ")

    if message.content == "!명령어":
        await message.channel.send("!주식빵, !식빵이, !유튜브 채널, !니얼굴, !엔젤탱, !연두색필통, !주빵식, 공포. 더 추가 할 예정 입니다")

    if message.content == "!식빵이":
        await message.channel.send("부르셨습니까? (!명령어) 를 쳐보세요")

    if message.content == "!유튜브 채널":
        await message.channel.send("https://www.youtube.com/channel/UCQE0eMpssVivw3niNRZJsaw 개발자 유튜브 채널 입니다. 구독 해주시면 감사하겠습니다")

    if message.content == "!니얼굴":
        await message.channel.send("????? 미쳤습니까 휴먼")

    if message.content == "!엔젤탱":
        await message.channel.send("지상 최고의 미모: https://www.youtube.com/channel/UC6jXEHo58cbzIUZDDmGyRSg")

    if message.content == "!연두색필통":
        await message.channel.send("지상 최고의 게임실력: https://www.youtube.com/channel/UCz7DEfvHpcjhr2CutmvEhDg")

    if message.content == "!주빵식":
        await message.channel.send("우리 손자")

    if message.content == "!공포":
        await message.channel.send("ㅎㅎㅎ 놀자~ ㅎㅎㅎ~~!!!")

    if message.content == "!코딩":
        await message.channel.send("이 봇은 유튜브 주식빵에 의해서 만들어졌습니다. 파이썬 운영채제로 만들어 졌습니다. 이것은 if message.content == "메시지": 형식으로 만들어 졌습니다.")

client.run(token)
