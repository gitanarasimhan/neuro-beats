# Neuro-Beats

https://github.com/user-attachments/assets/feaef44f-6eb6-4d47-8b5c-af48765fa6ef

AI-powered mood-based music recommendation system that suggests personalized playlists and activities based on your emotional state.

## Project Structure

```
neuro-beats/
├── backend/                     # Flask backend application
│   ├── src/                    # Source code
│   │   ├── models/            # Data models and mappings
│   │   ├── routes/            # API route handlers
│   │   ├── services/          # Business logic and external services
│   │   └── utils/             # Helper functions
│   ├── Dockerfile             # Backend container configuration
│   ├── requirements.txt       # Python dependencies
│   └── env.template           # Environment variables template
├── frontend/                   # React frontend application
│   ├── src/                   # Source code
│   │   ├── assets/           # Images and static files
│   │   └── components/       # React components
│   ├── public/               # Public assets
│   ├── Dockerfile            # Frontend container configuration
│   └── nginx.conf            # Nginx configuration
├── docker-compose.yml         # Docker services orchestration
├── deploy.sh                  # Deployment script
└── .gitignore                # Git ignore rules
```

## Setup and Installation

### Prerequisites
- Docker and Docker Compose
- Node.js 18+ (for local development)
- Python 3.11+ (for local development)
- mkcert (for SSL certificates)

### Environment Setup

1. Clone the repository:
```bash
git clone https://github.com/gitanarasimhan/neuro-beats.git
cd neuro-beats
```

2. Create backend environment file:
```bash
cp backend/.env.template backend/.env
```

3. Generate SSL certificates (development):
```bash
mkcert -install
mkcert -key-file backend/certs/localhost+2-key.pem -cert-file backend/certs/localhost+2.pem localhost 127.0.0.1
```

4. Update environment variables in `backend/.env`:
```env
# Required secrets (DO NOT commit actual values)
SECRET_KEY=your-secure-random-key
SPOTIFY_CLIENT_ID=your-spotify-client-id
SPOTIFY_CLIENT_SECRET=your-spotify-client-secret
```

### Running with Docker

1. Build and start the containers:
```bash
./deploy.sh
```

Or manually:
```bash
docker-compose build
docker-compose up -d
```

2. Access the application:
- Frontend: https://localhost
- Backend API: https://localhost/api
- Health check: https://localhost/api/health

### Local Development

#### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```

#### Frontend
```bash
cd frontend
npm install
npm start
```

## Features

- 🎵 Mood-based music recommendations
- 🎯 Personalized activity suggestions
- 🔒 Secure HTTPS communication
- 🚀 Docker containerization
- 🔄 Health monitoring
- 📱 Responsive web design

## API Endpoints

- `POST /api/recommend`
  - Input: `{ "input": "your mood description" }`
  - Output: 
    ```json
    {
      "mood": "detected_mood",
      "music_suggestion": "genre",
      "spotify_playlist_url": "playlist_url",
      "activity_suggestion": "suggested_activity"
    }
    ```

## Security

- HTTPS enabled by default
- Environment-based configuration
- Secure headers in Nginx
- Rate limiting
- CORS protection

## Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details. 
