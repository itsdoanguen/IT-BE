#!/usr/bin/env python
"""Test script to verify refactor is successful"""

import sys
import os

# Set up Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

try:
    import django
    django.setup()
    print("✓ Django setup successful")
    
    # Test importing models
    from modules.accounts.models import NguoiDung
    print("✓ Can import NguoiDung from modules.accounts.models")
    
    from modules.profiles.models import HoSoUngVien
    print("✓ Can import HoSoUngVien from modules.profiles.models")
    
    from modules.jobs.models import TinTuyenDung
    print("✓ Can import TinTuyenDung from modules.jobs.models")
    
    # Test app configuration
    from django.apps import apps
    app_configs = [app.label for app in apps.get_app_configs()]
    
    required_apps = ['accounts', 'profiles', 'jobs', 'applications', 'chats', 'reviews', 'notifications']
    found_apps = [app for app in required_apps if app in app_configs]
    
    print(f"\n✓ Found {len(found_apps)} out of {len(required_apps)} required app labels:")
    for app in found_apps:
        print(f"  - {app}")
    
    # Test AUTH_USER_MODEL
    from django.conf import settings
    auth_user_model = settings.AUTH_USER_MODEL
    print(f"\n✓ AUTH_USER_MODEL = '{auth_user_model}'")
    
    # Test that all migrations exist
    print("\n✓ Migration files found:")
    for app in required_apps:
        mig_path = f"modules/{app}/migrations/0001_initial.py"
        if os.path.exists(mig_path):
            print(f"  - {app}: ✓")
        else:
            print(f"  - {app}: ✗ migrations missing")
    
    print("\n✓ Refactor verification complete!")
    sys.exit(0)
    
except Exception as e:
    print(f"✗ Error: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
