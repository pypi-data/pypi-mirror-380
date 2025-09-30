import os
import inspect
import importlib

def show_source(module_name: str):
    """
    Print the source code of a given module in the gdd package.
    
    Args:
        module_name (str): Name of the module to show (e.g., "exp2_olap")
    
    Example:
        gdd.show_source("exp2_olap")
        gdd.show_source("exp3_dt")
    """
    try:
        # Get the current package directory
        package_dir = os.path.dirname(__file__)
        filepath = os.path.join(package_dir, f"{module_name}.py")
        
        # Check if file exists
        if not os.path.exists(filepath):
            raise FileNotFoundError(f"File {module_name}.py not found")
        
        # Read and print the source code
        with open(filepath, "r", encoding='utf-8') as f:
            print(f"\n{'='*60}")
            print(f"SOURCE CODE: {os.path.basename(filepath)}")
            print(f"{'='*60}")
            print(f.read())
            print(f"{'='*60}")
            
    except FileNotFoundError:
        print(f"Error: Module '{module_name}' not found.")
        print("Available modules: exp2_olap, exp3_dt, exp4_lr, exp5_kmeans, exp6_hcluster, exp7_ap")
    except Exception as e:
        print(f"Error: {e}")

# Lazy imports - modules will be imported when show_source() is called
# This prevents NumPy compatibility issues at package import time
