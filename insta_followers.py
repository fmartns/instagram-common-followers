import instaloader
import os

def get_followers(profile_name, loader):
    profile = instaloader.Profile.from_username(loader.context, profile_name)
    return set(f.username for f in profile.get_followers())

def main():
    username = input("Your Instagram username: ")
    password = input("Your password: ")

    profile1 = input("First profile to compare: ")
    profile2 = input("Second profile to compare: ")

    loader = instaloader.Instaloader()

    session_file = f"{username}.session"

    if os.path.exists(session_file):
        print("Loading saved session...")
        try:
            loader.load_session_from_file(username, session_file)
        except Exception as e:
            print(f"Error loading session: {e}")

    if not loader.context.is_logged_in:
        print("Logging in...")
        try:
            loader.login(username, password)
        except instaloader.exceptions.TwoFactorAuthRequiredException:
            code = input("Enter 2FA code (Google Authenticator): ")
            loader.two_factor_login(code)
        except Exception as e:
            print(f"Login error: {e}")
            return

        loader.save_session_to_file(session_file)

    print("Fetching followers... this may take a while.")

    try:
        followers1 = get_followers(profile1, loader)
        followers2 = get_followers(profile2, loader)
    except Exception as e:
        print(f"Error fetching followers: {e}")
        return

    common_followers = followers1 & followers2

    print(f"\nCommon followers between {profile1} and {profile2}:")
    for user in common_followers:
        print(f" - {user}")

    print(f"\nTotal common followers: {len(common_followers)}")

if __name__ == "__main__":
    main()