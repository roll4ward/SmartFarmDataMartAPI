import requests



class _SmartFarmAPIRequester:
    def __init__(self, secrete_key):
        self.secrete_key = secrete_key
        self.base_url = "http://www.smartfarmkorea.net/Agree_WS/webservices"

    def _send_request(self, endpoint, params=None):
        """Send an HTTP request to the specified endpoint."""
        response = requests.get(f'{self.base_url}{endpoint}', params=params)
        
        if response.status_code == 200:
            return response.json()  # Return JSON content
        else:
            response.raise_for_status()  # Raise HTTPError for bad responses


class SmartFarmProductionAPI(_SmartFarmAPIRequester):
    def getIdentityDataList(self):
        """
        상세 기능 번호  : 1
        상세 기능 설명  : 스마트팜 보급 농가의 사용자ID, 시설ID, 지역, 품목코드 조회    
        """
        endpoint = f"/ProvideRestService/getIdentityDataList/{self.secrete_key}"
        return self._send_request(endpoint)
    
    def getCroppingSeasonDataList(self, userId):
        """
        상세 기능 번호  : 2
        상세 기능 설명  : 스마트팜 보급 농가 사용자의 작기 정보 조회 
        """
        endpoint = f"/ProvideRestService/getCroppingSeasonDataList/{self.secrete_key}/{userId}"
        return self._send_request(endpoint)
    
    def getEnvDataList(
        self,
        facilityId: str, measDate: str, fldCode: str, 
        sectCode: str, fatrCode: str, itemCode: str
    ):
        """
        상세 기능 번호  : 3
        상세 기능 설명  : 스마트팜 보급 농가 시설의 환경 정보 조회 
        
        args:    
            facilityId  : 시설 ID
            measDate    : 측정 일자
            fldCode     : 분야코드 (별첨 2. 분야코드 참고)
            sectcode    : 분류코드 (별첨 3. 분류코드 참고)
            fatrCode    : 항목코드 (별첨 4. 항목코드 참고)
            itemCode    : 품목코드 (별첨 1. 품목코드 참고)
        """
        endpoint = f"/ProvideRestService/getEnvDataList/{self.secrete_key}/{facilityId}/{measDate}/{fldCode}/{sectCode}/{fatrCode}/{itemCode}"
        return self._send_request(endpoint)
    
    def getStrbCultivateDataList(
        self,
        userId: str, croppingSerlNo: int, startDate: str, endDate: str
    ):
        """
        상세 기능 번호  : 4
        상세 기능 설명  : 스마트팜 보급 농가 사용자의 딸기 생육 정보 조회
        
        args:    
            userId          : 사용자 ID
            croppingSerlNo  : 작기 일련번호
            startDate       : 조회 시작 일자 (형식: yyyy-mm-dd)
            endDate         : 조회 종료 일자 (형식: yyyy-mm-dd)
        """
        endpoint = f"/ProvideRestService/getStrbCultivateDataList/{self.secrete_key}/{userId}/{croppingSerlNo}/{startDate}/{endDate}"
        return self._send_request(endpoint)
    
    def getMumCultivateDataList(
        self,
        userId: str, croppingSerlNo: int, startDate: str, endDate: str
    ):
        """
        상세 기능 번호  : 5
        상세 기능 설명  : 스마트팜 보급 농가 사용자의 국화 생육 정보 조회
        
        args:    
            userId          : 사용자 ID
            croppingSerlNo  : 작기 일련번호
            startDate       : 조회 시작 일자 (형식: yyyy-mm-dd)
            endDate         : 조회 종료 일자 (형식: yyyy-mm-dd)
        """
        endpoint = f"/ProvideRestService/MumCultivateDataList/{self.secrete_key}/{userId}/{croppingSerlNo}/{startDate}/{endDate}"
        return self._send_request(endpoint)
    
    def getFruitCultivateDataList(
        self,
        userId: str, croppingSerlNo: int, startDate: str, endDate: str
    ):
        """
        상세 기능 번호  : 6
        상세 기능 설명  : 스마트팜 보급 농가 사용자의 참외 정보 조회
        
        args:    
            userId          : 사용자 ID
            croppingSerlNo  : 작기 일련번호
            startDate       : 조회 시작 일자 (형식: yyyy-mm-dd)
            endDate         : 조회 종료 일자 (형식: yyyy-mm-dd)
        """
        endpoint = f"/ProvideRestService/getFruitCultivateDataList/{self.secrete_key}/{userId}/{croppingSerlNo}/{startDate}/{endDate}"
        return self._send_request(endpoint)
    
    def getCultivateDataList(
        self,
        userId: str, croppingSerlNo: int, startDate: str, endDate: str
    ):
        """
        상세 기능 번호  : 7
        상세 기능 설명  : 스마트팜 보급 농가 사용자의 딸기·국화·참외를 제외한 생육 정보 조회 
        
        args:    
            userId          : 사용자 ID
            croppingSerlNo  : 작기 일련번호
            startDate       : 조회 시작 일자 (형식: yyyy-mm-dd)
            endDate         : 조회 종료 일자 (형식: yyyy-mm-dd)
        """
        endpoint = f"/ProvideRestService/getCultivateDataList/{self.secrete_key}/{userId}/{croppingSerlNo}/{startDate}/{endDate}"
        return self._send_request(endpoint)


class SmartFarmCropSeasonAPI(_SmartFarmAPIRequester):
    def getCroppingSeasonDataList(self, year: str):
        """
        상세 기능 번호  : 1
        상세 기능 설명  : 스마트팜 보급 농가 사용자의 작기 정보 조회 
        
        args:    
            year    : 작기 시작 년도 (yyyy)
        """
        endpoint = f"/CropseasonRestService/getCroppingSeasonDataList/{self.secrete_key}/{year}"
        return self._send_request(endpoint)
    
    def getCroppingSeasonEnvDataList(
        self, 
        croppingSerlNo: int,
        pageNum: int
    ):
        """
        상세 기능 번호  : 2
        상세 기능 설명  : 스마트팜 보급 농가 사용자의 작기별 환경 정보 조회
        
        args:    
            croppingSerlNo      : 작기 일련번호
            pageNum             : 한 페이지당 1000건 조회
        """
        endpoint = f"/CropseasonRestService/getCroppingSeasonEnvDataList/{self.secrete_key}/{croppingSerlNo}/{pageNum}"
        return self._send_request(endpoint)
    
    def getCroppingSeasonManlDataList(
        self, 
        croppingSerlNo: int,
        pageNum: int
    ):
        """
        상세 기능 번호  : 3
        상세 기능 설명  : 스마트팜 보급 농가 사용자의 작기별 제어 정보 조회
        
        args:    
            croppingSerlNo      : 작기 일련번호
            pageNum             : 한 페이지당 1000건 조회
        """
        endpoint = f"/CropseasonRestService/getCroppingSeasonManlDataList/{self.secrete_key}/{croppingSerlNo}/{pageNum}"
        return self._send_request(endpoint)
    
    def getCultivateDataList(
        self, 
        croppingSerlNo: int,
    ):
        """
        상세 기능 번호  : 4
        상세 기능 설명  : 스마트팜 보급 농가 사용자의 작기별 생육 정보 조회
        
        args:    
            croppingSerlNo      : 작기 일련번호
            pageNum             : 한 페이지당 1000건 조회
        """
        endpoint = f"/CropseasonRestService/getCultivateDataList/{self.secrete_key}/{croppingSerlNo}"
        return self._send_request(endpoint)