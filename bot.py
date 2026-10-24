# -gold-ai-signal-botimport os
import requests
from datetime import datetime, timezone

TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

def send_message(message):
    if not TOKEN or not CHAT_ID:
        print("Telegram settings are missing.")
        return

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    response = requests.post(
        url,
        json={"chat_id": CHAT_ID, "text": message},
        timeout=15
    )
    response.raise_for_status()

def main():
    message = (
        "🤖 Gold AI Signal Bot\n\n"
        "🟡 Status: SETUP IN PROGRESS\n"
        "📊 Pair: XAUUSD\n"
        "⏱️ Timeframe: M5\n\n"
        "No live signal yet. Market data must be connected "
        "before BUY or SELL signals can be generated.\n\n"
        f"Checked: {datetime.now(timezone.utc).strftime('%H:%M UTC')}"
    )
    send_message(message)

if __name__ == "__main__":
    main()
