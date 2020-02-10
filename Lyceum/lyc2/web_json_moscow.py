from zipfile import ZipFile
import json
import os

c = 0

with ZipFile('input.zip') as myzip:
    for el in myzip.infolist():
        if not el.is_dir():
            # print(el.filename)
            name, ext = os.path.splitext(os.path.basename(el.filename))
            if ext == ".json":
                with myzip.open(el.filename, 'r') as file:
                    moscow_json = json.loads(file.read())
                    # print(moscow_json)
                    if moscow_json['city'] == 'Москва':
                        c += 1
print(c)
