Generate and sign the certificate:
```shell 
openssl req -newkey rsa:2048 -x509 -keyout key.pem -out cert.pem -days 365
openssl pkcs12 -export -in cert.pem -inkey key.pem -out certificate.p12 -name "certificate"
```
Add it to the `resources` folder. Configure application properties:
```
server.ssl.key-store-type=PKCS12
server.ssl.key-store=classpath:certificate.p12
server.ssl.key-store-password=12345
```