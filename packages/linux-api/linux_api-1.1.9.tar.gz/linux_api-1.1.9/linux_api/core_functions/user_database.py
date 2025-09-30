import os
import hmac
import hashlib
import secrets
import sqlite3
from enum import Enum
from datetime import datetime
from dotenv import load_dotenv
from dataclasses import dataclass
from typing import Optional, Dict, List

load_dotenv(dotenv_path="config.env")

DEMO_MODE = os.getenv("DEMO_MODE", "false").lower() == "true"

resetted_database = False

_user_db_instance = None

class UserRole(Enum):
    USER = "user"
    ADMIN = "admin"

@dataclass
class User:
    username: str
    role: UserRole
    api_key_hash: str
    salt: str
    created_at: datetime
    last_login: Optional[datetime] = None
    is_active: bool = True

class SecureUserDatabase:
    def __init__(self, db_path: str = "users.db", pepper: Optional[str] = None):

        self.db_path = db_path
        self.pepper = pepper or secrets.token_hex(32)
        
        self.iterations = 600000
        self.salt_length = 32
        self.hash_length = 64
        
        self._init_database()
    
    def _init_database(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()

            conn.execute("PRAGMA journal_mode=WAL;")
            conn.execute("PRAGMA synchronous=NORMAL;")

            cursor.execute('''
                CREATE TABLE IF NOT EXISTS users (
                    username TEXT PRIMARY KEY,
                    role TEXT NOT NULL,
                    api_key_hash TEXT NOT NULL,
                    salt TEXT NOT NULL,
                    created_at TEXT NOT NULL,
                    last_login TEXT,
                    is_active INTEGER NOT NULL DEFAULT 1
                )
            ''')
            
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS settings (
                    key TEXT PRIMARY KEY,
                    value TEXT NOT NULL
                )
            ''')
            
            cursor.execute('SELECT value FROM settings WHERE key = ?', ('pepper',))
            existing_pepper = cursor.fetchone()
            
            if existing_pepper:
                self.pepper = existing_pepper[0]
            else:
                cursor.execute('INSERT INTO settings (key, value) VALUES (?, ?)', 
                             ('pepper', self.pepper))
            
            conn.commit()
    
    def _generate_api_key(self) -> str:
        key = secrets.token_hex(64)
        return key

    def _generate_salt(self) -> str:
        return secrets.token_hex(self.salt_length)
    
    def _hash_api_key(self, api_key: str, salt: str) -> str:
        key_with_pepper = api_key + self.pepper
        
        hash_bytes = hashlib.pbkdf2_hmac(
            'sha256',
            key_with_pepper.encode('utf-8'),
            salt.encode('utf-8'),
            self.iterations,
            self.hash_length
        )
        
        return hash_bytes.hex()
    
    def _secure_compare(self, a: str, b: str) -> bool:
        return hmac.compare_digest(a.encode('utf-8'), b.encode('utf-8'))
    
    def add_user(self, username: str, role: UserRole, api_key: str = "", first_run: bool = False) -> str | bool:
        if api_key == "":
            api_key = self._generate_api_key()

        if username == "admin" and role == UserRole.ADMIN and first_run:
            print(f"Init admin key: {api_key}")

        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            cursor.execute('SELECT username FROM users WHERE username = ?', (username,))
            if cursor.fetchone():
                return False
            
            if self._api_key_exists(api_key):
                return False
            
            salt = self._generate_salt()
            api_key_hash = self._hash_api_key(api_key, salt)
            
            try:
                cursor.execute('''
                    INSERT INTO users (username, role, api_key_hash, salt, created_at, is_active)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (username, role.value, api_key_hash, salt, datetime.now().isoformat(), 1))
                
                conn.commit()
                return api_key
            except sqlite3.Error:
                return False
    
    def _api_key_exists(self, api_key: str) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT api_key_hash, salt FROM users')
            
            for api_key_hash, salt in cursor.fetchall():
                candidate_hash = self._hash_api_key(api_key, salt)
                if self._secure_compare(candidate_hash, api_key_hash):
                    return True
            
            return False
    
    def verify_api_key(self, api_key: str) -> Optional[tuple[str, UserRole]]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT username, role, api_key_hash, salt 
                FROM users 
                WHERE is_active = 1
            ''')
            
            for username, role, api_key_hash, salt in cursor.fetchall():
                candidate_hash = self._hash_api_key(api_key, salt)
                
                if self._secure_compare(candidate_hash, api_key_hash):
                    cursor.execute('''
                        UPDATE users 
                        SET last_login = ? 
                        WHERE username = ?
                    ''', (datetime.now().isoformat(), username))
                    conn.commit()
                    
                    return (username, UserRole(role))
            
            return None
    
    def get_user(self, username: str) -> Optional[User]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT username, role, api_key_hash, salt, created_at, last_login, is_active
                FROM users 
                WHERE username = ?
            ''', (username,))
            
            row = cursor.fetchone()
            if not row:
                return None
            
            username, role, api_key_hash, salt, created_at, last_login, is_active = row
            
            return User(
                username=username,
                role=UserRole(role),
                api_key_hash=api_key_hash,
                salt=salt,
                created_at=datetime.fromisoformat(created_at),
                last_login=datetime.fromisoformat(last_login) if last_login else None,
                is_active=bool(is_active)
            )
    
    def deactivate_user(self, username: str) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE users 
                SET is_active = 0 
                WHERE username = ?
            ''', (username,))
            
            if cursor.rowcount > 0:
                conn.commit()
                return True
            return False
    
    def delete_user(self, username: str) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM users WHERE username = ?', (username,))
            if cursor.rowcount > 0:
                conn.commit()
                return True
            return False

    def change_api_key(self, username: str, new_api_key: str) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            
            cursor.execute('SELECT username FROM users WHERE username = ?', (username,))
            if not cursor.fetchone():
                return False
            
            if self._api_key_exists(new_api_key):
                return False
            
            new_salt = self._generate_salt()
            new_hash = self._hash_api_key(new_api_key, new_salt)
            
            try:
                cursor.execute('''
                    UPDATE users 
                    SET salt = ?, api_key_hash = ? 
                    WHERE username = ?
                ''', (new_salt, new_hash, username))
                
                conn.commit()
                return True
            except sqlite3.Error:
                return False
    
    def list_users(self) -> List[Dict[str, any]]:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT username, role, created_at, last_login, is_active
                FROM users
                ORDER BY created_at
            ''')
            
            users = []
            for username, role, created_at, last_login, is_active in cursor.fetchall():
                users.append({
                    "username": username,
                    "role": role,
                    "created_at": created_at,
                    "last_login": last_login,
                    "is_active": bool(is_active)
                })
            
            return users

def reset_database(db_path: str = "users.db") -> bool:
    global resetted_database

    try:
        if os.path.exists(db_path):
            os.remove(db_path)

        resetted_database = True
        return True
    except Exception:
        return False

def initialize_default_users(db_path: str = "users.db", first_run: bool = False) -> SecureUserDatabase | str:
    db = SecureUserDatabase(db_path=db_path)
    demo_api_key = ...

    if not db.get_user("admin"):
        demo_api_key = db.add_user("admin", UserRole.ADMIN, first_run=first_run)
    
    return db, demo_api_key

def get_user_database(db_path: str = "users.db") -> SecureUserDatabase | str:
    global _user_db_instance

    demo_api_key = ...

    if DEMO_MODE and not resetted_database:
        print("Demo mode is enabled, resetting user database and creating default admin user with a new API key.")
        reset_database(db_path=db_path)
        _user_db_instance = None

    if _user_db_instance is None:
        _user_db_instance, demo_api_key = initialize_default_users(db_path=db_path, first_run=True)

    return _user_db_instance, demo_api_key