import requests

from products_crawler.crawlers.category_crawler import CategoryCrawler
from products_crawler.crawlers.transaction_crawler import TransactionCrawler
from products_crawler.utils import parse_cookie_str

import requests
s = requests.Session()
# cookie = parse_cookie_str('ali_apache_id=11.227.118.141.1526012022212.196322.1; cna=BZhfEugJQwYCAbdQdies5exT; _ga=GA1.2.1603360291.1526012031; _uab_collina=152612787798485772062051; _gid=GA1.2.2062811205.1526236165; __utma=3375712.1603360291.1526012031.1526236353.1526236353.1; __utmz=3375712.1526236353.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ali_beacon_id=11.227.118.141.1526012022212.196322.1; aep_common_f=AfY8lja5UMZl9FDy5rbguF/P7gSeAjHK6IuJbnyD82uHegi5XOGYxA==; intl_locale=en_US; _mle_tmp_harden0=COMyBPKnGxIg1PC5i8KdrwWzAMSTYaiYp2YmDvfssKImdc%2FmV6BBObpDdQ8TF0sDjL9D0tmM9zYIHkOkTyoihqbp6A%2B0Rec7jINry5Xkea6je75hAxKruE9MKwz7HM9F; _umdata=428F97F4B1282F4E8AC86D579EEA80802B7EDD5DFFE13C1F58104AE993D12B4DB45E631225AEE061CD43AD3E795C914C6006F0B97FA9219221322A4410F44EE1; aep_history=keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%0932854134267%0932826062424%0932855909405%0932848645038; _hvn_login=13; aep_usuc_t=ber_l=A0; xman_f=OJsTTTSZnXcfe87aKOex+YZ/E0rwhJ+mMfaQBTFQLTLTRIEN0/7BiqwPrZcygTsPmdNRumcEuUOfyxy49cdKOY/wcetJFr5F5XhKtzaWPqwKuQNGEw/ZVhh0iE9vN0Jg8n8SA3Sq13qJ+JV5VK1zSscZzOmjfB2PCzZ/KY+c+RzhdAAcG11xAwU25tPBT3qoFMdrUJtSGbiQ+RSJ/PyzuVBvmbqIHopWjyg8LIQco1HTx/3+VJXkKlw/6Y9ANhdEiK9lbDSe8CkGi9aUcka+tk82YBzYNqEALHugg/PaWoVEmIS8FDbeniDMnnhgLj171xZVtweQYHcPF5LLhj8eCoheVolvOyvKlLJPkofKRYTyK961f0mCX77Kja9MAB2K3eu4Hhg4hKlIFk9ZqO15lZyrtR52qeJVMpMsrxw8ktc=; xman_t=G49n7tq5+UwM+5FZaP16E79ig0edGApaYgRGWfuMnCGyjyISXlxIFzPZ9fE6mNVX; acs_usuc_t=x_csrf=1n20z0qtfm35e&acs_rt=9e8229d34aba4a50b195e1db24452611; JSESSIONID=52A8A8CC7181A164F8B9CAF3049F7633; xman_us_f=x_l=1&x_locale=en_US&no_popup_today=n&x_user=VN|Nix|Grave|ifm|1766821924&zero_order=y&last_popup_time=1526236636895; _mle_tmp0=iiCGajxLJhPRfqiVFROq8nIkdZAZr3NpAV27Mg%2Bjb4iWLxb%2BM3c4hzLNLUuiZR%2BeF7uKbG9ne8FfVqmdvggfpaKbJ69V5wyaRFprbYs%2BXBEw7Oc1WwQYpLizd1LYZ7h2; aep_usuc_f=site=glo_v&region=US&b_locale=en_US&isb=y&c_tp=USD&x_alimid=1766821924; intl_common_forever=AcrTmUCalF4/PW1+BZ7wd5/emwh4c83wrF9Aa3sdTIhg6h938Yoprw==; ali_apache_track=mt=1|mid=vn164933924mouae; ali_apache_tracktmp=W_signed=Y; isg=BLW1YoX1A47NtWc9v_YeAFVyxDivmmhMx2a99zfaQyx1DtQA_4d5FexMXMo4ToH8')
# res = s.post('https://passport.aliexpress.com/newlogin/login.do',
#             headers={
#                 'Accept'                    : '*/*',
#                 'Cache-Control'             : 'no-cache',
#                 'Pragma'                    : 'no-cache',
#                 'upgrade-insecure-requests' : '1',
#                 'Content-Type'              : 'application/x-www-form-urlencoded; charset=UTF-8',
#                 'User-Agent'                : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/62.0.3202.94 Chrome/62.0.3202.94 Safari/537.36'
#             },data='loginId=stricker.reno%40gmail.com&password2=320f2b99e8af00643e72116889613109055e4292cf4eb6f6c62ab659050ad6b7d53e04977b4da228b8692966bc7e8bae070d8e9cf8c9a1fa2d0954240614b261a99aa090cc1a892d49d4568ecf9dde0284d0c07027fe44a3d36835bc968e0dbab0d13b190e8b856a11ef4b38e43c0abb3900fdadfbb6f1cf424e8337464fa431&checkCode=&appName=aebuyer&appEntrance=default&bizParams=&ua=108%23fqb%2F1%2FR2%2FYpfq3GtcpuwDWExxUlncLd8nA3JIfl%2F6BM5%2FcdAPWr12ZkYFBRH0fraPi9Gmif101cUCl9p905rcSy7HPa%2FZ%2FWs4%2FKUSE81eY9TUZPEIKknxLUBIBERtTxfkyHrkDDLX%2FLTeIzDuI3XBSnyyof35w48JE8H15bUbLiBErKYojDWOdisvT%2Bt7NTezOw2mJDp1HF724YqcWmDS0pFgSTJRuchjnU9gkjoTVEeIt3xA4yDFNRcAZWtNnNOu9WMNJvZfaECUWos5K8qThE%2B0nALhEDu6PoIp3UEM6SUygRz8iVEhFfU4vy2WPr8G76WVasipr9aymENKL5AkemQcAasAKGctp4zviw9NGGMlyhgvm2cHFB4FMewwjc9o6KCQUn7idmKLfvDvXj6BALqipFJl1%2BwnWvgbkHwEjW9SmOCxDq88E%2Fiuzbv%2F7ls0hwKYmySc6MCv4gkeiNLDkdbneXEIGUK3YOpDdQfJiuQKRF4hu%2FS5jwF9jVDIdlGJSLVQoRhs3XWgPvT9YpuckZBX7DIM9wSZFeZpZbvqo8o2wOEwBXcDSQG9WfJn4lxm1MBxo1ZF%2FMzPELEznhRs1KieeBaDvDbbkjdFt7SeEVfg1CgRLXWLCO0dud0TAlwAENmw%2FVJ57FLCUoTGlbK%2BVb177ukOD%2B0H81M5y8yuXnvRGKxCxCPbtz%2B9WuFMab5fS8hgClb4f40EBHcZ1pfWvNuqxgt%2FYceH7ueSt3qT3WZQoJiw90BkE77G1Cr5IIuzT89P9zvI0ui%2FP%2BtUsyuIU1LiErexrsJXaYK2ci7ErIDAwq9ZlQxqEhBMJMIGdXf1rdwfVaBawho3wSB1zTdIDpwrq9zrmYgmsK%2BLGcZElzEQc6ppFgg6wCV2ClGgXCq2s5RnbR3QMXRrqkojotuXwHjeSH4Xo6XBceM1GspxSD69yj8TE4ZyQ71vA%2FmUs5Kn8RPVt2Emp3zAEg3wThZ%2ByqqY0iARGcDqGbGTMLOfiDbfIiqt%2Bqm&hsid=bS6LFQEdyxC6V3F4erLXIw&rdsToken=&umidToken=c1c76c807224aee6da11c686c2feb4fe5bb4fce7&isRequiresHasTimeout=false&isRDSReady=true&isUMIDReady=true&umidGetStatusVal=255&lrfcf=&lang=en_US&scene=&isMobile=false&screenPixel=1920x1080&navlanguage=en-US&navUserAgent=Mozilla%2F5.0+(X11%3B+Linux+x86_64)+AppleWebKit%2F537.36+(KHTML%2C+like+Gecko)+Ubuntu+Chromium%2F63.0.3239.84+Chrome%2F63.0.3239.84+Safari%2F537.36&navAppVersion=&navPlatform=Linux+x86_64&token=&nocAppKey=&csessionid=&sig=&captchaToken=&_csrf_token=VncluqFNpRT9YVRSJ0LRE')
#
# print(res.json())

res = s.get('https://www.aliexpress.com/category/100003070/men-clothing-accessories.html',headers={
    'Accept'                    : '*/*',
    'Cache-Control'             : 'no-cache',
    'Pragma'                    : 'no-cache',
    'upgrade-insecure-requests' : '1',
    'User-Agent'                : 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/62.0.3202.94 Chrome/62.0.3202.94 Safari/537.36'
},proxies={
    'http':'socks5://x4126276:N3qv87Ven8@proxy-nl.privateinternetaccess.com:1080',
    'https':'socks5://x4126276:N3qv87Ven8@proxy-nl.privateinternetaccess.com:1080'
}
            )


print(res.request.headers)
print(res.text[:550])

