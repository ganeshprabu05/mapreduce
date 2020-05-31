import sys
import argparse
import logging
import os
import requests
import json

def parse_args():
    print('Inside Parser')
    parser = argparse.ArgumentParser(
        description="This process to check the process type"
    )

    parser.add_argument("--from-instance", help = "from jenkins instance.", required = True)

    parser.add_argument("--to-instance", help = "to jenkins instance.", required = True)

    parser.add_argument("--process-type", help = "clone view or job", required = True)

    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = parse_args()
    
   
    if args.process_type == 'view':
        print('Process type is view')
    elif args.process_type == 'job':
        print('Process type is job')
    elif args.process_type == 'mutli_job':
        print('Process type is multi_job')
    
