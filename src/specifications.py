import requests

from src.decorator import print_docstring



class _SmartFarmAPIRequester:
    def __init__(self, secrete_key):
        self._secrete_key = secrete_key
        self._base_url = "http://www.smartfarmkorea.net/Agree_WS/webservices"

    def _send_request(self, endpoint, params=None):
        """Send an HTTP request to the specified endpoint."""
        response = requests.get(f'{self._base_url}{endpoint}', params=params)
        
        if response.status_code == 200:
            return response.json()  # Return JSON content
        else:
            response.raise_for_status()  # Raise HTTPError for bad responses


class SmartFarmProvideAPI(_SmartFarmAPIRequester):
    @print_docstring
    def getIdentityDataList(self):
        """
        상세 기능 번호  : 1
        상세 기능 설명  : 스마트팜 보급 농가의 사용자ID, 시설ID, 지역, 품목코드 조회   
        
        * 요청 메세지 명세 *
            - `None`
        
        * 응답 메세지 명세 *
            - `userId`      : 사용자 ID
            - `facilityId`  : 시설 ID
            - `addressName` : 지역명 (법정동명)
            - `itemCode`    : 품목코드 (별첨 1. 품목코드 참고: ItemCode.get_code())
        """
        endpoint = f"/ProvideRestService/getIdentityDataList/{self._secrete_key}"
        return self._send_request(endpoint)
    
    @print_docstring
    def getCroppingSeasonDataList(self, userId):
        """
        상세 기능 번호  : 2
        상세 기능 설명  : 스마트팜 보급 농가 사용자의 작기 정보 조회 
        
        * 요청 메세지 명세 *
            userId      : 사용자 ID 

        * 응답 메세지 명세 *
            croppingS   erlNo: 작기 일련번호 Integer
            croppingSeasonName: 작기명 String
            itemCode: 품목코드 (별첨 1. 품목코드 참고: ItemCode.get_code())
            croppingDate: 작기 시작 일자 String (형식 : yyyy-mm-dd)
            croppingEndDate: 작기 종료 일자 String (형식 : yyyy-mm-dd)
            croppingSystem: 재배방식 코드 String (1: 토경, 2: 수경)
            cultivationArea: 재배 면적(평) Double 온실의 총 재배 면적 (단위 : 평)
            calCultivationArea: 재배 면적(㎡) Double (온실의 총 재배 면적 (단위 : ㎡))
            plantNum: 재식수량 Double (심은 총 작물의 수)
            calPlantNum: 1㎡당 재식수량 (1㎡당 심은 총 작물의 수)
            stemSlabNum: 배지 1개당 작물의 줄기 수
            planSlabNum: 배지 1개당 작물의 수
            plantDensity: 재식밀도
            standardPlantDensity: 기준 재식밀도
            floodlightDec: 투광율 (온실 내 투광량의 감소량)
            leafArea: 엽면적기준 (잎의 면적)
            stndTemp: 기준온도
            stndWeight: 기준과중
            열매의 무게
            stndSolar: 기준광
            stndMeta: 기초대사 (작물의 기초대사)
        """
        endpoint = f"/ProvideRestService/getCroppingSeasonDataList/{self._secrete_key}/{userId}"
        return self._send_request(endpoint)
    
    @print_docstring
    def getEnvDataList(
        self,
        facilityId: str, measDate: str, fldCode: str, 
        sectCode: str, fatrCode: str, itemCode: str
    ):
        """
        상세 기능 번호  : 3
        상세 기능 설명  : 스마트팜 보급 농가 시설의 환경 정보 조회 
        
        * 요청 메세지 명세 *    
            facilityId: 시설 ID String 
            measDate: 측정 일자 String (형식 : yyyy-mm-dd)
            fldCode: 분야코드 String (별첨 2. 분야코드 참고 (Fldcode))
            sectCode: 분류코드 String (별첨 3. 분류코드 참고 (SectCode))
            fatrCode: 항목코드 String (별첨 4. 항목코드 참고 (FatrCode))
            itemCode: 품목코드 String (별첨 1. 품목코드 참고 (ItemCode))

        * 응답 메세지 명세 *
            facilityId: 시설 ID String 
            measDate: 측정 일시 String (형식 : yyyy-mm-dd hh:mm:ss)
            itemCode: 품목코드 String (별첨 1. 품목코드 참고)
            fldCode: 분야코드 String (별첨 2. 분야코드 참고)
            sectCode: 분류코드 String (별첨 3. 분류코드 참고)
            fatrCode: 항목코드 String (별첨 4. 항목코드 참고)
            senVal: 측정값 String 
        """
        endpoint = f"/ProvideRestService/getEnvDataList/{self._secrete_key}/{facilityId}/{measDate}/{fldCode}/{sectCode}/{fatrCode}/{itemCode}"
        return self._send_request(endpoint)
    
    @print_docstring
    def getStrbCultivateDataList(
        self,
        userId: str, croppingSerlNo: int, startDate: str, endDate: str
    ):
        """
        상세 기능 번호  : 4
        상세 기능 설명  : 스마트팜 보급 농가 사용자의 딸기 생육 정보 조회
        
        * 요청 메세지 명세 *    
            userId: 사용자 ID String 
            croppingSerlNo: 작기 일련번호 Integer 
            startDate: 조회 시작 일자 String (형식 : yyyy-mm-dd)
            endDate: 조회 종료 일자 String (형식 : yyyy-mm-dd)
            
        * 응답 메세지 명세 *
            userId: 사용자 ID String 
            itemCode: 품목코드 String (별첨 1. 품목코드 참고)
            sampleNum: 표본번호 String 
            measDate: 측정일자 String (형식 : yyyy-mm-dd)
            leavesNum: 엽수 Double (잎의 수)
            nan: nan nan (단위 : 개)
            leavesLength: 엽장 Double (잎의 길이)
            nan: nan nan (단위 : mm)
            petioleLength: 엽병장 Double (엽신과 줄기 사이의 길이)
            nan: nan nan (단위 : cm)
            thecaDiameter: 관부 직경 Double (단위 : mm)
            fruitClusterNum: 화방수 Double (단위 : 개)
            firstFlowerNum: 1화방 꽃수 Double (단위 : 개)
            secondFlowerNum: 2화방 꽃수 Double (단위 : 개)
            thirdFlowerNum: 3화방 꽃수 Double (단위 : 개)
            firstFruitsNum: 1화방 착과수 Double (단위 : 개)
            secondFruitsNum: 2화방 착과수 Double (단위 : 개)
            thirdFruitsNum: 3화방 착과수 Double (단위 : 개)
            
        """
        endpoint = f"/ProvideRestService/getStrbCultivateDataList/{self._secrete_key}/{userId}/{croppingSerlNo}/{startDate}/{endDate}"
        return self._send_request(endpoint)
    
    @print_docstring
    def getMumCultivateDataList(
        self,
        userId: str, croppingSerlNo: int, startDate: str, endDate: str
    ):
        """
        상세 기능 번호  : 5
        상세 기능 설명  : 스마트팜 보급 농가 사용자의 국화 생육 정보 조회
        
        * 요청 메세지 명세 *    
            userId: 사용자 ID String 
            croppingSerlNo: 작기 일련번호 Integer 
            startDate: 조회 시작 일자 String (형식 : yyyy-mm-dd)
            endDate: 조회 종료 일자 String (형식 : yyyy-mm-dd)
            
        * 응답 메세지 명세 *
            userId: 사용자 ID String 
            itemCode: 품목코드 String (별첨 1. 품목코드 참고)
            sampleNum: 표본번호 String 
            measDate: 측정 일자 String (형식 : yyyy-mm-dd)
            flowerLength: 초장 Double (지표에서 선단까지의 길이) (단위 : mm)
            stemDiameter: 줄기 직경 Double (단위 : mm)
            leavesNum: 엽수 Double (잎의 수) (단위 : 개)
        """
        endpoint = f"/ProvideRestService/MumCultivateDataList/{self._secrete_key}/{userId}/{croppingSerlNo}/{startDate}/{endDate}"
        return self._send_request(endpoint)
    
    @print_docstring
    def getFruitCultivateDataList(
        self,
        userId: str, croppingSerlNo: int, startDate: str, endDate: str
    ):
        """
        상세 기능 번호  : 6
        상세 기능 설명  : 스마트팜 보급 농가 사용자의 참외 정보 조회
        
        * 요청 메세지 명세 *   
            userId: 사용자 ID String 
            croppingSerlNo: 작기 일련번호 Integer 
            startDate: 조회 시작 일자 String (형식 : yyyy-mm-dd)
            endDate: 조회 종료 일자 String (형식 : yyyy-mm-dd)
            
        * 응답 메세지 명세 *
            userId: 사용자 ID String 
            itemCode: 품목코드 String (별첨 1. 품목코드 참고)
            sampleNum: 표본번호 String 
            measDate: 측정 일자 String (형식 : yyyy-mm-dd)
            leavesLength: 엽장 Double (잎의 길이) (단위 : mm)
            leavesWidth: 엽폭 Double (잎의 너비) (단위 : mm)
            thecaDiameter: 관부 직경 Double (단위 : mm)
        """
        endpoint = f"/ProvideRestService/getFruitCultivateDataList/{self._secrete_key}/{userId}/{croppingSerlNo}/{startDate}/{endDate}"
        return self._send_request(endpoint)
    
    @print_docstring
    def getCultivateDataList(
        self,
        userId: str, croppingSerlNo: int, startDate: str, endDate: str
    ):
        """
        상세 기능 번호  : 7
        상세 기능 설명  : 스마트팜 보급 농가 사용자의 딸기·국화·참외를 제외한 생육 정보 조회 
        
        * 요청 메세지 명세 *   
            userId: 사용자 ID String 
            croppingSerlNo: 작기 일련번호 Integer 
            startDate: 조회 시작 일자 String (형식 : yyyy-mm-dd)
            endDate: 조회 종료 일자 String (형식 : yyyy-mm-dd)
            
        * 응답 메세지 명세 *
            userId: 사용자 ID String 
            itemCode: 품목코드 String (별첨 1. 품목코드 참고)
            sampleNum: 표본번호 String 
            measDate: 측정 일자 String (형식 : yyyy-mm-dd)
            growLength: 생장 길이 Double (단위 : mm)
            flowerTop: 화방 높이 Double (단위 : mm)
            stemDiameter: 줄기 직경 Double (단위 : mm)
            leavesLength: 엽장 Double (잎의 길이) (단위 : mm)
            leavesWidth: 엽폭 Double (잎의 너비) (단위 : mm)
            leavesNum: 엽수 Double (잎의 수) (단위 : 개)
            flowerPosition: 개화군 Double (꽃이 핀 무리) (단위 : 점)
            fruitsPosition: 착과군 Double (과일이 맺힌 무리) (단위 : 점)
            fruitsNum: 열매수 Double (단위 : 개)
            harvestPosition: 수확군 Double (단위 : 점)
            ped: PED Double 
            solarCorrection: 수광량 Double (작물이 받는 빛의 양)
            fruitsWeight: 평균과중 Double (평균 열매의 무게) (단위 : g)
        """
        endpoint = f"/ProvideRestService/getCultivateDataList/{self._secrete_key}/{userId}/{croppingSerlNo}/{startDate}/{endDate}"
        return self._send_request(endpoint)


class SmartFarmCropSeasonAPI(_SmartFarmAPIRequester):
    @print_docstring
    def getCroppingSeasonDataList(self, year: str):
        """
        상세 기능 번호  : 1
        상세 기능 설명  : 스마트팜 보급 농가 사용자의 작기 정보 조회 
        
        * 요청 메세지 명세 *    
            year: 작기 시작 년도 String (형식 : yyyy)
            
        * 응답 메세지 명세 *
            facilityId: 시설 ID String 
            addressName: 지역명 String (법정동명)
            croppingSerlNo: 작기 일련번호 Integer 
            itemCode       : 품목코드 String 
            itemName: 품목명 String
            croppingDate: 작기 시작 일자 String (형식 : yyyy-mm-dd)
            croppingEndDate: 작기 종료 일자 String (형식 : yyyy-mm-dd)
            acqAutoYn: 환경정보 등록 유무 String (Y : 등록, N : 미등록)
            acqManlYn: 제어정보 등록 유무 String (Y : 등록, N : 미등록)
            acqCultiYn: 생육정보 등록 유무 String (Y : 등록, N : 미등록)
            acqMgmtYn : 경영정보 등록 유무 String (Y : 등록, N : 미등록)
        """
        endpoint = f"/CropseasonRestService/getCroppingSeasonDataList/{self._secrete_key}/{year}"
        return self._send_request(endpoint)
    
    @print_docstring
    def getCroppingSeasonEnvDataList(
        self, 
        croppingSerlNo: int,
        pageNum: int
    ):
        """
        상세 기능 번호  : 2
        상세 기능 설명  : 스마트팜 보급 농가 사용자의 작기별 환경 정보 조회
        
        * 요청 메세지 명세 *   
            croppingSerlNo: 작기 일련번호 Integer 
            pageNum: 페이지 번호 Integer (1페이지당 1000건 조회)
            
        * 응답 메세지 명세 *
            facilityId: 시설 ID String 
            measDate: 측정 일자 String (형식 : yyyy-mm-dd hh:mm:ss)
            itemCode: 품목코드 String (별첨 1. 품목코드 참고)
            fldCode: 분야코드 String (별첨 2. 분야코드 참고)
            sectCode: 분류코드 String (별첨 3. 분류코드 참고)
            fatrCode: 항목코드 String (별첨 4. 항목코드 참고)
            senVal: 측정값 String 
            ymd: 수집 일자 String (형식 : yyyymmdd)
            cntCollect: 수집 건수 String 
            num: 순번 Integer 
            totalRows: 전체 건수 Integer 
            currentPage: 현재 페이지 String 
            totalPage: 전체 페이지 String 
        """
        endpoint = f"/CropseasonRestService/getCroppingSeasonEnvDataList/{self._secrete_key}/{croppingSerlNo}/{pageNum}"
        return self._send_request(endpoint)
    
    @print_docstring
    def getCroppingSeasonManlDataList(
        self, 
        croppingSerlNo: int,
        pageNum: int
    ):
        """
        상세 기능 번호  : 3
        상세 기능 설명  : 스마트팜 보급 농가 사용자의 작기별 제어 정보 조회
        
        * 요청 메세지 명세 *   
            croppingSerlNo: 작기 일련번호 Integer 
            pageNum: 페이지 번호 Integer (1페이지당 1000건 조회)
            
        * 응답 메세지 명세 *
            facilityId: 시설 ID String 
            measDate: 측정 일자 String (형식 : yyyy-mm-dd hh:mm:ss)
            itemCode: 품목코드 String (별첨 1. 품목코드 참고)
            fldCode: 분야코드 String (별첨 2. 분야코드 참고)
            sectCode: 분류코드 String (별첨 3. 분류코드 참고)
            fatrCode: 항목코드 String (별첨 4. 항목코드 참고)
            senVal: 측정값 String 
            ymd: 수집 일자 String (형식 : yyyymmdd)
            cntCollect: 수집 건수 String 
            num: 순번 Integer 
            totalRows: 전체 건수 Integer 
            currentPage: 현재 페이지 String 
            totalPage: 전체 페이지 String 
        """
        endpoint = f"/CropseasonRestService/getCroppingSeasonManlDataList/{self._secrete_key}/{croppingSerlNo}/{pageNum}"
        return self._send_request(endpoint)
    
    @print_docstring
    def getCultivateDataList(
        self, 
        croppingSerlNo: int,
    ):
        """
        상세 기능 번호  : 4
        상세 기능 설명  : 스마트팜 보급 농가 사용자의 작기별 생육 정보 조회
        
        * 요청 메세지 명세 *   
            croppingSerlNo: 작기 일련번호 Integer 
            
        * 응답 메세지 명세 *
            fcltyId: 시설 ID String 
            croppingSerlNo: 작기 일련번호 Integer 
            itemCode: 품목코드 String (별첨 1. 품목코드 참고)
            sampleNo: 표본 번호 Integer 
            examinMasterSn: 생육조사마스터 일련번호 Integer 
            examinSn: 조사 일련번호 Integer 
            examinDe: 조사 일자 String (형식 : yyyymmdd)
            examinIemCode: 조사 항목 코드 String 
            examinIemNm: 조사 항목명 String 
            examinIemValue: 조사 항목 측정값 Double 
            examinIemUnit: 조사 항목 단위 String 
        """
        endpoint = f"/CropseasonRestService/getCultivateDataList/{self._secrete_key}/{croppingSerlNo}"
        return self._send_request(endpoint)