# tests/test_suite/test_all.py
from tests.test_suite.test_utils import test_utils_processing
from tests.test_suite.test_filters import test_filters_processing
from tqdm import tqdm

def test_all(verbose=False):
    steps = [
        ("Utils Test", test_utils_processing),
        ("Filters Test", test_filters_processing),
    ]

    for label, func in tqdm(steps, desc="Running Test Suite", unit="step"):
        if verbose:
            print(f"\n🔧 {label}...")
        func(verbose=verbose)

    if verbose:
        print("\n✅ All sample tests passed.")