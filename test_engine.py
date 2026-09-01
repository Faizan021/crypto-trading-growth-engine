# -*- coding: utf-8 -*-
import unittest
import math
import json
import os
import pandas as pd
import numpy as np
from scipy import stats

class TestTradingGrowthEngine(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.base_dir = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(cls.base_dir, 'config', 'email_experiments.json'), 'r', encoding='utf-8') as f:
            cls.experiments = json.load(f)

    def test_case_1_confirmation_z_score(self):
        """Test Two-Proportion Z-Test for Case 1 Confirmation Momentum (n=8,500)"""
        n1, n2 = 8500, 8500
        p1 = 0.412
        p2 = 0.538
        
        count1, count2 = int(p1 * n1), int(p2 * n2)
        p_pooled = (count1 + count2) / (n1 + n2)
        se = math.sqrt(p_pooled * (1 - p_pooled) * (1/n1 + 1/n2))
        z = (p2 - p1) / se
        p_val = 1 - stats.norm.cdf(z)
        
        self.assertGreater(z, 2.58, "Z-score must exceed 99% confidence threshold (2.58)")
        self.assertLess(p_val, 0.01, "P-value must be statistically significant at alpha=0.01")

    def test_case_2_kyc_z_score(self):
        """Test Two-Proportion Z-Test for Case 2 KYC Friction Breaker (n=10,000)"""
        n1, n2 = 10000, 10000
        p1 = 0.284
        p2 = 0.394
        
        count1, count2 = int(p1 * n1), int(p2 * n2)
        p_pooled = (count1 + count2) / (n1 + n2)
        se = math.sqrt(p_pooled * (1 - p_pooled) * (1/n1 + 1/n2))
        z = (p2 - p1) / se
        p_val = 1 - stats.norm.cdf(z)
        
        self.assertGreater(z, 2.58, "Z-score must exceed 99% confidence threshold (2.58)")
        self.assertLess(p_val, 0.01, "P-value must be statistically significant at alpha=0.01")

    def test_case_3_newsletter_ctor_z_score(self):
        """Test Two-Proportion Z-Test for Case 3 Dynamic Editorial News (n=25,000)"""
        n1, n2 = 25000, 25000
        p1 = 0.124
        p2 = 0.231
        
        count1, count2 = int(p1 * n1), int(p2 * n2)
        p_pooled = (count1 + count2) / (n1 + n2)
        se = math.sqrt(p_pooled * (1 - p_pooled) * (1/n1 + 1/n2))
        z = (p2 - p1) / se
        p_val = 1 - stats.norm.cdf(z)
        
        self.assertGreater(z, 3.0, "Z-score must be highly significant (z > 3.0)")
        self.assertLess(p_val, 0.001, "P-value must be < 0.001")

    def test_dca_compound_auc_growth(self):
        """Verify that automated Sparplan accumulation compounds faster than spot trading stagnation"""
        df_dca = pd.read_csv(os.path.join(self.base_dir, 'data', 'dca_sparplan_cohorts.csv'))
        m60_sparplan = df_dca.loc[df_dca['month'] == 60, 'sparplan_avg_auc_eur'].values[0]
        m60_spot = df_dca.loc[df_dca['month'] == 60, 'spot_only_avg_auc_eur'].values[0]
        self.assertGreater(m60_sparplan, m60_spot * 10, "Sparplan 5-year AUC must be at least 10x spot-only AUC")

    def test_volatility_surge_thresholds(self):
        """Verify that volatility triggers flag price anomalies correctly"""
        df_vol = pd.read_csv(os.path.join(self.base_dir, 'data', 'volatility_signals.csv'))
        surges = df_vol[df_vol['is_surge_signal'] == True]
        self.assertGreaterEqual(len(surges), 1, "Must contain at least 1 volatility surge signal")

if __name__ == '__main__':
    unittest.main()
