Generate a self-signed certificate and package it as PKCS#12:
```shell
openssl req -newkey rsa:2048 -x509 -keyout key.pem -out cert.pem -days 365
openssl pkcs12 -export -in cert.pem -inkey key.pem -out dragonbank.p12 -name "dragonbank"
```
Put it in `src/main/resources` and configure:
```properties
server.ssl.key-store-type=PKCS12
server.ssl.key-store=classpath:dragonbank.p12
server.ssl.key-store-password=12345
```
> **Compare:** in Quarkus the same keystore works with `quarkus.http.ssl.certificate.key-store-file=dragonbank.p12` and `quarkus.http.ssl.certificate.key-store-password=12345`. You can also use the PEM files directly with `quarkus.http.ssl.certificate.files=cert.pem` and `quarkus.http.ssl.certificate.key-files=key.pem`. HTTPS listens on 8443.
