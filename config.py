class Config:

    # Twilio 账户信息
    ACCOUNT_SID = 'AC3a2a866f096ace58342aba574d30cdee'
    AUTH_TOKEN = "5a8d1890b5bc8542a9ed8bb1166fd1ba"

    TWILIO_WHATSAPP_NUMBER = "+14155238886"
    CONVERSATION_IDS = ""
    ENROLLED_NUMBER = ""

    DIFY_URL = "https://api.dify.ai/v1"
    DIFY_API_KEY = "app-bxNi8LXuBob9M5SMUC2WNySs"


class DevelopmentConfig(Config):
    DEBUG = True

config = {
    'development': DevelopmentConfig,

    "default": DevelopmentConfig
}