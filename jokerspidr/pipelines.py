# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

import pika
from itemadapter import ItemAdapter


class JokerspidrPipeline:
    def process_item(self, item, spider):
        # print(item)
        itemDic = {
            "domain": item["domain"],
            "url": item["url"],
            "title": item["title"],
            "author": item["author"],
            "content": item["content"],
            "pubtime": item["pubtime"],
            "clickNum": item["clickNum"],
            "category": item["category"]
        }
        connection = pika.BlockingConnection(
            pika.ConnectionParameters('localhost', 5672)  # 默认端口5672，可不写
        )
        # 声明一个管道，在管道里发消息
        channel = connection.channel()
        # 在管道里声明queue
        channel.queue_declare(queue='hello')
        # RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
        channel.basic_publish(exchange='',
                              routing_key='hello',  # queue名字
                              body=json.dumps(itemDic,ensure_ascii=False))  # 消息内容
        connection.close()  # 队列关闭
        return item
