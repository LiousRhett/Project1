class Config:

    # Twilio 账户信息
    ACCOUNT_SID = 'AC3a2a866f096ace58342aba574d30cdee'
    AUTH_TOKEN = "[AuthToken]"
    TWILIO_WHATSAPP_NUMBER = "whatsapp:+8613075581109"


class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig
}