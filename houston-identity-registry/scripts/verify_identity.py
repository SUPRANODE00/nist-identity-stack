import json
import sys

def audit_record(file_path):
    try:
        with open(file_path, 'r') as f:
            data = json.load(f)
        
        required = ["full_name", "jurisdiction", "record_identifier", "crypto_hash"]
        for field in required:
            if field not in data:
                raise ValueError(f"Missing essential validation field: {field}")
                
        print(f"[VERIFIED] Record structure intact for: {data['full_name']} in {data['jurisdiction']}")
        return True
    except Exception as err:
        print(f"[ERROR] Audit failed: {err}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        audit_record(sys.argv[1])
    else:
        print("Usage: python3 scripts/verify_identity.py <path-to-record.json>")
