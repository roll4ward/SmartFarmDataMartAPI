from typing import Any


class ResponseErrorCode:
    error_dict = {
        "00": "정상",
        "01": "어플리케이션 에러",
        "02": "DB 에러",
        "03": "데이터없음 에러",
        "04": "HTTP 에러",
        "05": "서비스 연결 실패 에러",
        "10": "잘못된 요청 파라미터 에러",
        "11": "필수요청 파라미터 없음 에러",
        "12": "해당 OPENAPI 서비스가 없거나 폐기됨 에러",
        "20": "서비스 접근 거부 에러",
        "21": "일시적으로 사용할 수 없는 서비스키 에러",
        "22": "서비스 요청 제한 횟수 초과 에러",
        "30": "등록되지 않은 서비스키 에러",
        "31": "기한만료된 서비스키 에러",
        "32": "등록되지 않은 IP 주소 에러",
        "33": "서명되지 않은 호출 에러",
        "99": "기타 에러",
    }
    
    @staticmethod
    def get_error_message(status_code: str) -> str:
        return ResponseErrorCode.error_dict.get(status_code, "알 수 없는 에러 코드")
    
    