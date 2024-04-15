
# username-generator Script

This Python script generates various transformations of names from a wordlist file. It can generate both lowercase and uppercase permutations of names.

## Requirements

- Python 3.x
- argparse module (usually included in Python standard library)

## Usage

1. Clone the repository or download the script file (`username-generator.py`).
2. Open a terminal or command prompt.
3. Navigate to the directory containing the script.
4. Run the script with the following command:

    ```bash
    python username-generator.py -w path/to/wordlist.txt
    ```

   Replace `path/to/wordlist.txt` with the path to your wordlist file.

## Options

- `-w, --wordlist`: Specify the path to the wordlist file containing names.
- `-u, --uppercase`: (Optional) Also produce uppercase permutations of names. Disabled by default.

## Example

```bash
python username-generator.py -w example/wordlist.txt -u
