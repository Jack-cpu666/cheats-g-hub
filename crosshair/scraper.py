"""
Valorant Crosshair Database Scraper
Downloads all crosshair codes from vcrdb.net for use in the UI
"""

import requests
import json
import os
import time
from datetime import datetime

# Constants
API_URL = "https://www.vcrdb.net/apiv3/get/0"
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(OUTPUT_DIR, "crosshairs.json")
OUTPUT_SIMPLE = os.path.join(OUTPUT_DIR, "crosshairs_simple.json")


def fetch_crosshairs():
    """Fetch all crosshairs from the vcrdb.net API"""
    print("[*] Fetching crosshairs from vcrdb.net...")
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.9",
        "Referer": "https://www.vcrdb.net/user",
        "Origin": "https://www.vcrdb.net"
    }
    
    try:
        response = requests.get(API_URL, headers=headers, timeout=30)
        response.raise_for_status()
        
        data = response.json()
        print(f"[+] Successfully fetched {len(data)} crosshairs")
        return data
        
    except requests.exceptions.RequestException as e:
        print(f"[-] Error fetching crosshairs: {e}")
        return None


def process_crosshairs(data):
    """Process and clean the crosshair data"""
    processed = []
    
    for item in data:
        crosshair = {
            "id": item.get("id"),
            "name": item.get("name", "Unnamed"),
            "code": item.get("code", ""),
            "copied": item.get("copied", 0),
            "tags": item.get("tags", "")
        }
        
        # Only include if there's a valid code
        if crosshair["code"]:
            processed.append(crosshair)
    
    # Sort by popularity (most copied first)
    processed.sort(key=lambda x: x.get("copied", 0), reverse=True)
    
    return processed


def save_crosshairs(crosshairs):
    """Save crosshairs to JSON files"""
    
    # Full data with all fields
    full_data = {
        "last_updated": datetime.now().isoformat(),
        "total_count": len(crosshairs),
        "crosshairs": crosshairs
    }
    
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        json.dump(full_data, f, indent=2, ensure_ascii=False)
    
    print(f"[+] Saved full data to: {OUTPUT_FILE}")
    
    # Simple format (just name and code) for UI integration
    simple_list = [{"name": c["name"], "code": c["code"]} for c in crosshairs]
    
    with open(OUTPUT_SIMPLE, "w", encoding="utf-8") as f:
        json.dump(simple_list, f, indent=2, ensure_ascii=False)
    
    print(f"[+] Saved simple format to: {OUTPUT_SIMPLE}")


def load_crosshairs():
    """Load crosshairs from the saved JSON file"""
    if not os.path.exists(OUTPUT_FILE):
        print("[-] Crosshairs file not found. Run download first.")
        return None
    
    with open(OUTPUT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    return data.get("crosshairs", [])


def search_crosshairs(query, crosshairs=None):
    """Search crosshairs by name"""
    if crosshairs is None:
        crosshairs = load_crosshairs()
    
    if not crosshairs:
        return []
    
    query = query.lower()
    results = [c for c in crosshairs if query in c["name"].lower()]
    return results


def get_top_crosshairs(n=50, crosshairs=None):
    """Get the top N most popular crosshairs"""
    if crosshairs is None:
        crosshairs = load_crosshairs()
    
    if not crosshairs:
        return []
    
    # Already sorted by popularity
    return crosshairs[:n]


def main():
    """Main function to download and save crosshairs"""
    print("=" * 60)
    print("  Valorant Crosshair Database Scraper")
    print("  Source: https://www.vcrdb.net")
    print("=" * 60)
    print()
    
    # Fetch from API
    raw_data = fetch_crosshairs()
    
    if not raw_data:
        print("[-] Failed to fetch crosshairs. Exiting.")
        return
    
    # Process data
    crosshairs = process_crosshairs(raw_data)
    print(f"[+] Processed {len(crosshairs)} valid crosshairs")
    
    # Save to files
    save_crosshairs(crosshairs)
    
    # Show some stats
    print()
    print("=" * 60)
    print("  Top 10 Most Popular Crosshairs:")
    print("=" * 60)
    
    for i, c in enumerate(crosshairs[:10], 1):
        print(f"  {i:2}. {c['name'][:30]:<30} ({c['copied']:,} copies)")
        print(f"      Code: {c['code'][:50]}...")
    
    print()
    print("[+] Done! Crosshairs saved and ready for UI integration.")


if __name__ == "__main__":
    main()
