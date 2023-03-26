import argparse
import paperqa
import pypdf
from pathlib import Path

parser = argparse.ArgumentParser()

parser.add_argument("-d", "--dir")
parser.add_argument("-q", "--query")

args = parser.parse_args()

p = Path(args.dir)

docs = paperqa.Docs()
for path in p.glob("*.pdf"):
    try:
        docs.add(str(path))
    except pypdf.errors.PdfReadError as e:
        # sometimes this happens if PDFs aren't downloaded or readable
        print("Could not read", path, e)
    except ValueError as e:
        # sometimes this happens if PDFs aren't downloaded or readable
        print("Could not read", path, e)

answer = docs.query(args.query)
print(answer.formatted_answer)
