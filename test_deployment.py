#!/usr/bin/env python3
"""
Test script to verify deployment setup
"""

import os
import sys
import pandas as pd

def test_csv_loading():
    """Test if CSV file can be loaded"""
    print("Testing CSV file loading...")
    
    possible_paths = [
        "LLC Data.csv",
        r"C:\rozy\LLC Data.csv",
        "./LLC Data.csv",
    ]
    
    for csv_path in possible_paths:
        if os.path.exists(csv_path):
            try:
                df = pd.read_csv(csv_path)
                print(f"✅ Successfully loaded CSV from: {csv_path}")
                print(f"   - Records: {len(df)}")
                print(f"   - Columns: {list(df.columns)}")
                return True
            except Exception as e:
                print(f"❌ Error loading CSV from {csv_path}: {e}")
        else:
            print(f"⚠️  File not found: {csv_path}")
    
    print("❌ Could not load CSV from any location")
    return False

def test_imports():
    """Test if all required modules can be imported"""
    print("\nTesting imports...")
    
    try:
        import flask
        print("✅ Flask imported successfully")
    except ImportError as e:
        print(f"❌ Flask import failed: {e}")
        return False
    
    try:
        import pandas
        print("✅ Pandas imported successfully")
    except ImportError as e:
        print(f"❌ Pandas import failed: {e}")
        return False
    
    try:
        import werkzeug
        print("✅ Werkzeug imported successfully")
    except ImportError as e:
        print(f"❌ Werkzeug import failed: {e}")
        return False
    
    return True

def test_templates():
    """Test if template files exist"""
    print("\nTesting template files...")
    
    required_templates = [
        "templates/base.html",
        "templates/index.html",
        "templates/service.html",
        "templates/service_state.html",
        "templates/top10_llc_services.html",
        "templates/about.html",
        "templates/contact.html",
        "templates/privacy_policy.html",
        "templates/terms_and_conditions.html",
    ]
    
    all_exist = True
    for template in required_templates:
        if os.path.exists(template):
            print(f"✅ {template}")
        else:
            print(f"❌ {template} - MISSING")
            all_exist = False
    
    return all_exist

def test_config_files():
    """Test if configuration files exist"""
    print("\nTesting configuration files...")
    
    config_files = [
        "vercel.json",
        "requirements.txt",
        "app.py",
    ]
    
    all_exist = True
    for config_file in config_files:
        if os.path.exists(config_file):
            print(f"✅ {config_file}")
        else:
            print(f"❌ {config_file} - MISSING")
            all_exist = False
    
    return all_exist

def main():
    """Run all tests"""
    print("🚀 Deployment Setup Test")
    print("=" * 50)
    
    tests = [
        ("CSV Loading", test_csv_loading),
        ("Imports", test_imports),
        ("Templates", test_templates),
        ("Config Files", test_config_files),
    ]
    
    results = []
    for test_name, test_func in tests:
        print(f"\n📋 {test_name}")
        print("-" * 30)
        result = test_func()
        results.append((test_name, result))
    
    print("\n" + "=" * 50)
    print("📊 Test Results Summary")
    print("=" * 50)
    
    passed = 0
    total = len(results)
    
    for test_name, result in results:
        status = "✅ PASS" if result else "❌ FAIL"
        print(f"{test_name}: {status}")
        if result:
            passed += 1
    
    print(f"\nOverall: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! Your deployment setup is ready.")
        print("\nNext steps:")
        print("1. Push your code to GitHub")
        print("2. Connect to Vercel")
        print("3. Deploy!")
    else:
        print("⚠️  Some tests failed. Please fix the issues before deploying.")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
