# Rose Bot

> A modern Discord bot with an integrated web dashboard, built for reliable server management, utility, and music features.

---

## Features

- Discord bot built with Python and `discord.py`
- Integrated FastAPI web dashboard
- Discord OAuth2 authentication
- Music system with Lavalink
- Real-time player and queue controls
- Server and guild management
- SQLite database support
- Automatic cog loading
- Centralized configuration
- Custom Discord application emojis
- Environment-based secrets and configuration

---

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core bot |
| discord.py | Discord API |
| FastAPI | Web dashboard |
| Lavalink | Music playback |
| SQLite | Database |
| Jinja2 | Dashboard templates |
| aiohttp | Async HTTP requests |

---

## Project Structure

```text
Rose-Bot/
├── cogs/              # Bot commands and events
├── dashboard/         # Web dashboard and OAuth2
├── scripts/           # Utility scripts
├── utils/             # Database and helper modules
├── config.py          # Main configuration
├── emojis.py          # Discord emoji definitions
├── main.py            # Bot entry point
└── requirements.txt   # Python dependencies
```

---

## Installation

### 1. Clone the Repository

```bash
git clone <repository-url>
cd Rose-Bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure Environment

Create a `.env` file and configure the required credentials:

```env
BOT_TOKEN=your_bot_token
DASHBOARD_ENABLED=true
DASHBOARD_PORT=8080
```

> Never commit your `.env` file, bot token, OAuth credentials, or other private secrets to GitHub.

---

## Running the Bot

Start Rose using:

```bash
python main.py
```

The bot will initialize its required services, load the available cogs, connect to the configured Lavalink node, and start the dashboard when enabled.

---

## Dashboard

Rose includes an integrated web dashboard with Discord OAuth2 authentication.

The dashboard can provide:

- Discord authentication
- Guild selection
- Music player controls
- Queue information
- Player status
- Server configuration

---

## Music System

Rose uses Lavalink for high-performance Discord audio playback.

Configure your Lavalink node through the project's configuration instead of hardcoding credentials or connection details.

---

## Configuration

Main settings can be managed through the project's configuration files.

Typical configuration includes:

```text
Bot Token
Owner IDs
Command Prefix
Lavalink Nodes
Dashboard Settings
OAuth2 Settings
Database Settings
```

---

## Security

Keep all sensitive credentials private.

```text
.env
Bot Token
OAuth2 Client Secret
Session Secret
Database Credentials
Lavalink Credentials
```

Do not upload secrets to public repositories or include them directly in source code.

---

## Credits

Developed and maintained by:

> **r3novadcl**

Part of:

> **FX DEVELOPMENT**

---

## License

This project is intended for development and personal use.

See the repository's license and documentation for applicable usage terms.
