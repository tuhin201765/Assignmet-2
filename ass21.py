import searchconsole

account = searchconsole.authenticate(client_config='client_secret.json')
webproperty = account['https://localhost:8080/']
report = webproperty.query.range('today', days=7).dimension('query').get()
print(report.rows)
