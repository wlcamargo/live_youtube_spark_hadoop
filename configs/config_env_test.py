credential_postgres_adventureworks = {
    'host': '172.31.156.222',
    'dbname': 'Adventureworks',
    'user': 'postgres',
    'password': 'postgres',
    'port': 5433
}

hdfs_path = {
    'landing_zone': 'hdfs://namenode:9000/landing_zone/',
    'bronze' : 'hdfs://namenode:9000/bronze/',
    'silver' : 'hdfs://namenode:9000/silver/',
    'gold' : 'hdfs://namenode:9000/gold/'
}

tables_postgres_adventureworks = {
    '1': 'sales.countryregioncurrency',
    '2': 'sales.creditcard',
    '3': 'sales.currency',
    '4': 'sales.currencyrate',
    '5': 'sales.customer',
    '6': 'sales.personcreditcard',
    '7': 'sales.salesorderdetail',
    '8': 'sales.salestaxrate',  
    '9': 'sales.salesorderheadersalesreason',
    '10': 'sales.salesperson',
    '11': 'sales.salespersonquotahistory',
    '12': 'sales.salesreason',
    '13': 'sales.salestaxrate',
    '14': 'sales.salesterritory',
    '15': 'sales.salesterritoryhistory',
    '16': 'sales.shoppingcartitem',
    '17' : 'sales.specialoffer',
    '18': 'sales.specialofferproduct',
    '19': 'sales.store'
}

prefix_layer_name = {
    '1': 'bronze_',
    '2': 'silver_',
    '3': 'gold_'
}





