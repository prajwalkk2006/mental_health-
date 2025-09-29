RECOMMENDATIONS = {
    "happy": [
        "Share your joy with someone you care about.",
        "Write down what made you happy today."
    ],
    "sad": [
        "Try a short walk in fresh air.",
        "Write down 3 positive things in your life."
    ],
    "angry": [
        "Take 10 deep breaths before reacting.",
        "Try counting backwards from 20 slowly."
    ],
    "fear": [
        "Practice grounding: 5 things you see, 4 you touch, 3 you hear.",
        "Do 2 minutes of slow breathing."
    ],
    "love": [
        "Send a message of appreciation to a loved one.",
        "Write down why you value this relationship."
    ],
    "neutral": [
        "Take a short mindful break.",
        "Stretch your body for 2 minutes."
    ]
}

def get_recommendations(emotion):
    return RECOMMENDATIONS.get(emotion, RECOMMENDATIONS["neutral"])
