from typing import Any
import asyncio
from collections.abc import Callable
import re
from urllib.parse import urljoin
from bs4 import BeautifulSoup
import random
import httpx
import pandas as pd
import backoff
# Internals
from ..exceptions import (
    ComponentError,
    DataNotFound,
    DataError
)
from ..interfaces.http import ua
from .reviewscrap import ReviewScrapper, on_backoff, bad_gateway_exception
from ..utils.json import json_decoder, json_encoder


class NetworkNinjaClaims(ReviewScrapper):
    """NetworkNinjaClaims.

    Extract Claims Data from NetworkNinja.com
    """
    def __init__(
        self,
        loop: asyncio.AbstractEventLoop = None,
        job: Callable = None,
        stat: Callable = None,
        **kwargs,
    ):
        super().__init__(
            loop=loop,
            job=job,
            stat=stat,
            **kwargs
        )
        # Always use proxies:
        self.use_proxy: bool = True
        self._free_proxy: bool = False
        self.cookies = {
            "PHPSESSID": "ronenhpd11jnk76do5e9eiqco0",
            "sid": "8645d9379a8133e058141506ad85f2dc12e93f31",
            "claims_page": "1",
            "claims_showFavorites": "false"
        }
        self.headers: dict = {
            'authority': 'networkninja.com',
            "Host": "flex.troc.networkninja.com",
            'Accept': 'application/json, text/javascript, */*; q=0.01',
            'X-Requested-With': 'XMLHttpRequest',
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-US,en;q=0.9,en-US;q=0.8,en;q=0.7,es-419;q=0.6",
            "content-language": "en-US",
            "Origin": "https://flex.troc.networkninja.com/",
            "Sec-CH-UA": '"Not A(Brand";v="8", "Chromium";v="132", "Google Chrome";v="132"',
            "Sec-CH-UA-Mobile": "?0",
            "Sec-CH-UA-Platform": '"Linux"',
            'sec-fetch-site': 'none',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-dest': 'document',
            "Sec-Fetch-Site": "none",
            "User-Agent": random.choice(ua),
            "Connection": "keep-alive",
            'dnt': '1',
            'upgrade-insecure-requests': '1',
        }
        self.semaphore = asyncio.Semaphore(10)

    @backoff.on_exception(
        backoff.expo,
        (httpx.TimeoutException, httpx.ConnectTimeout, httpx.HTTPStatusError, httpx.HTTPError),
        max_tries=3,
        jitter=backoff.full_jitter,
        on_backoff=on_backoff,
        giveup=lambda e: not bad_gateway_exception(e) and not isinstance(e, httpx.ConnectTimeout)
    )
    async def _fetch_claims(self, cookies) -> list:
        async with self.semaphore:
            # Prepare payload for the API request
            base_url = "https://flex.troc.networkninja.com/payroll/claims.php"
            result = []
            total_records = 0
            page = 1
            try:
                while True:
                    json_data, error = await self.session(
                        url=base_url,
                        method='post',
                        headers=self.headers,
                        follow_redirects=True,
                        use_json=True,
                        data={
                            "xhr": True,
                            "loadCount": 1,
                            "page": page,
                            "perPage": 100,
                            "orderBy": "",
                            "orderDirection": "",
                            "search": "",
                            "saveFilter": False,
                            "showFavorites": False,
                            "selectedItems": [],
                            "currentColumns": [],
                            "checkAll": False,
                            "columnState": []
                        },
                        cookies=cookies
                    )
                    print('fetched page ', page)
                    if not error:
                        data = json_decoder(json_data)
                        total_records = int(data.get('total_records', 0))
                        result.extend(data.get('data', []))
                        print('fetched records ', len(result), ' of ', total_records)
                        if len(result) >= total_records:
                            break
                        page += 1
                        await asyncio.sleep(
                            random.uniform(1, 3)
                        )  # Be polite with a random delay
                # Convert result to DataFrame
                if result:
                    df = pd.DataFrame(result)
                    print(df)
                    return df
                else:
                    raise DataNotFound("No claims data found.")
            except Exception as e:
                print('error fetching claims ', e)
                raise ComponentError(
                    f"An error occurred: {e}"
                ) from e

    async def claims(self):
        """claims.

        NetworkNinja Claims Data.
        """
        httpx_cookies = httpx.Cookies()
        for key, value in self.cookies.items():
            if key == "PHPSESSID":
                httpx_cookies.set(
                    key, value,
                    domain='.troc.networkninja.com',
                    path='/'
                )
            else:
                httpx_cookies.set(
                    key, value,
                    domain='.flex.troc.networkninja.com',
                    path='/'
                )

        # Iterate over each row in the DataFrame
        print('starting ...')
        result = await self._fetch_claims(
            httpx_cookies
        )
        self._result = result
        return self._result
