import re
import boto3
import xlsxwriter
from test_decorator import timed_func

@timed_func
def test():
    command_id = 'cadf87b7-8369-4521-8d01-956cb2d466e2'

    patterns = ['Important','Important Updates', 'Critical','Moderate','Low', 'Unspecified', 'Optional Updates', 'Total Updates'] 

    client = boto3.client('ssm')

    workbook = xlsxwriter.Workbook('commandDetails.xlsx')
    worksheet = workbook.add_worksheet()
    bold = workbook.add_format({'bold': 1})

    worksheet.write('A1', 'CommandId', bold)
    worksheet.write('B1', 'InstanceId', bold)
    worksheet.write('C1', 'Status', bold)
    worksheet.write('D1', 'DocumentName', bold)
    worksheet.write('E1', 'Important', bold)
    worksheet.write('F1', 'ImportantUpdates', bold)
    worksheet.write('G1', 'Critical', bold)
    worksheet.write('H1', 'Moderate', bold)
    worksheet.write('I1', 'Low', bold)
    worksheet.write('J1', 'Unspecified', bold)
    worksheet.write('K1', 'OptionalUpdates', bold)
    worksheet.write('L1', 'TotalUpdates', bold)

    row = 1
    col = 0


    response = client.list_command_invocations(CommandId=command_id, Details=True)
    for item in response['CommandInvocations']:
        worksheet.write_string(row, col, item['CommandId'])
        worksheet.write_string(row, col + 1, item['InstanceId'])
        worksheet.write_string(row, col + 2, item['Status'])
        worksheet.write_string(row, col + 3, item['DocumentName'])
        for data in item['CommandPlugins']:
            output = data['Output']
            if item['DocumentName'] == 'AWS-FindWindowsUpdates':
                col = 4
                for pattern in patterns:
                    key = pattern.replace(" ", "")
                    data_dict = re.search(r""+pattern+":    (?P<"+key+">\d+)", output).groupdict()
                    worksheet.write_string(row, col, data_dict[key])
                    col += 1
        row += 1
        col = 0
    workbook.close()

test()
