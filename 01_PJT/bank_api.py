# 금융 상품 데이터 수집 API
import pprint
import requests

def get_deposit_product():
    api_key = "957d9a90c722f26f20d21e7fbbefeab1"

    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json'
    params = {
        'auth' : api_key,
        # 금융회사 코드 ---
        'topFinGrpNo' : '020000',
        'pageNo' : 1
    }

    # 응답을 json 형태로 변환
    response = requests.get(url, params=params).json()
    term_deposit = response["result"]
    base_List = term_deposit["baseList"]
    option_list = term_deposit["optionList"]
    
    whole_new_bank_list = []
   
    # baseList를 순회한다
    for base_item in base_List:
        new_bank_list = {}
        whole_new_option_list = []
        # OptionList의 목록이
        for option_item in option_list:
            if option_item["fin_prdt_cd"] == base_item["fin_prdt_cd"]:
                new_option_list = {}
                new_option_list["저축 금리"] =  option_item["intr_rate"]
                new_option_list["저축 기간"] = option_item["save_trm"]
                new_option_list["저축금리유형"] = option_item["intr_rate_type"]
                new_option_list["저축금리유형명"] = option_item["intr_rate_type_nm"]
                new_option_list["최고 우대금리"] = option_item["intr_rate2"]
                whole_new_option_list.append(new_option_list)

        new_bank_list["금리정보"] = whole_new_option_list
        new_bank_list["금융상품명"] = base_item["fin_prdt_nm"]
        new_bank_list["금융회사명"] = base_item["kor_co_nm"]
        whole_new_bank_list.append(new_bank_list)

    return whole_new_bank_list

if __name__ == '__main__':
    # json형태의 데이터 반환
    result = get_deposit_product()
    # pprint.pprint(): json을 보기 좋은 형식으로 출력
    pprint.pprint(result)