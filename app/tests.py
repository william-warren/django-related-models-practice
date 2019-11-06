from django.test import TestCase
from app import models


class TestSongFormattedDuration(TestCase):
    def test_1_minute(self):
        sixty_second_song = models.Song(seconds=60)
        self.assertEqual(sixty_second_song.formatted_duration(), "1:00")

    def test_45_seconds(self):
        fourty_five_second_song = models.Song(seconds=45)
        self.assertEqual(fourty_five_second_song.formatted_duration(), "0:45")

    def test_2_minutes_10_seconds(self):
        two_minutes_ten_seconds = models.Song(seconds=130)
        self.assertEqual(two_minutes_ten_seconds.formatted_duration(), "2:10")
