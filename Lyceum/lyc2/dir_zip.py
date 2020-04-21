import os
import zipfile
import click


def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))


dir1 = click.prompt('Введите каталог для архивирования: ', default=os.getcwd())
dir2 = click.prompt('Введите каталог куда положить архив: ', default='C:')

zipf = zipfile.ZipFile(dir1, 'w')
zipdir(dir2, zipf)
zipf.close()
