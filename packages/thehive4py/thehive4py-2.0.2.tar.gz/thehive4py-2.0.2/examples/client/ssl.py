from thehive4py import TheHiveApi

hive = TheHiveApi(
    url="http://localhost:9000",
    apikey="h1v3b33",
    verify="/etc/ssl/certs/ca-certificates.crt",
)
