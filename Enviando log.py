from zeus import client

z = client.ZeusClient('7caecc05', 'api.ciscozeus.io')

logs = [
    {"message": "My Test Log"},
    {"message": "My Second Test Log"}
]
z.sendLog("Sensor1",logs)

'''
z.getLog('<LOG_NAME>',
          pattern='*',
          from_date=123456789,
          to_date=126235344235,
          offset=23,
          limit=10)
          '''