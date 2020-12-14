import ssl
import OpenSSL
from datetime import datetime
from seatable_api import Base, context

SERVER_URL = context.server_url or "https://cloud.seatable.cn"
API_TOKEN = context.api_token or "32225b0988e0fe8e87bfa99be3d2879ba9a84925"


# Table config
TABLE_NAME = "云端服务"
IGNORED_DOMAINS = ["archive.seafile.com","Windows-OfficeOnline"]
CERTIFICATION_EXPIRED_COLUMN = "证书过期时间"
DOMAIN_COLUMN = "Name"

def _get_cert_expiration(domain):
    cert = ssl.get_server_certificate((domain, 443))
    x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, cert)
    expiration = datetime.strptime(x509.get_notAfter().decode("utf-8"), "%Y%m%d%H%M%SZ")
    return expiration

def update_certification_expiration():
    base = Base(API_TOKEN, SERVER_URL)
    base.auth()

    rows = base.list_rows(TABLE_NAME)
    for row in rows:
        domain = row.get(DOMAIN_COLUMN, '')
        current_expiration_str = row.get(CERTIFICATION_EXPIRED_COLUMN, '')
        if not domain:
            continue
        if not current_expiration_str:
            continue
        if domain in IGNORED_DOMAINS:
            continue
        try:
            expiration = _get_cert_expiration(domain)
            current_expiration = datetime.strptime(current_expiration_str, "%Y-%m-%d %H:%M")
            if current_expiration.date() != expiration.date():
                base.update_row(TABLE_NAME, row['_id'], {CERTIFICATION_EXPIRED_COLUMN: str(expiration)})
                print("%s's(%s) new expiration is %s" % (domain, str(current_expiration), str(expiration)))
            else:
                print("%s(current expiration: %s) no need to update" % (domain, str(current_expiration)))
        except Exception as e:
            print("%s error: %s" % (domain, e))

if __name__ == '__main__':
    update_certification_expiration()

