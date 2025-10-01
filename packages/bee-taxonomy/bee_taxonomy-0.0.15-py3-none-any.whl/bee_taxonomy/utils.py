import glob
import json
import os

def normalize_street_name(street: str):
    """
    Normalize the first word of a Catalan street name abbreviation.
    
    This function takes a street name string and replaces the first word if it matches
    a known Catalan street abbreviation. The mapping is based on common abbreviations
    used in Catalan street names and their corresponding full forms.
    
    Parameters:
        street (str): The input street name string to normalize.
    
    Returns:
        str: The normalized street name with the first word replaced if it's an abbreviation.
    """
    s = street.split()  # Split the street name into individual words (not used in final logic)
    
    MAPPING = {
        "CL": "Carrer",
        "BJ": "Baixada",
        "PZ": "Plaça",  # Catalan for "Plaza"
        "AV": "Avinguda",  # Catalan for "Avenue"
        "PJ": "Passatge",  # Catalan for "Passage"
        "PS": "Passeig",  # Catalan for "Promenade"
        "RB": "Rambla",  # A type of pedestrian street in Catalan cities
        "TT": "Torrent"  # A type of natural stream or path in Catalan geography
    }

    # Split the street name into two parts at the first whitespace
    parts = street.strip().split(maxsplit=1)
    first_word = parts[0]  # Extract the first word (street abbreviation)
    rest = parts[1]  # Extract the remaining part of the street name
    
    # Replace the first word with its normalized form using the MAPPING dictionary
    # If the abbreviation isn't in the mapping, keep the original first word
    normalized_first = MAPPING.get(first_word, first_word)
    
    # Combine the normalized first word with the rest of the name and return
    return f"{normalized_first} {rest}".strip()

def load_checkpoint(tmp_file: str):
    """
    Load a previous classification checkpoint from a temporary file.
    
    Args:
        tmp_file: Path to the checkpoint file
    
    Returns:
        Dictionary of previously classified items or empty dict if file doesn't exist
    """
    if os.path.exists(tmp_file):
        with open(tmp_file, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_checkpoint(tmp_file, data):
    """
    Save current classification progress to a temporary file.
    
    Args:
        tmp_file: Path where to save the checkpoint
        data: Dictionary of field-to-classification mappings to persist
    """
    with open(tmp_file, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def deprecate_cache_file(file: str = None):
    """
    Delete a specific cache file or all temporary files in the current directory.
    
    Args:
        file: Optional specific file path to delete. If None, deletes all .tmp files.
    """
    if os.path.isfile(file):
        os.remove(file)
        print(f"Removed file: {file}")
    else:
        files = glob.glob("*.tmp")
        if files:
            for f in files:
                try:
                    os.remove(f)
                    print(f"Removed file: {f}")
                except Exception as e:
                    print(f"Cannot remove {f}: {e}")
        else:
            print("No files to remove")
