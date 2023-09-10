# Trainz KUID Downloader

This script allows you to download Trainz assets (KUIDs) from the Trainz-mp website.

### Prerequisites
- Python 3.x
- Required Python libraries: `requests`, `beautifulsoup4`

### Installation
1. Clone the repository or download the script file.
2. Install the required Python libraries by running the following command:
   ```
   pip install requests beautifulsoup4
   ```

### Usage
1. Run the script using the following command:
   ```
   python trainz_kuid_downloader.py
   ```
2. Enter the KUIDs you want to download when prompted.
3. The script will connect to the Trainz-mp website, search for the specified KUIDs, and download the corresponding assets (`.cdp` files).
4. The downloaded files will be saved in the `D:/dfolder/` directory.

Please note that the script downloads the assets one by one, so the process may take some time depending on the number of KUIDs and their sizes.

### Limitations
- This script relies on the Trainz-mp website's structure and may break if the website layout changes.
- Make sure to comply with the terms of use and licensing of the downloaded assets.
