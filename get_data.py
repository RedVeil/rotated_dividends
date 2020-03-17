import requests
import json


def get_historic_data(ticker, api_token, params):
    session = requests.Session()
    url_historic = f"https://eodhistoricaldata.com/api/eod/{ticker}?api_token={api_token}&fmt=json"
    reponse_historic = session.get(url_historic, params=params)
    if reponse_historic.status_code == requests.codes.ok:
        historic_data = json.loads(reponse_historic.text)
        return historic_data
    else:
        print(f"{ticker} historic status problem")


def get_dividend_data(ticker, api_token, params):
    session = requests.Session()
    url_dividends = f"https://eodhistoricaldata.com/api/div/{ticker}?api_token={api_token}&from=2000-01-01&fmt=json"
    reponse_dividends = session.get(url_dividends, params=params)
    if reponse_dividends.status_code == requests.codes.ok:
        dividend_data = json.loads(reponse_dividends.text)
        return dividend_data
    else:
        print(f"{ticker} dividend status problem")

def get_eod_data(eod_ticker, api_token):
    params = {"api_token": api_token}
    historic_data = get_historic_data(eod_ticker, api_token, params)
    dividend_data = get_dividend_data(eod_ticker, api_token, params)
    return historic_data, dividend_data


def get_ticker(api_token):
    exchange_codes={"GER":"XETRA"} #done: ("AT":"VI","DEN":"CO", "CHF":"VX","SWE":"ST"; "FR":"PA","SP":"MC","IT":"MI","NOR":"OL","CA":"TO","UK":"LSE") /to_do: ,"US":"US",,
    session = requests.Session()
    params = {"api_token": api_token}
    companies = {}

    for key in exchange_codes.keys():
        print(f"geting ticker from {exchange_codes[key]}")
        url_exchange= f"https://eodhistoricaldata.com/api/exchanges/{exchange_codes[key]}?api_token={api_token}&fmt=json"
        reponse_exchange = session.get(url_exchange, params=params)
        if reponse_exchange.status_code == requests.codes.ok:
            print("status ok")
            exchange_data = json.loads(reponse_exchange.text)
            common_stocks = []
            for security in exchange_data:
                if security["Type"] == "Common Stock":
                    common_stocks.append(security)

    return common_stocks


if __name__ == "__main__":
    api_token = "5d19ac0dbbdd85.51123060"
    #available_companies = get_ticker(api_token)
    #print(available_companies)
    historic_data, dividend_data = get_eod_data("BMW.XETRA",api_token)
    print(dividend_data)



## BMW + BMW3 Ticker beide als common stock angezeigt aber eins ist st und die andere ist vz