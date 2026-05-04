import unittest

from src.decision_logic import DecisionInput, build_truth_table, evaluate_decision, parse_yes_no


class DecisionLogicTests(unittest.TestCase):
    def test_local_output(self):
        result = evaluate_decision(
            DecisionInput(
                complexity=True,
                real_time=False,
                cost_sensitive=False,
                privacy_sensitive=True,
            )
        )

        self.assertTrue(result.local)

    def test_cloud_output(self):
        result = evaluate_decision(
            DecisionInput(
                complexity=True,
                real_time=False,
                cost_sensitive=False,
                privacy_sensitive=False,
            )
        )

        self.assertTrue(result.cloud)

    def test_hybrid_output(self):
        result = evaluate_decision(
            DecisionInput(
                complexity=True,
                real_time=True,
                cost_sensitive=False,
                privacy_sensitive=False,
            )
        )

        self.assertTrue(result.hybrid)

    def test_lightweight_output(self):
        result = evaluate_decision(
            DecisionInput(
                complexity=False,
                real_time=False,
                cost_sensitive=True,
                privacy_sensitive=False,
            )
        )

        self.assertTrue(result.lightweight)

    def test_multiple_outputs_can_be_active(self):
        result = evaluate_decision(
            DecisionInput(
                complexity=True,
                real_time=True,
                cost_sensitive=False,
                privacy_sensitive=True,
            )
        )

        self.assertEqual((result.local, result.cloud, result.hybrid, result.lightweight), (True, False, True, False))

    def test_truth_table_has_all_input_combinations(self):
        self.assertEqual(len(build_truth_table()), 16)

    def test_parse_yes_no(self):
        self.assertTrue(parse_yes_no("yes"))
        self.assertTrue(parse_yes_no("1"))
        self.assertFalse(parse_yes_no("no"))
        self.assertFalse(parse_yes_no("0"))


if __name__ == "__main__":
    unittest.main()
