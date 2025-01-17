from dotenv import load_dotenv
import os

def get_bot_token():
    # Load environment variables from the .env file
    load_dotenv()

    # Retrieve the BOT_TOKEN value
    bot_token = os.getenv("BOT_TOKEN")

    # Ensure the token is retrieved
    if not bot_token:
        raise ValueError("BOT_TOKEN is not set in the .env file.")

    # Print the BOT_TOKEN (for debugging purposes only; avoid in production)
    print(f"BOT_TOKEN: {bot_token}")

    return bot_token

# Example usage
if __name__ == "__main__":
    get_bot_token()