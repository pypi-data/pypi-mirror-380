import argparse
import random
import requests
import sys
from catfacts import __version__

# Local database of cat facts
FACTS = [
    "Cats sleep for 70% of their lives.",
    "A group of cats is called a clowder.",
    "Cats have over 20 muscles that control their ears.",
    "The oldest known pet cat existed 9,500 years ago.",
    "Cats can rotate their ears 180 degrees.",
    "A house cat’s genome is 95.6 percent tiger.",
    "The oldest cat ever recorded was 38 years old.",
    "A queen (female cat) can begin mating when she is between 5 and 9 months old.",
    "Tests done by the Behavioral Department of the Musuem of Natural History conclude that while a dog's memory lasts about 5 minutes, a cat's recall can last as long as 16 hours.",
    "Cats eat grass to aid their digestion and to help them get rid of any fur in their stomachs."
]

API_URL = "https://catfact.ninja/fact"


def get_api_fact():
    """Fetch a cat fact from the API."""
    try:
        response = requests.get(API_URL, timeout=5)
        if response.status_code == 200:
            return response.json().get("fact")
    except requests.RequestException:
        return None
    return None


def get_facts(count, source="local", unique=False):
    """Return cat facts from local DB or API, with optional unique filter."""
    facts = []

    if source == "local":
        if unique:
            # pick without replacement
            facts = random.sample(FACTS, min(count, len(FACTS)))
        else:
            # allow duplicates
            facts = [random.choice(FACTS) for _ in range(count)]

    else:  # API source
        seen = set()
        retries = 0
        while len(facts) < count and retries < count * 5:
            fact = get_api_fact()
            retries += 1
            if not fact:
                continue
            if unique:
                if fact in seen:
                    continue
                seen.add(fact)
            facts.append(fact)

        # if unique but not enough results found
        if unique and len(facts) < count:
            print(f"⚠️ Only {len(facts)} unique facts could be retrieved from API (requested {count}).",
                  file=sys.stderr)

    # final deduplication pass (safe guard)
    if unique:
        facts = list(dict.fromkeys(facts))  # removes dupes, keeps order

    return facts


def main():
    parser = argparse.ArgumentParser(description="🐱 Get fun cat facts!")
    parser.add_argument("--version", action="store_true", help="Show version and exit")
    parser.add_argument("--count", type=int, default=1, help="Number of cat facts to show")
    parser.add_argument("--source", choices=["local", "api"], default="local",
                        help="Choose fact source: local database or API")
    parser.add_argument("--unique", action="store_true", help="Ensure all facts are unique (no duplicates)")
    parser.add_argument("--output", choices=["text", "json", "list"], default="text",
                        help="Output format: text, json, or list")

    args = parser.parse_args()

    if args.version:
        print(f"🐾 catfacts-cli version {__version__}")
        return

    facts = get_facts(args.count, args.source, args.unique)

    if args.output == "text":
        for fact in facts:
            print(f"🐱 Cat Fact: {fact}")
    elif args.output == "json":
        import json
        print(json.dumps({"facts": facts}, indent=2, ensure_ascii=False))
    elif args.output == "list":
        for i, fact in enumerate(facts, 1):
            print(f"{i}. {fact}")


if __name__ == "__main__":
    main()
