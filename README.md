# 🔗 Rebrandly Link Scraper & Exporter

## 📌 About Rebrandly

[Rebrandly](https://www.rebrandly.com/) is a URL shortening platform that allows users to create branded, customizable short links. It provides APIs to manage, track, and analyze links programmatically, including advanced features like traffic analytics, UTM parameters, and workspaces.

This script extracts your Rebrandly link data via API and exports it to **Google BigQuery** for further analysis.

---

## 🚀 Features

- Fetches **all links** using Rebrandly's API
- Handles **pagination** automatically using the `last` parameter
- Saves a **raw JSON backup** of all fetched links
- Normalizes and cleans data using `pandas`
- Adds **scraping timestamp**
- Uploads final data directly to **Google BigQuery**

---

## 🧰 Requirements

Install the required libraries:

```bash
pip install requests pandas isodate google-cloud-bigquery pyarrow

