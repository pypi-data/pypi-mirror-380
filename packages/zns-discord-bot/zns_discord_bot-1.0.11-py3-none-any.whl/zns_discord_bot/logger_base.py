import functools
import logging
from typing import Optional, Union

from discord import Colour, User, ClientUser
from discord.ext.commands import Context
from discord.utils import MISSING
from zns_logging import ZnsLogger
from zns_logging.utility.LogHandlerFactory import LogHandlerFactory

from zns_discord_bot.components.easy_embed import EasyEmbed


class LoggerBase(ZnsLogger):
    """
    A class that extends ZnsLogger to provide flexible logging configurations.

    Args:
        reconnect (bool): Enables automatic reconnection when needed.
        log_handler (logging.Handler): The logging handler, default is determined if not provided.
        log_formatter (logging.Formatter): The log format, retrieved from the handler if not provided.
        log_level (int): The logging level.
        root_logger (bool): Specifies whether to use the root logger.
    """

    level_colors = {
        "debug": Colour.blue(),
        "info": Colour.green(),
        "warning": Colour.gold(),
        "error": Colour.red(),
        "critical": Colour.purple(),
    }

    def __init__(
        self,
        reconnect: bool = True,
        log_handler: Optional[logging.Handler] = MISSING,
        log_formatter: logging.Formatter = MISSING,
        log_level: int = logging.INFO,
        root_logger: bool = False,
        use_easy_embed: bool = False,
        use_bot_colour: bool = False,
        colour: Optional[Union[int, Colour]] = None,
        log_file_path_bot: str = None,
        **options,
    ):
        name, _, _ = __name__.partition(".")

        super().__init__(
            name=name,
            level=log_level,
            file_path=log_file_path_bot,
            **options,
        )

        self.reconnect = reconnect
        self.log_handler = log_handler
        self.log_formatter = log_formatter
        self.log_level = log_level
        self.root_logger = root_logger
        self.use_easy_embed = use_easy_embed
        self.use_bot_colour = use_bot_colour
        self.colour = colour if colour is not None else Colour.default()

        self._process_system_logger_params()

    def _process_system_logger_params(self):
        if not self.log_handler:
            self.log_handler = LogHandlerFactory.create_console_handler()

        if not self.log_formatter:
            self.log_formatter = self.log_handler.formatter

    @staticmethod
    def _process_command_name(command_name: str) -> str:
        if "_" in command_name:
            command_name = command_name.replace("_", " ").title()
        return command_name

    def _create_easy_embed(
        self, ctx: Context, message: str, level: str = "info", colour: Optional[Union[int, Colour]] = None
    ) -> EasyEmbed:
        if self.use_bot_colour:
            colour = self.colour
        elif colour is None:
            colour = self.level_colors.get(level.lower(), self.colour)
        else:
            # Use the provided colour
            pass

        command_name = ctx.command.name if ctx.command else "Unknown Command"
        command_name = self._process_command_name(command_name)

        return EasyEmbed(
            title=f"Command: {command_name}",
            description=message,
            colour=colour,
            type="rich",
            author_name=ctx.author.display_name,
            author_url=ctx.author.display_avatar.url,
            author_icon_url=ctx.author.display_avatar.url,
            thumbnail_url=ctx.bot.user.display_avatar.url if ctx.bot and isinstance(ctx.bot.user, (User, ClientUser)) else None,
        )

    @staticmethod
    def _create_send_log_method(log_level: str):
        def decorator(func):
            @functools.wraps(func)
            async def wrapper(self, ctx: Context, message: str, colour: Optional[Union[int, Colour]] = None):
                command_name = ctx.command.name if ctx.command else "Unknown Command"
                command_name = self._process_command_name(command_name)
                getattr(self, log_level)(f"Command {log_level}: [{command_name}] -> [{message}]")
                if self.use_easy_embed:
                    embed = self._create_easy_embed(ctx, message, level=log_level, colour=colour)
                    await ctx.send(embed=embed)
                else:
                    await ctx.send(content=message)

            return wrapper

        return decorator

    @staticmethod
    def _create_reply_log_method(log_level: str):
        def decorator(func):
            @functools.wraps(func)
            async def wrapper(
                self, ctx: Context, message: str, colour: Optional[Union[int, Colour]] = None, mention_author: bool = False
            ):
                command_name = ctx.command.name if ctx.command else "Unknown Command"
                command_name = self._process_command_name(command_name)
                getattr(self, log_level)(f"Command {log_level}: [{command_name}] -> [{message}]")
                if self.use_easy_embed:
                    embed = self._create_easy_embed(ctx, message, level=log_level, colour=colour)
                    await ctx.reply(embed=embed, mention_author=mention_author)
                else:
                    await ctx.reply(content=message, mention_author=mention_author)

            return wrapper

        return decorator

    @_create_send_log_method("debug")
    async def send_debug(self, ctx: Context, message: str, colour: Optional[Union[int, Colour]] = None): ...

    @_create_send_log_method("info")
    async def send_info(self, ctx: Context, message: str, colour: Optional[Union[int, Colour]] = None): ...

    @_create_send_log_method("warning")
    async def send_warning(self, ctx: Context, message: str, colour: Optional[Union[int, Colour]] = None): ...

    @_create_send_log_method("error")
    async def send_error(self, ctx: Context, message: str, colour: Optional[Union[int, Colour]] = None): ...

    @_create_send_log_method("critical")
    async def send_critical(self, ctx: Context, message: str, colour: Optional[Union[int, Colour]] = None): ...

    @_create_reply_log_method("debug")
    async def reply_debug(
        self, ctx: Context, message: str, colour: Optional[Union[int, Colour]] = None, mention_author: bool = False
    ): ...

    @_create_reply_log_method("info")
    async def reply_info(
        self, ctx: Context, message: str, colour: Optional[Union[int, Colour]] = None, mention_author: bool = False
    ): ...

    @_create_reply_log_method("warning")
    async def reply_warning(
        self, ctx: Context, message: str, colour: Optional[Union[int, Colour]] = None, mention_author: bool = False
    ): ...

    @_create_reply_log_method("error")
    async def reply_error(
        self, ctx: Context, message: str, colour: Optional[Union[int, Colour]] = None, mention_author: bool = False
    ): ...

    @_create_reply_log_method("critical")
    async def reply_critical(
        self, ctx: Context, message: str, colour: Optional[Union[int, Colour]] = None, mention_author: bool = False
    ): ...
