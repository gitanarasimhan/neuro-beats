import React, { useState, useCallback, memo } from 'react';
import PropTypes from 'prop-types';
import logo from './assets/neuro-beats.png';
import './App.css';

// API Constants
const API_ENDPOINT = process.env.REACT_APP_API_ENDPOINT || 'https://localhost:5000';
const RECOMMEND_ENDPOINT = `${API_ENDPOINT}/recommend`;

// Error Boundary Component
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }

  static getDerivedStateFromError(error) {
    return { hasError: true };
  }

  componentDidCatch(error, errorInfo) {
    console.error('Error caught by boundary:', error, errorInfo);
  }

  render() {
    if (this.state.hasError) {
      return (
        <div className="error-container">
          <h2>Oops! Something went wrong.</h2>
          <button onClick={() => window.location.reload()}>Refresh Page</button>
        </div>
      );
    }
    return this.props.children;
  }
}

ErrorBoundary.propTypes = {
  children: PropTypes.node.isRequired,
};

// Memoized Result Component
const ResultDisplay = memo(({ result }) => {
  if (!result) return null;

  return (
    <div className="result-container">
      <h3 className="mood-heading">Detected Mood: <em>{result.mood}</em></h3>
      <p><strong>🎶 Genre:</strong> {result.music_suggestion}</p>
      <p><strong>Suggested Activity:</strong> {result.activity_suggestion}</p>

      <div className="spotify-container">
        <iframe
          src={`https://open.spotify.com/embed/playlist/${result.spotify_playlist_url.split('/').pop()}`}
          width="100%"
          height="380"
          allowtransparency="true"
          allow="encrypted-media"
          title="Spotify playlist"
        ></iframe>
      </div>

      <p>
        <a 
          href={result.spotify_playlist_url} 
          target="_blank" 
          rel="noopener noreferrer" 
          className="spotify-link"
          aria-label="Open full Spotify playlist in a new tab"
        >
          🔗 Open full Spotify playlist
        </a>
      </p>
    </div>
  );
});

ResultDisplay.propTypes = {
  result: PropTypes.shape({
    mood: PropTypes.string.isRequired,
    music_suggestion: PropTypes.string.isRequired,
    activity_suggestion: PropTypes.string.isRequired,
    spotify_playlist_url: PropTypes.string.isRequired,
  }),
};

ResultDisplay.displayName = 'ResultDisplay';

export default function App() {
  const [input, setInput] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleSubmit = useCallback(async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    if (!input.trim()) {
      setError('Please enter how you are feeling');
      setLoading(false);
      return;
    }

    try {
      const res = await fetch(RECOMMEND_ENDPOINT, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ input }),
      });

      if (!res.ok) {
        throw new Error(`HTTP error! status: ${res.status}`);
      }

      const data = await res.json();
      setResult(data);
    } catch (error) {
      console.error('Error fetching recommendation:', error);
      setError('Failed to get recommendation. Please try again later.');
    } finally {
      setLoading(false);
    }
  }, [input]);

  const extractYouTubeEmbedUrl = (url) => {
    const searchParams = new URLSearchParams(url.split('?')[1]);
    const query = searchParams.get('search_query');
    if (query) {
      return `https://www.youtube.com/embed?autoplay=1&listType=search&list=${encodeURIComponent(query)}`;
    }
    return null;
  };

  return (
    <ErrorBoundary>
      <div className="app-container">
        <header className="app-header">
          <img src={logo} alt="Neurobeats Logo" className="app-logo" />
          <span className="app-title">Neurobeats</span>
        </header>

        <main className="main-content">
          <h1 className="main-heading">🎧 Tune Into Your Mood 🎵</h1>
          
          <form onSubmit={handleSubmit} aria-label="Mood input form">
            <textarea
              className="mood-textarea"
              placeholder="How are you feeling today?"
              value={input}
              onChange={(e) => setInput(e.target.value)}
              aria-label="Enter your current mood"
              required
            />
            <button
              type="submit"
              disabled={loading}
              className="submit-button"
              aria-busy={loading}
            >
              {loading ? 'Getting your recommendations...' : 'Get Recommendation'}
            </button>
          </form>

          {error && (
            <div className="error-message" role="alert">
              {error}
            </div>
          )}

          <ResultDisplay result={result} />
        </main>

        <footer className="app-footer">
          <p>&copy; {new Date().getFullYear()} Neurobeats. Crafted with 🎶 and ☕.</p>
        </footer>
      </div>
    </ErrorBoundary>
  );
}


