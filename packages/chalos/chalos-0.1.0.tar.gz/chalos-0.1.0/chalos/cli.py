from __future__ import annotations

import argparse
import json
import sys
import time
import urllib.request
import urllib.error
import webbrowser
from dataclasses import dataclass, field
from datetime import timezone, timedelta, datetime, time as dtime
from typing import List, Dict, Any, Optional

DEFAULT_LOGO = """ ______     __  __     ______     __         ______     ______   
/\  ___\   /\ \_\ \   /\  __ \   /\ \       /\  __ \   /\  ___\  
\ \ \____  \ \  __ \  \ \  __ \  \ \ \____  \ \ \/\ \  \ \___  \ 
 \ \_____\  \ \_\ \_\  \ \_\ \_\  \ \_____\  \ \_____\  \/\_____\\
  \/_____/   \/_/\/_/   \/_/\/_/   \/_____/   \/_____/   \/_____/
 C H A L O S   C L I   O R D E R I N G
"""

@dataclass
class Location:
    id: str
    name: str

@dataclass
class OpenWindow:
    open: str  # "HH:MM"
    close: str # "HH:MM"

@dataclass
class MenuConfig:
    empanadas: Dict[str, Any]
    breakfast_burrito: Dict[str, Any]
    chicken_sandwich: Dict[str, Any]
    coffee: Dict[str, Any]

@dataclass
class Config:
    restaurant_name: str
    ascii_logo: Optional[str]
    lambda_checkout_url: str
    lambda_menu_url: str
    locations: List[Location]
    open_hours: Dict[str, List[OpenWindow]]

PST = timezone(timedelta(hours=-8))

def now_epoch_millis() -> int:
    return int(datetime.now(PST).timestamp() * 1000)

def hhmm_to_epoch(day: datetime, hhmm: str) -> int:
    hh, mm = map(int, hhmm.split(":"))
    dt = datetime(day.year, day.month, day.day, hh, mm, tzinfo=PST)
    return int(dt.timestamp() * 1000)

def is_open(open_hours: Dict[str, List[OpenWindow]], now_ms: int) -> bool:
    now_dt = datetime.fromtimestamp(now_ms / 1000, PST)
    day_name = now_dt.strftime("%A").lower()
    todays = open_hours.get(day_name, [])
    for w in todays:
        try:
            start_ms = hhmm_to_epoch(now_dt, w.open)
            end_ms = hhmm_to_epoch(now_dt, w.close)
            if end_ms < start_ms:
                end_ms += 24 * 60 * 60 * 1000
            if start_ms <= now_ms <= end_ms:
                return True
        except Exception:
            continue
    return False

def parse_open_hours(raw: Dict[str, Any]) -> Dict[str, List[OpenWindow]]:
    out: Dict[str, List[OpenWindow]] = {}
    for day, windows in raw.items():
        lst: List[OpenWindow] = []
        for w in windows:
            lst.append(OpenWindow(open=w["open"], close=w["close"]))
        out[day.lower()] = lst
    return out

def animatedLogo(logo: str, fast: bool = False) -> None:
    total = 40
    sys.stdout.write("\n")

    if not fast:
        for i in range(total + 1):
            bar = "#" * i + "-" * (total - i)
            percent = int((i / total) * 100)
            sys.stdout.write(f"\rLoading Delicious Data [{bar}] {percent}%")
            sys.stdout.flush()
            sleep_time = 0.1 * (1 - (i / total))**2 + 0.005
            time.sleep(sleep_time)

    for line in logo.splitlines():
        sys.stdout.write("\n")
        for char in line:
            sys.stdout.write(char)
            sys.stdout.flush()
            if not fast:
                time.sleep(0.0001)

    sys.stdout.write("\n\n")
    sys.stdout.flush()

    if not fast:
        time.sleep(1)

def fetch_json(url: str, timeout: float = 10.0) -> Any:
    req = urllib.request.Request(url, headers={"User-Agent": "chalos-cli/0.1"})
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        data = resp.read().decode(charset)
        return json.loads(data)

def post_json(url: str, payload: Any, timeout: float = 10.0) -> Any:
    b = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=b,
        method="POST",
        headers={
            "User-Agent": "chalos-cli/0.1",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        data = resp.read().decode(charset)
        if not data.strip():
            return {}
        return json.loads(data)

def ask_int(prompt: str, valid: List[int]) -> int:
    valid_set = set(valid)
    while True:
        ans = input(f"{prompt} {valid}: ").strip()
        if ans.isdigit() and int(ans) in valid_set:
            return int(ans)
        print(f"Please enter one of {valid}.")

def ask_choice(prompt: str, options: List[str], allow_none: bool=False) -> Optional[str]:
    while True:
        print(prompt)
        for i, opt in enumerate(options, 1):
            print(f"  {i}) {opt}")
        if allow_none:
            print(f"  0) None / Skip")
        sel = input("Select: ").strip()
        if allow_none and sel == "0":
            return None
        if sel.isdigit() and 1 <= int(sel) <= len(options):
            return options[int(sel) - 1]
        print("Invalid selection. Try again.")

def ask_multi_select(prompt: str, options: List[str]) -> List[str]:
    print(prompt)
    for i, opt in enumerate(options, 1):
        print(f"  {i}) {opt}")
    print("Enter numbers separated by commas (or press Enter for none):")
    sel = input("Select: ").strip()
    if not sel:
        return []
    picks = []
    for token in sel.split(","):
        token = token.strip()
        if token.isdigit():
            idx = int(token)
            if 1 <= idx <= len(options):
                picks.append(options[idx-1])
    # de-dup while preserving order
    seen = set()
    out = []
    for p in picks:
        if p not in seen:
            seen.add(p); out.append(p)
    return out

@dataclass
class CartItem:
    kind: str
    details: Dict[str, Any]
    qty: int = 1

@dataclass
class Cart:
    items: List[CartItem] = field(default_factory=list)
    location_id: Optional[str] = None

    def add(self, item: CartItem) -> None:
        self.items.append(item)

    def remove(self, index: int) -> bool:
        if 0 <= index < len(self.items):
            del self.items[index]
            return True
        return False

    def to_payload(self) -> Dict[str, Any]:
        return {
            "location_id": self.location_id,
            "items": [ {"kind": it.kind, "qty": it.qty, "details": it.details} for it in self.items ]
        }

    def show(self) -> None:
        if not self.items:
            print("\nCart is empty.\n")
            return
        print("\n--- Cart ---")
        for idx, it in enumerate(self.items):
            print(f"{idx+1}) {it.kind} x{it.qty} - {json.dumps(it.details)}")
        print("------------\n")

def flow_empanadas(menu: Dict[str, Any], cart: Cart) -> None:
    amounts = [1, 3, 6, 13]
    total = ask_int("How many empanadas?", amounts)
    flavors: List[str] = menu.get("flavors", [])
    if not flavors:
        print("No flavors configured.")
        return
    remaining = total
    picks: Dict[str, int] = {f: 0 for f in flavors}
    print("\nChoose flavors. Type the number; you'll keep picking until the total is reached.")
    while remaining > 0:
        print(f"Remaining: {remaining}")
        for i, f in enumerate(flavors, 1):
            print(f"  {i}) {f} (chosen {picks[f]})")
        sel = input("Select flavor #: ").strip()
        if sel.isdigit():
            idx = int(sel)
            if 1 <= idx <= len(flavors):
                picks[flavors[idx-1]] += 1
                remaining -= 1
                continue
        print("Invalid selection.")
    # compress to only selected flavors
    final = {k: v for k, v in picks.items() if v > 0}
    cart.add(CartItem(kind="empanadas", qty=total, details={"flavors": final}))
    print("Added empanadas to cart.\n")

def flow_breakfast_burrito(menu: Dict[str, Any], cart: Cart) -> None:
    types = menu.get("types", ["bacon", "sausage", "none"])
    salsas = menu.get("salsas", ["spicy", "mild", "none"])
    mods = menu.get("modifiers", ["avocado", "sour cream", "no cheese"])
    burritoType = ask_choice("Choose your burrito:", types)
    salsa = ask_choice("Choose salsa:", salsas)
    chosen_mods = ask_multi_select("Add modifiers (optional):", mods)
    cart.add(CartItem(kind="breakfast_burrito", details={
        "type": burritoType, "salsa": salsa, "modifiers": chosen_mods
    }))
    print("Added breakfast burrito to cart.\n")

def flow_coffee(menu: Dict[str, Any], cart: Cart) -> None:
    versions: List[str] = menu.get("versions", [])
    if not versions:
        print("No coffee sizes configured.")
        return
    print("\nChoose a coffee size:")
    for i, v in enumerate(versions, 1):
        print(f"  {i}) {v}")
    sel = input("Select size #: ").strip()
    if sel.isdigit():
        idx = int(sel)
        if 1 <= idx <= len(versions):
            choice = versions[idx - 1]
            cart.add(CartItem(kind="coffee", qty=1, details={"size": choice}))
            print(f"Added {choice} coffee to cart.\n")
            return
    print("Invalid selection.\n")

def flow_chicken_sandwich(menu: Dict[str, Any], cart: Cart) -> None:
    versions = menu.get("versions", ["classic", "spicy"])
    mods = menu.get("modifiers", ["no cheese", "no slaw", "no sauce"])
    version = ask_choice("Choose chicken sandwich version:", versions)
    chosen_mods = ask_multi_select("Add modifiers (optional):", mods)
    cart.add(CartItem(kind="chicken_sandwich", details={
        "version": version, "modifiers": chosen_mods
    }))
    print("Added chicken sandwich to cart.\n")

def edit_cart(cart: Cart) -> None:
    while True:
        cart.show()
        if not cart.items:
            return
        print("Options:")
        print("  1) Remove an item")
        print("  2) Go back")
        sel = input("Select: ").strip()
        if sel == "1":
            idx = input("Enter item number to remove: ").strip()
            if idx.isdigit():
                ok = cart.remove(int(idx)-1)
                if not ok:
                    print("Invalid item number.")
            else:
                print("Please enter a number.")
        elif sel == "2":
            return
        else:
            print("Invalid selection.")

def main(argv: Optional[List[str]] = None) -> int:
    try:
        return _main(argv)
    except KeyboardInterrupt:
        print("\nGoodbye!")
        return 130

def _main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Restaurant CLI")
    parser.add_argument(
        "--configOverride",
        help="Path to local JSON config override"
    )
    parser.add_argument(
        "--fast",
        action="store_true",
        help="Disable animated logo, get the menu faster (for when you are REALLY hungry)"
    )
    args = parser.parse_args(argv)
    animatedLogo(DEFAULT_LOGO,args.fast)

    base_url = "https://chalos.s3.us-east-2.amazonaws.com/config.json"
    raw = None
    if args.configOverride:
        try:
            with open(args.configOverride, "r", encoding="utf-8") as f:
                raw = json.load(f)
        except Exception as e:
            print(f"Failed to load local config file {args.configOverride}: {e}")
            return 1
    else:
        try:
            raw = fetch_json(base_url)
        except urllib.error.HTTPError as e:
            print(f"Failed to fetch base config (HTTP {e.code}).")
            return 1
        except Exception as e:
            print(f"Failed to fetch base config: {e}")
            return 1

    try:
        locations = [Location(**loc) for loc in raw["locations"]]
        open_hours: Dict[str, Dict[str, List[OpenWindow]]] = {}
        for loc_id, hours in raw["open_hours"].items():
            open_hours[loc_id] = parse_open_hours(hours)

        cfg = Config(
            restaurant_name=raw["restaurant_name"],
            ascii_logo=raw.get("ascii_logo"),
            lambda_checkout_url=raw["lambda_checkout_url"],
            lambda_menu_url=raw["lambda_menu_url"],
            locations=locations,
            open_hours=open_hours,
        )
    except KeyError as e:
        print(f"Invalid config; missing key: {e}")
        return 1

    # Choose location
    print("Choose your location:")
    for i, loc in enumerate(cfg.locations, 1):
        print(f"  {i}) {loc.name}")
    loc_idx = None
    while True:
        sel = input("Select: ").strip()
        if sel.isdigit() and 1 <= int(sel) <= len(cfg.locations):
            loc_idx = int(sel) - 1
            break
        print("Invalid selection.")

    selected_location = cfg.locations[loc_idx]
    cart = Cart(location_id=selected_location.id)

    # Check open hours
    now_ms = now_epoch_millis()
    loc_open_hours = cfg.open_hours.get(selected_location.id, {})
    if not is_open(loc_open_hours, now_ms):
        now_dt = datetime.fromtimestamp(now_ms / 1000, PST)
        print(f"Sorry, {selected_location.name} is currently CLOSED (PST).")
        return 0

    # Grab menu from lambda which will remove out of stock items
    try:
        menu = post_json(cfg.lambda_menu_url, {
            "location_id": selected_location.id
        })
    except Exception as e:
        print(f"Failed to fetch menu from Lambda: {e}")
        return 1

    # Menu loop
    while True:
        cart.show()
        print("\nMain Menu:")
        opts = []
        if "empanadas" in menu:
            print("  1) Empanadas"); opts.append("empanadas")
        if "breakfast_burrito" in menu:
            print("  2) Breakfast Burrito"); opts.append("breakfast_burrito")
        if "chicken_sandwich" in menu:
            print("  3) Chicken Sandwich"); opts.append("chicken_sandwich")
        if "coffee" in menu:
            print("  4) Coffee"); opts.append("coffee")
        print("  5) Edit Cart")
        print("  6) Checkout")
        print("  7) Exit")

        sel = input("Select: ").strip()
        if sel == "1" and "empanadas" in menu:
            flow_empanadas(menu["empanadas"], cart)
        elif sel == "2" and "breakfast_burrito" in menu:
            flow_breakfast_burrito(menu["breakfast_burrito"], cart)
        elif sel == "3" and "chicken_sandwich" in menu:
            flow_chicken_sandwich(menu["chicken_sandwich"], cart)
        elif sel == "4" and "coffee" in menu:
            flow_coffee(menu["coffee"], cart)
        elif sel == "5":
            edit_cart(cart)
        elif sel == "6":
            payload = cart.to_payload()
            try:
                resp = post_json(cfg.lambda_checkout_url, payload)
            except Exception as e:
                print(f"Checkout failed: {e}")
                continue
            checkout_url = (resp or {}).get("checkout_url")
            if not checkout_url:
                print("Checkout response missing 'checkout_url'.")
                continue
            print("Opening checkout in your browser...")
            webbrowser.open(checkout_url, new=2, autoraise=True)
            print("Thank you!")
            return 0
        elif sel == "7":
            print("Goodbye!")
            return 0
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    sys.exit(main())
