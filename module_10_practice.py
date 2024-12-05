import datetime
import multiprocessing as mp
from PIL import Image
from queue import Empty


def resize_image(image_paths, queue):
    for image_path in image_paths:
        image = Image.open(image_path)
        image = image.resize((256, 256))
        queue.put((image_path, image))


def change_color(queue):
    while True:
        try:
            image_path, image = queue.get(timeout=5)
        except Empty:
            break
        image = image.convert('L')
        image.save(image_path)


if __name__ == '__main__':
    data = []
    queue = mp.Queue()

    for image in range(1, 100):
        data.append(f'./images/img_{image}.png')

    resize_process = mp.Process(target=resize_image, args=(data, queue))
    color_process = mp.Process(target=change_color, args=(queue, ))
    start = datetime.datetime.now()
    resize_process.start()
    color_process.start()
    resize_process.join()
    color_process.join()
    end = datetime.datetime.now()
    print(end - start)