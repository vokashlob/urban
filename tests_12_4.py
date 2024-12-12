import unittest
import logging
import rt_with_exceptions

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                    format='%(asctime)s ☺ %(levelname)s ☺ %(message)s')


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            r1 = rt_with_exceptions.Runner('Усейн Болт', -5)
            for _ in range(10):
                r1.walk()
            self.assertEqual(r1.distance, 50)
            logging.info('test_walk выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            r2 = rt_with_exceptions.Runner(42, 10)
            for _ in range(10):
                r2.run()
            self.assertEqual(r2.distance, 100)
            logging.info('test_run выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    # @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    # def test_challenge(self):
    #     r1 = rt_with_exceptions.Runner('Усейн Болт')
    #     r2 = rt_with_exceptions.Runner('Джошуа Чептегеи')
    #     for _ in range(10):
    #         r1.run()
    #         r2.walk()
    #     self.assertNotEqual(r1.distance, r2.distance)


if __name__ == '__main__':
    unittest.main()
