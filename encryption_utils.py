# encryption_utils.py

def mask_ssn(ssn: str) -> str:
    """Mask the entire SSN as 'xxx-xx-xxxx' regardless of input."""
    if not ssn or ssn == "Hidden":
        return "Hidden"
    return "xxx-xx-xxxx"


# For compatibility
encrypt_ssn = mask_ssn
decrypt_ssn = lambda s: s  # no decryption possible with masking
