import argparse
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
            else:
                print("Warning no session cookie provided.")

    def download_input(self, year, day, output_file=None):
        url = f"{self.base_url}/{year}/day/{day}/input"
        response = self.session.get(url)

        if response.status_code == 200:
            if output_file:
                with open(output_file, "w") as file:
                    file.write(response.text)
                print(f"Input for Year {year} Day {day} saved to {output_file}")
            else:
                print(response.text)
        else:
            print(f"Failed to download input: {response.status_code} - {response.text}")
