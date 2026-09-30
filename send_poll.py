import os
import sys
import requests

TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
CHAT_ID = os.environ["TELEGRAM_CHAT_ID"]

POLLS = {
    "monday": {
        "question": "삼일예배 사전출결 설문에 참여해주세요",
        "options": [
            "정오예배",
            "저녁예배",
            "타교회 대면예배",
            "목,금 대체예배",
            "불참",
        ],
    },
    "friday": {
        "question": "주일예배 사전출결 설문에 참여해주세요",
        "options": [
            "정오예배",
            "오후예배",
            "저녁예배",
            "타교회 대면예배",
            "월,화 대체예배",
            "불참",
        ],
    },
}

poll = POLLS[sys.argv[1]]

response = requests.post(
    f"https://api.telegram.org/bot{TOKEN}/sendPoll",
    json={
        "chat_id": CHAT_ID,
        "message_thread_id": 3,
        "question": poll["question"],
        "options": [{"text": option} for option in poll["options"]],
        "is_anonymous": False,
        "allows_multiple_answers": False,
    },
    timeout=30,
)


if not response.ok:
    print("Telegram error:", response.status_code, response.text)

response.raise_for_status()
print("Poll sent successfully.")
