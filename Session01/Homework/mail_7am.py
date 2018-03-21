from gmail import GMail, Message #viet hoa Message va GMail
from random import choice
import datetime

gmail = GMail('chi.c4e16@gmail.com','phamthucchi')
# msg = Message('Mail to you',to='techkidsc4e16@gmail.com',text='Hello')
html_template = """
<p style="text-align: center;"><span style="font-size: 14pt;">Đơn xin nghỉ học</span></p>
<p>Th&acirc;n gửi thầy c&ocirc; bộ m&ocirc;n,</p>
<p>V&igrave; l&yacute; do {{ly do}}, em kh&ocirc;ng thể tham gia lớp học v&agrave;o h&ocirc;m nay. Do vậy, em viết thư n&agrave;y để xin ph&eacute;p thầy/ c&ocirc; cho em nghỉ buổi học n&agrave;y.</p>
<p>Em xin cảm ơn.</p>
<p>Th&acirc;n,</p>
<p>Chi</p>
<p>&nbsp;</p>
"""

# placeholder:
reasons = ["dau dau", "hong xe", "lol", "ban"]
reason = choice(reasons)

html_content = html_template.replace("{{ly do}}", reason)
msg = Message('Don xin nghi hoc',to='chi.c4e16@gmail.com',text="",html= html_content)

now = datetime.datetime.now()
time_not_7am = True
while True:
    if now.hour == 7:
        gmail.send(msg)
        break
