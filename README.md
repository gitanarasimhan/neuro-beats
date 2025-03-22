# AI Song Recommender

A full-stack application that recommends songs based on mood using AI and Spotify's API.

## Project Structure

```
ai-song-recommender/
├── backend/
│   ├── src/
│   │   ├── __init__.py
│   │   ├── app.py
│   │   ├── config.py
│   │   ├── models/
│   │   ├── routes/
│   │   └── services/
│   ├── tests/
│   ├── config/
│   ├── requirements.txt
│   └── env.template
├── frontend/
│   └── song-recommender-frontend/
│       ├── src/
│       ├── public/
│       ├── package.json
│       └── .env.template
└── README.md
```

## Setup Instructions

### Backend Setup

1. Create a virtual environment:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   ```bash
   cp env.template .env
   ```
   Then edit `.env` with your actual credentials.

### Frontend Setup

1. Install dependencies:
   ```bash
   cd frontend/song-recommender-frontend
   npm install
   ```

2. Set up environment variables:
   ```bash
   cp .env.template .env.local
   ```
   Then edit `.env.local` with your configuration.

## Running the Application

### Backend
```bash
cd backend
flask run
```

### Frontend
```bash
cd frontend/song-recommender-frontend
npm start
```

## Environment Variables

### Backend Variables
- `FLASK_ENV`: Application environment (development/production)
- `SECRET_KEY`: Flask secret key
- `SPOTIFY_CLIENT_ID`: Your Spotify API client ID
- `SPOTIFY_CLIENT_SECRET`: Your Spotify API client secret
- `DATABASE_URL`: Database connection string
- `CORS_ORIGINS`: Allowed CORS origins

### Frontend Variables
- `REACT_APP_API_ENDPOINT`: Backend API endpoint
- `REACT_APP_ENV`: Application environment
- `REACT_APP_ANALYTICS_ID`: (Optional) Analytics ID
- `REACT_APP_ERROR_REPORTING`: (Optional) Enable error reporting
- `REACT_APP_ENABLE_YOUTUBE`: (Optional) Enable YouTube integration
- `REACT_APP_ENABLE_DARK_MODE`: (Optional) Enable dark mode feature

## Development

### Code Style
- Backend: Uses Black for Python code formatting
- Frontend: Uses Prettier for JavaScript code formatting

### Testing
- Backend: `pytest`
- Frontend: `npm test`

## Production Deployment

### Backend
1. Set `FLASK_ENV=production`
2. Use gunicorn for serving:
   ```bash
   gunicorn -w 4 "src.app:create_app()"
   ```

### Frontend
1. Build the production bundle:
   ```bash
   npm run build
   ```
2. Serve using a static file server

## Security Notes

- Never commit `.env` files
- Keep API keys and secrets secure
- Use HTTPS in production
- Implement rate limiting
- Set up proper CORS configuration 