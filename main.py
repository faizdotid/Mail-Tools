import re
import os

class SplitMail:
    
    def __init__(self, *mail_list):
        self.mail_list = mail_list
        self.domain_conf = {}

    def save_to_file(self, filename, text, dirname="Result"):
        if not os.path.isdir(dirname):
            os.mkdir(dirname)
        else:
            pass
        with open(dirname + "/" + filename, "a") as f:
            f.write(text + '\n')
            f.close()

    def split_mail_pass(self):
        for mails in self.mail_list:
            splitter = re.search(r'[\|\:]', mails)
            try:
                mail, pwd = mails.split(splitter.group())
                self.save_to_file("mail_list.txt", mail)
            except (IndexError, AttributeError):
                pass
        print('Done splitting and check your result folder :) ')

    def add(self, domain):
        if domain in self.domain_conf:
            self.domain_conf[domain] += 1
        else:
            self.domain_conf[domain] = 1

    def filter_domain(self):
        for mail in self.mail_list:
            try:
                usr, domain = mail.split('@')
                domainsave = domain.split('.')[0]
                self.add(domain)
                self.save_to_file(domainsave+".txt", mail)
            except (IndexError, ValueError):
                pass
        if len(self.domain_conf) > 0:
            for k,v in self.domain_conf.items():
                print("{:<30} => {}".format(k.capitalize(), str(v)))
            print('Done filterring and check your result folder :) ')

def main():
    print("""

█▀▄▀█ ▄▀█ █ █░░ ▄▄ █▀ █▀█ █░░ █ ▀█▀ █▀▀ █▀█
█░▀░█ █▀█ █ █▄▄ ░░ ▄█ █▀▀ █▄▄ █ ░█░ ██▄ █▀▄
\tTelegram: https://t.me/istmepaiz

1. Split email & password
2. Filter email by domain

""")
    try:
        choose = input("Choose ? ")
        if re.search(r'[1,2]', choose):
            list_ = open(input("List ? "), "r").read().splitlines()
            chosedixct = {
                "1": SplitMail(*list_).split_mail_pass,
                "2": SplitMail(*list_).filter_domain
            }
            chosedixct[choose]()
        else:
            print("Wrong choose")
    except FileNotFoundError:
        print("File not found")

if __name__ == "__main__":
    main()
