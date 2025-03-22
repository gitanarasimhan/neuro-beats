"""
Route handlers for mood-based recommendations.
"""
from flask import Blueprint, request, jsonify
from ..services.mood_service import MoodService
from ..services.spotify_service import SpotifyService
from ..models.mood_mappings import mood_to_genre, mood_to_activity

bp = Blueprint('recommendation', __name__)
mood_service = MoodService()
spotify_service = SpotifyService()

@bp.route('/recommend', methods=['POST'])
def recommend():
    """
    Get personalized recommendations based on user's mood.
    """
    data = request.get_json()
    user_input = data.get('input')

    # Step 1: Detect mood from input text
    detected_mood = mood_service.detect_mood(user_input)

    # Step 2: Get corresponding music genre from mood
    genre = mood_to_genre.get(detected_mood, 'pop')

    # Step 3: Get Spotify recommendations
    playlist_url = spotify_service.get_recommendations(genre)

    # Step 4: Get activity suggestion
    activity_suggestion = mood_to_activity.get(
        detected_mood, 
        'Take some time for self-care and relax.'
    )

    # Step 5: Create response
    response = {
        'mood': detected_mood,
        'music_suggestion': genre,
        'spotify_playlist_url': playlist_url,
        'activity_suggestion': activity_suggestion
    }

    return jsonify(response) 