#!/usr/bin/env python3
"""
CLI tool to download Advent of Code input files.
Usage: python download_input_cli.py --year 2015 --day 1
"""

import argparse
import sys
from pathlib import Path

# Import the existing downloader class
try:
    from download_input_from_year_day import AoCDownloader
except ImportError:
    # If we can't import it, create a minimal version for standalone use
    import requests
    import os
    
    class AoCDownloader:
        def __init__(self, session_cookie=None):
            self.base_url = "https://adventofcode.com"
            self.session = requests.Session()
            if session_cookie:
                self.session.cookies.set(
                    "session", session_cookie, domain="adventofcode.com"
                )
            else:
                session_cookie = os.getenv("AOC_SESSION")
                if session_cookie:
                    self.session.cookies.set(
                        "session", session_cookie, domain="adventofcode.com"
                    )

        def download_input(self, year, day, output_file=None):
            """Download input for a given year and day."""
            url = f"{self.base_url}/{year}/day/{day}/input"
            
            response = self.session.get(url)
            
            if response.status_code == 200:
                content = response.text
                
                # If no output file specified, create default filename
                if not output_file:
                    output_file = f"{year}/day{day}.txt"
                    
                # Create directory if it doesn't exist
                Path(output_file).parent.mkdir(parents=True, exist_ok=True)
                
                with open(output_file, "w") as f:
                    f.write(content)
                
                print(f"Input downloaded to {output_file}")
                return True
            else:
                print(f"Failed to download input. Status code: {response.status_code}")
                return False

def main():
    parser = argparse.ArgumentParser(description="Download Advent of Code input file")
    parser.add_argument("--year", "-y", type=int, required=True, help="Advent of Code year (e.g., 2015)")
    parser.add_argument("--day", "-d", type=int, required=True, help="Day number (1-25)")
    parser.add_argument("--output", "-o", type=str, help="Output file path")
    
    args = parser.parse_args()
    
    # Validate inputs
    if not 1 <= args.day <= 25:
        print("Error: Day must be between 1 and 25")
        sys.exit(1)
    
    # Create downloader instance
    downloader = AoCDownloader()
    
    # Download input
    success = downloader.download_input(args.year, args.day, args.output)
    
    if not success:
        sys.exit(1)

if __name__ == "__main__":
    main()
