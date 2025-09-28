import datetime
from typing import Literal, Optional, Union

from discord import Embed, Colour

EmbedType = Literal['rich', 'image', 'video', 'gifv', 'article', 'link', 'poll_result']

class EasyEmbed(Embed):
    def __init__(
        self,
        title: Optional[str] = None,
        description: Optional[str] = None,
        url: Optional[str] = None,
        type: EmbedType = "rich",
        colour: Optional[Union[int, Colour]] = None,
        timestamp: Optional[datetime.datetime] = None,
        author_name: Optional[str] = None,
        author_url: Optional[str] = None,
        author_icon_url: Optional[str] = None,
        footer_text: Optional[str] = None,
        footer_icon_url: Optional[str] = None,
        thumbnail_url: Optional[str] = None,
        image_url: Optional[str] = None,
    ):
        super().__init__(
            title=title,
            description=description,
            url=url,
            type=type,
            colour=colour,
            timestamp=timestamp if timestamp is not None else datetime.datetime.now(datetime.timezone.utc)
        )

        if thumbnail_url:
            self.set_thumbnail(url=thumbnail_url)

        if author_name:
            self.set_author(
                name=author_name,
                url=author_url,
                icon_url=author_icon_url
            )

        if footer_text:
            self.set_footer(
                text=footer_text,
                icon_url=footer_icon_url
            )

        if image_url:
            self.set_image(url=image_url)
