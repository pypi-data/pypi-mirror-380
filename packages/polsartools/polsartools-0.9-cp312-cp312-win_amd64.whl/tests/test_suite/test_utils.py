from tests.test_suite.synthetic_data import gen_S2, gen_T3
import os
import logging, shutil
from polsartools.analysis.pauliRGB import pauliRGB

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_utils_processing(verbose=False):
    T3_folder = './tests/test_data/T3'
    os.makedirs(T3_folder, exist_ok=True)

    s11, s12, s22 = gen_S2('./tests/test_data/S2')
    gen_T3(T3_folder, s11, s12, s22)

    if verbose:
        logger.info("Running Pauli RGB generation...")
    pauliRGB(T3_folder)

    output_files = [
        os.path.join(T3_folder, 'PauliRGB.png'),
        os.path.join(T3_folder, 'PauliRGB_thumb.png'),
    ]

    for file_path in output_files:
        assert os.path.exists(file_path), f"{file_path} not found"
        assert os.path.getsize(file_path) > 0, f"{file_path} is empty"
        if verbose:
            logger.info(f"Verified {file_path}")
        os.remove(file_path)
        if verbose:
            logger.info(f"Deleted {file_path}")
        
    shutil.rmtree('./tests/test_data')