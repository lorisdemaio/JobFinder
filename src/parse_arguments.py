import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(
        description="Find remote jobs offers using Remotive API."
    )

    # KEYWORD
    parser.add_argument(
        "-k", "--keyword",
        type=str,
        help="Use keyword (e.g. Junior, Developer, Designer)",
        required=True
    )

    # LOCATION
    parser.add_argument(
        "-l", "--location",
        type=str,
        help="Filter by location.",
        required=False
    )

    # Offers number
    parser.add_argument(
        "-lt", "--limit",
        type=int,
        default=10,
        help="Maximum number of result (default: 10)",
        required=False
    )

    # Export job offers to a CSV file.
    parser.add_argument(
        "--csv",
        help="Save job offers in CSV file.",
        action="store_true",
        required=False
    ) 
    
    return parser.parse_args()