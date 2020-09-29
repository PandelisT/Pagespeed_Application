import os
import requests


def get_pagespeed(website_address: str, strategy: str) -> tuple:
    # Returns performance score and other metrics using the Google PageSpeed API
    try:
        google_api_key = os.environ.get("GOOGLE_API")
        base_url = "https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url="
        response_url = f"{base_url}https://{website_address}&key={google_api_key}&strategy={strategy}"
        response = requests.get(response_url)
        json_data = response.json()
        score = json_data["lighthouseResult"]["categories"]["performance"]["score"]
        first_meaningful_paint = json_data["lighthouseResult"]["audits"]["first-meaningful-paint"]["displayValue"]
        speed_index = json_data["lighthouseResult"]["audits"]["speed-index"]["displayValue"]
        time_to_interactive = json_data["lighthouseResult"]["audits"]["interactive"]["displayValue"]
        return (score * 100, first_meaningful_paint, speed_index, time_to_interactive)
    except KeyError:
        print("Unable to connect to Google Page Insights API.")
        return (0, "0", "0", "0")


page_performance = get_pagespeed("nerdypandy.com.au", "strategy_unspecified")
print(f"Your page performance is {page_performance[0]}, First Meaningful Paint: {page_performance[1]}, Speed Index: {page_performance[2]},  Time To Interactive: {page_performance[3]}")
