__author__ = 'batulu'
from selenium import webdriver
import exescript

d=webdriver.PhantomJS("phantomjs")
#d.get("http://www.cnblogs.com/")
d.get("http://www.wandoujia.com/tag/%E5%BD%B1%E9%9F%B3%E5%9B%BE%E5%83%8F")
exejs=exescript.ExeJs(d)
exejs.exeWrap('$(".card").length')
print exejs.getMsg()
#out:
"""
20
"""

jsstr="""(function(){
var r=[];
$(".card").each(function(){
  var $this=$(this);
  var $a=$this.find("a");
  r.push($a.text());
});
setTimeout("$('.load-more').click()", 1000);
$(".card").each(function(){
  var $this=$(this);
  var $a=$this.find("a");
  r.push($a.text());
});
return r.join(',');})()"""
exejs.exeWrap(jsstr)
l=exejs.getMsg()
for title in l.split(','):
    print title

#out: