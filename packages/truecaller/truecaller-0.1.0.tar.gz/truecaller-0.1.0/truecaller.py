#!/usr/bin/env python3
import argparse
import requests
import subprocess
import json
import sys
import time
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn
from rich.panel import Panel

# --- Settings ---
WORKER_API = "https://truecaller.wasdark336.workers.dev/index.cpp"
WORKER_KEY = "dark"

CLEAROUT_URL = "https://api.clearoutphone.io/v1/phonenumber/validate"
CLEAROUT_TOKEN = "ccd95e9fa49159a72e8bdcdcb5f839ef:eae98d375a5d99ee9cd4e9ad0410d75f3877d72652083ef85915cb0942b30444"

console = Console()

# ----------- API Fetchers -----------

def fetch_worker(number: str):
    url = f"{WORKER_API}?key={WORKER_KEY}&number={number}"
    try:
        result = subprocess.run(
            ["curl", "-s", url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=10
        )
        output = result.stdout.decode("utf-8").strip()
        try:
            return json.loads(output)
        except json.JSONDecodeError:
            return {"error": "Failed to parse Worker response"}
    except Exception as e:
        console.print(f"[bold red]❌ Worker API Error:[/bold red] {e}")
        return {}

def fetch_clearout(number: str):
    headers = {
        "Authorization": f"Bearer {CLEAROUT_TOKEN}",  # ✅ correct format
        "Content-Type": "application/json"
    }
    payload = {
        "number": number,
        "country_code": "IN"
    }
    try:
        response = requests.post(CLEAROUT_URL, headers=headers, json=payload, timeout=10)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        console.print(f"[bold red]❌ Clearout API Error:[/bold red] {e}")
        return {}

# ----------- Merge + Display -----------

def build_summary(worker_data, clearout_data):
    """Return merged data as dict."""
    name = "-"
    carrier = "-"
    country = "-"
    spam = "-"
    number = "-"

    # Worker API
    if worker_data:
        if isinstance(worker_data, list) and worker_data:
            w = worker_data[0]
        else:
            w = worker_data
        name = w.get("name", "-")
        carrier = w.get("carrier", "-")
        number = w.get("phone_number") or w.get("formatted_number", "-")
        spam = w.get("spam_flag", "-")

    # Clearout API
    if clearout_data:
        data = clearout_data.get("data", {})
        if data.get("country_name"):
            country = data.get("country_name")
        elif data.get("country"):
            country = data.get("country")

        if data.get("carrier") and carrier == "-":
            carrier = data.get("carrier")

        if number == "-" and data.get("international_format"):
            number = data.get("international_format")

    return {
        "name": name,
        "number": number,
        "carrier": carrier,
        "country": country,
        "spam": spam,
    }

def display_summary(summary):
    """Pretty print using Rich."""
    spam_value = summary["spam"]

    if spam_value in ["-", "0", 0, None]:
        spam_display = "[green]Safe[/green]"
    else:
        spam_display = f"[red]Spam ({spam_value})[/red]"

    panel_text = f"""
[bold cyan]Name:[/bold cyan] {summary['name']}
[bold cyan]Number:[/bold cyan] {summary['number']}
[bold cyan]Carrier:[/bold cyan] {summary['carrier']}
[bold cyan]Country:[/bold cyan] {summary['country']}
[bold cyan]Spam Flag:[/bold cyan] {spam_display}
[bold cyan]Developer:[/bold cyan] Darkboy
"""
    console.print(Panel(panel_text, title="📞 Truecaller", subtitle="Merged View", style="bold green"))

# ----------- Public Function -----------

def search_num(number: str):
    """Reusable function for import."""
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="🍳 Cooking your number 🔥", total=None)
        time.sleep(1.2)

    worker_data = fetch_worker(number)
    clearout_data = fetch_clearout(number)
    return build_summary(worker_data, clearout_data)

# ----------- CLI Entry -----------

def main():
    parser = argparse.ArgumentParser(description="Truecaller Lookup CLI")
    parser.add_argument("-s", "--search", required=True, help="Phone number to search")
    args = parser.parse_args()

    number = args.search.strip()

    summary = search_num(number)

    console.print("\n[bold underline green]✅ Lookup Complete[/bold underline green]\n")
    display_summary(summary)

if __name__ == "__main__":
    main()
