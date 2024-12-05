# ⚙️ **NotPx-Ad**

This is a Telegram mini-app bot for automatically watching ads using query IDs.

---

### ⚙️ **Setup in Termux**

Follow the steps below to set up **Not-pixel-auto-watch-ads** on Termux.

#### 1. **Update & Upgrade Termux**

```bash
pkg update && pkg upgrade -y
```

#### 2. **Remove Existing Python Version**

```bash
pkg rem python -y
```

#### 3. **Install Necessary Repositories**

```bash
pkg i tur-repo -y
```

#### 4. **Install Python 3.10**

```bash
pkg i python3.10 -y
```

#### 5. **Create Symlink for Python 3**

```bash
ln -sf /data/data/com.termux/files/usr/bin/python3.10 /data/data/com.termux/files/usr/bin/python3
```

#### 6. **Verify Python Installation**

```bash
python3 --version
```

If it shows `python3.10.xx` (e.g., `python 3.10.14`), the setup is complete.

---

### ⚙️ **Installation**

Follow the instructions below to set up the bot.

#### 1. **Install Git and Nano**

```bash
pkg install git nano -y
```

#### 2. **Clone the Repository**

```bash
git clone https://github.com/asish1346/NotPX-Ad.git
```

#### 3. **Navigate into the Cloned Directory**

```bash
cd NotPX-Ad
```

#### 4. **Install Python Dependencies**

```bash
pip3.10 install -r requirements.txt
```

#### 5. **Edit `query_ids.txt` to Add Your Query IDs**

```bash
nano query_ids.txt
```

---

### ⚙️ **Proxy Setup (Optional)**

If you want to add a proxy, follow these steps:

1. **Edit `proxies.txt`:**

```bash
nano proxies.txt
```

2. **Install `patchelf` to Modify the Binary:**

```bash
pkg install patchelf -y
```

3. **Run the Following Command to Add Python Runtime to the Binary:**

```bash
patchelf --add-needed libpython3.10.so.1.0 pyarmor_runtime_004817/android_aarch64/pyarmor_runtime.so
```

---

### ⚠️ **Important Warning**

**⚠️ WARNING: Running unlimited ads can be risky and may lead to account bans or other issues. Use at your own risk. ⚠️**

Ensure that you're aware of the potential consequences of running automated scripts to watch ads, as it may violate the terms of service of platforms involved. Always use such tools responsibly.

---

### ⚙️ **Running the Bot**

Once everything is set up, you can start the bot with the following command:

```bash
python3.10 wrap.py
```

---

By following these steps, your **NotPX-Ad** bot will be up and running on Termux, ready to automate ad-watching tasks using your query IDs.
