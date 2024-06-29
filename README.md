# TikTok Automator

This script automates interactions with the TikTok automation script to increase followers, hearts, comment hearts, views, shares, and favorites on TikTok. The script uses Selenium to control a web browser and interact with the website.

## Features
- Automates interactions with Zefoy to boost TikTok metrics.
- Handles CAPTCHA input manually.
- Allows selection of different metrics to boost.
- Adds a 30-second cooldown after each action to avoid rate limits.
- Adds a 30-times run each link limits.

## Requirements
- Python 3.x
- Google Chrome

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/zefoy-automator.git
    cd zefoy-automator
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Install `undetected_chromedriver` separately:
    ```bash
    pip install undetected-chromedriver
    ```

4. Update the `config.json` file in the same directory as the script with your TikTok video links. The structure should look like this:
    ```json
    {
        "links": [
            "https://www.tiktok.com/@user/video/1234567890",
            "https://www.tiktok.com/@user/video/0987654321"
        ]
    }
    ```

## Usage

1. Run the script:
    ```bash
    python automator.py
    ```

2. Follow the instructions displayed in the console to complete CAPTCHA input and select the desired metric to boost.

## Configuration

- `config.json`:
    - `"links"`: A list of TikTok video links to which views will be sent.

## Notes

- Ensure that Google Chrome is installed and up to date.
- The script uses `undetected_chromedriver` to avoid detection by the website.
- The script includes a 30-second cooldown after each successful submission to comply with rate limits.

## About Programmers Beats

Programmers Beats is a YouTube channel dedicated to providing high-quality content that caters to the needs of developers. From coding tutorials and programming tips to software development insights and industry trends, Programmers Beats offers a wide range of resources to help developers enhance their skills and stay updated with the latest advancements in technology with music.

### Check out the Programmers Beats YouTube Channel:
[![Programmers Beats](https://img.shields.io/badge/YouTube-Programmers%20Beats-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/@ProgrammersBeats)

## Credits

This script is developed by **Programmers Beats** and **Ameer Hamza**.

## Contributing

If you'd like to contribute to this project, please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License.
