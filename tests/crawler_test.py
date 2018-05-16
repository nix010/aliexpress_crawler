from products_crawler.crawlers.category_crawler import CategoryCrawler
from products_crawler.crawlers.transaction_crawler import TransactionCrawler
from products_crawler.utils import parse_cookie_str

cookie = parse_cookie_str('ali_apache_id=11.227.118.141.1526012022212.196322.1; cna=BZhfEugJQwYCAbdQdies5exT; _ga=GA1.2.1603360291.1526012031; _uab_collina=152612787798485772062051; _gid=GA1.2.2062811205.1526236165; __utma=3375712.1603360291.1526012031.1526236353.1526236353.1; __utmz=3375712.1526236353.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ali_beacon_id=11.227.118.141.1526012022212.196322.1; aep_common_f=AfY8lja5UMZl9FDy5rbguF/P7gSeAjHK6IuJbnyD82uHegi5XOGYxA==; intl_locale=en_US; _mle_tmp_harden0=COMyBPKnGxIg1PC5i8KdrwWzAMSTYaiYp2YmDvfssKImdc%2FmV6BBObpDdQ8TF0sDjL9D0tmM9zYIHkOkTyoihqbp6A%2B0Rec7jINry5Xkea6je75hAxKruE9MKwz7HM9F; _umdata=428F97F4B1282F4E8AC86D579EEA80802B7EDD5DFFE13C1F58104AE993D12B4DB45E631225AEE061CD43AD3E795C914C6006F0B97FA9219221322A4410F44EE1; aep_history=keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%0932854134267%0932826062424%0932855909405%0932848645038; _hvn_login=13; aep_usuc_t=ber_l=A0; xman_f=OJsTTTSZnXcfe87aKOex+YZ/E0rwhJ+mMfaQBTFQLTLTRIEN0/7BiqwPrZcygTsPmdNRumcEuUOfyxy49cdKOY/wcetJFr5F5XhKtzaWPqwKuQNGEw/ZVhh0iE9vN0Jg8n8SA3Sq13qJ+JV5VK1zSscZzOmjfB2PCzZ/KY+c+RzhdAAcG11xAwU25tPBT3qoFMdrUJtSGbiQ+RSJ/PyzuVBvmbqIHopWjyg8LIQco1HTx/3+VJXkKlw/6Y9ANhdEiK9lbDSe8CkGi9aUcka+tk82YBzYNqEALHugg/PaWoVEmIS8FDbeniDMnnhgLj171xZVtweQYHcPF5LLhj8eCoheVolvOyvKlLJPkofKRYTyK961f0mCX77Kja9MAB2K3eu4Hhg4hKlIFk9ZqO15lZyrtR52qeJVMpMsrxw8ktc=; xman_t=G49n7tq5+UwM+5FZaP16E79ig0edGApaYgRGWfuMnCGyjyISXlxIFzPZ9fE6mNVX; acs_usuc_t=x_csrf=1n20z0qtfm35e&acs_rt=9e8229d34aba4a50b195e1db24452611; JSESSIONID=52A8A8CC7181A164F8B9CAF3049F7633; xman_us_f=x_l=1&x_locale=en_US&no_popup_today=n&x_user=VN|Nix|Grave|ifm|1766821924&zero_order=y&last_popup_time=1526236636895; _mle_tmp0=iiCGajxLJhPRfqiVFROq8nIkdZAZr3NpAV27Mg%2Bjb4iWLxb%2BM3c4hzLNLUuiZR%2BeF7uKbG9ne8FfVqmdvggfpaKbJ69V5wyaRFprbYs%2BXBEw7Oc1WwQYpLizd1LYZ7h2; aep_usuc_f=site=glo_v&region=US&b_locale=en_US&isb=y&c_tp=USD&x_alimid=1766821924; intl_common_forever=AcrTmUCalF4/PW1+BZ7wd5/emwh4c83wrF9Aa3sdTIhg6h938Yoprw==; ali_apache_track=mt=1|mid=vn164933924mouae; ali_apache_tracktmp=W_signed=Y; isg=BLW1YoX1A47NtWc9v_YeAFVyxDivmmhMx2a99zfaQyx1DtQA_4d5FexMXMo4ToH8')
res = CategoryCrawler('https://www.aliexpress.com/category/200000775/jackets-coats.html?site=glo&g=y&isrefine=y',cookies=cookie).crawl_now()
TransactionCrawler(trans_id='32848645038',page=1,cookies=cookie).crawl_now()

# print (res)

"""
ali_apache_id=11.227.118.141.1526012022212.196322.1
cna=BZhfEugJQwYCAbdQdies5exT
_ga=GA1.2.1603360291.1526012031
_uab_collina=152612787798485772062051
_gid=GA1.2.2062811205.1526236165
__utma=3375712.1603360291.1526012031.1526236353.1526236353.1
__utmz=3375712.1526236353.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)
ali_beacon_id=11.227.118.141.1526012022212.196322.1
aep_common_f=AfY8lja5UMZl9FDy5rbguF/P7gSeAjHK6IuJbnyD82uHegi5XOGYxA==
xman_f=OJsTTTSZnXcfe87aKOex+YZ/E0rwhJ+mMfaQBTFQLTLTRIEN0/7BiqwPrZcygTsPmdNRumcEuUOfyxy49cdKOY/wcetJFr5F5XhKtzaWPqwKuQNGEw/ZVhh0iE9vN0Jg8n8SA3Sq13qJ+JV5VK1zSscZzOmjfB2PCzZ/KY+c+RzhdAAcG11xAwU25tPBT3qoFMdrUJtSGbiQ+RSJ/PyzuVBvmbqIHopWjyg8LIQco1HTx/3+VJXkKlw/6Y9ANhdEiK9lbDSe8CkGi9aUcka+tk82YBzYNqEALHugg/PaWoVEmIS8FDbeniDMnnhgLj171xZVtweQYHcPF5LLhj8eCoheVolvOyvKlLJPkofKRYTyK961f0mCX77Kja9MAB2K3eu4Hhg4hKlIFk9ZqO15lZyrtR52qeJVMpMsrxw8ktc=
intl_locale=en_US
xman_t=KPg8TE+xUaCnoW2ERpk+UnD3zTOyxmpLf3tBYLc+oLx/gBgpww7SIQXai1yCkHC/
_umdata=428F97F4B1282F4E8AC86D579EEA80802B7EDD5DFFE13C1F58104AE993D12B4DB45E631225AEE061CD43AD3E795C914CCD84116AFEA4E62F9D3C93CA3E9D3411
acs_usuc_t=acs_rt=c47f53f2f8504eb8b7c82e39b406bb5b&x_csrf=mcgra6y7rmbs
_mle_tmp_harden0=COMyBPKnGxIg1PC5i8KdrzyjQ0%2BPP2dXv6w%2FEdP%2FWRTQ5r9zpbE7od%2BiH2ciPIUSmHvtPKz5cE0S8kdXxaWLbeMKakukiO0xeC4VGk06ioJBWMdlGc%2FtOw0Gqj72VXun
aep_history=keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%0932854134267%0932826062424%0932855909405%0932848645038%0932651825183%0932633561482
JSESSIONID=588B9B2E3E3978BCE66E72C392DC5458
xman_us_f=x_l=1&x_locale=en_US&no_popup_today=n&x_user=VN|Nix|Grave|ifm|1766821924&zero_order=y&last_popup_time=1526236636895
_mle_tmp0=iiCGajxLJhPRfqiVFROq8ndP19Thrc16Kmf8D25B30fnWeKq%2BvDPukp0GA1bXvixRW0l7RrUCrcV4zk6Y9hJB%2F%2BfVluv9E0jWK5BKu7lekd2B7lBPtdby7WliOLN9hJ%2F
aep_usuc_f=site=glo_v&region=US&b_locale=en_US&isb=y&c_tp=USD&x_alimid=1766821924
intl_common_forever=X8+McCbxiHEDM6iOZPhEH+g08ATovycidG4ac1Kbr9+yhCNMLkfecg==
ali_apache_track=mt=1|mid=vn164933924mouae
ali_apache_tracktmp=
_gat=1
isg=BBYWvJDkUB1YImSwqJPNtXp_Z8XYH1v5WHt-OoB_AvmUQ7bd6EeqAXw538eva1IJ

{'ali_apache_id': '11.227.118.141.1526012022212.196322.1', 'cna': 'BZhfEugJQwYCAbdQdies5exT', '_ga': 'GA1.2.1603360291.1526012031', '_uab_collina': '152612787798485772062051', '_gid': 'GA1.2.2062811205.1526236165', '__utma': '3375712.1603360291.1526012031.1526236353.1526236353.1', '__utmz': '3375712.1526236353.1.1.utmcsr', 'ali_beacon_id': '11.227.118.141.1526012022212.196322.1', 'aep_common_f': 'AfY8lja5UMZl9FDy5rbguF/P7gSeAjHK6IuJbnyD82uHegi5XOGYxA', 'xman_f': 'OJsTTTSZnXcfe87aKOex+YZ/E0rwhJ+mMfaQBTFQLTLTRIEN0/7BiqwPrZcygTsPmdNRumcEuUOfyxy49cdKOY/wcetJFr5F5XhKtzaWPqwKuQNGEw/ZVhh0iE9vN0Jg8n8SA3Sq13qJ+JV5VK1zSscZzOmjfB2PCzZ/KY+c+RzhdAAcG11xAwU25tPBT3qoFMdrUJtSGbiQ+RSJ/PyzuVBvmbqIHopWjyg8LIQco1HTx/3+VJXkKlw/6Y9ANhdEiK9lbDSe8CkGi9aUcka+tk82YBzYNqEALHugg/PaWoVEmIS8FDbeniDMnnhgLj171xZVtweQYHcPF5LLhj8eCoheVolvOyvKlLJPkofKRYTyK961f0mCX77Kja9MAB2K3eu4Hhg4hKlIFk9ZqO15lZyrtR52qeJVMpMsrxw8ktc', 'intl_locale': 'en_US', 'xman_t': 'KPg8TE+xUaCnoW2ERpk+UnD3zTOyxmpLf3tBYLc+oLx/gBgpww7SIQXai1yCkHC/', '_umdata': '428F97F4B1282F4E8AC86D579EEA80802B7EDD5DFFE13C1F58104AE993D12B4DB45E631225AEE061CD43AD3E795C914CCD84116AFEA4E62F9D3C93CA3E9D3411', 'acs_usuc_t': 'acs_rt', '_mle_tmp_harden0': 'COMyBPKnGxIg1PC5i8KdrzyjQ0%2BPP2dXv6w%2FEdP%2FWRTQ5r9zpbE7od%2BiH2ciPIUSmHvtPKz5cE0S8kdXxaWLbeMKakukiO0xeC4VGk06ioJBWMdlGc%2FtOw0Gqj72VXun', 'aep_history': 'keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%0932854134267%0932826062424%0932855909405%0932848645038%0932651825183%0932633561482', 'JSESSIONID': '588B9B2E3E3978BCE66E72C392DC5458', 'xman_us_f': 'x_l', '_mle_tmp0': 'iiCGajxLJhPRfqiVFROq8ndP19Thrc16Kmf8D25B30fnWeKq%2BvDPukp0GA1bXvixRW0l7RrUCrcV4zk6Y9hJB%2F%2BfVluv9E0jWK5BKu7lekd2B7lBPtdby7WliOLN9hJ%2F', 'aep_usuc_f': 'site', 'intl_common_forever': 'X8+McCbxiHEDM6iOZPhEH+g08ATovycidG4ac1Kbr9+yhCNMLkfecg', 'ali_apache_track': 'mt', 'ali_apache_tracktmp': '', '_gat': '1', 'isg': 'BBYWvJDkUB1YImSwqJPNtXp_Z8XYH1v5WHt-OoB_AvmUQ7bd6EeqAXw538eva1IJ'}


"""
