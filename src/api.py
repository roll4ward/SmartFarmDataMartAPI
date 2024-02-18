import yaml

from src.decorator import singleton
from src.specifications import SmartFarmProvideAPI
from src.specifications import SmartFarmCropSeasonAPI

@singleton
class SmartFarmAPI:
    def __init__(self, config) -> None:
        # Get service_key from config.yaml
        service_key = self._read_service_key_from_config(config)
        
        self.provide = SmartFarmProvideAPI(service_key)
        self.crop_season = SmartFarmCropSeasonAPI(service_key)
    
        # Checking sanity of service_key
        self.__sanity_check_for_service_key()
    
    def _read_service_key_from_config(self, config):
        with open(config, 'r') as file:
            data = yaml.safe_load(file)

        service_key = data["service_key"]
        
        if service_key  : return service_key
        else            : raise RuntimeError("Service key 를 입력해주세요.")
    
    def __sanity_check_for_service_key(self):
        from codes.error import ResponseErrorCode
        
        print(f"Snaity check를 위해 스마트팜 보급 농가의 사용자ID, 시설ID, 지역, 품목코드 조회합니다.")
        
        result = self.provide.getIdentityDataList() # Check if service_key is correct
        status_code = result[0]["statusCode"] # 첫 줄은 status_code 를 응답함.
        
        if status_code != "00":
            raise RuntimeError(ResponseErrorCode.get_description(status_code))
        else:
            print("Service key가 유효합니다.")
        
        
        

