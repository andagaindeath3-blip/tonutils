import telebot
import requests
import sqlite3
import time
from tonsdk.boc import begin_cell
from tonsdk.utils import Address, to_nano, bytes_to_b64str
from tonsdk.contract.wallet import Wallets, WalletVersionEnum
from tonsdk.contract.token.ft import JettonWallet

# Константы (ЗАМЕНИТЕ НА ТЕСТОВЫЕ ДЛЯ БЕЗОПАСНОСТИ!)
BOT_TOKEN = '8364743173:AAH0G2L3ZmaqQZ1ZB7CAhFBYFUL-wKMxVBU'
JETTON_MASTER_STR = 'EQAdQwBMtEeyAUfJHcDwAXnhOwcA7xAAGW3PKnFdM1XvRkNB'
MNEMONIC_WORDS = [
    'leaf', 'genius', 'grit', 'skull', 'culture', 'expose', 'balcony', 'harvest',
    'fish', 'often', 'govern', 'hospital', 'stock', 'stay', 'oak', 'lunar',
    'athlete', 'argue', 'piece', 'tube', 'maze', 'avoid', 'wait', 'way'
]
TON_CENTER_API_KEY = '861aeee4c9cb8d807832d05c7763a25c8cfade56e61cda631a3e839cd772f757'
API_BASE = 'https://toncenter.com/api/v3'
bot = telebot.TeleBot(BOT_TOKEN)
CLAIM_LIMIT = 1000  # Максимум 1000 Jetton за раз
CLAIM_COOLDOWN = 2397600  # 666 часов в секундах (≈27.75 дней)

# Инициализация базы данных SQLite
def init_db():
    conn = sqlite3.connect('claims.db')
    c = conn.cursor()
    # Таблица для логов запросов
    c.execute('''CREATE TABLE IF NOT EXISTS claims
                 (user_id INTEGER, amount REAL, timestamp INTEGER, success INTEGER)''')
    # Таблица для адресов пользователей
    c.execute('''CREATE TABLE IF NOT EXISTS user_addresses
                 (user_id INTEGER PRIMARY KEY, address TEXT, timestamp INTEGER)''')
    conn.commit()
    conn.close()

# Инициализация кошелька
mnemonics_list = MNEMONIC_WORDS
version = WalletVersionEnum.v4r2
workchain = 0
_, _, _, wallet = Wallets.from_mnemonics(mnemonics=mnemonics_list, version=version, workchain=workchain)
wallet_address_str = wallet.address.to_string(True, True, True)
jetton_master = Address(JETTON_MASTER_STR)

def api_get(url, params=None):
    """Вспомогательная функция для GET-запросов к TON Center API"""
    if params is None:
        params = {}
    params['api_key'] = TON_CENTER_API_KEY
    response = requests.get(f"{API_BASE}/{url}", params=params)
    result = response.json()
    if not result.get('ok'):
        raise ValueError(f"API error: {result}")
    return result['result']

def get_wallet_info():
    """Получить seqno и другие данные кошелька"""
    data = api_get('wallet', {'address': wallet_address_str})
    return data['wallet']

def get_jetton_wallet_info():
    """Получить адрес и баланс Jetton-кошелька бота"""
    params = {
        'address': wallet_address_str,
        'jetton': jetton_master.to_string(True, True, True)
    }
    data = api_get('jetton/wallets', params)
    if not data['wallets']:
        raise ValueError("Jetton wallet not found. Deploy it first.")
    return data['wallets'][0]

def check_balance_sufficient(amount_nano):
    """Проверка, достаточно ли Jetton на балансе бота"""
    jetton_info = get_jetton_wallet_info()
    balance_nano = int(jetton_info['balance'])
    return balance_nano >= amount_nano

def log_claim(user_id, amount, success=True):
    """Логирование запроса в SQLite"""
    conn = sqlite3.connect('claims.db')
    c = conn.cursor()
    c.execute("INSERT INTO claims (user_id, amount, timestamp, success) VALUES (?, ?, ?, ?)",
              (user_id, amount, int(time.time()), 1 if success else 0))
    conn.commit()
    conn.close()

def get_user_address(user_id):
    """Получить TON-адрес пользователя из базы данных"""
    conn = sqlite3.connect('claims.db')
    c = conn.cursor()
    c.execute("SELECT address FROM user_addresses WHERE user_id = ?", (user_id,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None

def set_user_address(user_id, address):
    """Сохранить или обновить TON-адрес пользователя"""
    try:
        Address(address)  # Проверка валидности адреса
        conn = sqlite3.connect('claims.db')
        c = conn.cursor()
        c.execute("INSERT OR REPLACE INTO user_addresses (user_id, address, timestamp) VALUES (?, ?, ?)",
                  (user_id, address, int(time.time())))
        conn.commit()
        conn.close()
        return True
    except ValueError:
        return False