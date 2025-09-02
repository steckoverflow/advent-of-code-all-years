#!/usr/bin/env python3
"""
Script to recursively rename folders from 1/ to 01/, 2/ to 02/, etc.
to ensure proper sorting.
"""

import os
import sys

def rename_day_folders(root_dir):
    """Recursively rename day folders with leading zeros."""
    # Process each year directory (e.g., 2015)
    for year_dir in os.listdir(root_dir):
        year_path = os.path.join(root_dir, year_dir)
        
        # Only process directories that look like years
        if not os.path.isdir(year_path) or not year_dir.isdigit() or len(year_dir) != 4:
            continue
            
        print(f"Processing year: {year_dir}")
        
        # Process each day directory within the year
        for day_dir in os.listdir(year_path):
            day_path = os.path.join(year_path, day_dir)
            
            # Only process directories that look like days (1-31)
            if not os.path.isdir(day_path) or not day_dir.isdigit():
                continue
                
            # Convert to integer and back to 2-digit string
            day_num = int(day_dir)
            new_day_name = f"{day_num:02d}"
            
            # Rename only if needed
            if day_dir != new_day_name:
                old_path = os.path.join(year_path, day_dir)
                new_path = os.path.join(year_path, new_day_name)
                
                print(f"  Renaming '{day_dir}' to '{new_day_name}'")
                try:
                    os.rename(old_path, new_path)
                except OSError as e:
                    print(f"    Error renaming: {e}")

def main():
    """Main function."""
    if len(sys.argv) > 1:
        root_directory = sys.argv[1]
    else:
        root_directory = "."
    
    # Check if the directory exists
    if not os.path.exists(root_directory):
        print(f"Error: Directory '{root_directory}' does not exist.")
        return
    
    rename_day_folders(root_directory)

if __name__ == "__main__":
    main()
