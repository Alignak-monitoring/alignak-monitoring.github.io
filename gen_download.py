#!/usr/bin/python 


import sys
import os
from jinja2 import Environment, FileSystemLoader


if len(sys.argv) > 1:
    ALIGNAK_PATH = sys.argv[1]
else:
    ALIGNAK_PATH = os.getcwd()

TEMPLATE = "downloads.template"

env = Environment(loader=FileSystemLoader(os.path.join(ALIGNAK_PATH, 'templates')))
template = env.get_template(TEMPLATE)

distros = []
for dirpath, dirnames, filenames in os.walk(os.path.join(ALIGNAK_PATH,"build")):
    if len(filenames) > 0:
        distros.append({"name": dirpath.split("/")[-1],
                        "link": os.path.join('/build', dirpath.split("/")[-1], filenames[0])})

out_file = file(os.path.join(ALIGNAK_PATH, TEMPLATE.replace("template","md")),'w')
out_file.write(template.render(distros=distros, layout="layout: page", title="title: Download", permalink="permalink: /download/", menu="menu: true"))
out_file.close()
