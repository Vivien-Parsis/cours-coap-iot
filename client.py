import asyncio
import aiocoap

async def main():
        ctx = await aiocoap.Context.create_client_context()
        req = aiocoap.Message(code=aiocoap.Code.GET, uri="coap://127.0.0.1/temp")
        rep = await ctx.request(req).response
        print("Temperature:", rep.payload.decode())
        await ctx.shutdown()

asyncio.run(main()) 