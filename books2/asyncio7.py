import aiohttp
import asyncio
import async_timeout

#httpクライアントのrequestsはブロッキングするので
#asyncioに対応してくれるaiohttpを使ってリクエスト

async def fetch(session, url):
    print("{} start".format(url))
    async with async_timeout.timeout(10):
        async with session.get(url) as response:
            text = await response.text()
            print("{} done".format(url))
            return text

async def main():
    async with aiohttp.ClientSession() as session:
        urls = [
          'https://www.youtube.com',
          'https://www.python.org',
          'https://www.google.co.jp',
          'https://www.facebook.com'
        ]
        promises = [fetch(session, u) for u in urls]
        await asyncio.gather(*promises)

if __name__ == '__main__':
    loop = asyncio.get_event_loop()    
    loop.run_until_complete(main())


#参考
#https://www.sambaiz.net/article/162/

