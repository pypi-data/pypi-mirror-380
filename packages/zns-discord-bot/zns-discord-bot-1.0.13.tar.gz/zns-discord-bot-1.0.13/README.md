<h1 align="center">zns-discord-bot</h1>

<h3 align="center">A Discord bot library that integrates many functionalities for Python</h3>

# Installation

```bash
pip install zns-discord-bot
```

# Usage

```python
from discord import Intents

from zns_discord_bot.zns_discord_bot import ZnsDiscordBot

bot = ZnsDiscordBot(
    token="YOUR.DISCORD.BOT.TOKEN",
    command_prefix="!",
    intents=Intents.default(),
)

if __name__ == "__main__":
    bot.init()
```

# Features

(Will be updated soon)

# Change Log

```markdown
1.0.0

- Status: Yanked
- Changes: Initial release.
- Reason: Wrong README.md documentation.

1.0.1

- Status: Yanked
- Changes: Fix README.md documentation.
- Reason: `log_level` default value in `Logging` class is not set.

1.0.2

- Status: Released
- Changes: Fix `log_level` default value in `Logging` class.

1.0.3

- Status: Released
- Changes: Change `KeyboardInterrupt` log level from `ERROR` to `INFO`.

1.0.4

- Status: Released
- Changes:
    - Add file logging for bot and system loggers.
    - Add send log and reply log methods.

1.0.5.

- Status: Released
- Changes: Change the way to assign the name for bot logger.

1.0.6

- Status: Released
- Changes: Change the way to assign the name for bot logger.

1.0.7

- Status: Released
- Changes: Small update in `LoggerBase` class.

1.0.8

- Status: Yanked
- Accidentally uploaded test module.
- Changes: Big update in `LoggerBase` class.

1.0.9

- Status: Yanked
- Accidentally uploaded test module.
- Changes: Small update in `LoggerBase` class.

1.0.10

- Status: Yanked
- Accidentally uploaded test module.
- Changes: Small update in `LoggerBase` class.

1.0.11

- Status: Yanked
- Accidentally uploaded test module.
- Changes: Small update in `LoggerBase` class.

1.0.12

- Status: Yanked
- Accidentally uploaded test module.
- Changes: Small update in `LoggerBase` class.

1.0.13
- Status: Released
- Changes: Remove test module.
```


