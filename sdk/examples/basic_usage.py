"""
VAP SDK - Basic Usage Example
"""

from vape_client import VAPClient, VAPAuthenticationError, VAPInsufficientBalanceError

# Initialize client
client = VAPClient(api_key="your_api_key_here")

# Generate an image
def generate_image():
    try:
        result = client.generate(
            prompt="A beautiful sunset over mountains",
            aspect_ratio="16:9",
        )

        if result.success:
            print(f"Image URL: {result.image_url}")
            print(f"Task ID: {result.task_id}")
        else:
            print(f"Error: {result.error}")

    except VAPAuthenticationError:
        print("Invalid API key")
    except VAPInsufficientBalanceError:
        print("Insufficient balance")
    except Exception as e:
        print(f"Error: {e}")


# Check balance
def check_balance():
    balance = client.get_balance()
    print(f"Balance: ${balance.balance} {balance.currency}")


if __name__ == "__main__":
    print("VAP SDK Example")
    print("Replace 'your_api_key_here' with your actual API key")
    # generate_image()
    # check_balance()
