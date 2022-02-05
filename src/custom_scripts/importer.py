from item_master.models import Item
import yaml
import os
BASE_DIR = '/home/aj355y/workspace/opensource/rm/croma/src/custom_scripts/'

file_name = os.path.join(BASE_DIR, 'item_master.yaml')
with open(file_name, 'r') as yaml_file:
    try:
        data = yaml.safe_load(yaml_file)
        for dt in data:
            print(dt)
            Item.objects.create(name=dt['fields']['name'])
    except yaml.YAMLError as exc:
        print(exc)