# ⚙️ **Not-pixel-auto-watch-ads**

This is a Telegram mini-app bot for automatically watching ads using query IDs.

---

### ⚙️ **Setup in Termux**

First, ensure your Termux environment is up-to-date and configured with Python 3.10. Follow the steps below:

1. **Update & Upgrade Termux:**
   ```bash
   pkg update && pkg upgrade

2. Remove any existing Python versions:

pkg rem python -y


3. Install necessary repositories:

pkg i tur-repo -y


4. Install Python 3.10:

pkg i python3.10 -y


5. Create a symlink for Python 3:

ln -sf /data/data/com.termux/files/usr/bin/python3.10 /data/data/com.termux/files/usr/bin/python3


6. Verify Python installation:

python3 --version

If it shows python3.10.xx (e.g., python 3.10.14), the setup is complete.




---

⚙️ Installation

Follow the instructions below to set up the bot:

1. Install Git and Nano:

pkg install git
pkg install nano


2. Clone the repository:

git clone https://github.com/asish1346/NotPX-Ad.git


3. Navigate into the cloned directory:

cd NotPX-Ad


4. Install Python dependencies:

pip3.10 install -r requirements.txt


5. Edit query_ids.txt to add your query IDs:

nano query_ids.txt




---

⚙️ Proxy Setup (Optional)

If you want to add a proxy, follow these steps:

1. Edit proxies.txt:

nano proxies.txt


2. Install patchelf to modify the binary:

pkg install patchelf


3. Run the following command to add Python runtime to the binary:

patchelf --add-needed libpython3.10.so.1.0 pyarmor_runtime_004817/android_aarch64/pyarmor_runtime.so




---

⚠️ Important Warning

⚠️ WARNING: Running unlimited ads can be risky and may lead to account bans or other issues. Use at your own risk. ⚠️

Ensure that you're aware of the potential consequences of running automated scripts to watch ads, as it may violate the terms of service of platforms involved. Always use such tools responsibly.


---

⚙️ Running the Bot

Once everything is set up, you can start the bot with the following command:

python3.10 wrap.py


---

