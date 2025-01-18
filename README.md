
# Laboratory Assignment 1 - DSCI 560

This assignment involves setting up the development environment, working with Linux terminal commands, Python scripting, and performing basic data scraping and processing tasks.

## Prerequisites
- VMware
- Ubuntu Desktop ISO image
- Python 3 and pip

## Setup Instructions

### 1. Install VMware and Set Up Ubuntu VM
1. Download VMware: Follow the [VMware Academic Program Guide](https://viterbiit.usc.edu/services/software/vmware-academic-program/).
2. Download Ubuntu Desktop ISO from the [official website](https://ubuntu.com/download).
3. Create a new virtual machine in VMware:
   - Select "Linux" and "Ubuntu (64-bit)" as the OS type.
   - Allocate at least 2GB RAM and 20GB disk space.
   - Use the downloaded ISO as the installation medium.
4. Complete the Ubuntu installation process.

### 2. Install Python on Linux
1. Update the package list:
   ```bash
   sudo apt update
   ```
2. Install Python 3:
   ```bash
   sudo apt install python3
   ```
3. Verify installation:
   ```bash
   python3 --version
   ```
4. Install pip:
   ```bash
   sudo apt install python3-pip
   ```
5. Verify pip installation:
   ```bash
   pip3 --version
   ```

## Tasks

### 1. Linux Terminal Basics
- Create a directory structure:
  - `<name>_<USCid>` folder with `data` and `scripts` subfolders.
- Create an empty Python file `task_1.py` in the `scripts` folder.

### 2. Python Scripts

#### Task 1: Basic Python Script
1. Open `task_1.py` in a text editor (e.g., `vim` or `nano`).
2. Write a script to greet the user:
   ```python
   name = input("Enter your name: ")
   print(f"Hello, {name}!")
   ```
3. Save, exit, and run the script in the terminal.

#### Task 2: Web Scraping
1. Create a new file `web_scraper.py` in the `scripts` folder.
2. Install required libraries:
   ```bash
   pip install requests beautifulsoup4
   ```
3. Write a script to scrape data from [CNBC World](https://www.cnbc.com/world/?region=world):
   - Save the raw HTML in the `raw_data` folder as `web_data.html`.
   - Print the first 10 lines of the HTML file to the terminal.

#### Task 3: Data Filtering
1. Create a file `data_filter.py`.
2. Read `web_data.html` and extract:
   - **Market Data**: Symbols, positions, and percentage changes.
   - **News Data**: Timestamps, titles, and links.
3. Save the data into CSV files:
   - `market_data.csv` (in `processed_data` folder).
   - `news_data.csv` (in `processed_data` folder).
4. Print status messages in the terminal (e.g., "Filtering fields", "CSV created").

## Outputs
- **Raw Data**: `web_data.html` (stored in the `raw_data` folder).
- **Processed Data**:
  - `market_data.csv`
  - `news_data.csv`
 
  MARKET_DATA.CSV
 

NEWS_DATA.CSV
![image](https://github.com/user-attachments/assets/6d37043e-8bbe-4452-9bd5-6a2f12bf2402)

