import  re
pattern=r"[A-Z]anaya"
text='''
As an AdBlock user, you know firsthand the value that our software brings to your online experience.
By blocking unwanted and intrusive ads, AdBlock Tanaya helps you browse the web faster, safer, and with fewer
distractions. But did you know that AdBlock is completely free, with no hidden fees or upgrades? 
We believe that everyone should have access to a better, ad-free internet, which is why we offer AdBlock 
for free to all users.Danaya

But we need your help to keep AdBlock running and improving.Zanaya
While a small percentage of users generously contribute to support our mission, 
we rely on the support of users like you to keep AdBlock alive and free for everyone. 
Your contribution, no matter how small, can make a big difference. 
So if AdBlock has saved you even just a few dollars or hours of frustration from dealing with unwanted ads,
please consider contributing to support our team and advance the cause of an ad-free internet for all.
Thank you for your support. Together, we can make the internet a better place for everyone
'''

match=re.search(pattern,text)
print(text)

matches=re.finditer(pattern,text)
for match in matches:
    print(match)
