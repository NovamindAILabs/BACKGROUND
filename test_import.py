#!/usr/bin/env python3
"""
Test script to verify all imports work correctly
"""

try:
    print("Testing imports...")
    
    # Test basic imports
    import torch
    print("✓ torch imported successfully")
    
    import numpy as np
    print("✓ numpy imported successfully")
    
    from PIL import Image
    print("✓ PIL imported successfully")
    
    import flask
    print("✓ flask imported successfully")
    
    # Test model import
    try:
        from model_u2net import U2NET, REBNCONV
        print("✓ model_u2net imported successfully")
    except ImportError as e:
        print(f"✗ model_u2net import failed: {e}")
    
    # Test remover import
    try:
        from remover import BackgroundRemover
        print("✓ BackgroundRemover imported successfully")
        
        # Test creating an instance
        remover = BackgroundRemover()
        print("✓ BackgroundRemover instance created successfully")
        
    except ImportError as e:
        print(f"✗ BackgroundRemover import failed: {e}")
    except Exception as e:
        print(f"✗ BackgroundRemover creation failed: {e}")
    
    print("\nAll tests completed!")
    
except ImportError as e:
    print(f"Import error: {e}")
    print("Please make sure all dependencies are installed:")
    print("pip install -r requirements.txt")