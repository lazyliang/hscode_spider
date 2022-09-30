# -*- coding: utf-8 -*-
"""
    __init__
"""
import hscode_spider.row as row
import hscode_spider.spider as spider

# Search all codes by chapter
search_chapter = spider.search_chapter
# Get the details of hscode
get_code_info = spider.parse_details

Hscode = row.Hscode
TaxInfo = row.TaxInfo
BaseInfo = row.BaseInfo
