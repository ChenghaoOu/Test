import requests
from jsonpath import jsonpath

project_list = ["badger","uniswap","sushiswap","aaveV1","aaveV2","compound","yearn","curve","vesper","synthetix","origin","pancakeSwap","qucikswap"]
request = requests.session()
for project_name in project_list:
    if project_name == "badger":
        url = "https://tokenpad-api.dev.57blocks.com/defi/portfolio?projectId=badger&userAddr=0x60758B3A6933192D0Ac28Fc1f675364bb4dFAb1d&chain=Ethereum"
        tag = ['deposit', 'yield']
        try:
            response = request.get(url)
            assert response.status_code == 200,"badger接口异常"
            assert sorted(jsonpath(response.json(),"$..tag")) == sorted(tag),"badger数据缺失"
        except AssertionError as e:
            print(e)
        finally:
            continue

    elif project_name == "unsiwap":
        url = "https://tokenpad-api.dev.57blocks.com/defi/portfolio?projectId=uniswap&userAddr=0x60758B3A6933192D0Ac28Fc1f675364bb4dFAb1d&chain=Ethereum"
        try:
            response = request.get(url)
            assert response.status_code == 200,"uniswap接口异常"
            assert sorted(jsonpath(response.json(),"$..tag")) == ['liquidity'],"uniswap数据缺失"
        except AssertionError as e:
            print(e)
        finally:
            continue

    elif project_name == "sushiswap":
        url = "https://tokenpad-api.dev.57blocks.com/defi/portfolio?projectId=sushiswap&userAddr=0x60758B3A6933192D0Ac28Fc1f675364bb4dFAb1d&chain=Ethereum"
        tag = ['liquidity', 'farming', 'yield']
        try:
            response = request.get(url)
            assert response.status_code == 200,"shushiswap接口异常"
            assert sorted(jsonpath(response.json(),"$..tag")) == sorted(tag),"sushiswap数据缺失"
        except AssertionError as e:
            print(e)
        finally:
            continue

    elif project_name == "aaveV2":
        url = "https://tokenpad-api.dev.57blocks.com/defi/portfolio?projectId=aaveV2&userAddr=0x3cc542c4198990bcd1c98bc6af99865dceebc6a4&chain=Ethereum"
        tag = ['yield', 'loan', 'loan']
        try:
            response = request.get(url)
            assert response.status_code == 200,"aaveV2接口异常"
            assert sorted(jsonpath(response.json(),"$..tag")) == sorted(tag),"aaveV2数据缺失"
        except AssertionError as e:
            print(e)
        finally:
            continue

    elif project_name == "aaveV1":
        url = "https://tokenpad-api.dev.57blocks.com/defi/portfolio?projectId=aaveV1&userAddr=0x3cc542c4198990bcd1c98bc6af99865dceebc6a4&chain=Ethereum"
        tag = ['loan', 'loan']
        try:
            response = request.get(url)
            assert response.status_code == 200,"aaveV1接口异常"
            assert sorted(jsonpath(response.json(),"$..tag")) == sorted(tag),"aaveV1数据缺失"
        except AssertionError as e:
            print(e)
        finally:
            continue

    elif project_name == "compound":
        url = "https://tokenpad-api.dev.57blocks.com/defi/portfolio?projectId=compound&userAddr=0x3cc542c4198990bcd1c98bc6af99865dceebc6a4&chain=Ethereum"
        tag = ['loan', 'loan', 'yield']
        try:
            response = request.get(url)
            assert response.status_code == 200,"compound接口异常"
            assert sorted(jsonpath(response.json(),"$..tag")) == sorted(tag),"compound数据缺失"
        except AssertionError as e:
            print(e)
        finally:
            continue

    elif project_name == "yearn":
        url = "https://tokenpad-api.dev.57blocks.com/defi/portfolio?projectId=yearn&userAddr=0xA9f5422AC2454327f81503B65a3058b77Ad39545&chain=Ethereum"
        try:
            response = request.get(url)
            assert response.status_code == 200,"yearn接口异常"
            assert sorted(jsonpath(response.json(),"$..tag")) == ['deposit'],"yearn数据缺失"
        except AssertionError as e:
            print(e)
        finally:
            continue

    elif project_name == "curve":
        url = "https://tokenpad-api.dev.57blocks.com/defi/portfolio?projectId=curve&userAddr=0xA9f5422AC2454327f81503B65a3058b77Ad39545&chain=Ethereum"
        try:
            response = request.get(url)
            assert response.status_code == 200,"curve接口异常"
            assert sorted(jsonpath(response.json(),"$..tag")) == ['liquidity'],"curve数据缺失"
        except AssertionError as e:
            print(e)
        finally:
            continue

    elif project_name == "vesper":
        url = "https://tokenpad-api.dev.57blocks.com/defi/portfolio?projectId=vesper&userAddr=0xA9f5422AC2454327f81503B65a3058b77Ad39545&chain=Ethereum"
        tag = ['deposit', 'yield']
        try:
            response = request.get(url)
            assert response.status_code == 200,"vesper接口异常"
            assert sorted(jsonpath(response.json(),"$..tag")) == sorted(tag),"vesper数据缺失"
        except AssertionError as e:
            print(e)
        finally:
            continue

    elif project_name == "synthetix":
        url = "https://tokenpad-api.dev.57blocks.com/defi/portfolio?projectId=synthetix&userAddr=0xc15025E98Ba033F9475785083e31B7811b0Fd0A4&chain=Ethereum"
        tag = ['yield', 'yield', 'loan']
        try:
            response = request.get(url)
            assert response.status_code == 200,"synthetix接口异常"
            assert sorted(jsonpath(response.json(),"$..tag")) == sorted(tag),"synthetix数据缺失"
        except AssertionError as e:
            print(e)
        finally:
            continue

    elif project_name == "origin":
        url = "https://tokenpad-api.dev.57blocks.com/defi/portfolio?projectId=origin&userAddr=0xc15025E98Ba033F9475785083e31B7811b0Fd0A4&chain=Ethereum"
        tag = ['deposit', 'yield']
        try:
            response = request.get(url)
            assert response.status_code == 200,"origin接口异常"
            assert sorted(jsonpath(response.json(),"$..tag")) == sorted(tag),"origin数据缺失"
        except AssertionError as e:
            print(e)
        finally:
            continue

    elif project_name == "pancakeSwap":
        url = f"https://tokenpad-api.dev.57blocks.com/defi/portfolio?projectId={project_name}&userAddr=0xa37145a1edb49fcd376d49890c07454ea48cd313&chain=BSC"
        tag = ['liquidity', 'liquidity', 'farming', 'farming', 'deposit', 'yield']
        try:
            response = request.get(url)
            assert response.status_code == 200,"pancakeSwap接口异常"
            assert sorted(jsonpath(response.json(),"$..tag")) == sorted(tag),"pancakeSwap数据缺失"
        except AssertionError as e:
            print(e)
        finally:
            continue

    elif project_name == "quickswap":
        url = f"https://tokenpad-api.dev.57blocks.com/defi/portfolio?projectId=quickswap&userAddr=0xa32321E3aAfc3C947c232f2CAbbDA043768e6953&chain=Polygon"
        tag =['liquidity', 'liquidity', 'farming', 'farming', 'farming', 'farming', 'farming', 'farming', 'farming', 'deposit', 'yield', 'yield', 'yield', 'yield', 'yield', 'yield']
        try:
            response = request.get(url)
            assert response.status_code == 200,"quickswap接口异常"
            assert sorted(jsonpath(response.json(),"$..tag")) == sorted(tag),"quickswap数据缺失"
        except AssertionError as e:
            print(e)
        finally:
            continue


