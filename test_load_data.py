import csv
import unittest
import os

from read_csv import read_csv


class TestCsv(unittest.TestCase):

    def setUp(self):
        self.df_tenant_trans, self.df_tenants = read_csv('load_test_data.csv')

    def tearDown(self):
        # os.remove(test_file)
        pass

    def test_no_inclusive_values_with_zero(self):
        self.assertEqual(self.df_tenant_trans.shape[0], 4)

    def test_null_period_gets_data_from_cell_above(self):
        self.assertFalse(self.df_tenant_trans["Inclusive"].isnull().any())

    def test_tenats_with_null_vacate_dates_are_active(self):
        self.assertTrue(self.df_tenants.loc[self.df_tenants['UserCode']=='2897', 'is_active'].item())
        self.assertFalse(self.df_tenants.loc[self.df_tenants['UserCode']=='2542', 'is_active'].item())

if __name__ == "__main__":
    unittest.main()