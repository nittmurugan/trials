import requests

def send_simple_message():
    return requests.post(
        "https://api.mailgun.net/v3/sandbox91572a13092d49929842f0201c4663d5.mailgun.org/messages",
        auth=("api", "key-c9d6f9438f88a5af753ca7d935ab9ebe"),
        data={"from": "Mailgun Sandbox <postmaster@sandbox91572a13092d49929842f0201c4663d5.mailgun.org>",
              "to": "Murugan <nitt.murugan@gmail.com>",
              "subject": "Hello Murugan",
              "text": "Congratulations Murugan, you just sent an email with Mailgun!\
                You are truly awesome!  You can see a record of this email in your\
                 logs: https://mailgun.com/cp/log .  You can send up to 300 emails/day\
                  from this sandbox server.  Next, you should add your own domain\
                   so you can send 10,000 emails/month for free."})
