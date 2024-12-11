import runner_and_tournament
import unittest

DISTANCE = 90


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.r1 = runner_and_tournament.Runner('Усейн', 10)
        self.r2 = runner_and_tournament.Runner('Андрей', 9)
        self.r3 = runner_and_tournament.Runner('Ник', 3)

    @classmethod
    def tearDownClass(self):
        while self.all_results:
            print(self.all_results.pop(0))

    def testRun1(self):
        run1 = runner_and_tournament.Tournament(DISTANCE, self.r1, self.r3)
        self.all_results.append(run1.start())
        self.assertTrue(self.all_results[-1].get(2) == self.r3.name)

    def testRun2(self):
        run2 = runner_and_tournament.Tournament(DISTANCE, self.r2, self.r3)
        self.all_results.append(run2.start())
        self.assertTrue(self.all_results[-1].get(2) == self.r3.name)

    def testRun3(self):
        run3 = runner_and_tournament.Tournament(DISTANCE, self.r1, self.r2, self.r3)
        self.all_results.append(run3.start())
        self.assertTrue(self.all_results[-1].get(3) == self.r3.name)
