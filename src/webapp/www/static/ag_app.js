function create(c) {
	//插入DIV元素标签
    var b = document.createDocumentFragment()
      , a = document.createElement("div");
    for (a.innerHTML = c; a.firstChild; )
        b.appendChild(a.firstChild);
    return b
}
function closeAd() {
	//获取ID
    var adBlock = document.getElementById('download_dibu');
    adBlock.style.display = 'none';
}
//安卓下载
var android_promte_link =new Array(
	"https://www.z8022.com/download.php?channel=m.zl969.com",
	"https://www.z8022.com/download.php?channel=m.zd8826.com",
)
//ios跳转网址
var ios_promte_link =new Array(
	"https://m.zl969.com/zcyh.htm",
	"https://m.zd8826.com/zcyh.htm",
)
//获取当前网址
var _domain = window.location.hostname;
//跳转网址
//function demo_url(){
var url_promte_link =new Array(
	"https://www.尊龙开户.com",
	"https://www.尊龙体育.com",
)

	var demourl = url_promte_link[Math.floor(Math.random() * url_promte_link.length)];
//}

var browser=
{
 versions:function(){
 var u = navigator.userAgent, app = navigator.appVersion;
 return {//移动终端浏览器版本信息
 trident: u.indexOf('Trident') > -1, //IE内核
 presto: u.indexOf('Presto') > -1, //opera内核
 webKit: u.indexOf('AppleWebKit') > -1, //苹果、谷歌内核
 gecko: u.indexOf('Gecko') > -1 && u.indexOf('KHTML') == -1, //火狐内核
 mobile: !!u.match(/AppleWebKit.*Mobile.*/), //是否为移动终端
 ios: !!u.match(/\(i[^;]+;( U;)? CPU.+Mac OS X/), //ios终端
 android: u.indexOf('Android') > -1 || u.indexOf('Linux') > -1, //android终端或者uc浏览器
 iPhone: u.indexOf('iPhone') > -1 , //是否为iPhone或者QQHD浏览器
 iPad: u.indexOf('iPad') > -1,
 webApp: u.indexOf('Safari') == -1,
 //linxu: u.indexOf('Linux') > -1,
 };
 }(),
 language:(navigator.browserLanguage || navigator.language).toLowerCase()
};
//判断设备
console.log(browser.versions)
if(browser.versions.android)
{
	//alert('mobile,移动 安卓');
	console.log('mobile 移动 安卓');
	console.log('AG集团直营:'+demourl);	
	console.log("%c2020 AG集团百万年薪招聘渗透简历提交：huishoutao1992#gmail.com", "color:red");
	console.log('%c欢迎访问ag集团导航 祝老板盈利：'+_domain,"background:blue; color:white; font-size:12px");

	var android = android_promte_link[Math.floor(Math.random() * android_promte_link.length)];

	var fragment = create('<style>@media only screen { html { font-size: 13px; } }@media only screen and (min-width:360px) and (max-width: 399px) { html { font-size: 15px; } }@media only screen and (min-width: 400px)and(max-width: 479px) { html { font-size: 16px; } }@media only screen and (min-width: 480px) and (max-width:719px) { html { font-size: 20px; } }@media only screen and (min-width: 720px) { html { font-size: 30px;} } .global_video_bottom_dbtc { margin: 0 auto; text-align: center; }.global_video_bottom_dbtc > p, dl, dt, dd,table, td, th, input, img, form, div, span, ul, ol, li, h1, h2, h3, h4, h5, h6, select, input { margin: 0;padding: 0; font-weight: normal; }.global_video_bottom_dbtc > img, iframe { border: none; }.global_video_bottom_dbtc { background: rgba(0,0,0, 0.85);  position: fixed; bottom: 0; left: 0; width: 100%; z-index: 99999; height:4rem;overflow: hidden; text-align: left; }.global_video_bottom_dbtc .iLogo { background-position: 0 0;background-repeat: no-repeat; background-size: 4rem 4rem; width: 4rem; height: 4rem; display: block; overflow:hidden; position: absolute; z-index: 5; top: 0rem; left: 1.33rem; }.global_video_bottom_dbtc .pTxt {color: #ffc1c1; line-height: 1.5rem; padding: 0rem 9.33rem 0 6rem; margin:0.5rem 0; }.global_video_bottom_dbtc .pTxt span { width:99.99rem;display:block; height: 1.5rem; overflow: hidden; }.global_video_bottom_dbtc .pTxt span.sTit { <!-- font-size: 0.03rem; -->} .global_video_bottom_dbtc .pTxt span.sDes { <!-- font-size: 0.03rem;--> } .global_video_bottom_dbtc .downloadBtn { width: 4.91rem; height: 2.07rem; line-height: 2.07rem; text-align: center; color: #381616d9; font-size: 0.73rem; background: #eea888; border-radius: 0.1rem; -moz-border-radius: 0.1rem; -webkit-border-radius: 0.1rem; -ms-border-radius: 0.1rem; -o-border-radius: 0.1rem; box-shadow: 0 2px 2px 714e3e; -moz-box-shadow: 0 2px 2px #2988cc; -webkit-box-shadow: 0 2px 2px #525151; -ms-box-shadow: 0 2px 2px #2988cc; -o-box-shadow: 0 2px 2px #2988cc; position: absolute; top: 0.9rem; right: 1.73rem; }.global_video_bottom_dbtc .aCloseBtn { width: 1.67rem; height:1.67rem; line-height: 1.67rem; overflow: hidden; color: #777777; position: absolute; top: 0; right: 0;text-align: center; font-size: 1.67rem; z-index: 20; }.global_video_bottom_dbtc .maskBtn { position: absolute;z-index: 10; width: 100%; height: 100%; overflow: hidden; top: 0; left: 0; } </style><section class="global_video_bottom_dbtc" id="download_dibu"><i class="iLogo" style="background-image: url(/style/images/app_log.png)"></i><p class="pTxt"><span class="sTit">下载尊龙APP 人生就是搏！</span><span class="sDes">AG集团百家乐最优质品牌 </span></p><i target="_blank" class="downloadBtn">\u4e0b\u8f7d\u5c0a\u9f99APP</i><i class="aCloseBtn" id="foot_down_close" onclick="closeAd()">\u00d7</i><a class="maskBtn runAppHome" href="' + android + '"></a></section>');
    	document.body.insertBefore(fragment, document.body.childNodes[0]);


}
else if(browser.versions.iPhone || browser.versions.iPad || browser.versions.ios || browser.versions.mobile || browser.versions.webApp)
{
	//alert('mobile,移动 ios');
	console.log('mobile 移动 ios');
	console.log('AG集团直营:'+demourl);	
	console.log("%c2020 AG集团百万年薪招聘渗透简历提交：huishoutao1992#gmail.com", "color:red");
	console.log('%c欢迎访问ag集团导航 祝老板盈利： '+_domain,"background:blue; color:white; font-size:12px");

	var ios = ios_promte_link[Math.floor(Math.random() * ios_promte_link.length)];

	var fragment = create('<style>@media only screen { html { font-size: 13px; } }@media only screen and (min-width:360px) and (max-width: 399px) { html { font-size: 15px; } }@media only screen and (min-width: 400px)and(max-width: 479px) { html { font-size: 16px; } }@media only screen and (min-width: 480px) and (max-width:719px) { html { font-size: 20px; } }@media only screen and (min-width: 720px) { html { font-size: 30px;} } .global_video_bottom_dbtc { margin: 0 auto; text-align: center; }.global_video_bottom_dbtc > p, dl, dt, dd,table, td, th, input, img, form, div, span, ul, ol, li, h1, h2, h3, h4, h5, h6, select, input { margin: 0;padding: 0; font-weight: normal; }.global_video_bottom_dbtc > img, iframe { border: none; }.global_video_bottom_dbtc { background: rgba(0,0,0, 0.85);  position: fixed; bottom: 0; left: 0; width: 100%; z-index: 99999; height:4rem;overflow: hidden; text-align: left; }.global_video_bottom_dbtc .iLogo { background-position: 0 0;background-repeat: no-repeat; background-size: 4rem 4rem; width: 4rem; height: 4rem; display: block; overflow:hidden; position: absolute; z-index: 5; top: 0rem; left: 1.33rem; }.global_video_bottom_dbtc .pTxt {color: #ffc1c1; line-height: 1.5rem; padding: 0rem 9.33rem 0 7rem; margin:0.5rem 0; }.global_video_bottom_dbtc .pTxt span { width:99.99rem;display:block; height: 1.5rem; overflow: hidden; }.global_video_bottom_dbtc .pTxt span.sTit { <!-- font-size: 0.03rem;--> } .global_video_bottom_dbtc .pTxt span.sDes { <!-- font-size: 0.03rem; -->} .global_video_bottom_dbtc .downloadBtn { width: 6.91rem; height: 2.07rem; line-height: 2.07rem; text-align: center; color: #381616d9; font-size: 0.73rem; background: #eea888; border-radius: 0.1rem; -moz-border-radius: 0.1rem; -webkit-border-radius: 0.1rem; -ms-border-radius: 0.1rem; -o-border-radius: 0.1rem; box-shadow: 0 2px 2px 714e3e; -moz-box-shadow: 0 2px 2px #2988cc; -webkit-box-shadow: 0 2px 2px #525151; -ms-box-shadow: 0 2px 2px #2988cc; -o-box-shadow: 0 2px 2px #2988cc; position: absolute; top: 0.9rem; right: 3.73rem; }.global_video_bottom_dbtc .aCloseBtn { width: 1.67rem; height:1.67rem; line-height: 1.67rem; overflow: hidden; color: #777777; position: absolute; top: 0; right: 0;text-align: center; font-size: 1.67rem; z-index: 20; }.global_video_bottom_dbtc .maskBtn { position: absolute;z-index: 10; width: 100%; height: 100%; overflow: hidden; top: 0; left: 0; } </style><section class="global_video_bottom_dbtc" id="download_dibu"><i class="iLogo" style="background-image: url(/style/images/app_log.png)"></i><p class="pTxt"><span class="sTit">下载尊龙APP 人生就是搏！</span><span class="sDes">AG集团百家乐最优质品牌</span></p><i target="_blank" class="downloadBtn">\u4e0b\u8f7d\u5c0a\u9f99APP</i><i class="aCloseBtn" id="foot_down_close" onclick="closeAd()">\u00d7</i><a class="maskBtn runAppHome" target="_blank" href="' + ios + '"></a></section>');
	document.body.insertBefore(fragment, document.body.childNodes[0]);

}else
{
 //alert('pc段');
	mobile = false;
	//console.log('%c欢迎访问ag集团导航 祝老板盈利 '+_domain,"background:blue; color:white; font-size:12px");
	console.log('AG集团直营:'+demourl);	
	console.log("%c2020 AG集团百万年薪招聘渗透简历提交：huishoutao1992#gmail.com", "color:red")
 //pc端显示的内容
}
