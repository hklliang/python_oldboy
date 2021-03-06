# -*- coding:utf-8 -*-  
__author__ = 'hklliang'
__date__ = '2017-08-24 13:59'

import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

#只需要定义exchange，不需要定义队列
#类似广播，如果消费者没有接受到就没有了
#每个消费者都能收到
#类似订阅

""""
# 声明queue
channel.queue_declare(queue='hello')

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello',#queue名字
                      body='Hello World!',
                      properties=pika.BasicProperties(delivery_mode=2)#make message persistent
                      )
"""



channel.exchange_declare(exchange='logs',
                         type='fanout')

message = ' '.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs',
                      routing_key='',
                      body=message)
print(" [x] Sent %r" % message)
connection.close()