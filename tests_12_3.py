import runner_and_tournament
import unittest

DISTANCE = 90


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        r1 = (runner_and_tournament.Runner('Усейн Болт'))
        for _ in range(10):
            r1.walk()
        self.assertEqual(r1.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        r2 = runner_and_tournament.Runner('Джошуа Чептегеи')
        for _ in range(10):
            r2.run()
        self.assertEqual(r2.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        r1 = runner_and_tournament.Runner('Усейн Болт')
        r2 = runner_and_tournament.Runner('Джошуа Чептегеи')
        for _ in range(10):
            r1.run()
            r2.walk()
        self.assertNotEqual(r1.distance, r2.distance)


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def setUp(self):
        self.r1 = runner_and_tournament.Runner('Усейн', 10)
        self.r2 = runner_and_tournament.Runner('Андрей', 9)
        self.r3 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        while cls.all_results:
            print(cls.all_results.pop(0))

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def testRun1(self):
        run1 = runner_and_tournament.Tournament(DISTANCE, self.r1, self.r3)
        self.all_results.append(run1.start())
        self.assertTrue(self.all_results[-1].get(2) == self.r3.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def testRun2(self):
        run2 = runner_and_tournament.Tournament(DISTANCE, self.r2, self.r3)
        self.all_results.append(run2.start())
        self.assertTrue(self.all_results[-1].get(2) == self.r3.name)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def testRun3(self):
        run3 = runner_and_tournament.Tournament(DISTANCE, self.r1, self.r2, self.r3)
        self.all_results.append(run3.start())
        self.assertTrue(self.all_results[-1].get(3) == self.r3.name)


if __name__ == '__main__':
    unittest.main()
