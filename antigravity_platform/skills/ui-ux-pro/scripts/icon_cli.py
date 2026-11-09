"""
UI/UX Pro Icon Helper CLI
Provides fast lookup and code generation for professional vector SVG icons.
"""

import sys
import os
import json
import argparse

RESOURCES_DIR = os.path.join(os.path.dirname(__file__), "..", "resources")
ICONS_FILE = os.path.join(RESOURCES_DIR, "icons.json")


def load_icons():
    if not os.path.exists(ICONS_FILE):
        return {}
    with open(ICONS_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("categories", {})


def get_all_icons_flat(categories):
    flat = {}
    for cat, icons in categories.items():
        for name, svg in icons.items():
            flat[name] = {"category": cat, "svg": svg}
    return flat


def format_svg(svg: str, size: int = None, color: str = None, class_name: str = None):
    res = svg
    if size:
        res = res.replace('width="20"', f'width="{size}"').replace('height="20"', f'height="{size}"')
    if class_name:
        res = res.replace('<svg ', f'<svg class="{class_name}" ')
    return res


def main():
    parser = argparse.ArgumentParser(description="UI/UX Pro Professional Vector Icon CLI")
    parser.add_argument("name", nargs="?", help="Icon name to retrieve (e.g. search, check, filter)")
    parser.add_argument("--list", "-l", action="store_true", help="List all available icons")
    parser.add_argument("--search", "-s", type=str, help="Search icons by keyword")
    parser.add_argument("--size", type=int, default=20, help="Width/Height in pixels (default: 20)")
    parser.add_argument("--class-name", "-c", type=str, help="CSS classes to inject (e.g. 'w-4 h-4 text-blue-500')")
    parser.add_argument("--jsx", action="store_true", help="Format for React JSX (camelCase attributes)")

    args = parser.parse_args()
    categories = load_icons()
    flat = get_all_icons_flat(categories)

    if args.list:
        print("# Available Professional Vector Icons (UI/UX Pro)\n")
        for cat, icons in categories.items():
            print(f"### Category: {cat.capitalize()} ({len(icons)} icons)")
            icon_names = sorted(icons.keys())
            print(", ".join(icon_names))
            print()
        print(f"Total Icons: {len(flat)}")
        return

    if args.search:
        q = args.search.lower()
        matches = {k: v for k, v in flat.items() if q in k or q in v["category"]}
        print(f"Found {len(matches)} matching icons for '{q}':\n")
        for name, info in sorted(matches.items()):
            print(f"- **{name}** (Category: {info['category']})")
        return

    if args.name:
        name = args.name.lower()
        if name in flat:
            svg = flat[name]["svg"]
            formatted = format_svg(svg, size=args.size, class_name=args.class_name)
            if args.jsx:
                formatted = formatted.replace("stroke-width", "strokeWidth")
                formatted = formatted.replace("stroke-linecap", "strokeLinecap")
                formatted = formatted.replace("stroke-linejoin", "strokeLinejoin")
                formatted = formatted.replace("class=", "className=")
            print(formatted)
        else:
            print(f"Error: Icon '{name}' not found. Run with --list or --search.", file=sys.stderr)
            sys.exit(1)
        return

    parser.print_help()


if __name__ == "__main__":
    main()

