#! /usr/bin/env python3

import json
import sys

import yaml

if len(sys.argv) >= 2:
    yaml_file = open(sys.argv[1])
else:
    yaml_file = sys.stdin

obj = yaml.safe_load(yaml_file)
yaml_file.close()

json.dump(obj, sys.stdout, indent=2, ensure_ascii=False)
