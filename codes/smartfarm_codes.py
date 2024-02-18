"""별첨. Code class 정의"""


class SmartFarmCodes:
    @classmethod
    def get_description(cls, code: str) -> str:
        return cls.code_dict.get(code, "알 수 없는 에러 코드")
    
    @classmethod
    def get_codes(cls) -> dict:
        return cls.code_dict