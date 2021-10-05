import asyncio
from asyncio.exceptions import CancelledError

import aio_pika

from database import config


async def produceblog(blog_id: int):
    connection = await aio_pika.connect(
        f"amqp://guest:guest@{config.queue}/", loop=asyncio.get_event_loop()
    )

    async with connection:
        routing_key = "consumer"

        channel = await connection.channel()

        await channel.default_exchange.publish(
            aio_pika.Message(body=f"{blog_id}".encode()), routing_key=routing_key,
        )


async def consumeblog():
    connection = await aio_pika.connect(
        f"amqp://guest:guest@{config.queue}/", loop=asyncio.get_event_loop()
    )

    queue_name = "consumer"

    async with connection:
        channel = await connection.channel()
        rabbit_queue = await channel.declare_queue(queue_name, auto_delete=True)

        try:
            async with rabbit_queue.iterator() as queue_iter:
                async for message in queue_iter:
                    async with message.process():
                        # simulate long running process
                        await asyncio.sleep(5)
                        return message.body.decode()
        except CancelledError:
            pass
