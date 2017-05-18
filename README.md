# code_challenge

<br>crawler_setting 裡的資料是domain及要爬取的tag的屬性參數</br>
<br>例如:要抓取此標籤 \<a class="url fn n" rel="author">Joe Linton\</a> 可在 crawler_setting 中加入{"rel":"author"}
<br>\<a href="/users/brigette-brown/"> Brigette Brown\</a> ---> {"href":"/users/.+"} 也支援這樣的正規表示法

 會這樣設計的原因是因為如果未來有新的來源網站，只要在crawler_setting中增加domain及相對應的屬性即可抓取
