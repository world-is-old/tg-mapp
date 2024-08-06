import asyncio
import telegram
import props

async def main():
    bot = telegram.Bot(props.bot_token)
    async with bot:
        async with bot:
            updates = (await bot.get_updates())
            print(updates)


if __name__ == '__main__':
    asyncio.run(main())