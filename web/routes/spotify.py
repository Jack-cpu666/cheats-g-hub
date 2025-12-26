"""
Spotify Integration for Full Access Members
Provides search, streaming, and playlist functionality using YouTube as audio source
"""

from flask import Blueprint, jsonify, request
import subprocess
import json
import os
import hashlib
import threading
import re

spotify_bp = Blueprint('spotify', __name__)

# Cache directory for downloaded audio
CACHE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.spotify_cache')
os.makedirs(CACHE_DIR, exist_ok=True)

# Popular tracks data (fallback when API unavailable)
POPULAR_TRACKS = [
    {"title": "Blinding Lights", "artist": "The Weeknd", "thumbnail": "https://i.scdn.co/image/ab67616d0000b2738863bc11d2aa12b54f5aeb36"},
    {"title": "Shape of You", "artist": "Ed Sheeran", "thumbnail": "https://i.scdn.co/image/ab67616d0000b273ba5db46f4b838ef6027e6f96"},
    {"title": "Dance Monkey", "artist": "Tones and I", "thumbnail": "https://i.scdn.co/image/ab67616d0000b273c6f7af36ecdc3ed6e0a1f169"},
    {"title": "Rockstar", "artist": "Post Malone ft. 21 Savage", "thumbnail": "https://i.scdn.co/image/ab67616d0000b2739478c87599550dd73bfa7e02"},
    {"title": "Someone You Loved", "artist": "Lewis Capaldi", "thumbnail": "https://i.scdn.co/image/ab67616d0000b273fc2101e6889d6ce9025f85f2"},
    {"title": "Señorita", "artist": "Shawn Mendes & Camila Cabello", "thumbnail": "https://i.scdn.co/image/ab67616d0000b273c1db37b16b6aa9999e7b5cf3"},
    {"title": "Bad Guy", "artist": "Billie Eilish", "thumbnail": "https://i.scdn.co/image/ab67616d0000b27350a3147b4edd7701a876c6ce"},
    {"title": "Sunflower", "artist": "Post Malone & Swae Lee", "thumbnail": "https://i.scdn.co/image/ab67616d0000b27392f6e4fa1c17c9c5c2c4e6c6"},
    {"title": "Without Me", "artist": "Halsey", "thumbnail": "https://i.scdn.co/image/ab67616d0000b273d48ac38a87bb3aa9f98da3ad"},
    {"title": "Happier", "artist": "Marshmello & Bastille", "thumbnail": "https://i.scdn.co/image/ab67616d0000b2739abf7d2f2ad11af3def3b610"},
]

# Playlists
PLAYLISTS = {
    "top50": [
        {"title": "Paint The Town Red", "artist": "Doja Cat", "thumbnail": ""},
        {"title": "Vampire", "artist": "Olivia Rodrigo", "thumbnail": ""},
        {"title": "Cruel Summer", "artist": "Taylor Swift", "thumbnail": ""},
        {"title": "Last Night", "artist": "Morgan Wallen", "thumbnail": ""},
        {"title": "Flowers", "artist": "Miley Cyrus", "thumbnail": ""},
        {"title": "Kill Bill", "artist": "SZA", "thumbnail": ""},
        {"title": "Karma", "artist": "Taylor Swift", "thumbnail": ""},
        {"title": "Anti-Hero", "artist": "Taylor Swift", "thumbnail": ""},
        {"title": "Creepin'", "artist": "Metro Boomin, The Weeknd, 21 Savage", "thumbnail": ""},
        {"title": "Boy's a Liar Pt. 2", "artist": "PinkPantheress, Ice Spice", "thumbnail": ""},
    ],
    "gaming": [
        {"title": "Warriors", "artist": "Imagine Dragons", "thumbnail": ""},
        {"title": "Legends Never Die", "artist": "League of Legends, Against The Current", "thumbnail": ""},
        {"title": "RISE", "artist": "League of Legends, The Glitch Mob, Mako", "thumbnail": ""},
        {"title": "Enemy", "artist": "Imagine Dragons & JID", "thumbnail": ""},
        {"title": "Centuries", "artist": "Fall Out Boy", "thumbnail": ""},
        {"title": "Believer", "artist": "Imagine Dragons", "thumbnail": ""},
        {"title": "Natural", "artist": "Imagine Dragons", "thumbnail": ""},
        {"title": "Thunder", "artist": "Imagine Dragons", "thumbnail": ""},
        {"title": "Whatever It Takes", "artist": "Imagine Dragons", "thumbnail": ""},
        {"title": "Radioactive", "artist": "Imagine Dragons", "thumbnail": ""},
    ],
    "chill": [
        {"title": "Sweater Weather", "artist": "The Neighbourhood", "thumbnail": ""},
        {"title": "Somewhere Only We Know", "artist": "Keane", "thumbnail": ""},
        {"title": "Chasing Cars", "artist": "Snow Patrol", "thumbnail": ""},
        {"title": "The Night We Met", "artist": "Lord Huron", "thumbnail": ""},
        {"title": "Electric Feel", "artist": "MGMT", "thumbnail": ""},
        {"title": "Little Dark Age", "artist": "MGMT", "thumbnail": ""},
        {"title": "Notion", "artist": "The Rare Occasions", "thumbnail": ""},
        {"title": "Sofia", "artist": "Clairo", "thumbnail": ""},
        {"title": "Line Without a Hook", "artist": "Ricky Montgomery", "thumbnail": ""},
        {"title": "Heather", "artist": "Conan Gray", "thumbnail": ""},
    ],
    "hiphop": [
        {"title": "HUMBLE.", "artist": "Kendrick Lamar", "thumbnail": ""},
        {"title": "God's Plan", "artist": "Drake", "thumbnail": ""},
        {"title": "Sicko Mode", "artist": "Travis Scott", "thumbnail": ""},
        {"title": "Lucid Dreams", "artist": "Juice WRLD", "thumbnail": ""},
        {"title": "XO Tour Llif3", "artist": "Lil Uzi Vert", "thumbnail": ""},
        {"title": "Congratulations", "artist": "Post Malone ft. Quavo", "thumbnail": ""},
        {"title": "Hot N*gga", "artist": "Bobby Shmurda", "thumbnail": ""},
        {"title": "Mo Bamba", "artist": "Sheck Wes", "thumbnail": ""},
        {"title": "Goosebumps", "artist": "Travis Scott ft. Kendrick Lamar", "thumbnail": ""},
        {"title": "DNA.", "artist": "Kendrick Lamar", "thumbnail": ""},
    ]
}


def get_cache_path(query):
    """Generate a cache file path for a query"""
    hash_str = hashlib.md5(query.encode()).hexdigest()
    return os.path.join(CACHE_DIR, f"{hash_str}.mp3")


def search_youtube(query, max_results=10):
    """Search YouTube for tracks matching query using yt-dlp library"""
    try:
        import yt_dlp
        
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'extract_flat': True,
            'force_generic_extractor': False,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(f"ytsearch{max_results}:{query}", download=False)
        
        if not result or 'entries' not in result:
            return []
        
        tracks = []
        for entry in result['entries']:
            if entry:
                # Skip songs shorter than 60 seconds
                duration = entry.get('duration', 0)
                if duration and duration < 60:
                    continue
                    
                thumbnail = ''
                if entry.get('thumbnails'):
                    thumbnail = entry['thumbnails'][-1].get('url', '')
                elif entry.get('thumbnail'):
                    thumbnail = entry['thumbnail']
                
                tracks.append({
                    'title': entry.get('title', 'Unknown'),
                    'artist': entry.get('uploader', entry.get('channel', 'Unknown Artist')),
                    'thumbnail': thumbnail,
                    'duration': format_duration(duration),
                    'duration_seconds': duration,
                    'url': entry.get('url', entry.get('webpage_url', ''))
                })
        
        return tracks
    except Exception as e:
        print(f"[Spotify] Search error: {e}")
        return []


def format_duration(seconds):
    """Format duration in seconds to mm:ss"""
    if not seconds:
        return ""
    mins = int(seconds) // 60
    secs = int(seconds) % 60
    return f"{mins}:{secs:02d}"


def get_stream_url(query):
    """Get direct audio stream URL for a query using yt-dlp library"""
    try:
        import yt_dlp
        
        # Check cache first
        cache_path = get_cache_path(query)
        if os.path.exists(cache_path):
            return f"/api/spotify/audio/{hashlib.md5(query.encode()).hexdigest()}"
        
        ydl_opts = {
            'quiet': True,
            'no_warnings': True,
            'format': 'bestaudio[ext=m4a]/bestaudio/best',
            'extract_flat': False,
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            result = ydl.extract_info(f"ytsearch1:{query}", download=False)
        
        if result and 'entries' in result and result['entries']:
            entry = result['entries'][0]
            # Get the audio URL
            if entry.get('url'):
                return entry['url']
            elif entry.get('formats'):
                # Find best audio format
                for fmt in reversed(entry['formats']):
                    if fmt.get('acodec') != 'none' and fmt.get('url'):
                        return fmt['url']
        
        return None
    except Exception as e:
        print(f"[Spotify] Stream URL error: {e}")
        return None


@spotify_bp.route('/api/spotify/search', methods=['POST'])
def api_spotify_search():
    """Search for tracks"""
    try:
        data = request.get_json()
        query = data.get('query', '')
        
        if not query:
            return jsonify({'success': False, 'message': 'No query provided'})
        
        tracks = search_youtube(query)
        
        return jsonify({
            'success': True,
            'tracks': tracks
        })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})


@spotify_bp.route('/api/spotify/stream', methods=['POST'])
def api_spotify_stream():
    """Get stream URL for a track"""
    try:
        data = request.get_json()
        query = data.get('query', '')
        
        if not query:
            return jsonify({'success': False, 'message': 'No query provided'})
        
        stream_url = get_stream_url(query)
        
        if stream_url:
            return jsonify({
                'success': True,
                'stream_url': stream_url
            })
        else:
            return jsonify({
                'success': False,
                'message': 'Could not get stream URL'
            })
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)})


@spotify_bp.route('/api/spotify/popular')
def api_spotify_popular():
    """Get popular tracks"""
    return jsonify({
        'success': True,
        'tracks': POPULAR_TRACKS
    })


@spotify_bp.route('/api/spotify/playlist/<playlist_type>')
def api_spotify_playlist(playlist_type):
    """Get a preset playlist"""
    tracks = PLAYLISTS.get(playlist_type, [])
    return jsonify({
        'success': True,
        'tracks': tracks
    })


@spotify_bp.route('/api/spotify/audio/<file_hash>')
def api_spotify_audio(file_hash):
    """Serve cached audio file"""
    from flask import send_file
    
    cache_path = os.path.join(CACHE_DIR, f"{file_hash}.mp3")
    
    if os.path.exists(cache_path):
        return send_file(cache_path, mimetype='audio/mpeg')
    
    return jsonify({'error': 'File not found'}), 404
