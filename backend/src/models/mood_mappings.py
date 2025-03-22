"""
Contains the mood mapping models for genre and activity suggestions.
"""

# Mood-to-genre mapping
mood_to_genre = {
    'sadness': 'blues',
    'anger': 'rock',
    'fear': 'electronic',
    'disgust': 'metal',
    'surprise': 'pop',
    'happiness': 'pop',
    'love': 'romantic',
    'calm': 'chill',
    'anxiety': 'ambient',
    'cheerful': 'pop',
    'content': 'acoustic',
    'empty mood': 'ambient',
    'enjoyment': 'dance',
    'amusement': 'indie',
    'average mood': 'jazz',
    'charitable': 'classical',
    'confused': 'experimental',
    'empathetic': 'soul',
    'envy': 'hip-hop',
    'irritability': 'punk',
    'lonely': 'lo-fi',
    'shame': 'gothic',
    'joy': 'jazz'
}

# Mood-to-activity mapping
mood_to_activity = {
    'sadness': 'Take a walk outside to clear your mind.',
    'anger': 'Try meditation or some breathing exercises.',
    'fear': 'Engage in a relaxing activity like deep breathing.',
    'disgust': 'Take a moment for self-care, maybe with a warm bath.',
    'surprise': 'Try something spontaneous and fun!',
    'happiness': 'Dance to your favorite songs.',
    'love': 'Spend quality time with a loved one.',
    'calm': 'Read a book or enjoy some quiet time.',
    'anxiety': 'Practice mindfulness and relaxation techniques.',
    'cheerful': 'Enjoy an outdoor activity or explore a new hobby.',
    'joy': 'Enjoy an outdoor activity or explore a new hobby',
    'content': 'Enjoy a cup of tea and unwind.',
    'empty mood': 'Take a break and spend time in nature.',
    'enjoyment': 'Go for a jog or enjoy a dance party.',
    'amusement': 'Watch a comedy show or play a fun game.',
    'average mood': 'Engage in a hobby that brings you joy.',
    'charitable': 'Volunteer or help someone in need.',
    'confused': 'Take some time to relax and clear your mind.',
    'empathetic': 'Spend time with loved ones or engage in helping others.',
    'envy': 'Focus on personal growth and take time for yourself.',
    'irritability': 'Try deep breathing exercises or a physical workout.',
    'lonely': 'Reach out to friends or do something creative.',
    'shame': 'Practice self-compassion and try journaling.',
} 