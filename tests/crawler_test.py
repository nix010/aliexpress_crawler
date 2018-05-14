from products_crawler.crawlers.category_crawler import CategoryCrawler
from products_crawler.crawlers.transaction_crawler import TransactionCrawler
from products_crawler.utils import parse_cookie_str

cookie = parse_cookie_str('ali_apache_id=11.227.118.141.1526012022212.196322.1; cna=BZhfEugJQwYCAbdQdies5exT; _ga=GA1.2.1603360291.1526012031; _uab_collina=152612787798485772062051; _gid=GA1.2.2062811205.1526236165; __utma=3375712.1603360291.1526012031.1526236353.1526236353.1; __utmz=3375712.1526236353.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); ali_beacon_id=11.227.118.141.1526012022212.196322.1; aep_common_f=AfY8lja5UMZl9FDy5rbguF/P7gSeAjHK6IuJbnyD82uHegi5XOGYxA==; intl_locale=en_US; JSESSIONID=BADA3BBB763B3CA4B631277D630CF516; _mle_tmp_harden0=COMyBPKnGxIg1PC5i8KdrwWzAMSTYaiYp2YmDvfssKImdc%2FmV6BBObpDdQ8TF0sDjL9D0tmM9zYIHkOkTyoihqbp6A%2B0Rec7jINry5Xkea6je75hAxKruE9MKwz7HM9F; acs_usuc_t=acs_rt=9e8229d34aba4a50b195e1db24452611&x_csrf=qrip09ybretc; _umdata=428F97F4B1282F4E8AC86D579EEA80802B7EDD5DFFE13C1F58104AE993D12B4DB45E631225AEE061CD43AD3E795C914C6006F0B97FA9219221322A4410F44EE1; _mle_tmp0=iiCGajxLJhPRfqiVFROq8mXB6lly3WVr5dNzhw6%2BSYF7JubHl6gjIkhUJZVNiaRvtlqFSLnhCRaFy3E6Ef96GTL3nOhj0mGkpelhAff6tUbNHz28YLG3rTmQW0yoU56x; aep_history=keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%0932854134267%0932826062424%0932855909405%0932848645038; xman_us_f=x_l=1&x_locale=en_US&no_popup_today=n&x_user=VN|Nix|Grave|ifm|1766821924&zero_order=y&last_popup_time=1526236636895; _hvn_login=13; xman_us_t=x_lid=vn164933924mouae&sign=y&x_user=36ugFompsk1vaWxW0uY3hh7bfdd6HJNsmX8Hcoaje7I=&ctoken=u0zvewfzgi4x&need_popup=y&l_source=aliexpress; aep_usuc_t=ber_l=A0; xman_f=OJsTTTSZnXcfe87aKOex+YZ/E0rwhJ+mMfaQBTFQLTLTRIEN0/7BiqwPrZcygTsPmdNRumcEuUOfyxy49cdKOY/wcetJFr5F5XhKtzaWPqwKuQNGEw/ZVhh0iE9vN0Jg8n8SA3Sq13qJ+JV5VK1zSscZzOmjfB2PCzZ/KY+c+RzhdAAcG11xAwU25tPBT3qoFMdrUJtSGbiQ+RSJ/PyzuVBvmbqIHopWjyg8LIQco1HTx/3+VJXkKlw/6Y9ANhdEiK9lbDSe8CkGi9aUcka+tk82YBzYNqEALHugg/PaWoVEmIS8FDbeniDMnnhgLj171xZVtweQYHcPF5LLhj8eCoheVolvOyvKlLJPkofKRYTyK961f0mCX77Kja9MAB2K3eu4Hhg4hKlIFk9ZqO15lZyrtR52qeJVMpMsrxw8ktc=; aep_usuc_f=site=glo_v&region=US&b_locale=en_US&isb=y&c_tp=USD&x_alimid=1766821924; intl_common_forever=H5p9sdojOG9I+bYU1b+D3btFQsonY5ICNWrFrWN/YPSsn/OmuOoVlw==; ali_apache_track=mt=1|ms=|mid=vn164933924mouae; ali_apache_tracktmp=W_signed=Y; isg=BCgohe4-5jLKsMq6ijXbT_jh-R_6-Y1TmjWQsOJZdKOWPcinimFc675_Mc3NDUQz; xman_t=oA0Kg+6mnx2VK7oDyaJK+3N9whIrehV4bBHJXJItPt03Xl9FBDro9654kIVHLcfpDooVIpWt076a+GbUWwhbaX+uyOtEkX7ELLw3aWMUKBIwmNL/RPybCdd56yLIzIqFat9N7nSBIMh9aaNSNzc9dNwz5vmgU8XpCuKjwScp6lTj/0MnfEB0+KrZFhvLRsgMlEdRBvsFlNhYN4QHiuRU+9aVJXfcTckinUxE7k397+uEEYowNwevFiNu7S0H0UtiPVDxRPVorFXnZpMLXBL8RwIuVB0iI4Db54j1iUhECN/+1J9LE+iuPyRdjliRMd86W3gP9eV9SXlaJd8YNgZMTxb3P88ytTrdXonOmAkCHJOlxLpLeVv1ptr0/nBqeBoZi5zFv2FglfjigbXKJdPOvInS1RBK72Xbxu+5/NFpJusNd79r+85c5P2/CJhL9QOjTRB5ldWsabwOOvw3ph9okL/1MVjTSklCzKopHIv3/qhs9d/zV4+o0IyC0pPYAPQyI9tX4mkoK3t5MBOd53Mlu4739erzvgcqCh+FmHgceKXgdGF9NF9fVLq/IYvHbmEKGo7Fex2UzMXarrb3jbwfLl541+Z3zWvkY7oVeRIf0CPUnhuLneMU0s6nPl4f6JcIuvYDlHyehTw=')
# CategoryCrawler('https://www.aliexpress.com/category/200000775/jackets-coats.html?site=glo&g=y&isrefine=y',cookies=cookie).crawl_now()
TransactionCrawler(trans_id='32848645038',page=1,cookies=cookie).crawl_now()