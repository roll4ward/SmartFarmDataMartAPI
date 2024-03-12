## 스마트팜코리아 데이터마트 SmartFarmDataMartAPI

Python의 다양한 데이터 분석 라이브러리를 활용하기 위해 스마트팜코리아 데이터마트 API를 python으로 랩핑하는 프로젝트입니다.

[스마트팜코리아 데이터마트 홈페이지](https://data.smartfarmkorea.net)에서도 다양한 농가에서 수집된 데이터를 csv형식의 파일로 다운로드 받을 수 있는 UI를 제공하지만 사용에 몇가지 제한이 있습니다.

> #### 기존 방식의 문제
> 1. REST, SOAP API로만 데이터를 제공하기 때문에 이를 다시 파싱하여 사용해야합니다.
> 2. 필요한 데이터를 multi-step 으로 요청해야함. ( (__1.__)전체 농가의 serialID만을 먼저 요청하여 필요한 serialID를 저장해두고 (__2.__) 다시 특정 농가의 데이터를 요청해야합니다.) 
> 3. 에러 코드, 응답 코드, 요청 코드등이 해시처럼 코드로 명시돼있어 명세 문서를 보지 않고는 사용이 어렵습니다. <br>

이러한 문제를 해결하기 위해 다음과 같은 목표를 갖는 프로젝트를 수행합니다.

> #### Contributions
> 1. 🐍 Python으로 openAPI를 wrapping.
>> 다양한 데이터 라이브러리를 활용할 수 있도록 스마트팜 데이터마트 openAPI를 python으로 wrapping 하여 별다른 파싱 없이 바로 사용하거나 csv, excel등의 포맷으로 저장할 수 있도록 합니다.
> 2. ⛓️ 여러 기본 API를 엮습니다. 
>> 더욱 복합적인 데이터를 요청할 수 있도록 기존의 API를 묶어 한 번에 데이터를 요청할 수 있도록 합니다.
> 3. ☝🏻 Notebook을 활용한 user-interactive tool. 
>> 복잡한 에러, 요청, 응답코드들을 명세 문서를 참고하지 않고도 사용할 수 있도록 user-interactive한 사용 환경을 제공합니다. 

---
## Usage

### 🛠️ Requirements
```shell
pip install ipykernel
pip install requests
pip install pyyaml
```

### 🚀 How to use?
1. OpenAPI service key를 [스마트팜코리아 데이터마트]발급 받습니다.(https://data.smartfarmkorea.net/openApi/openApiUseInfo.do?menuId=M060501)
2. 발급받은 service key를 `config.yaml` 파일에 입력합니다.<br>
```yaml
service_key: "9d7b25ec.................."
```
3. 자세한 활용방법은 `usage_code.ipynb` 를 참고하세요. 간단합니다!
4. package로 사용하기 위해서는 setup.py 파일을 활용하여 package로 사용합니다.
```shell
python -m pip install -e .
```

### 🖌 사용 가능한 API lists
- `provide`
    - `getIdentityDataList`: 아이덴티티 정보
    - `getCroppingSeasonDataList`: 작기 정보
    - `getEnvDataList`: 환경 정보
    - `getStrbCultivateDataList`: 생육 정보(딸기)
    - `getMumCultivateDataList`: 생육 정보(국화)
    - `getFruitCultivateDataList`: 생육 정보(참외)
    - `getCultivateDataList`: 생육 정보(그외)

- `crop_season`
    - `getCroppingSeasonDataList`: 농가별 작기 정보
    - `getCroppingSeasonEnvDataList`: 작기별 환경 정보
    - `getCroppingSeasonManlDataList`: 작기별 제어 정보
    - `getCultivateDataList`: 작기별 생육 정보

### 별첨 코드
- 1. __품목코드__ (`ItemCode`)
    - example usage: `codes.appendix.ItemCode.get_code()`
- 2. __분야코드__ (`FldCode`)
    - example usage: `codes.appendix.FldCode.get_code()`
- 3. __분류코드__ (`SectCode`)
    - example usage: `codes.appendix.SectCode.get_code()`
- 4. __항목코드__ (`FatrCode`)
    - example usage: `codes.appendix.FatrCode.get_code()`






