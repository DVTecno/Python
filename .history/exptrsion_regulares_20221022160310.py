import string
import secrets
import random
import re

def check_password(password):
    password_pattern="(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&/_=;:<>|#,\*\'\"\-\+\[
        ]])"