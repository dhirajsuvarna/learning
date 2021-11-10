import argparse
import pyperclip as clip

args = argparse.ArgumentParser()
args.add_argument("--key", required=True, help="Keyphrase")

commands = args.parse_args()
keyphrase = commands.key


TEXT = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

if keyphrase in TEXT.keys():
    clip.copy(TEXT[keyphrase])
    print(f"Text for {keyphrase} copied to clipboard")
else:
    print(f"There is no text for {keyphrase}")

