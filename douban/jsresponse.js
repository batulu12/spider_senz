/**
 * Created by batulu on 15/3/29.
 */
// a phantomjs example,saved as pdf file
var page = require('webpage').create();
page.open("http://www.wandoujia.com/tag/%E5%BD%B1%E9%9F%B3%E5%9B%BE%E5%83%8F", function(status) {
   if ( status === "success" ) {
      console.log(page.responseText);
      page.paperSize = { format: 'A4',
            orientation: 'portrait',
            border: '1cm' };
      page.render("front-Thinking.pdf");
   } else {
      console.log("Page failed to load.");
   }
   phantom.exit(0);
});