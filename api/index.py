import sys
import os

# Add backend to path so internal imports resolve
backend_path = os.path.join(os.path.dirname(__file__), '..', 'backend')
sys.path.insert(0, os.path.abspath(backend_path))

from main import app