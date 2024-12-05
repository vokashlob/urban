from PIL import Image, ImageOps, ImageFilter
import pandas as pd

# PILLOW

DEFAULT_SIZE = 512
IMG_PATH = './images/lenna.png'

original = Image.open(IMG_PATH)
# original.show('Картинка 2048х2048')

print(f" Программа: {original.info['Software']}, размер: {original.size}, "
      f"формат: {original.format.upper()}, режим: {original.mode}")
if original.size[0] > DEFAULT_SIZE or original.size[1] > DEFAULT_SIZE:
    resized = ImageOps.contain(original, (512, 512))
    print(f'Новый размер: {resized.size}')
    new_name = IMG_PATH[:-4] + '_resized.jpg'
    resized.save(new_name, format='JPEG')
    print(f'Файл сохранен под именем: {new_name}')
    filtered = resized.filter(ImageFilter.CONTOUR())
    filtered.show()

# PANDAS

try:
    df = pd.read_excel('hole.xlsx')
    print(df.info())
except FileNotFoundError:
    print('Файл не найден')
    exit()

print(df.head())
print(df.shape)
print(df.describe())

df = df.rename(columns={'Unnamed: 0': 'Date'})
df.loc[37, 'rinsing'] = 1
rinsing_map = {0: False, 1: True}
df.rinsing = df.rinsing.map(rinsing_map)
print(df.head())
print(f'Максимальная дневная температура за весь период: {df.temp_day_max.max()} \n'
      f'Cредняя дневная температура за весь период {round(df.temp_day_max.mean(), 1)} \n'
      f'Количество промываний за весь период: {df["rinsing"].loc[lambda x: x == True].sum()}')
