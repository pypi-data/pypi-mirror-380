#!/usr/bin/env python3

"""
Simple test script to verify the web application setup.
Run this to check if all components are properly configured.
"""

import os
import sys
from pathlib import Path

def check_project_structure():
    """Check if the project structure is correct."""
    print("🔍 Checking project structure...")
    
    required_files = [
        "frontend/package.json",
        "frontend/src/App.tsx",
        "frontend/src/components/MainInterface.tsx",
        "backend/requirements.txt",
        "backend/app/main.py",
        "backend/run_server.py",
        "start.sh",
        "README.md"
    ]
    
    missing_files = []
    for file_path in required_files:
        if not Path(file_path).exists():
            missing_files.append(file_path)
    
    if missing_files:
        print("❌ Missing files:")
        for file in missing_files:
            print(f"   - {file}")
        return False
    else:
        print("✅ Project structure is correct")
        return True

def check_python_dependencies():
    """Check if Python dependencies can be imported."""
    print("🐍 Checking Python dependencies...")
    
    try:
        import fastapi
        print(f"   ✅ FastAPI {fastapi.__version__}")
    except ImportError:
        print("   ❌ FastAPI not installed")
        return False
    
    try:
        import uvicorn
        print(f"   ✅ Uvicorn available")
    except ImportError:
        print("   ❌ Uvicorn not installed")
        return False
    
    try:
        import pydantic
        print(f"   ✅ Pydantic {pydantic.__version__}")
    except ImportError:
        print("   ❌ Pydantic not installed")
        return False
    
    return True

def check_programasweights():
    """Check if ProgramAsWeights can be imported."""
    print("🧠 Checking ProgramAsWeights integration...")
    
    # Add project root to path
    project_root = Path(__file__).parent.parent
    sys.path.insert(0, str(project_root))
    
    try:
        import programasweights as paw
        print(f"   ✅ ProgramAsWeights {paw.__version__} imported successfully")
        
        # Check if compile function is available
        if hasattr(paw, 'compile'):
            print("   ✅ Compile function available")
        else:
            print("   ❌ Compile function not found")
            return False
            
        # Check if function loader is available
        if hasattr(paw, 'function'):
            print("   ✅ Function loader available")
        else:
            print("   ❌ Function loader not found")
            return False
            
        return True
    except ImportError as e:
        print(f"   ❌ ProgramAsWeights import failed: {e}")
        print("   💡 Make sure ProgramAsWeights is installed: pip install -e .")
        return False

def check_frontend_dependencies():
    """Check if frontend dependencies are installed."""
    print("🎨 Checking frontend dependencies...")
    
    frontend_dir = Path("frontend")
    if not frontend_dir.exists():
        print("   ❌ Frontend directory not found")
        return False
    
    node_modules = frontend_dir / "node_modules"
    if not node_modules.exists():
        print("   ❌ Node modules not installed")
        print("   💡 Run: cd frontend && npm install")
        return False
    
    package_json = frontend_dir / "package.json"
    if package_json.exists():
        print("   ✅ package.json found")
        print("   ✅ Node modules installed")
        return True
    else:
        print("   ❌ package.json not found")
        return False

def main():
    """Run all checks."""
    print("🧪 Testing ProgramAsWeights Web Application Setup")
    print("=" * 50)
    
    checks = [
        check_project_structure,
        check_python_dependencies,
        check_programasweights,
        check_frontend_dependencies
    ]
    
    results = []
    for check in checks:
        results.append(check())
        print()
    
    print("📊 Test Results:")
    print("=" * 50)
    
    if all(results):
        print("🎉 All checks passed! Your web application is ready to run.")
        print()
        print("🚀 To start the application:")
        print("   ./start.sh")
        print()
        print("📖 Or start components separately:")
        print("   Backend:  cd backend && python run_server.py")
        print("   Frontend: cd frontend && npm run dev")
    else:
        print("❌ Some checks failed. Please fix the issues above before running the application.")
    
    return all(results)

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
