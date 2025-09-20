import requests
import re

def fetch_and_print_grid(url: str):
 
    response = requests.get(url)
    response.raise_for_status()
    docText = response.text

    regexPattern = re.compile(r"(.)\s*\(x=(\d+),\s*y=(\d+)\)")
    coordinates = []
    for match in regexPattern.finditer(docText):
        char = match.group(1)
        x = int(match.group(2))
        y = int(match.group(3))
        coordinates.append((char, x, y))

    if not coordinates:
        print("Characters not found")
        return

    max_x = max(x for _, x, _ in coordinates)
    max_y = max(y for _, _, y in coordinates)

    grid = [[" " for _ in range(max_x + 1)] for _ in range(max_y + 1)]

    for char, x, y in coordinates:
        grid[y][x] = char

    for row in grid:
        print("".join(row))


if __name__ == "__main__":
    fetch_and_print_grid("https://docs.google.com/document/d/e/2PACX-1vTMOmshQe8YvaRXi6gEPKKlsC6UpFJSMAk4mQjLm_u1gmHdVVTaeh7nBNFBRlui0sTZ-snGwZM4DBCT/pub")
