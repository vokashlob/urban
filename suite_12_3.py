import unittest
import tests_12_3

runnersTS = unittest.TestSuite()
runnersTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.RunnerTest))
runnersTS.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(runnersTS)
