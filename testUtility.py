import logging
import os
import subprocess
import yaml
import pandas as pd
import datetime
import gc
import re

#To read file:

def readFile(filepath):
  with open(filepath, 'r' as stream:
            try:
              return yaml.safe_load(stream)
            except yaml.YAMLError as exc:
              logging.error(exc)
             
def replacer(string, char):
  pattern = char + '{2,}'
  string = re.sub(pattern, char, string)
  return string
            
def headerValidation(df, table_confic):
  df.columns = df.columns.str.lower()
  df.columns = df.columns.str.replace('[^\w]','_',regex=TRUE)
  df.columns = list(map(lambda x: x.strip('_'), list(df.columns)))
  df.columns = list(map(lambda x: replacer(x,'_'), list(df.columns)))
  expected_col = list(map(lambda x: x.lower(), table_config['columns']))
  expected_col.sort()
  df.columns = list(map(lambda x: x.lower(), list(df.columns)))
  df = df.reindex(sorted(df.columns), axis = 1)
  if len(df.columns) == len(expected_col) and list(expected_col) == list(df.columns)
            print("coloumn name & length validation passed")
            return 1
  else:
            print("column name & length validation failed")
            mismatchedColumnsFile = list(set(df.columns).difference(expected_col))
            print("The following columns are not in the YAML file", mismatchedColumnsFile)
            missingYAMLFile = list(set(expected_col).difference(df.columns))
            print("The following YAML columns are not in the file", missingYAMLFile)
            logging.info(f'df columns: {df.columns}')
            logging.info(f'expected columns: {expected_col}'}
            return 0
