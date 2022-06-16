"""
This test script concerns the extract functionality.
We will use the IDyOM outputs from the experiment "25-05-22_14.10.29"
"""

import unittest
from unittest import TestCase
from py2lispIDyOM.extract import MelodyInfo, ExperimentInfo


class TestExtract(TestCase):
    experiment_folder_path = 'experiment_history/25-05-22_14.10.29/'

    def test_experimentinfo_extract(self):
        experiment_folder_path = 'experiment_history/25-05-22_14.10.29/'

        my_exp = ExperimentInfo(experiment_folder_path=experiment_folder_path)
        all_melodies = my_exp.access_melodies()
        self.assertEqual(len(all_melodies), 15)
        for i in range(len(all_melodies)):
            self.assertIsInstance(obj=all_melodies[i], cls=MelodyInfo)

    def test_melodyinfo_extract(self):
        experiment_folder_path = 'experiment_history/25-05-22_14.10.29/'
        my_exp = ExperimentInfo(experiment_folder_path=experiment_folder_path)
        test_melody = my_exp.access_melodies(melody_names=['"chor-005"'])[0]

        keywords_to_match = ['cpitch', 'onset', 'information.content', 'probability', 'entropy', 'melody.name']

        for idx, val in enumerate(keywords_to_match):
            self.assertIn(val, test_melody.get_idyom_output_keyword_list())

if __name__=='__main__':
    unittest.main()