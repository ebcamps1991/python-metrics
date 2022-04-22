import sys
import asyncio
import logging
from random import randint

import config


# Logger stuff
from prometheus_client import Summary, start_http_server, Counter

logger = logging.getLogger('amazing_app')
stream_handler = logging.StreamHandler(sys.stdout)
logger.setLevel(logging.INFO)
logger.addHandler(stream_handler)

# Prometheus instrumentation

sleeping_time_seconds = Summary(
    'amazing_app_sleeping_time_seconds',
    'It measures the time that it sleeps'
)

sleeping_seconds_total = Counter(
    'amazing_app_sleeping_seconds_total',
    'It measures the total number of seconds that the application was sent '
    'to sleep'
)


async def do_sleep(sleeping_time: int):
    """
    This function just do what everybody would love to do: sleep

    :param int sleeping_time: The time in seconds to get sleep
    """
    logger.info(f'Working on sleep for {sleeping_time}')
    with sleeping_time_seconds.time():
        await asyncio.sleep(sleeping_time)
    logger.info('Wake up!')


async def start_sleeping_stuff():
    """
    The sleeping scheduler function. This functions aims to predict the
    number of seconds that our app needs to sleep and launch the sleeping
    coroutine
    """
    try:
        while True:
            seconds_to_sleep = randint(1, 5)
            sleeping_seconds_total.inc(seconds_to_sleep)
            await do_sleep(seconds_to_sleep)
    except KeyboardInterrupt:
        logger.info('Exiting from sleep')


async def do_crawl(site: str):
    """
    This function do perform an imaginary crawl on the given site

    :param str site: url to the site to be crawled
    """
    site = config.CRAWL_SITES[randint(0, len(config.CRAWL_SITES) - 1)]
    logger.info(f'Working on crawling {site}')
    await asyncio.sleep(randint(1, 7))


async def start_crawling_stuff():
    """
    The crawling scheduler function. This functions aims send to crawl the
    next site exquisitely choose between the ones on the settings
    """
    try:
        while True:
            site = 'http://some_site.com'
            await do_crawl(site)
    except KeyboardInterrupt:
        logger.info('Exiting from crawling')


def main():
    event_loop = asyncio.get_event_loop()
    logger.info('Starting sleeping tasks')
    # Creating tasks from futures
    event_loop.create_task(start_crawling_stuff())
    event_loop.create_task(start_sleeping_stuff())
    # Running the event loop
    try:
        loop.run_forever()
    finally:
        loop.close()


if __name__ == '__main__':
    # Starting metrics server
    start_http_server(8000)
    loop = asyncio.get_event_loop()
    logger.info('Running the amazing app!')
    main()
