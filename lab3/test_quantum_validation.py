import errno
from pathlib import Path
import subprocess
import tempfile
import unittest


class QuantumValidationTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.directory = tempfile.TemporaryDirectory()
        cls.binary = Path(cls.directory.name) / "rr"
        source = Path(__file__).with_name("rr.c")
        subprocess.run(["cc", "-Wall", "-Wextra", str(source), "-o", str(cls.binary)], check=True)
        cls.processes = Path(cls.directory.name) / "processes.txt"
        cls.processes.write_text("1\n1, 0, 1\n")

    @classmethod
    def tearDownClass(cls):
        cls.directory.cleanup()

    def test_zero_quantum_is_rejected_without_hanging(self):
        try:
            result = subprocess.run([str(self.binary), str(self.processes), "0"],
                                    capture_output=True, timeout=1)
        except subprocess.TimeoutExpired:
            self.fail("zero quantum hangs instead of returning EINVAL")
        self.assertEqual(result.returncode, errno.EINVAL)

    def test_positive_quantum_still_schedules(self):
        result = subprocess.run([str(self.binary), str(self.processes), "1"],
                                capture_output=True, text=True, timeout=1)
        self.assertEqual(result.returncode, 0)
        self.assertIn("Average waiting time: 0.00", result.stdout)


if __name__ == "__main__":
    unittest.main()
