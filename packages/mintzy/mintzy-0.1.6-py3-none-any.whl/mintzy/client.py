
# # mintzy/client.py
# import requests

# class Client:
#     # Define valid keys (for soft protection)
#     VALID_KEYS = {"XYZ123", "ABC456", "CLIENT789"}

#     def __init__(self, api_key, base_url="http://34.172.210.29/predict"):
#         self.base_url = base_url
#         self.api_key = api_key

#     def _check_key(self):
#         return self.api_key in self.VALID_KEYS

#     def get_prediction(self, tickers, time_frame, parameters):
#         if not self._check_key():
#             return {"success": False, "error": "Unauthorized: Invalid API key"}

#         # Ensure tickers is a list and max 3 allowed
#         if isinstance(tickers, str):
#             tickers = [tickers]
#         if not isinstance(tickers, list):
#             return {"success": False, "error": "Tickers must be a string or list"}
#         if len(tickers) > 3:
#             return {"success": False, "error": "Maximum of 3 tickers allowed"}

#         # Ensure parameters is a list
#         if isinstance(parameters, str):
#             parameters = [parameters]

#         payload = {
#             "action": {
#                 "action_type": "predict",
#                 "predict": {
#                     "given": {"ticker": tickers, "time_frame": time_frame},
#                     "required": {"parameters": parameters}
#                 }
#             }
#         }

#         try:
#             response = requests.post(
#                 self.base_url,
#                 json=payload,
#                 headers={"X-API-Key": self.api_key},
#                 timeout=30
#             )
#             response.raise_for_status()
#             return {"success": True, "data": response.json()}

#         except requests.exceptions.HTTPError as e:
#             return {"success": False, "error": "Server error occurred, please try again later"}
#         except requests.exceptions.Timeout:
#             return {"success": False, "error": "Request timed out, please try again"}
#         except requests.exceptions.ConnectionError:
#             return {"success": False, "error": "Failed to connect to server"}
#         except Exception:
#             return {"success": False, "error": "Unexpected error occurred"}

#     def batch_predict(self, tickers, time_frame, parameters=None):
#         if not self._check_key():
#             return [{"success": False, "error": "Unauthorized: Invalid API key", "ticker": t} for t in tickers]

#         if len(tickers) > 3:
#             return [{"success": False, "error": "Maximum of 3 tickers allowed", "ticker": t} for t in tickers]

#         results = []
#         for ticker in tickers:
#             result = self.get_prediction([ticker], time_frame, parameters)
#             result["ticker"] = ticker
#             results.append(result)
#         return results

import requests
import pandas as pd
import time
import io
from datetime import datetime

class Client:
    VALID_KEYS = {"XeyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9"}

    def __init__(self, api_key, base_url="http://34.172.210.29/predict"):
        self.base_url = base_url
        self.api_key = api_key

    def _check_key(self):
        return self.api_key in self.VALID_KEYS

    def _format_table(self, response_json, tickers, parameters):
        try:
            rows = []
            result = response_json.get("result", {})  

            for ticker in tickers:
                for param in parameters:
                    if ticker not in result or param not in result[ticker]:
                        rows.append(pd.DataFrame([{
                            "Ticker": ticker,
                            "Parameter": param,
                            "Error": "No prediction data available"
                        }]))
                        continue

                    raw_data = result[ticker][param].get("data", "")

                    if not raw_data:
                        rows.append(pd.DataFrame([{
                            "Ticker": ticker,
                            "Parameter": param,
                            "Error": "Empty prediction data"
                        }]))
                        continue

                    #  FIX: use io.StringIO (not pd.compat.StringIO)
                    df = pd.read_csv(io.StringIO(raw_data), sep=r"\s+", engine="python")
                    df["Date"] = pd.to_datetime(df["Timestamp"]).dt.date
                    df["Time"] = pd.to_datetime(df["Timestamp"]).dt.time
                    df.rename(columns={f"Predicted_{param.capitalize()}": "Predicted Price"}, inplace=True)
                    df["Ticker"] = ticker

                    rows.append(df[["Ticker", "Date", "Time", "Predicted Price"]])

            # Merge all tickers in one table
            final_df = pd.concat(rows, ignore_index=True)
            return final_df
        except Exception as e:
            return pd.DataFrame([{"Error": str(e)}])

    def get_prediction(self, tickers, time_frame, parameters):
        if not self._check_key():
            return {"success": False, "error": "Unauthorized: Invalid API key"}

        if isinstance(tickers, str):
            tickers = [tickers]
        if not isinstance(tickers, list):
            return {"success": False, "error": "Tickers must be a string or list"}
        if len(tickers) > 3:
            return {"success": False, "error": "Maximum of 3 tickers allowed"}

        if isinstance(parameters, str):
            parameters = [parameters]

        payload = {
            "action": {
                "action_type": "predict",
                "predict": {
                    "given": {"ticker": tickers, "time_frame": time_frame},
                    "required": {"parameters": parameters}
                }
            }
        }

        while True:
            try:
                response = requests.post(
                    self.base_url,
                    json=payload,
                    headers={"X-API-Key": self.api_key},
                    timeout=30
                )
                response.raise_for_status()
                response_json = response.json()

                # Format clean DataFrame
                df = self._format_table(response_json, tickers, parameters)

                # Clear console + print updated table
                print("\033c", end="")  # Linux/Mac (use os.system("cls") on Windows)
                print(f"Live Predictions ({time_frame}) — {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
                print(df.to_string(index=False))

            except requests.exceptions.RequestException as e:
                print(f"⚠️ Error: {e}")

            # Wait 15 minutes before next update
            time.sleep(900)
