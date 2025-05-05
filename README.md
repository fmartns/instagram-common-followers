Instagram Common Followers Finder
A Python script to find common followers between two Instagram profiles using the Instaloader library.
Features

Authenticates with Instagram using username and password
Supports two-factor authentication (2FA)
Saves login session for reuse
Retrieves and compares followers of two Instagram profiles
Displays common followers and their count

Requirements

Instaloader library (pip install instaloader)

Installation

Clone the repository:
git clone https://github.com/fmartns/instagram-common-followers.git
cd instagram-common-followers


Set up a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate


Install dependencies:
pip install instaloader



Usage

Activate the virtual environment (if not already activated):
source venv/bin/activate  # On Windows: venv\Scripts\activate


Run the script:
python insta_followers.py


Follow the prompts to enter:

Your Instagram username and password
Two Instagram profile usernames to compare
2FA code (if applicable)


The script will:

Load a saved session or log in
Fetch followers for both profiles
Display common followers and the total count



Notes

The script saves a session file (<username>.session) to avoid repeated logins.
Ensure a stable internet connection, as fetching followers can take time.
Be aware of Instagram's rate limits to avoid temporary blocks.

