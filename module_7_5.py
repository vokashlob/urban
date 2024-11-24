
import os, time

def walk_without_exclusions(root_dir, exclude_dirs, file_extension_to_exclude):
    for dirpath, dirnames, filenames in os.walk(root_dir):

        # Удаляем из списка dirnames те, которые указаны в exclude_dirs
        dirnames[:] = [dirname for dirname in dirnames if dirname not in exclude_dirs]

        # Фильтруем список файлов, оставляя только те, у которых расширение не равно file_extension_to_exclude

        filtered_filenames = [filename for filename in filenames if not filename.endswith(file_extension_to_exclude)]
        yield dirpath, dirnames, filtered_filenames


root_directory = os.getcwd()
exclude_directories = ['.git', '__pycache__', '.idea', 'snake']
file_extension_to_exclude = 'xml'

for path, dirs, files in walk_without_exclusions(root_directory, exclude_directories, file_extension_to_exclude):
        for file in files:
            filepath = os.path.join(path, file)
            filetime = os.path.getmtime(filepath)
            formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
            filesize = os.path.getsize(filepath)
            parent_dir = os.path.dirname(filepath)

            print(f'Обнаружен файл: {file}, Путь: {filepath}, Размер: {filesize} байт, Время изменения: {formatted_time}, Родительская директория: {parent_dir}')

