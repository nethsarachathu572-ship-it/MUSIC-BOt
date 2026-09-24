import os
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass


class Config:
    TOKEN = os.getenv("BOT_TOKEN") or os.getenv("DISCORD_TOKEN")
    DEFAULT_PREFIX = os.getenv("DEFAULT_PREFIX", ">")

    # Owner IDs can be comma-separated in environment variable or default
    _raw_owners = os.getenv("OWNER_IDS", "1492423585875099719")
    OWNER_IDS = [int(i.strip()) for i in _raw_owners.split(",") if i.strip().isdigit()]

    # ── Lavalink Nodes ──
    # Default public Lavalink nodes
    LAVALINK_NODES = [
        {
            "host": "lavalinkv4.serenetia.com",
            "port": 443,
            "password": "https://dsc.gg/ajidevserver",
            "region": "us",
            "name": "ajie",
            "ssl": True,
        },
        {
            "host": "lavalink.jirayu.net",
            "port": 13592,
            "password": "youshallnotpass",
            "region": "us",
            "name": "jirayu",
            "ssl": False,
        },
    ]

    # Prepend custom node if provided in environment variables
    _custom_host = os.getenv("LAVALINK_HOST")
    if _custom_host:
        _custom_node = {
            "host": _custom_host,
            "port": int(os.getenv("LAVALINK_PORT", "2333")),
            "password": os.getenv("LAVALINK_PASSWORD", "youshallnotpass"),
            "region": os.getenv("LAVALINK_REGION", "us"),
            "name": os.getenv("LAVALINK_NAME", "custom-node"),
            "ssl": os.getenv("LAVALINK_SECURE", "false").lower() in ("true", "1", "yes"),
        }
        LAVALINK_NODES.insert(0, _custom_node)

    # ── Accent Color: None (Components V2) ──
    ACCENT_COLOR = None

    # ── Bot Info ──
    BOT_NAME = os.getenv("BOT_NAME", "Rose")
    SUPPORT_SERVER = os.getenv("SUPPORT_SERVER", "https://discord.gg/yourserver")
    WEBSITE = os.getenv("WEBSITE", None)

    # ── Dashboard ──
    DASHBOARD_ENABLED = os.getenv("DASHBOARD_ENABLED", "true").lower() == "true"