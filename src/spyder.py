"""Spyder

Usage:
  spyder url URL

"""

from docopt import docopt
from urllib.parse import urljoin

import asyncio
import httpx

from urllib.parse import urlparse, urljoin

from loguru import logger as log
from lxml.html import fromstring as string2html


async def spy(page, client, url, source):
    done.add(url)
    if url.startswith(SEED):
        await spy_contexte(page, client, url, source)
    else:
        await spy_external(client, url, source)

SEED = "https://en.wikipedia.org/wiki/Wikipedia:Vital_articles/Level/5"


def wikipedia(path):
    return "https://en.wikipedia.org{}".format(path)


async def spyder(url):
    async with httpx.AsyncClient() as client:
        response = await client.get(SEED)
        html = string2html(response.text)
        for path in html.xpath('//tr/td/a/@href'):
            response = await client.get(wikipedia(path))
            html = string2html(response.text)
            for path in html.xpath('//ol/li/a/@href'):
                print(wikipedia(path))


if __name__ == '__main__':
    arguments = docopt(__doc__, version='spyder 0.0.0')
    # log.debug(arguments)
    # log.debug("Starting webspyder...")
    asyncio.run(spyder(arguments["URL"]))
