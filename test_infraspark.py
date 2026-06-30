# test_infraspark.py
"""
Tests for InfraSpark module.
"""

import unittest
from infraspark import InfraSpark

class TestInfraSpark(unittest.TestCase):
    """Test cases for InfraSpark class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = InfraSpark()
        self.assertIsInstance(instance, InfraSpark)
        
    def test_run_method(self):
        """Test the run method."""
        instance = InfraSpark()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
