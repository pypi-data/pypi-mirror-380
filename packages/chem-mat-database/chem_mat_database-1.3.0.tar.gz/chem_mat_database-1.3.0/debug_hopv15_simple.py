#!/usr/bin/env python3
"""
Simple debug script for HOPV15 parser without pycomex dependencies.
"""

import os
import tempfile
from chem_mat_data.connectors import FileDownloadSource
from chem_mat_data.data import HOPV15Parser

def main():
    print("Testing HOPV15 Parser on large dataset...")
    print("=" * 50)

    # Download the dataset using the same connector as the original script
    print("Downloading dataset...")
    try:
        with FileDownloadSource(
            'https://figshare.com/ndownloader/files/4513735',
            verbose=True,
            ssl_verify=False,
        ) as source:
            path = source.fetch()
            print(f"Downloaded to: {path}")

            # Check file size
            file_size = os.path.getsize(path)
            print(f"File size: {file_size:,} bytes")

            # Test the parser
            print("\nTesting HOPV15Parser...")
            parser = HOPV15Parser(path=path)

            # Test parse_all
            print("Parsing all molecules...")
            mol_tuples = parser.parse_all()
            print(f"Found {len(mol_tuples)} molecules")

            # Show first few molecules
            print("\nFirst 3 molecules:")
            for i, (mol, info) in enumerate(mol_tuples[:3]):
                print(f"{i+1}. SMILES: {info['smiles']}")
                print(f"   Atoms: {mol.GetNumAtoms()}")
                print(f"   Has exp. properties: {'experimental_properties' in info}")
                if 'experimental_properties' in info:
                    exp_props = info['experimental_properties']
                    print(f"   PCE: {exp_props.get('PCE', 'N/A')}")
                print()

    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()