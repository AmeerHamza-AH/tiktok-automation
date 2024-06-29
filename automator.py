import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, ElementNotInteractableException

try:
    import undetected_chromedriver as uc
    from colorama import Fore, init, Style
    import ctypes, platform, os, time
    import selenium, requests, webbrowser

except ImportError as e:
    print(f"You do not have all of the modules required installed: {e}")
    os._exit(1)

# Load config.json
with open('config.json', 'r') as f:
    config = json.load(f)

text = "Programmers Beats"

class Zefoy:

    def __init__(self):
        self.driver = uc.Chrome()
        self.captcha_box = '/html/body/div[5]/div[2]/form/div/div'
        self.clear = "clear"

        if platform.system() == "Windows":
            self.clear = "cls"

        self.color = Fore.BLUE
        self.sent = 0
        self.xpaths = {
            "followers": "/html/body/div[6]/div/div[2]/div/div/div[2]/div/button",
            "hearts": "/html/body/div[6]/div/div[2]/div/div/div[3]/div/button",
            "comment_hearts": "/html/body/div[6]/div/div[2]/div/div/div[4]/div/button",
            "views": "/html/body/div[6]/div/div[2]/div/div/div[5]/div/button",
            "shares": "/html/body/div[6]/div/div[2]/div/div/div[6]/div/button",
            "favorites": "/html/body/div[6]/div/div[2]/div/div/div[7]/div/button",
        }

    def main(self):
        os.system(self.clear)
        self.change_title("TikTok Automator using zefoy.com | Github: @xtekky")

        print(self.color + text)
        print("\n" + self._print("Waiting for Zefoy to load... 502 Error = Blocked country or VPN is on"))

        self.driver.get("https://zefoy.com")
        self.wait_for_xpath(self.captcha_box)

        print(self._print("Site loaded, enter the CAPTCHA to continue."))
        print(self._print("Waiting for you..."))

        self.wait_for_xpath(self.xpaths["followers"])
        os.system(self.clear)
        status = self.check_status()

        print(self.color + text)
        print()
        print(self._print(f"Select your option below." + "\n"))

        counter = 1
        for thing in status:
            print(self._print(f"{thing} {status[thing]}", counter))
            counter += 1

        print(self._print(f""))
        option = int(input("\n" + self._print(f"")))

        if option == 1:
            div = "7"
            self.click_element(self.xpaths["followers"])

        elif option == 2:
            div = "8"
            self.click_element(self.xpaths["hearts"])

        elif option == 3:
            div = "9"
            self.click_element(self.xpaths["comment_hearts"])

        elif option == 4:  # Views
            div = "10"
            self.click_element(self.xpaths["views"])

        elif option == 5:
            div = "11"
            self.click_element(self.xpaths["shares"])

        elif option == 6:
            div = "12"
            self.click_element(self.xpaths["favorites"])

        else:
            os._exit(1)

        for link in config['links']:
            self.send_views_to_link(link, div)

    def send_views_to_link(self, link, div):
        video_url_box = f'/html/body/div[{div}]/div/form/div/input'
        search_box = f'/html/body/div[{div}]/div/form/div/div/button'

        for _ in range(30):  # Repeat 30 times for each link
            self.send_bot(search_box, video_url_box, link, div)

    def click_element(self, xpath):
        try:
            element = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
            element.click()
        except TimeoutException:
            print(f"Timeout waiting for element: {xpath}")
        except ElementNotInteractableException:
            print(f"Element not interactable: {xpath}")
        except Exception as e:
            print(f"Error clicking element: {xpath}, {e}")

    def send_bot(self, search_button, main_xpath, vid_info, div):
        while True:
            try:
                element = WebDriverWait(self.driver, 20).until(
                    EC.element_to_be_clickable((By.XPATH, main_xpath))
                )
                element.clear()
                element.send_keys(vid_info)
                self.driver.find_element(By.XPATH, search_button).click()
                time.sleep(30)

                ratelimit_seconds, full = self.check_submit(div)
                if "(s)" in str(full):
                    print(f"Rate limit hit, waiting for {ratelimit_seconds} seconds...")
                    self.main_sleep(ratelimit_seconds)
                    continue  # Continue the loop to resend after cooldown

                time.sleep(30)

                send_button = f'/html/body/div[{div}]/div/div/div[1]/div/form/button'
                self.driver.find_element(By.XPATH, send_button).click()
                self.sent += 1
                print(self._print(f"Sent {self.sent} times."))

                time.sleep(30)
                break  # Exit the while loop after successful submission

            except ElementNotInteractableException:
                print(f"Element not interactable: {main_xpath}")
            except TimeoutException:
                print(f"Timeout waiting for element: {main_xpath}")
            except NoSuchElementException:
                print(f"No such element: {main_xpath}")
            except Exception as e:
                print(f"Error in send_bot: {main_xpath}, {e}")

    def main_sleep(self, delay):
        while delay != 0:
            time.sleep(1)
            delay -= 1
            self.change_title(f"TikTok Zefoy Automator using Zefoy.com | Cooldown: {delay}s | Github: @useragents")

    def convert(self, min, sec):
        seconds = 0

        if min != 0:
            answer = int(min) * 60
            seconds += answer

        seconds += int(sec) + 5
        return seconds

    def check_submit(self, div):
        remaining = f"/html/body/div[{div}]/div/div/h4"

        try:
            element = self.driver.find_element(By.XPATH, remaining)
        except NoSuchElementException:
            return None, None

        if "READY" in element.text:
            return True, True

        if "seconds for your next submit" in element.text:
            output = element.text.split("Please wait ")[1].split(" for")[0]
            minutes = element.text.split("Please wait ")[1].split(" ")[0]
            seconds = element.text.split("(s) ")[1].split(" ")[0]
            sleep_duration = self.convert(minutes, seconds)

            return sleep_duration, output

        return element.text, None

    def check_status(self):
        statuses = {}

        for thing in self.xpaths:
            value = self.xpaths[thing]
            try:
                element = self.driver.find_element(By.XPATH, value)
                if not element.is_enabled():
                    statuses.update({thing: f"{Fore.RED}[OFFLINE]"})
                else:
                    statuses.update({thing: f"{Fore.GREEN}[WORKS]"})
            except NoSuchElementException:
                statuses.update({thing: f"{Fore.RED}[NOT FOUND]"})

        return statuses

    def _print(self, msg, status="-"):
        return f" {Fore.WHITE}[{self.color}{status}{Fore.WHITE}] {msg}"

    def change_title(self, arg):
        if self.clear == "cls":
            ctypes.windll.kernel32.SetConsoleTitleW(arg)

    def wait_for_xpath(self, xpath):
        try:
            WebDriverWait(self.driver, 20).until(EC.presence_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            print(f"Timeout waiting for {xpath}")


if __name__ == "__main__":
    obj = Zefoy()
    obj.main()
    input()
