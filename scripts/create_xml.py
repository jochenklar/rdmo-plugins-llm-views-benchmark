#!/usr/bin/env python3
import copy
import xml.etree.ElementTree as ET

from config import MODELS, PROVIDER, VIEW_PATH, XML_PATH

uri_attr = '{http://purl.org/dc/elements/1.1/}uri'

tree = ET.parse(VIEW_PATH)
root = tree.getroot()
view = template = root.find('view')

for model in MODELS[PROVIDER]:
    uri_suffix = f'-{PROVIDER}-{model}'.lower().replace('.', '-').replace(':', '-')

    node = copy.deepcopy(template)
    node.set(uri_attr, f'{node.get(uri_attr)}{uri_suffix}')
    node.find('uri_path').text = node.find('uri_path').text + uri_suffix
    node.find("help[@lang='en']").text = f'{PROVIDER}, {model}'
    node.find("help[@lang='de']").text = f'{PROVIDER}, {model}'
    node.find('template').text = node.find('template').text.replace(
        'README {% llm_reset %}', f'README ({PROVIDER}, {model}) {{% llm_reset %}}'
    )
    node.find('template').text = node.find('template').text.replace(
        '{% llm %}', f'{{% llm model="{model}" metadata="true" %}}'
    )
    root.append(node)

root.remove(view)

XML_PATH.parent.mkdir(exist_ok=True, parents=True)
tree.write(XML_PATH, encoding='utf-8', xml_declaration=True)
