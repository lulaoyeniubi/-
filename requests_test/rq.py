import requests
import re
from lxml import etree


def reptile():
    url = 'https://movie.douban.com/chart'
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
    # ck = {
    #     'Cookie': 'bid=qu8_up_lFzY; douban-fav-remind=1; ll="108090"; __yadk_uid=r3wDBmHg4GRZw0BJxIxDcqLVm2ccRr3d; __gads=ID=8a698112d2ef7778-22d948d311c900b1:T=1622441606:RT=1622441606:S=ALNI_MbNBrTg9_xc0qOuajWnh_u4Xs23Zg; _vwo_uuid_v2=D63FA01AB3367210D085D77D3CFDED491|26d96d3b010cecaa91122726395fc80f; __utmz=30149280.1628063956.8.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=223695111.123554772.1622441604.1624030729.1628063956.3; __utmz=223695111.1628063956.3.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utma=30149280.748937160.1620493156.1628063956.1628267078.9; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1634805743%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DW07PKcAi-hmIbMtNGevtCYwCdFQe1pptlG_QEaxOSGml9YnYUEcwn3v4FAM71PZB-7C-Z1eqdn53ZkqYd1OhP_%26wd%3D%26eqid%3D94bab45c0006735e00000006610a48ca%22%5D; _pk_id.100001.4cf6=acbfa4ea8e9e2628.1622441604.4.1634805743.1628064121.; _pk_ses.100001.4cf6=*; ap_v=0,6.0; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1634805749; Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c=1634805749'}
    rq = requests.get(url=url, headers=header)
    page = rq.text
    # print(page)

    # <a class="nbg" href="https://movie.douban.com/subject/35208823/"  title="灵媒">
    # <span class="rating_nums">6.4</span>
    movies = re.findall(r'subject/\d+/"  title="(.*?)">.*?<span class="rating_nums">(.*?)</span>', page, re.S)
    print(movies)
    movies.sort(key=lambda x: x[1], reverse=False)
    print(movies)


def reptile_test():
    url = 'https://www.minhngoc.net.vn/ket-qua-xo-so/mien-bac/ha-noi.html'
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
    rq = requests.get(url=url, headers=header)
    page = rq.text

    # print(page)
    # Award_announcement = re.findall(r'<div>(.*?)</div></td>',page)
    # Award_announcement = Award_announcement[0]
    # print(Award_announcement)


def download():
    url = 'https://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CD%BC%C6%AC&fr=ala&ala=1&alatpl=normal&pos=0&dyTabStr=MCwzLDYsMSw0LDIsNSw3LDgsOQ%3D%3D'
    header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36'}
    cookie = {'Cookie': 'BDqhfp=%E5%B0%BC%E5%85%8B%E6%9D%A8%26%26NaN-1undefined%26%260%26%261; BIDUPSID=E86EEEAAAF6E5AA478780D70EB446945; PSTM=1617371882; BAIDUID=E86EEEAAAF6E5AA478780D70EB446945:SL=0:NR=10:FG=1; __yjs_duid=1_b6d857b8422f486a8533987f3e9ade801619971630704; indexPageSugList=%5B%22%E5%AE%89%E5%85%B9%20%E5%9B%BE%E7%89%87%22%2C%22%E9%98%BF%E6%8B%89%E6%96%AF%E5%8A%A0%E4%B8%BA%E4%BB%80%E4%B9%88%E6%98%AF%E7%BE%8E%E5%9B%BD%E7%9A%84%22%2C%22%E5%9B%BE%E7%89%87%22%5D; delPer=0; ZD_ENTRY=baidu; BDRCVFR[rBwlvnElmLY]=aUGzC--3FZsmh-MULIdQhPEUf; H_PS_PSSID=; PSINO=7; BDORZ=FFFB88E999055A3F8A630C64834BD6D0; BAIDUID_BFESS=CCE2B985D540B4274B34C5C47F177DA9:FG=1; BA_HECTOR=058l0h0580aha02lrl1gn2qpe0r; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=ala; ab_sr=1.0.1_NzI2Njg0NTcxZDY3NWY4NGVkNGVkOTZkOTI1ODI4Mzc1ODc2MWI2MGE1ZTEzMDZhYWNkY2ZjYWMzMTQ0NmQ2MmY4NTFhM2RmNzBkMzc3MmMyYTVhNTg4N2I5YzA5MTA2MmYxMmFhNDkzNjNmYmUwMTFjMGY4MDI3Yzk4ZmQ4OGM5MTYwOTBlNzU0MmIyZTE1NTY1NWFjZDc5M2UwMWU2OA==; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1634576155,1634822968; Hm_lpvt_eaa57ca47dacb4ad4f5a257001a3457c=1634822968'}
    rq = requests.get(url=url, headers=header,cookies=cookie)
    page = rq.text
    # print(page)

    # html = etree.HTML(rq.text)
    # for quota in html.xpath("//img"):
    #     print(quota.get('src'))

    image = re.findall(r'"thumbURL":"(.*?)"', page)
    # print(image)

    # for i in image:
    #     print(i)
    print(f'开始下载，总共{len(image)}张')
    for i,j in enumerate(image):
        print(f'正在下载第{i+1}张图片')
        with open(f'./imgs{i+1}.jpeg','wb') as f:
            r = requests.get(url=j,headers=header,cookies=cookie)
            f.write(r.content)
    else:
        print("下载完成")


if __name__ == '__main__':
    download()
