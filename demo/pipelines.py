# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import psycopg2



class DemoPipeline:
    def __init__(self):
        self.connection_function()
        # self.create_table()

    def connection_function(self):
        self.connection = psycopg2.connect(
            host="localhost",
            database="scrape",
            user="postgres",
            password="posm20031997"
        )
        self.cursor = self.connection.cursor()

    # def create_table(self):
    #     self.cursor.execute("""drop table if exists nitra_car""")
    #     self.cursor.execute("""create table nitra_car(
    #             marka varchar,
    #             qiymet varchar
    #         )""")

    def process_item(self, item, spider):
        self.store_db(item)
        return item

    def store_db(self, item):
        for i in range(len(item['marka'])):
            print("***************************",i,"***************************")
            self.cursor.execute(""" insert into nitra_car (marka, qiymet) values (%s,%s)""",(
                item['marka'][i],
                item['qiymet'][i]
            ))
        self.connection.commit()