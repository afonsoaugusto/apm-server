#!/usr/bin/env python3

import os
from jinja2 import Environment, FileSystemLoader


def getVariables():
    return {"elasticsearch_url": os.environ["ELASTICSEARCH_URL"]}


def renderFile(filename):
    env = Environment(loader=FileSystemLoader('/templates'))
    template = env.get_template(filename)
    output_from_parsed_template = template.render(getVariables())
    # print(output_from_parsed_template)

    # to save the results
    with open(filename.replace('.j2', ''), "w") as fh:
        fh.write(output_from_parsed_template)


renderFile('apm-server.yml.j2')
