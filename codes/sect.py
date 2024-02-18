"""별첨. 3.3. 분류코드 (sectCode)"""

from codes.smartfarm_codes import SmartFarmCodes


class SectCode(SmartFarmCodes):
    code_dict = {
        "CR": "제어정보",
        "EI": "내부환경",
        "EL": "토양환경",
        "EO": "외부환경",
        "NT": "양액정보",
    }