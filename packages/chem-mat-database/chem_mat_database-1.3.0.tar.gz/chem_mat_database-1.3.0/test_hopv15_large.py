#!/usr/bin/env python3
"""
Test script to download and parse a larger HOPV15 dataset file to debug the parser.
"""

import requests
import tempfile
import os
from chem_mat_data.data import HOPV15Parser

def download_hopv15_dataset():
    """Download the HOPV15 dataset from the official source."""
    url = 'https://figshare.com/ndownloader/files/4513735'

    print("Downloading HOPV15 dataset...")
    try:
        # Download with SSL verification disabled as in the original script
        response = requests.get(url, verify=False, stream=True, timeout=600)  # 10 minute timeout
        response.raise_for_status()

        # Save to temporary file
        with tempfile.NamedTemporaryFile(mode='wb', delete=False, suffix='.data') as f:
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
            temp_path = f.name

        print(f"Downloaded dataset to: {temp_path}")
        file_size = os.path.getsize(temp_path)
        print(f"File size: {file_size:,} bytes")

        return temp_path

    except Exception as e:
        print(f"Error downloading dataset: {e}")
        return None

def test_hopv15_parser(file_path):
    """Test the HOPV15 parser on the downloaded dataset."""
    print(f"\nTesting HOPV15Parser on: {file_path}")

    try:
        # Initialize parser
        parser = HOPV15Parser(path=file_path)
        print("✓ Parser initialized successfully")

        # Test single parse (first molecule)
        print("\nTesting single parse...")
        try:
            mol, info = parser.parse()
            print("✓ Single parse successful")
            print(f"  SMILES: {info.get('smiles', 'None')}")
            print(f"  Molecule atoms: {mol.GetNumAtoms() if mol else 'None'}")
            print(f"  Has experimental properties: {'experimental_properties' in info}")
            print(f"  Number of conformers: {len(info.get('conformers', []))}")
        except Exception as e:
            print(f"✗ Single parse failed: {e}")
            import traceback
            traceback.print_exc()
            return False

        # Test parse_all (all molecules)
        print("\nTesting parse_all...")
        try:
            molecules = parser.parse_all()
            print(f"✓ Parse_all successful - found {len(molecules)} molecules")

            # Show statistics
            with_exp_props = sum(1 for _, info in molecules if 'experimental_properties' in info)
            total_conformers = sum(len(info.get('conformers', [])) for _, info in molecules)

            print(f"  Molecules with experimental properties: {with_exp_props}")
            print(f"  Total conformers across all molecules: {total_conformers}")

            # Show first few molecules
            print(f"\nFirst 3 molecules:")
            for i, (mol, info) in enumerate(molecules[:3]):
                print(f"  {i+1}. {info['smiles']} ({mol.GetNumAtoms()} atoms)")
                if 'experimental_properties' in info:
                    props = info['experimental_properties']
                    print(f"     PCE: {props.get('PCE', 'N/A')}, HOMO: {props.get('HOMO', 'N/A')}")

        except Exception as e:
            print(f"✗ Parse_all failed: {e}")
            import traceback
            traceback.print_exc()
            return False

        return True

    except Exception as e:
        print(f"✗ Parser initialization failed: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Main test function."""
    print("HOPV15 Parser Test on Large Dataset")
    print("=" * 50)

    # Download dataset
    dataset_path = download_hopv15_dataset()
    if not dataset_path:
        print("Failed to download dataset, exiting...")
        return

    try:
        # Test parser
        success = test_hopv15_parser(dataset_path)

        if success:
            print("\n✓ All tests passed successfully!")
        else:
            print("\n✗ Some tests failed!")

    finally:
        # Clean up
        if dataset_path and os.path.exists(dataset_path):
            os.unlink(dataset_path)
            print(f"\nCleaned up temporary file: {dataset_path}")

if __name__ == "__main__":
    main()