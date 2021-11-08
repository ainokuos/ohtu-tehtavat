import unittest
from statistics import Statistics
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )
    
    def test_top_scores(self):
        self.assertEqual(len(self.statistics.top_scorers(1)), 2)
    
    def test_search(self):
        player = self.statistics.search("Semenko")
        self.assertEqual(player.name, "Semenko")
        self.assertEqual(self.statistics.search("Maija"), None)
    
    def test_team(self):
        self.assertEqual(len(self.statistics.team("EDM")), 3)
