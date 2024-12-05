from PIL import Image

try:
    original = Image.open('./images/lenna.png')
    # original.show('Картинка 2048х2048')
    resized = original.resize((512, 512))
    for i in range(1, 201):
        resized.save(f'./images/img_{i}.png')
except FileNotFoundError:
    print('Я не нашел картинку')
