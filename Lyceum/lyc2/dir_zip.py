import os
import zipfile
import click
import datetime

now = datetime.datetime.now()


def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


dir1 = click.prompt('Введите каталог для архивирования: ', default=os.getcwd())
dir2 = click.prompt('Введите каталог куда положить архив: ', default='D:\\')

file = os.path.dirname(dir1).split("\\")[-1] + '_' + now.strftime("%d-%m-%Y_%H-%M-%S") + '.zip'

zipf = zipfile.ZipFile(os.path.join(dir2, file), 'w')
zipdir(dir1, zipf)
zipf.close()
print('Архив сохранён', os.path.join(dir2, file))
