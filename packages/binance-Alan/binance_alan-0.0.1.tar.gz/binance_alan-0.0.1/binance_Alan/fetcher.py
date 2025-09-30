import pandas as pd
from binance.client import Client
from datetime import datetime, timedelta
import os
from typing import Optional

class BinanceDataFetcher:
    """
    A class designed to fetch and process K-line (candlestick) data from the Binance.US API.

    This class encapsulates the connection to the Binance client, provides methods for
    fetching data for specific symbols and dates, and handles saving the data to
    either CSV or JSON formats.
    """

    # A class attribute for mapping user-friendly names to official Binance symbols.
    SYMBOL_MAP = {
    # Bitcoin
    'btc': 'BTC',
    'bitcoin': 'BTC',

    # Ethereum
    'eth': 'ETH',
    'ethereum': 'ETH',

    # Solana
    'sol': 'SOL',
    'solana': 'SOL',

    # Cardano
    'ada': 'ADA',
    'cardano': 'ADA',

    # Ripple
    'xrp': 'XRP',
    'ripple': 'XRP',

    # Polkadot
    'dot': 'DOT',
    'polkadot': 'DOT',

    # Dogecoin
    'doge': 'DOGE',
    'dogecoin': 'DOGE',

    # Litecoin
    'ltc': 'LTC',
    'litecoin': 'LTC',

    # Chainlink
    'link': 'LINK',
    'chainlink': 'LINK',

    # Binance Coin
    'bnb': 'BNB',
    'binancecoin': 'BNB',

    # Tether
    'usdt': 'USDT',
    'tether': 'USDT',

    # USD Coin
    'usdc': 'USDC',
    'usd coin': 'USDC',
}

    def __init__(self, tld: str = 'us', output_dir: str = 'crypto_data'):
        """
        Initializes the BinanceDataFetcher instance.

        :param tld: The top-level domain for the Binance API. 'us' corresponds to Binance.US.
        :param output_dir: The default directory where data files will be saved.
        """
        print("Initializing Binance client...")
        self.client = Client(tld=tld)
        self.output_dir = output_dir
        # Ensure the output directory exists upon initialization.
        os.makedirs(self.output_dir, exist_ok=True)
        print(f"Client initialized successfully. Data will be saved to '{self.output_dir}' by default.")

    def _map_symbol(self, symbol_name: str) -> Optional[str]:
        """
        An internal helper method to map a user-friendly name to an official trading pair.

        :param symbol_name: The common name for the cryptocurrency (e.g., 'bitcoin').
        :return: The formatted Binance trading pair (e.g., 'BTCUSD') or None if not found.
        """
        base_symbol = self.SYMBOL_MAP.get(symbol_name.lower())
        if not base_symbol:
            print(f"❌ Error: Unrecognized symbol name '{symbol_name}'.")
            return None
        # Assumes the trading pair is against USD for Binance.US
        return f"{base_symbol}USD"

    def fetch_daily_data(self, symbol_name: str, date_str: str) -> Optional[pd.DataFrame]:
        """
        Fetches 1-minute K-line data for a single day and returns it as a pandas DataFrame.

        This method is ideal when you want to get the data into memory for analysis
        without immediately saving it to a file.

        :param symbol_name: The user-friendly name of the cryptocurrency (e.g., 'btc').
        :param date_str: The target date in "YYYY-MM-DD" format.
        :return: A pandas DataFrame containing the K-line data, or None if the fetch fails.
        """
        binance_symbol = self._map_symbol(symbol_name)
        if not binance_symbol:
            return None

        print(f"\nFetching data for {binance_symbol} on {date_str}...")
        try:
            # The API requires a start and end date. To get a full day, we set the
            # end date to the following day. The API fetches up to, but not including, the end date.
            start_dt = datetime.strptime(date_str, "%Y-%m-%d")
            end_dt = start_dt + timedelta(days=1)

            klines = self.client.get_historical_klines(
                symbol=binance_symbol,
                interval=Client.KLINE_INTERVAL_1MINUTE,
                start_str=start_dt.strftime("%Y-%m-%d"),
                end_str=end_dt.strftime("%Y-%m-%d")
            )

            if not klines:
                print(f"  - No data found for {binance_symbol} on {date_str}.")
                return None

            # List comprehension for efficient data processing
            data = [[
                pd.to_datetime(candle[0], unit='ms', utc=True), # timestamp
                float(candle[1]), # open
                float(candle[2]), # high
                float(candle[3]), # low
                float(candle[4])  # close
            ] for candle in klines]

            columns = ['timestamp', 'open', 'high', 'low', 'close']
            df = pd.DataFrame(data, columns=columns)
            print(f"  - Successfully fetched {len(df)} data points.")
            return df

        except Exception as e:
            print(f"❌ An error occurred while fetching from Binance: {e}")
            return None

    def save_data(self, df: pd.DataFrame, file_path: str, output_format: str = 'csv') -> bool:
        """
        Saves a DataFrame to a file in the specified format.

        :param df: The pandas DataFrame to save.
        :param file_path: The full path where the file will be saved.
        :param output_format: The desired output format, either 'csv' or 'json'.
        :return: True if successful, False otherwise.
        """
        try:
            if output_format == 'csv':
                df.to_csv(file_path, index=False)
            elif output_format == 'json':
                df.to_json(file_path, orient='records', date_format='iso', indent=4)
            else:
                print(f"❌ Error: Unsupported output format '{output_format}'.")
                return False
            print(f"✅ Data successfully saved to '{file_path}'")
            return True
        except Exception as e:
            print(f"❌ An error occurred while saving the file: {e}")
            return False

    def get_daily_klines_as_file(self, symbol_name: str, date_str: str, output_format: str = 'csv'):
        """
        A high-level method that performs the complete process of fetching data
        and saving it directly to a file.

        :param symbol_name: The user-friendly name of the cryptocurrency (e.g., 'eth').
        :param date_str: The target date in "YYYY-MM-DD" format.
        :param output_format: The desired output format, 'csv' or 'json'.
        """
        df = self.fetch_daily_data(symbol_name, date_str)

        if df is not None and not df.empty:
            binance_symbol = self._map_symbol(symbol_name)
            file_name = f"{binance_symbol}_{date_str}.{output_format.lower()}"
            file_path = os.path.join(self.output_dir, file_name)
            self.save_data(df, file_path, output_format)

# --- How to use this Class ---
if __name__ == "__main__":
    # 1. Create an instance of the BinanceDataFetcher.
    #    You only need to do this once.
    fetcher = BinanceDataFetcher(output_dir='crypto_daily_data')

    # 2. Use the high-level method to directly fetch and save files.
    # Get Bitcoin data for 2025-09-24 and save as CSV.
    fetcher.get_daily_klines_as_file(
        symbol_name='bitcoin',
        date_str='2025-09-24',
        output_format='csv'
    )

    # Get Ethereum data for 2025-09-25 and save as JSON.
    fetcher.get_daily_klines_as_file(
        symbol_name='eth',
        date_str='2025-09-25',
        output_format='json'
    )