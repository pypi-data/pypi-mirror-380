from .common import Common
from .clickhouse import Clickhouse
import requests
from datetime import datetime,timedelta
import clickhouse_connect
import pandas as pd
import os
from dateutil import parser
import time
import hashlib
from io import StringIO
import json
import zipfile
import io
import csv


class MRKTbyDate:
    def __init__(self, bot_token:str = '', chats:str = '', message_type: str = '', subd: str = '',
                 host: str = '', port: str = '', username: str = '', password: str = '', database: str = '',
                 add_name: str = '', clientid:str = '', token: str  = '',  start: str = '', backfill_days: int = 0, reports :str = ''):
        self.bot_token = bot_token
        self.chat_list = chats.replace(' ', '').split(',')
        self.message_type = message_type
        self.common = Common(self.bot_token, self.chat_list, self.message_type)
        self.clientid = clientid
        self.token = token
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.database = database
        self.subd = subd
        self.add_name = self.common.transliterate_key(add_name)
        self.now = datetime.now()
        self.today = datetime.now().date()
        self.start = start
        self.reports = reports
        self.backfill_days = backfill_days
        self.yesterday = self.today - timedelta(days=1)
        self.yesterday_str = self.yesterday.strftime("%Y-%m-%d")
        self.platform = 'mrkt'

        self.err429 = False
        self.source_dict = {
            'stocks': {
                'platform': 'mrkt',
                'report_name': 'stocks',
                'upload_table': 'stocks',
                'func_name': self.get_all_stocks,
                'uniq_columns': 'warehouseId',
                'partitions': '',
                'merge_type': 'MergeTree',
                'refresh_type': 'delete_all',
                'history': False,
                'frequency': 'daily',  # '2dayOfMonth,Friday'
                'delay': 20
            },
            'mappings': {
                'platform': 'mrkt',
                'report_name': 'mappings',
                'upload_table': 'mappings',
                'func_name': self.fetch_all_offer_mappings,
                'uniq_columns': 'timeStamp',
                'partitions': '',
                'merge_type': 'MergeTree',
                'refresh_type': 'delete_all',
                'history': False,
                'frequency': 'daily',  # '2dayOfMonth,Friday'
                'delay': 20
            },
            'orders': {
                'platform': 'mrkt',
                'report_name': 'orders',
                'upload_table': 'orders',
                'func_name': self.fetch_all_orders,
                'uniq_columns': 'id,creationDate',
                'partitions': 'creationDate',
                'merge_type': 'ReplacingMergeTree(timeStamp)',
                'refresh_type': 'nothing',
                'history': True,
                'frequency': 'daily',  # '2dayOfMonth,Friday'
                'delay': 20
            },
            'price_report': {
                'platform': 'mrkt',
                'report_name': 'price_report',
                'upload_table': 'price_report',
                'func_name': self.get_price_report,
                'uniq_columns': 'first_date,file_name',
                'partitions': 'first_date',
                'merge_type': 'MergeTree',
                'refresh_type': 'delete_date',
                'history': True,
                'frequency': 'daily',  # '2dayOfMonth,Friday'
                'delay': 20
            },
            'orders_report': {
                'platform': 'mrkt',
                'report_name': 'orders_report',
                'upload_table': 'orders_report',
                'func_name': self.get_orders_report,
                'uniq_columns': 'first_date,file_name',
                'partitions': 'first_date',
                'merge_type': 'MergeTree',
                'refresh_type': 'delete_date',
                'history': True,
                'frequency': 'daily',  # '2dayOfMonth,Friday'
                'delay': 20
            },
        }

    def get_stocks_data(self, campaign_id, token, next_page_token=None):
        try:
            final_list = []
            url = f"https://api.partner.market.yandex.ru/campaigns/{campaign_id}/offers/stocks"
            headers = {
                "Authorization": f"Bearer {token}",
                "Content-Type": "application/json"  # Обязательно для POST-запроса
            }
            payload = {
                "limit": 100
            }
            data = {}
            if next_page_token:
                data = {"page_token": next_page_token}
            response = requests.post(url, headers=headers, json=payload, params=data)
            if response.status_code not in {200, 400, 404}:
                response.raise_for_status()
            result = response.json()
            if "result" not in result:
                return [], None
            warehouses = result["result"].get("warehouses", [])
            for wh in warehouses:
                wh_id = wh.get("warehouseId")
                offers = wh.get("offers", [])
                for o in offers:
                    stock = o.get("stocks", None)
                    updatedAt = o.get("updatedAt", None)
                    if stock != []:
                        for st in stock:
                            start_dict = {'warehouseId': wh_id, 'offerId': o['offerId'], 'updatedAt': updatedAt}
                            final_list.append(start_dict | st)
            next_page_token = result["result"].get("paging", {}).get("nextPageToken")
            return final_list, next_page_token
        except Exception as e:
            message = f'Платформа: MRKT. Имя: {self.add_name}. Даты: {str(date)}. Функция: get_stocks_data. Ошибка: {e}.'
            self.common.log_func(self.bot_token, self.chat_list, message, 3)
            raise


    def get_all_stocks(self, date=''):
        try:
            all_stocks = []
            next_page_token = None
            for _ in range(1000):
                stocks, next_page_token = self.get_stocks_data(self.clientid, self.token, next_page_token)
                all_stocks += stocks
                if not next_page_token:
                    break
                time.sleep(0.2)
            message = f'Платформа: MRKT. Имя: {self.add_name}. Дата: {str(date)}. Функция: get_stocks_data. Результат: ОК'
            self.common.log_func(self.bot_token, self.chat_list, message, 1)
            return all_stocks
        except Exception as e:
            message = f'Платформа: MRKT. Имя: {self.add_name}. Даты: {str(date)}. Функция: get_stocks_data. Ошибка: {e}.'
            self.common.log_func(self.bot_token, self.chat_list, message, 3)
            return message


    def get_orders_data(self,date, next_page_token=None):
        try:
            final_list = []
            url = f"https://api.partner.market.yandex.ru/campaigns/{self.clientid}/stats/orders"
            headers = {
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json"  # Обязательно для запросов
            }
            payload = {
                'dateFrom': date, 'dateTo': date
            }
            params = {"limit": 200}
            if next_page_token:
                params = {"limit": 200, "page_token": next_page_token}
            response = requests.post(url, headers=headers, json=payload, params=params)
            code = response.status_code
            if code not in {200}:
                response.raise_for_status()
            result = response.json()
            if "result" not in result:
                return [], None
            orders = result["result"].get("orders", [])
            for order in orders:
                final_list.append(order)
            next_page_token = result["result"].get("paging", {}).get("nextPageToken")
            return final_list, next_page_token
        except Exception as e:
            message = f'Платформа: MRKT. Имя: {self.add_name}. Даты: {str(date)}. Функция: get_orders_data. Ошибка: {e}.'
            self.common.log_func(self.bot_token, self.chat_list, message, 3)
            raise


    def fetch_all_orders(self, date):
        try:
            all_orders = []
            next_page_token = None
            for _ in range(1000):
                orders, next_page_token = self.get_orders_data(date, next_page_token)
                all_orders += orders
                if not next_page_token:
                    break
                time.sleep(0.1)
            message = f'Платформа: MRKT. Имя: {self.add_name}. Дата: {str(date)}. Функция: fetch_all_orders. Результат: ОК'
            self.common.log_func(self.bot_token, self.chat_list, message, 1)
            return self.common.spread_table(self.common.spread_table(self.common.spread_table(all_orders)))
        except Exception as e:
            message = f'Платформа: MRKT. Имя: {self.add_name}. Даты: {str(date)}. Функция: fetch_all_orders. Ошибка: {e}.'
            self.common.log_func(self.bot_token, self.chat_list, message, 3)
            return message


    def get_offer_mappings_data(self, next_page_token=None):
        try:
            url = f"https://api.partner.market.yandex.ru/businesses/{self.clientid}/offer-mappings"
            headers = {
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json"
            }
            params = {"limit": 200}
            if next_page_token:
                params["page_token"] = next_page_token
            response = requests.post(url, headers=headers, params=params)
            if response.status_code != 200:
                response.raise_for_status()
            result = response.json()
            if "result" not in result:
                return [], None
            offer_mappings = result["result"].get("offerMappings", [])
            next_page_token = result["result"].get("paging", {}).get("nextPageToken")
            return offer_mappings, next_page_token
        except Exception as e:
            message = f'Платформа: MRKT. Имя: {self.add_name}. Функция: get_offer_mappings_data. Ошибка: {e}.'
            self.common.log_func(self.bot_token, self.chat_list, message, 3)
            return message


    def fetch_all_offer_mappings(self,date=''):
        try:
            all_offer_mappings = []
            next_page_token = None
            for _ in range(1000):
                offer_mappings, next_page_token = self.get_offer_mappings_data(next_page_token)
                all_offer_mappings.extend(offer_mappings)
                if not next_page_token:
                    break
                time.sleep(0.1)
            message = f'Платформа: MRKT. Имя: {self.add_name}. Дата: {str(date)}. Функция: fetch_all_offer_mappings. Результат: ОК'
            self.common.log_func(self.bot_token, self.chat_list, message, 1)
            return self.common.spread_table(self.common.spread_table(self.common.spread_table(all_offer_mappings)))
        except Exception as e:
            message = f'Платформа: MRKT. Имя: {self.add_name}. Даты: {str(date)}. Функция: fetch_all_offer_mappings. Ошибка: {e}.'
            self.common.log_func(self.bot_token, self.chat_list, message, 3)
            return message


    def generate_price_report(self, year: str, month: str):
        try:
            url = "https://api.partner.market.yandex.ru/reports/united-marketplace-services/generate"
            headers = {"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"}
            params = {
                "format": "CSV",
                "language": "EN"
            }
            payload = {
            "businessId": self.clientid,
            "monthFrom": month,
            "monthTo": month,
            "yearFrom": year,
            "yearTo": year
        }
            response = requests.post(url, headers=headers, json=payload, params=params)
            code = response.status_code
            if code != 200:
                response.raise_for_status()
            result = response.json()
            report_id = result["result"].get("reportId")
            message = f'Платформа: MRKT. Имя: {self.add_name}. Дата: {str(year)}-{str(month)}. Функция: generate_price_report. Результат: ОК'
            self.common.log_func(self.bot_token, self.chat_list, message, 1)
            return report_id
        except Exception as e:
            message = f'Платформа: MRKT. Имя: {self.add_name}. Даты: {str(year)}-{str(month)}. Функция: generate_price_report. Ошибка: {e}.'
            self.common.log_func(self.bot_token, self.chat_list, message, 3)
            return message

    def generate_orders_report(self, date1: str, date2: str):
        try:
            url = "https://api.partner.market.yandex.ru/reports/united-orders/generate"
            headers = {"Authorization": f"Bearer {self.token}", "Content-Type": "application/json"}
            params = {
                "format": "CSV",
                "language": "EN"
            }
            payload = {
            "businessId": self.clientid,
            "dateFrom": date1,
            "dateTo": date2
        }
            response = requests.post(url, headers=headers, json=payload, params=params)
            code = response.status_code
            if code != 200:
                response.raise_for_status()
            result = response.json()
            report_id = result["result"].get("reportId")
            message = f'Платформа: MRKT. Имя: {self.add_name}. Дата: {str(date1)}-{str(date2)}. Функция: generate_orders_report. Результат: ОК'
            self.common.log_func(self.bot_token, self.chat_list, message, 1)
            return report_id
        except Exception as e:
            message = f'Платформа: MRKT. Имя: {self.add_name}. Даты: {str(date1)}-{str(date2)}. Функция: generate_orders_report. Ошибка: {e}.'
            self.common.log_func(self.bot_token, self.chat_list, message, 3)
            return message

    def check_report_status(self, report_id: str):
        try:
            url = f"https://api.partner.market.yandex.ru/reports/info/{report_id}"
            headers = {
                "Authorization": f"Bearer {self.token}",
                "Content-Type": "application/json"
            }
            response = requests.get(url, headers=headers)
            if response.status_code != 200:
                response.raise_for_status()
            result = response.json()
            file_url = result["result"].get("file")
            message = f'Платформа: MRKT. Имя: {self.add_name}. Отчёт: {str(report_id)}. Функция: check_report_status. Результат: ОК'
            self.common.log_func(self.bot_token, self.chat_list, message, 1)
            return file_url
        except Exception as e:
            message = f'Платформа: MRKT. Имя: {self.add_name}. Даты: {str(report_id)}. Функция: check_report_status. Ошибка: {e}.'
            self.common.log_func(self.bot_token, self.chat_list, message, 3)
            return message

    def process_report_files(self, file_url: str):
        try:
            headers = {
                "Authorization": f"Bearer {self.token}"
            }
            all_rows = []
            response = requests.get(file_url, headers=headers)
            if response.status_code != 200:
                response.raise_for_status()
            with zipfile.ZipFile(io.BytesIO(response.content)) as zip_file:
                for file_name in zip_file.namelist():
                    if file_name.endswith('.csv'):
                        with zip_file.open(file_name) as csv_file:
                            csv_content = csv_file.read().decode('utf-8')
                            csv_reader = csv.DictReader(io.StringIO(csv_content))
                            for row in csv_reader:
                                row['file_name'] = file_name.replace('.csv','')
                                row['first_date'] = self.common.get_month_start(self.yesterday_str)
                                all_rows.append(dict(row))
            message = f'Платформа: MRKT. Имя: {self.add_name}. Функция: process_report_files. Результат: ОК'
            self.common.log_func(self.bot_token, self.chat_list, message, 1)
            return self.common.transliterate_dict_keys_in_list(all_rows)
        except Exception as e:
            message = f'Платформа: MRKT. Имя: {self.add_name}. Функция: process_report_files. Ошибка: {e}.'
            self.common.log_func(self.bot_token, self.chat_list, message, 3)
            return message


    def get_price_report(self, date):
        try:
            first_date = self.common.get_month_start(self.yesterday_str)
            year = first_date.split('-')[0]
            month = first_date.split('-')[1]
            rep = self.generate_price_report(year, month)
            for att in range(50):
                time.sleep(10)
                rep_url = self.check_report_status(rep)
                if 'http' in rep_url and rep_url:
                    all_rows = self.process_report_files(rep_url)
                    break
            message = f'Платформа: MRKT. Имя: {self.add_name}. Дата: {str(date)}. Функция: get_price_report. Результат: ОК'
            self.common.log_func(self.bot_token, self.chat_list, message, 1)
            return all_rows
        except Exception as e:
            message = f'Платформа: MRKT. Имя: {self.add_name}. Дата: {str(date)}. Функция: get_price_report. Ошибка: {e}.'
            self.common.log_func(self.bot_token, self.chat_list, message, 3)
            return message

    def get_orders_report(self, date):
        try:
            first_date = self.common.get_month_start(self.yesterday_str)
            rep = self.generate_orders_report(first_date, self.yesterday_str)
            for att in range(50):
                time.sleep(10)
                rep_url = self.check_report_status(rep)
                if 'http' in rep_url and rep_url:
                    all_rows = self.process_report_files(rep_url)
                    break
            message = f'Платформа: MRKT. Имя: {self.add_name}. Дата: {str(date)}. Функция: get_orders_report. Результат: ОК'
            self.common.log_func(self.bot_token, self.chat_list, message, 1)
            return all_rows
        except Exception as e:
            message = f'Платформа: MRKT. Имя: {self.add_name}. Дата: {str(date)}. Функция: get_orders_report. Ошибка: {e}.'
            self.common.log_func(self.bot_token, self.chat_list, message, 3)
            return message

    # тип отчёта, дата -> данные в CH
    def collecting_manager(self):
        report_list = self.reports.replace(' ', '').lower().split(',')
        for report in report_list:
                self.clickhouse = Clickhouse(self.bot_token, self.chat_list, self.message_type, self.host, self.port, self.username, self.password,
                                             self.database, self.start, self.add_name, self.err429, self.backfill_days, self.platform)
                self.clickhouse.collecting_report(
                    self.source_dict[report]['platform'],
                    self.source_dict[report]['report_name'],
                    self.source_dict[report]['upload_table'],
                    self.source_dict[report]['func_name'],
                    self.source_dict[report]['uniq_columns'],
                    self.source_dict[report]['partitions'],
                    self.source_dict[report]['merge_type'],
                    self.source_dict[report]['refresh_type'],
                    self.source_dict[report]['history'],
                    self.source_dict[report]['frequency'],
                    self.source_dict[report]['delay']
                )
        self.common.send_logs_clear_anyway(self.bot_token, self.chat_list)









