# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from goods.models import Products
import os


class Command(BaseCommand):
    def handle(self, *args, **options):
        for Root, Dirs, Files in os.walk('/Users/skk/Desktop/GitHub/bottle/bottle/static/goods2'):
            for Dir in Dirs:
                for root, dirs, files in os.walk(Root + "/" + Dir):
                    print(root)
                    result = ""
                    for i in files:
                        if i.startswith('.'):
                            continue
                        elif os.path.isfile(root + "/" + i):
                            # print((root + "/" + i).split('static')[-1])
                            result += (root + "/" + i).split('static')[-1]  + ","
                    print(result)
                            # new_name = str(root + "/" + i).split("static2/")[-1].replace('/', '-')
                            # print root + "/" + new_name
                            # os.rename(root + "/" + i, root + "/" + i.replace('-', '_'))
