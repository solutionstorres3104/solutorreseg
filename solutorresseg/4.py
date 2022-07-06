


<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head id="Head2">

    <style>
        .sustentClass1 {
            font-size: 12px;
            color: #666666;
            font-weight: bolder;
            font-family: "gobCL";
        }

        .sustentClass2 {
            font-size: 12px;
            color: #666666;
            font-family: "gobCL";
        }
    </style>

    <meta http-equiv="X-UA-Compatible" content="IE=9" /><script type="text/javascript">window.NREUM||(NREUM={});NREUM.info = {"beacon":"bam.nr-data.net","errorBeacon":"bam.nr-data.net","licenseKey":"49ca6f4d08","applicationID":"5575733","transactionName":"NAZRZRECVkBTBUFdWA1McmIzTFVcVhNZUURMEVVTTAddR1MPWUdWABJGWBAKTFpdCBtVRBMb","queueTime":0,"applicationTime":190,"agent":"","atts":""}</script><script type="text/javascript">(window.NREUM||(NREUM={})).init={ajax:{deny_list:["bam.nr-data.net"]}};(window.NREUM||(NREUM={})).loader_config={xpid:"XAQOUF5VGwYFU1RVBAI=",licenseKey:"49ca6f4d08",applicationID:"5575733"};window.NREUM||(NREUM={}),__nr_require=function(t,e,n){function r(n){if(!e[n]){var o=e[n]={exports:{}};t[n][0].call(o.exports,function(e){var o=t[n][1][e];return r(o||e)},o,o.exports)}return e[n].exports}if("function"==typeof __nr_require)return __nr_require;for(var o=0;o<n.length;o++)r(n[o]);return r}({1:[function(t,e,n){function r(t){try{s.console&&console.log(t)}catch(e){}}var o,i=t("ee"),a=t(31),s={};try{o=localStorage.getItem("__nr_flags").split(","),console&&"function"==typeof console.log&&(s.console=!0,o.indexOf("dev")!==-1&&(s.dev=!0),o.indexOf("nr_dev")!==-1&&(s.nrDev=!0))}catch(c){}s.nrDev&&i.on("internal-error",function(t){r(t.stack)}),s.dev&&i.on("fn-err",function(t,e,n){r(n.stack)}),s.dev&&(r("NR AGENT IN DEVELOPMENT MODE"),r("flags: "+a(s,function(t,e){return t}).join(", ")))},{}],2:[function(t,e,n){function r(t,e,n,r,s){try{l?l-=1:o(s||new UncaughtException(t,e,n),!0)}catch(f){try{i("ierr",[f,c.now(),!0])}catch(d){}}return"function"==typeof u&&u.apply(this,a(arguments))}function UncaughtException(t,e,n){this.message=t||"Uncaught error with no additional information",this.sourceURL=e,this.line=n}function o(t,e){var n=e?null:c.now();i("err",[t,n])}var i=t("handle"),a=t(32),s=t("ee"),c=t("loader"),f=t("gos"),u=window.onerror,d=!1,p="nr@seenError";if(!c.disabled){var l=0;c.features.err=!0,t(1),window.onerror=r;try{throw new Error}catch(h){"stack"in h&&(t(14),t(13),"addEventListener"in window&&t(7),c.xhrWrappable&&t(15),d=!0)}s.on("fn-start",function(t,e,n){d&&(l+=1)}),s.on("fn-err",function(t,e,n){d&&!n[p]&&(f(n,p,function(){return!0}),this.thrown=!0,o(n))}),s.on("fn-end",function(){d&&!this.thrown&&l>0&&(l-=1)}),s.on("internal-error",function(t){i("ierr",[t,c.now(),!0])})}},{}],3:[function(t,e,n){var r=t("loader");r.disabled||(r.features.ins=!0)},{}],4:[function(t,e,n){function r(){U++,L=g.hash,this[u]=y.now()}function o(){U--,g.hash!==L&&i(0,!0);var t=y.now();this[h]=~~this[h]+t-this[u],this[d]=t}function i(t,e){E.emit("newURL",[""+g,e])}function a(t,e){t.on(e,function(){this[e]=y.now()})}var s="-start",c="-end",f="-body",u="fn"+s,d="fn"+c,p="cb"+s,l="cb"+c,h="jsTime",m="fetch",v="addEventListener",w=window,g=w.location,y=t("loader");if(w[v]&&y.xhrWrappable&&!y.disabled){var x=t(11),b=t(12),E=t(9),R=t(7),O=t(14),T=t(8),S=t(15),P=t(10),M=t("ee"),C=M.get("tracer"),N=t(23);t(17),y.features.spa=!0;var L,U=0;M.on(u,r),b.on(p,r),P.on(p,r),M.on(d,o),b.on(l,o),P.on(l,o),M.buffer([u,d,"xhr-resolved"]),R.buffer([u]),O.buffer(["setTimeout"+c,"clearTimeout"+s,u]),S.buffer([u,"new-xhr","send-xhr"+s]),T.buffer([m+s,m+"-done",m+f+s,m+f+c]),E.buffer(["newURL"]),x.buffer([u]),b.buffer(["propagate",p,l,"executor-err","resolve"+s]),C.buffer([u,"no-"+u]),P.buffer(["new-jsonp","cb-start","jsonp-error","jsonp-end"]),a(T,m+s),a(T,m+"-done"),a(P,"new-jsonp"),a(P,"jsonp-end"),a(P,"cb-start"),E.on("pushState-end",i),E.on("replaceState-end",i),w[v]("hashchange",i,N(!0)),w[v]("load",i,N(!0)),w[v]("popstate",function(){i(0,U>1)},N(!0))}},{}],5:[function(t,e,n){function r(){var t=new PerformanceObserver(function(t,e){var n=t.getEntries();s(v,[n])});try{t.observe({entryTypes:["resource"]})}catch(e){}}function o(t){if(s(v,[window.performance.getEntriesByType(w)]),window.performance["c"+p])try{window.performance[h](m,o,!1)}catch(t){}else try{window.performance[h]("webkit"+m,o,!1)}catch(t){}}function i(t){}if(window.performance&&window.performance.timing&&window.performance.getEntriesByType){var a=t("ee"),s=t("handle"),c=t(14),f=t(13),u=t(6),d=t(23),p="learResourceTimings",l="addEventListener",h="removeEventListener",m="resourcetimingbufferfull",v="bstResource",w="resource",g="-start",y="-end",x="fn"+g,b="fn"+y,E="bstTimer",R="pushState",O=t("loader");if(!O.disabled){O.features.stn=!0,t(9),"addEventListener"in window&&t(7);var T=NREUM.o.EV;a.on(x,function(t,e){var n=t[0];n instanceof T&&(this.bstStart=O.now())}),a.on(b,function(t,e){var n=t[0];n instanceof T&&s("bst",[n,e,this.bstStart,O.now()])}),c.on(x,function(t,e,n){this.bstStart=O.now(),this.bstType=n}),c.on(b,function(t,e){s(E,[e,this.bstStart,O.now(),this.bstType])}),f.on(x,function(){this.bstStart=O.now()}),f.on(b,function(t,e){s(E,[e,this.bstStart,O.now(),"requestAnimationFrame"])}),a.on(R+g,function(t){this.time=O.now(),this.startPath=location.pathname+location.hash}),a.on(R+y,function(t){s("bstHist",[location.pathname+location.hash,this.startPath,this.time])}),u()?(s(v,[window.performance.getEntriesByType("resource")]),r()):l in window.performance&&(window.performance["c"+p]?window.performance[l](m,o,d(!1)):window.performance[l]("webkit"+m,o,d(!1))),document[l]("scroll",i,d(!1)),document[l]("keypress",i,d(!1)),document[l]("click",i,d(!1))}}},{}],6:[function(t,e,n){e.exports=function(){return"PerformanceObserver"in window&&"function"==typeof window.PerformanceObserver}},{}],7:[function(t,e,n){function r(t){for(var e=t;e&&!e.hasOwnProperty(u);)e=Object.getPrototypeOf(e);e&&o(e)}function o(t){s.inPlace(t,[u,d],"-",i)}function i(t,e){return t[1]}var a=t("ee").get("events"),s=t("wrap-function")(a,!0),c=t("gos"),f=XMLHttpRequest,u="addEventListener",d="removeEventListener";e.exports=a,"getPrototypeOf"in Object?(r(document),r(window),r(f.prototype)):f.prototype.hasOwnProperty(u)&&(o(window),o(f.prototype)),a.on(u+"-start",function(t,e){var n=t[1];if(null!==n&&("function"==typeof n||"object"==typeof n)){var r=c(n,"nr@wrapped",function(){function t(){if("function"==typeof n.handleEvent)return n.handleEvent.apply(n,arguments)}var e={object:t,"function":n}[typeof n];return e?s(e,"fn-",null,e.name||"anonymous"):n});this.wrapped=t[1]=r}}),a.on(d+"-start",function(t){t[1]=this.wrapped||t[1]})},{}],8:[function(t,e,n){function r(t,e,n){var r=t[e];"function"==typeof r&&(t[e]=function(){var t=i(arguments),e={};o.emit(n+"before-start",[t],e);var a;e[m]&&e[m].dt&&(a=e[m].dt);var s=r.apply(this,t);return o.emit(n+"start",[t,a],s),s.then(function(t){return o.emit(n+"end",[null,t],s),t},function(t){throw o.emit(n+"end",[t],s),t})})}var o=t("ee").get("fetch"),i=t(32),a=t(31);e.exports=o;var s=window,c="fetch-",f=c+"body-",u=["arrayBuffer","blob","json","text","formData"],d=s.Request,p=s.Response,l=s.fetch,h="prototype",m="nr@context";d&&p&&l&&(a(u,function(t,e){r(d[h],e,f),r(p[h],e,f)}),r(s,"fetch",c),o.on(c+"end",function(t,e){var n=this;if(e){var r=e.headers.get("content-length");null!==r&&(n.rxSize=r),o.emit(c+"done",[null,e],n)}else o.emit(c+"done",[t],n)}))},{}],9:[function(t,e,n){var r=t("ee").get("history"),o=t("wrap-function")(r);e.exports=r;var i=window.history&&window.history.constructor&&window.history.constructor.prototype,a=window.history;i&&i.pushState&&i.replaceState&&(a=i),o.inPlace(a,["pushState","replaceState"],"-")},{}],10:[function(t,e,n){function r(t){function e(){f.emit("jsonp-end",[],l),t.removeEventListener("load",e,c(!1)),t.removeEventListener("error",n,c(!1))}function n(){f.emit("jsonp-error",[],l),f.emit("jsonp-end",[],l),t.removeEventListener("load",e,c(!1)),t.removeEventListener("error",n,c(!1))}var r=t&&"string"==typeof t.nodeName&&"script"===t.nodeName.toLowerCase();if(r){var o="function"==typeof t.addEventListener;if(o){var a=i(t.src);if(a){var d=s(a),p="function"==typeof d.parent[d.key];if(p){var l={};u.inPlace(d.parent,[d.key],"cb-",l),t.addEventListener("load",e,c(!1)),t.addEventListener("error",n,c(!1)),f.emit("new-jsonp",[t.src],l)}}}}}function o(){return"addEventListener"in window}function i(t){var e=t.match(d);return e?e[1]:null}function a(t,e){var n=t.match(l),r=n[1],o=n[3];return o?a(o,e[r]):e[r]}function s(t){var e=t.match(p);return e&&e.length>=3?{key:e[2],parent:a(e[1],window)}:{key:t,parent:window}}var c=t(23),f=t("ee").get("jsonp"),u=t("wrap-function")(f);if(e.exports=f,o()){var d=/[?&](?:callback|cb)=([^&#]+)/,p=/(.*)\.([^.]+)/,l=/^(\w+)(\.|$)(.*)$/,h=["appendChild","insertBefore","replaceChild"];Node&&Node.prototype&&Node.prototype.appendChild?u.inPlace(Node.prototype,h,"dom-"):(u.inPlace(HTMLElement.prototype,h,"dom-"),u.inPlace(HTMLHeadElement.prototype,h,"dom-"),u.inPlace(HTMLBodyElement.prototype,h,"dom-")),f.on("dom-start",function(t){r(t[0])})}},{}],11:[function(t,e,n){var r=t("ee").get("mutation"),o=t("wrap-function")(r),i=NREUM.o.MO;e.exports=r,i&&(window.MutationObserver=function(t){return this instanceof i?new i(o(t,"fn-")):i.apply(this,arguments)},MutationObserver.prototype=i.prototype)},{}],12:[function(t,e,n){function r(t){var e=i.context(),n=s(t,"executor-",e,null,!1),r=new f(n);return i.context(r).getCtx=function(){return e},r}var o=t("wrap-function"),i=t("ee").get("promise"),a=t("ee").getOrSetContext,s=o(i),c=t(31),f=NREUM.o.PR;e.exports=i,f&&(window.Promise=r,["all","race"].forEach(function(t){var e=f[t];f[t]=function(n){function r(t){return function(){i.emit("propagate",[null,!o],a,!1,!1),o=o||!t}}var o=!1;c(n,function(e,n){Promise.resolve(n).then(r("all"===t),r(!1))});var a=e.apply(f,arguments),s=f.resolve(a);return s}}),["resolve","reject"].forEach(function(t){var e=f[t];f[t]=function(t){var n=e.apply(f,arguments);return t!==n&&i.emit("propagate",[t,!0],n,!1,!1),n}}),f.prototype["catch"]=function(t){return this.then(null,t)},f.prototype=Object.create(f.prototype,{constructor:{value:r}}),c(Object.getOwnPropertyNames(f),function(t,e){try{r[e]=f[e]}catch(n){}}),o.wrapInPlace(f.prototype,"then",function(t){return function(){var e=this,n=o.argsToArray.apply(this,arguments),r=a(e);r.promise=e,n[0]=s(n[0],"cb-",r,null,!1),n[1]=s(n[1],"cb-",r,null,!1);var c=t.apply(this,n);return r.nextPromise=c,i.emit("propagate",[e,!0],c,!1,!1),c}}),i.on("executor-start",function(t){t[0]=s(t[0],"resolve-",this,null,!1),t[1]=s(t[1],"resolve-",this,null,!1)}),i.on("executor-err",function(t,e,n){t[1](n)}),i.on("cb-end",function(t,e,n){i.emit("propagate",[n,!0],this.nextPromise,!1,!1)}),i.on("propagate",function(t,e,n){this.getCtx&&!e||(this.getCtx=function(){if(t instanceof Promise)var e=i.context(t);return e&&e.getCtx?e.getCtx():this})}),r.toString=function(){return""+f})},{}],13:[function(t,e,n){var r=t("ee").get("raf"),o=t("wrap-function")(r),i="equestAnimationFrame";e.exports=r,o.inPlace(window,["r"+i,"mozR"+i,"webkitR"+i,"msR"+i],"raf-"),r.on("raf-start",function(t){t[0]=o(t[0],"fn-")})},{}],14:[function(t,e,n){function r(t,e,n){t[0]=a(t[0],"fn-",null,n)}function o(t,e,n){this.method=n,this.timerDuration=isNaN(t[1])?0:+t[1],t[0]=a(t[0],"fn-",this,n)}var i=t("ee").get("timer"),a=t("wrap-function")(i),s="setTimeout",c="setInterval",f="clearTimeout",u="-start",d="-";e.exports=i,a.inPlace(window,[s,"setImmediate"],s+d),a.inPlace(window,[c],c+d),a.inPlace(window,[f,"clearImmediate"],f+d),i.on(c+u,r),i.on(s+u,o)},{}],15:[function(t,e,n){function r(t,e){d.inPlace(e,["onreadystatechange"],"fn-",s)}function o(){var t=this,e=u.context(t);t.readyState>3&&!e.resolved&&(e.resolved=!0,u.emit("xhr-resolved",[],t)),d.inPlace(t,y,"fn-",s)}function i(t){x.push(t),m&&(E?E.then(a):w?w(a):(R=-R,O.data=R))}function a(){for(var t=0;t<x.length;t++)r([],x[t]);x.length&&(x=[])}function s(t,e){return e}function c(t,e){for(var n in t)e[n]=t[n];return e}t(7);var f=t("ee"),u=f.get("xhr"),d=t("wrap-function")(u),p=t(23),l=NREUM.o,h=l.XHR,m=l.MO,v=l.PR,w=l.SI,g="readystatechange",y=["onload","onerror","onabort","onloadstart","onloadend","onprogress","ontimeout"],x=[];e.exports=u;var b=window.XMLHttpRequest=function(t){var e=new h(t);try{u.emit("new-xhr",[e],e),e.addEventListener(g,o,p(!1))}catch(n){try{u.emit("internal-error",[n])}catch(r){}}return e};if(c(h,b),b.prototype=h.prototype,d.inPlace(b.prototype,["open","send"],"-xhr-",s),u.on("send-xhr-start",function(t,e){r(t,e),i(e)}),u.on("open-xhr-start",r),m){var E=v&&v.resolve();if(!w&&!v){var R=1,O=document.createTextNode(R);new m(a).observe(O,{characterData:!0})}}else f.on("fn-end",function(t){t[0]&&t[0].type===g||a()})},{}],16:[function(t,e,n){function r(t){if(!s(t))return null;var e=window.NREUM;if(!e.loader_config)return null;var n=(e.loader_config.accountID||"").toString()||null,r=(e.loader_config.agentID||"").toString()||null,f=(e.loader_config.trustKey||"").toString()||null;if(!n||!r)return null;var h=l.generateSpanId(),m=l.generateTraceId(),v=Date.now(),w={spanId:h,traceId:m,timestamp:v};return(t.sameOrigin||c(t)&&p())&&(w.traceContextParentHeader=o(h,m),w.traceContextStateHeader=i(h,v,n,r,f)),(t.sameOrigin&&!u()||!t.sameOrigin&&c(t)&&d())&&(w.newrelicHeader=a(h,m,v,n,r,f)),w}function o(t,e){return"00-"+e+"-"+t+"-01"}function i(t,e,n,r,o){var i=0,a="",s=1,c="",f="";return o+"@nr="+i+"-"+s+"-"+n+"-"+r+"-"+t+"-"+a+"-"+c+"-"+f+"-"+e}function a(t,e,n,r,o,i){var a="btoa"in window&&"function"==typeof window.btoa;if(!a)return null;var s={v:[0,1],d:{ty:"Browser",ac:r,ap:o,id:t,tr:e,ti:n}};return i&&r!==i&&(s.d.tk=i),btoa(JSON.stringify(s))}function s(t){return f()&&c(t)}function c(t){var e=!1,n={};if("init"in NREUM&&"distributed_tracing"in NREUM.init&&(n=NREUM.init.distributed_tracing),t.sameOrigin)e=!0;else if(n.allowed_origins instanceof Array)for(var r=0;r<n.allowed_origins.length;r++){var o=h(n.allowed_origins[r]);if(t.hostname===o.hostname&&t.protocol===o.protocol&&t.port===o.port){e=!0;break}}return e}function f(){return"init"in NREUM&&"distributed_tracing"in NREUM.init&&!!NREUM.init.distributed_tracing.enabled}function u(){return"init"in NREUM&&"distributed_tracing"in NREUM.init&&!!NREUM.init.distributed_tracing.exclude_newrelic_header}function d(){return"init"in NREUM&&"distributed_tracing"in NREUM.init&&NREUM.init.distributed_tracing.cors_use_newrelic_header!==!1}function p(){return"init"in NREUM&&"distributed_tracing"in NREUM.init&&!!NREUM.init.distributed_tracing.cors_use_tracecontext_headers}var l=t(28),h=t(18);e.exports={generateTracePayload:r,shouldGenerateTrace:s}},{}],17:[function(t,e,n){function r(t){var e=this.params,n=this.metrics;if(!this.ended){this.ended=!0;for(var r=0;r<p;r++)t.removeEventListener(d[r],this.listener,!1);return e.protocol&&"data"===e.protocol?void g("Ajax/DataUrl/Excluded"):void(e.aborted||(n.duration=a.now()-this.startTime,this.loadCaptureCalled||4!==t.readyState?null==e.status&&(e.status=0):i(this,t),n.cbTime=this.cbTime,s("xhr",[e,n,this.startTime,this.endTime,"xhr"],this)))}}function o(t,e){var n=c(e),r=t.params;r.hostname=n.hostname,r.port=n.port,r.protocol=n.protocol,r.host=n.hostname+":"+n.port,r.pathname=n.pathname,t.parsedOrigin=n,t.sameOrigin=n.sameOrigin}function i(t,e){t.params.status=e.status;var n=v(e,t.lastSize);if(n&&(t.metrics.rxSize=n),t.sameOrigin){var r=e.getResponseHeader("X-NewRelic-App-Data");r&&(t.params.cat=r.split(", ").pop())}t.loadCaptureCalled=!0}var a=t("loader");if(a.xhrWrappable&&!a.disabled){var s=t("handle"),c=t(18),f=t(16).generateTracePayload,u=t("ee"),d=["load","error","abort","timeout"],p=d.length,l=t("id"),h=t(24),m=t(22),v=t(19),w=t(23),g=t(25).recordSupportability,y=NREUM.o.REQ,x=window.XMLHttpRequest;a.features.xhr=!0,t(15),t(8),u.on("new-xhr",function(t){var e=this;e.totalCbs=0,e.called=0,e.cbTime=0,e.end=r,e.ended=!1,e.xhrGuids={},e.lastSize=null,e.loadCaptureCalled=!1,e.params=this.params||{},e.metrics=this.metrics||{},t.addEventListener("load",function(n){i(e,t)},w(!1)),h&&(h>34||h<10)||t.addEventListener("progress",function(t){e.lastSize=t.loaded},w(!1))}),u.on("open-xhr-start",function(t){this.params={method:t[0]},o(this,t[1]),this.metrics={}}),u.on("open-xhr-end",function(t,e){"loader_config"in NREUM&&"xpid"in NREUM.loader_config&&this.sameOrigin&&e.setRequestHeader("X-NewRelic-ID",NREUM.loader_config.xpid);var n=f(this.parsedOrigin);if(n){var r=!1;n.newrelicHeader&&(e.setRequestHeader("newrelic",n.newrelicHeader),r=!0),n.traceContextParentHeader&&(e.setRequestHeader("traceparent",n.traceContextParentHeader),n.traceContextStateHeader&&e.setRequestHeader("tracestate",n.traceContextStateHeader),r=!0),r&&(this.dt=n)}}),u.on("send-xhr-start",function(t,e){var n=this.metrics,r=t[0],o=this;if(n&&r){var i=m(r);i&&(n.txSize=i)}this.startTime=a.now(),this.listener=function(t){try{"abort"!==t.type||o.loadCaptureCalled||(o.params.aborted=!0),("load"!==t.type||o.called===o.totalCbs&&(o.onloadCalled||"function"!=typeof e.onload))&&o.end(e)}catch(n){try{u.emit("internal-error",[n])}catch(r){}}};for(var s=0;s<p;s++)e.addEventListener(d[s],this.listener,w(!1))}),u.on("xhr-cb-time",function(t,e,n){this.cbTime+=t,e?this.onloadCalled=!0:this.called+=1,this.called!==this.totalCbs||!this.onloadCalled&&"function"==typeof n.onload||this.end(n)}),u.on("xhr-load-added",function(t,e){var n=""+l(t)+!!e;this.xhrGuids&&!this.xhrGuids[n]&&(this.xhrGuids[n]=!0,this.totalCbs+=1)}),u.on("xhr-load-removed",function(t,e){var n=""+l(t)+!!e;this.xhrGuids&&this.xhrGuids[n]&&(delete this.xhrGuids[n],this.totalCbs-=1)}),u.on("xhr-resolved",function(){this.endTime=a.now()}),u.on("addEventListener-end",function(t,e){e instanceof x&&"load"===t[0]&&u.emit("xhr-load-added",[t[1],t[2]],e)}),u.on("removeEventListener-end",function(t,e){e instanceof x&&"load"===t[0]&&u.emit("xhr-load-removed",[t[1],t[2]],e)}),u.on("fn-start",function(t,e,n){e instanceof x&&("onload"===n&&(this.onload=!0),("load"===(t[0]&&t[0].type)||this.onload)&&(this.xhrCbStart=a.now()))}),u.on("fn-end",function(t,e){this.xhrCbStart&&u.emit("xhr-cb-time",[a.now()-this.xhrCbStart,this.onload,e],e)}),u.on("fetch-before-start",function(t){function e(t,e){var n=!1;return e.newrelicHeader&&(t.set("newrelic",e.newrelicHeader),n=!0),e.traceContextParentHeader&&(t.set("traceparent",e.traceContextParentHeader),e.traceContextStateHeader&&t.set("tracestate",e.traceContextStateHeader),n=!0),n}var n,r=t[1]||{};"string"==typeof t[0]?n=t[0]:t[0]&&t[0].url?n=t[0].url:window.URL&&t[0]&&t[0]instanceof URL&&(n=t[0].href),n&&(this.parsedOrigin=c(n),this.sameOrigin=this.parsedOrigin.sameOrigin);var o=f(this.parsedOrigin);if(o&&(o.newrelicHeader||o.traceContextParentHeader))if("string"==typeof t[0]||window.URL&&t[0]&&t[0]instanceof URL){var i={};for(var a in r)i[a]=r[a];i.headers=new Headers(r.headers||{}),e(i.headers,o)&&(this.dt=o),t.length>1?t[1]=i:t.push(i)}else t[0]&&t[0].headers&&e(t[0].headers,o)&&(this.dt=o)}),u.on("fetch-start",function(t,e){this.params={},this.metrics={},this.startTime=a.now(),this.dt=e,t.length>=1&&(this.target=t[0]),t.length>=2&&(this.opts=t[1]);var n,r=this.opts||{},i=this.target;if("string"==typeof i?n=i:"object"==typeof i&&i instanceof y?n=i.url:window.URL&&"object"==typeof i&&i instanceof URL&&(n=i.href),o(this,n),"data"!==this.params.protocol){var s=(""+(i&&i instanceof y&&i.method||r.method||"GET")).toUpperCase();this.params.method=s,this.txSize=m(r.body)||0}}),u.on("fetch-done",function(t,e){if(this.endTime=a.now(),this.params||(this.params={}),"data"===this.params.protocol)return void g("Ajax/DataUrl/Excluded");this.params.status=e?e.status:0;var n;"string"==typeof this.rxSize&&this.rxSize.length>0&&(n=+this.rxSize);var r={txSize:this.txSize,rxSize:n,duration:a.now()-this.startTime};s("xhr",[this.params,r,this.startTime,this.endTime,"fetch"],this)})}},{}],18:[function(t,e,n){var r={};e.exports=function(t){if(t in r)return r[t];if(0===(t||"").indexOf("data:"))return{protocol:"data"};var e=document.createElement("a"),n=window.location,o={};e.href=t,o.port=e.port;var i=e.href.split("://");!o.port&&i[1]&&(o.port=i[1].split("/")[0].split("@").pop().split(":")[1]),o.port&&"0"!==o.port||(o.port="https"===i[0]?"443":"80"),o.hostname=e.hostname||n.hostname,o.pathname=e.pathname,o.protocol=i[0],"/"!==o.pathname.charAt(0)&&(o.pathname="/"+o.pathname);var a=!e.protocol||":"===e.protocol||e.protocol===n.protocol,s=e.hostname===document.domain&&e.port===n.port;return o.sameOrigin=a&&(!e.hostname||s),"/"===o.pathname&&(r[t]=o),o}},{}],19:[function(t,e,n){function r(t,e){var n=t.responseType;return"json"===n&&null!==e?e:"arraybuffer"===n||"blob"===n||"json"===n?o(t.response):"text"===n||""===n||void 0===n?o(t.responseText):void 0}var o=t(22);e.exports=r},{}],20:[function(t,e,n){function r(){}function o(t,e,n,r){return function(){return u.recordSupportability("API/"+e+"/called"),i(t+e,[f.now()].concat(s(arguments)),n?null:this,r),n?void 0:this}}var i=t("handle"),a=t(31),s=t(32),c=t("ee").get("tracer"),f=t("loader"),u=t(25),d=NREUM;"undefined"==typeof window.newrelic&&(newrelic=d);var p=["setPageViewName","setCustomAttribute","setErrorHandler","finished","addToTrace","inlineHit","addRelease"],l="api-",h=l+"ixn-";a(p,function(t,e){d[e]=o(l,e,!0,"api")}),d.addPageAction=o(l,"addPageAction",!0),d.setCurrentRouteName=o(l,"routeName",!0),e.exports=newrelic,d.interaction=function(){return(new r).get()};var m=r.prototype={createTracer:function(t,e){var n={},r=this,o="function"==typeof e;return i(h+"tracer",[f.now(),t,n],r),function(){if(c.emit((o?"":"no-")+"fn-start",[f.now(),r,o],n),o)try{return e.apply(this,arguments)}catch(t){throw c.emit("fn-err",[arguments,this,t],n),t}finally{c.emit("fn-end",[f.now()],n)}}}};a("actionText,setName,setAttribute,save,ignore,onEnd,getContext,end,get".split(","),function(t,e){m[e]=o(h,e)}),newrelic.noticeError=function(t,e){"string"==typeof t&&(t=new Error(t)),u.recordSupportability("API/noticeError/called"),i("err",[t,f.now(),!1,e])}},{}],21:[function(t,e,n){function r(t){if(NREUM.init){for(var e=NREUM.init,n=t.split("."),r=0;r<n.length-1;r++)if(e=e[n[r]],"object"!=typeof e)return;return e=e[n[n.length-1]]}}e.exports={getConfiguration:r}},{}],22:[function(t,e,n){e.exports=function(t){if("string"==typeof t&&t.length)return t.length;if("object"==typeof t){if("undefined"!=typeof ArrayBuffer&&t instanceof ArrayBuffer&&t.byteLength)return t.byteLength;if("undefined"!=typeof Blob&&t instanceof Blob&&t.size)return t.size;if(!("undefined"!=typeof FormData&&t instanceof FormData))try{return JSON.stringify(t).length}catch(e){return}}}},{}],23:[function(t,e,n){var r=!1;try{var o=Object.defineProperty({},"passive",{get:function(){r=!0}});window.addEventListener("testPassive",null,o),window.removeEventListener("testPassive",null,o)}catch(i){}e.exports=function(t){return r?{passive:!0,capture:!!t}:!!t}},{}],24:[function(t,e,n){var r=0,o=navigator.userAgent.match(/Firefox[\/\s](\d+\.\d+)/);o&&(r=+o[1]),e.exports=r},{}],25:[function(t,e,n){function r(t,e){var n=[a,t,{name:t},e];return i("storeMetric",n,null,"api"),n}function o(t,e){var n=[s,t,{name:t},e];return i("storeEventMetrics",n,null,"api"),n}var i=t("handle"),a="sm",s="cm";e.exports={constants:{SUPPORTABILITY_METRIC:a,CUSTOM_METRIC:s},recordSupportability:r,recordCustom:o}},{}],26:[function(t,e,n){function r(){return s.exists&&performance.now?Math.round(performance.now()):(i=Math.max((new Date).getTime(),i))-a}function o(){return i}var i=(new Date).getTime(),a=i,s=t(33);e.exports=r,e.exports.offset=a,e.exports.getLastTimestamp=o},{}],27:[function(t,e,n){function r(t,e){var n=t.getEntries();n.forEach(function(t){"first-paint"===t.name?l("timing",["fp",Math.floor(t.startTime)]):"first-contentful-paint"===t.name&&l("timing",["fcp",Math.floor(t.startTime)])})}function o(t,e){var n=t.getEntries();if(n.length>0){var r=n[n.length-1];if(f&&f<r.startTime)return;var o=[r],i=a({});i&&o.push(i),l("lcp",o)}}function i(t){t.getEntries().forEach(function(t){t.hadRecentInput||l("cls",[t])})}function a(t){var e=navigator.connection||navigator.mozConnection||navigator.webkitConnection;if(e)return e.type&&(t["net-type"]=e.type),e.effectiveType&&(t["net-etype"]=e.effectiveType),e.rtt&&(t["net-rtt"]=e.rtt),e.downlink&&(t["net-dlink"]=e.downlink),t}function s(t){if(t instanceof w&&!y){var e=Math.round(t.timeStamp),n={type:t.type};a(n),e<=h.now()?n.fid=h.now()-e:e>h.offset&&e<=Date.now()?(e-=h.offset,n.fid=h.now()-e):e=h.now(),y=!0,l("timing",["fi",e,n])}}function c(t){"hidden"===t&&(f=h.now(),l("pageHide",[f]))}if(!("init"in NREUM&&"page_view_timing"in NREUM.init&&"enabled"in NREUM.init.page_view_timing&&NREUM.init.page_view_timing.enabled===!1)){var f,u,d,p,l=t("handle"),h=t("loader"),m=t(30),v=t(23),w=NREUM.o.EV;if("PerformanceObserver"in window&&"function"==typeof window.PerformanceObserver){u=new PerformanceObserver(r);try{u.observe({entryTypes:["paint"]})}catch(g){}d=new PerformanceObserver(o);try{d.observe({entryTypes:["largest-contentful-paint"]})}catch(g){}p=new PerformanceObserver(i);try{p.observe({type:"layout-shift",buffered:!0})}catch(g){}}if("addEventListener"in document){var y=!1,x=["click","keydown","mousedown","pointerdown","touchstart"];x.forEach(function(t){document.addEventListener(t,s,v(!1))})}m(c)}},{}],28:[function(t,e,n){function r(){function t(){return e?15&e[n++]:16*Math.random()|0}var e=null,n=0,r=window.crypto||window.msCrypto;r&&r.getRandomValues&&(e=r.getRandomValues(new Uint8Array(31)));for(var o,i="xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx",a="",s=0;s<i.length;s++)o=i[s],"x"===o?a+=t().toString(16):"y"===o?(o=3&t()|8,a+=o.toString(16)):a+=o;return a}function o(){return a(16)}function i(){return a(32)}function a(t){function e(){return n?15&n[r++]:16*Math.random()|0}var n=null,r=0,o=window.crypto||window.msCrypto;o&&o.getRandomValues&&Uint8Array&&(n=o.getRandomValues(new Uint8Array(t)));for(var i=[],a=0;a<t;a++)i.push(e().toString(16));return i.join("")}e.exports={generateUuid:r,generateSpanId:o,generateTraceId:i}},{}],29:[function(t,e,n){function r(t,e){if(!o)return!1;if(t!==o)return!1;if(!e)return!0;if(!i)return!1;for(var n=i.split("."),r=e.split("."),a=0;a<r.length;a++)if(r[a]!==n[a])return!1;return!0}var o=null,i=null,a=/Version\/(\S+)\s+Safari/;if(navigator.userAgent){var s=navigator.userAgent,c=s.match(a);c&&s.indexOf("Chrome")===-1&&s.indexOf("Chromium")===-1&&(o="Safari",i=c[1])}e.exports={agent:o,version:i,match:r}},{}],30:[function(t,e,n){function r(t){function e(){t(s&&document[s]?document[s]:document[i]?"hidden":"visible")}"addEventListener"in document&&a&&document.addEventListener(a,e,o(!1))}var o=t(23);e.exports=r;var i,a,s;"undefined"!=typeof document.hidden?(i="hidden",a="visibilitychange",s="visibilityState"):"undefined"!=typeof document.msHidden?(i="msHidden",a="msvisibilitychange"):"undefined"!=typeof document.webkitHidden&&(i="webkitHidden",a="webkitvisibilitychange",s="webkitVisibilityState")},{}],31:[function(t,e,n){function r(t,e){var n=[],r="",i=0;for(r in t)o.call(t,r)&&(n[i]=e(r,t[r]),i+=1);return n}var o=Object.prototype.hasOwnProperty;e.exports=r},{}],32:[function(t,e,n){function r(t,e,n){e||(e=0),"undefined"==typeof n&&(n=t?t.length:0);for(var r=-1,o=n-e||0,i=Array(o<0?0:o);++r<o;)i[r]=t[e+r];return i}e.exports=r},{}],33:[function(t,e,n){e.exports={exists:"undefined"!=typeof window.performance&&window.performance.timing&&"undefined"!=typeof window.performance.timing.navigationStart}},{}],ee:[function(t,e,n){function r(){}function o(t){function e(t){return t&&t instanceof r?t:t?f(t,c,a):a()}function n(n,r,o,i,a){if(a!==!1&&(a=!0),!l.aborted||i){t&&a&&t(n,r,o);for(var s=e(o),c=m(n),f=c.length,u=0;u<f;u++)c[u].apply(s,r);var p=d[y[n]];return p&&p.push([x,n,r,s]),s}}function i(t,e){g[t]=m(t).concat(e)}function h(t,e){var n=g[t];if(n)for(var r=0;r<n.length;r++)n[r]===e&&n.splice(r,1)}function m(t){return g[t]||[]}function v(t){return p[t]=p[t]||o(n)}function w(t,e){l.aborted||u(t,function(t,n){e=e||"feature",y[n]=e,e in d||(d[e]=[])})}var g={},y={},x={on:i,addEventListener:i,removeEventListener:h,emit:n,get:v,listeners:m,context:e,buffer:w,abort:s,aborted:!1};return x}function i(t){return f(t,c,a)}function a(){return new r}function s(){(d.api||d.feature)&&(l.aborted=!0,d=l.backlog={})}var c="nr@context",f=t("gos"),u=t(31),d={},p={},l=e.exports=o();e.exports.getOrSetContext=i,l.backlog=d},{}],gos:[function(t,e,n){function r(t,e,n){if(o.call(t,e))return t[e];var r=n();if(Object.defineProperty&&Object.keys)try{return Object.defineProperty(t,e,{value:r,writable:!0,enumerable:!1}),r}catch(i){}return t[e]=r,r}var o=Object.prototype.hasOwnProperty;e.exports=r},{}],handle:[function(t,e,n){function r(t,e,n,r){o.buffer([t],r),o.emit(t,e,n)}var o=t("ee").get("handle");e.exports=r,r.ee=o},{}],id:[function(t,e,n){function r(t){var e=typeof t;return!t||"object"!==e&&"function"!==e?-1:t===window?0:a(t,i,function(){return o++})}var o=1,i="nr@id",a=t("gos");e.exports=r},{}],loader:[function(t,e,n){function r(){if(!T++){var t=O.info=NREUM.info,e=m.getElementsByTagName("script")[0];if(setTimeout(f.abort,3e4),!(t&&t.licenseKey&&t.applicationID&&e))return f.abort();c(E,function(e,n){t[e]||(t[e]=n)});var n=a();s("mark",["onload",n+O.offset],null,"api"),s("timing",["load",n]);var r=m.createElement("script");0===t.agent.indexOf("http://")||0===t.agent.indexOf("https://")?r.src=t.agent:r.src=l+"://"+t.agent,e.parentNode.insertBefore(r,e)}}function o(){"complete"===m.readyState&&i()}function i(){s("mark",["domContent",a()+O.offset],null,"api")}var a=t(26),s=t("handle"),c=t(31),f=t("ee"),u=t(29),d=t(21),p=t(23),l=d.getConfiguration("ssl")===!1?"http":"https",h=window,m=h.document,v="addEventListener",w="attachEvent",g=h.XMLHttpRequest,y=g&&g.prototype,x=!1;NREUM.o={ST:setTimeout,SI:h.setImmediate,CT:clearTimeout,XHR:g,REQ:h.Request,EV:h.Event,PR:h.Promise,MO:h.MutationObserver};var b=""+location,E={beacon:"bam.nr-data.net",errorBeacon:"bam.nr-data.net",agent:"js-agent.newrelic.com/nr-spa-1216.min.js"},R=g&&y&&y[v]&&!/CriOS/.test(navigator.userAgent),O=e.exports={offset:a.getLastTimestamp(),now:a,origin:b,features:{},xhrWrappable:R,userAgent:u,disabled:x};if(!x){t(20),t(27),m[v]?(m[v]("DOMContentLoaded",i,p(!1)),h[v]("load",r,p(!1))):(m[w]("onreadystatechange",o),h[w]("onload",r)),s("mark",["firstbyte",a.getLastTimestamp()],null,"api");var T=0}},{}],"wrap-function":[function(t,e,n){function r(t,e){function n(e,n,r,c,f){function nrWrapper(){var i,a,u,p;try{a=this,i=d(arguments),u="function"==typeof r?r(i,a):r||{}}catch(l){o([l,"",[i,a,c],u],t)}s(n+"start",[i,a,c],u,f);try{return p=e.apply(a,i)}catch(h){throw s(n+"err",[i,a,h],u,f),h}finally{s(n+"end",[i,a,p],u,f)}}return a(e)?e:(n||(n=""),nrWrapper[p]=e,i(e,nrWrapper,t),nrWrapper)}function r(t,e,r,o,i){r||(r="");var s,c,f,u="-"===r.charAt(0);for(f=0;f<e.length;f++)c=e[f],s=t[c],a(s)||(t[c]=n(s,u?c+r:r,o,c,i))}function s(n,r,i,a){if(!h||e){var s=h;h=!0;try{t.emit(n,r,i,e,a)}catch(c){o([c,n,r,i],t)}h=s}}return t||(t=u),n.inPlace=r,n.flag=p,n}function o(t,e){e||(e=u);try{e.emit("internal-error",t)}catch(n){}}function i(t,e,n){if(Object.defineProperty&&Object.keys)try{var r=Object.keys(t);return r.forEach(function(n){Object.defineProperty(e,n,{get:function(){return t[n]},set:function(e){return t[n]=e,e}})}),e}catch(i){o([i],n)}for(var a in t)l.call(t,a)&&(e[a]=t[a]);return e}function a(t){return!(t&&t instanceof Function&&t.apply&&!t[p])}function s(t,e){var n=e(t);return n[p]=t,i(t,n,u),n}function c(t,e,n){var r=t[e];t[e]=s(r,n)}function f(){for(var t=arguments.length,e=new Array(t),n=0;n<t;++n)e[n]=arguments[n];return e}var u=t("ee"),d=t(32),p="nr@original",l=Object.prototype.hasOwnProperty,h=!1;e.exports=r,e.exports.wrapFunction=s,e.exports.wrapInPlace=c,e.exports.argsToArray=f},{}]},{},["loader",2,17,5,3,4]);</script><meta http-equiv="X-UA-Compatible" content="IE=edge,chrome=1" /><title>
	Ficha Licitación
</title>
        <script async src="https://www.googletagmanager.com/gtag/js?id=UA-51338325-2"></script>
        

    

    <script src="../../Includes/scripts/JQuery/jquery-1.7.2.min.js" type="text/javascript"></script>
    <script src="../../Includes/scripts/JQuery/jquery.blockUI.js" type="text/javascript"></script>
    <!-- Global Site Tag (gtag.js) - Google Analytics -->
    <!--<script async src="https://www.googletagmanager.com/gtag/js?id=UA-51338325-2"></script>-->
    <script src="../../Includes/scripts/analytics.js" type="text/javascript"></script>
    <script src="../../Includes/scripts/hotjar.js" type="text/javascript"></script>

    
    <link href="../../Includes/styles/FichaLight/style_principal.css" rel="stylesheet" type="text/css" /><link href="../../Includes/styles/FichaLight/textos.css" rel="stylesheet" type="text/css" /><link href="../../Includes/styles/FichaLight/estilo_tabla.css" rel="stylesheet" type="text/css" /><link href="../../Includes/styles/MOP/mop.css" rel="stylesheet" type="text/css" /><link rel="shortcut icon" href="/favicon.ico" />
    

    
    
    
    <script src="../../Includes/scripts/fancybox/v2.1.1/jquery.fancybox.pack.js" type="text/javascript"></script>
    <link href="../../Includes/scripts/fancybox/v2.1.1/jquery.fancybox.css" rel="stylesheet" type="text/css" />
    <script src="../../Includes/scripts/geo-cgr.js?v=1" type="text/javascript"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jszip/3.1.4/jszip.min.js" type="text/javascript"></script>
    <script type="text/javascript" src="https://fastcdn.org/FileSaver.js/1.1.20151003/FileSaver.js"></script>
    <script type="text/javascript">        

        function init() {
            document.addEventListener('evento-inter-direccion-ficha',
            function (event) {
                document.getElementById("lblFicha2Direccion").innerHTML = event.detail.direccion;
                var parametros = "?rbhCode=" + event.detail.codigo;
                parametros += "&direccion=" + encodeURIComponent(event.detail.direccion);
                var strURL = event.detail.url + parametros;
                document.getElementById("lnkFicha2EditarDireccion").setAttribute("href", strURL);
            },
                false);
            document.addEventListener('evento-inter-monto-estimado',
                function (event) {
                    document.getElementById("lblFicha7MontoEstimado").innerHTML = event.detail.monto;
                    var parametros = "?rbhCode=" + event.detail.codigo;
                    parametros += "&rbhTypeLC=" + event.detail.tipoLC;
                    parametros += "&montoLC=" + event.detail.monto;
                    parametros += "&moneda=" + event.detail.moneda;
                    var strURL = event.detail.url + parametros;
                    document.getElementById("lnkFicha7MontoEstimado").setAttribute("href", strURL);
                },
                false);
            document.addEventListener('evento-inter-fecha-licitacion',
                function (event) {
                    document.getElementById("lblFicha3Inicio").innerHTML = event.detail.fechainiciopregunta;
                    document.getElementById("lblFicha3Fin").innerHTML = event.detail.fechafinalpreguntas;
                    document.getElementById("lblFicha3PublicacionRespuestas").innerHTML = event.detail.fechapublicacionrespuesta;
                    document.getElementById("lblFicha3ActoAperturaTecnica").innerHTML = event.detail.fechaaperturatecnica;
                    document.getElementById("lblFicha3ActoAperturaEconomica").innerHTML = event.detail.fechaaperturaeconomica;
                    //document.getElementById("lblFicha3Adjudicacion").innerHTML = event.detail.fechaAdjudicacion;
                    document.getElementById("lblFicha3SoporteFisico").innerHTML = event.detail.fechaentregasoporte;
                    document.getElementById("lblFicha3FirmaContrato").innerHTML = event.detail.fechaestimadafirma;
                    document.getElementById("lblFicha3EvaluacionOfertas").innerHTML = event.detail.tiempoestimadoevaluacion;
                    var parametros = "?rbhCode=" + event.detail.codigo;
                    var strURL = event.detail.url + parametros;
                    document.getElementById("lnkEditarFechas").setAttribute("href", strURL);
                },
                false);
        }
        function OpenValidationMessagePopup() {
            var alink = document.getElementById("hiddenlink_confirm");
            alink.click();
        }
        $(document).ready(function () {
            init();
            $("td").removeAttr("noWrap");

            $("#imgRegistro").removeClass('fancy');
            $("#imgCuadroOferta").removeClass('cuadroOferta');


            $(".fancy").fancybox({
                width: '60%',
                height: '60%',
                fitToView: false,
                autoSize: false,
                closeClick: false,
                type: 'iframe',
                padding: 0,
                keys: null,
                helpers: { overlay: { closeClick: false } }
            });

            $(".fancyAdjunto").fancybox({
                'width': '58%',
                'height': '30%',
                'autoScale': false,
                'transitionIn': 'fade',
                'transitionOut': 'fade',
                'type': 'iframe',
                'overlayOpacity': 0.9,
                hideOnOverlayClick: false
            });
            $(".fancyFechas").fancybox({
                'width': '58%',
                'height': '30%',
                'autoScale': false,
                'transitionIn': 'fade',
                'transitionOut': 'fade',
                'type': 'iframe',
                'overlayOpacity': 0.9,
                hideOnOverlayClick: false
            });

            $(".cuadroOferta").fancybox({
                width: '90%',
                heigh: '90%',
                autoSize: false,
                'autoScale': false,
                'transitionIn': 'fade',
                'transitionOut': 'fade',
                'type': 'iframe',
                'overlayOpacity': 0.9,
                hideOnOverlayClick: false
            });

            $(".ofertarFB").fancybox({
                'width': 440,
                'height': 290,
                'autoScale': false,
                'transitionIn': 'none',
                'transitionOut': 'none',
                'type': 'iframe',
                'scrolling': 'no',
                hideOnOverlayClick: false
            });

            $(".fancyNBA").fancybox({
                'width': 800,
                'height': 1150,
                'autoScale': false,
                'transitionIn': 'fade',
                'transitionOut': 'fade',
                'type': 'iframe',
                'overlayOpacity': 0.9,
                hideOnOverlayClick: false
            });

            $(".fancyMontoLC").fancybox({
                'width': '58%',
                'height': '30%',
                'autoScale': false,
                'transitionIn': 'fade',
                'transitionOut': 'fade',
                'type': 'iframe',
                'overlayOpacity': 0.9,
                hideOnOverlayClick: false
            });
            //Solución para eliminar texto: "I18n entry not found:" En paso 5 Requisitos para contratar al proveedor adjudicado.
            //Obtener los textos para modificar su valor.
            $("span[id*=lblDocument]").each(function (index) {
                //Reemplazar el texto.
                var value = $(this).text().replace("I18n entry not found: ", "");
                //Incorporar el cambio en el control Label.
                $(this).text(value);
            })

        });
    </script>

    <script type="text/javascript">
    $(document).ready(function () {
        $(".fancyFechas").fancybox({
            'width': 700,
            'height': 600,
            'autoScale': false,
            'transitionIn': 'fade',
            'transitionOut': 'fade',
            'type': 'iframe',
            'overlayOpacity': 0.9,
            'hideOnOverlayClick': false
        });   
        });
    </script>
    <script type="text/javascript">
    $(document).ready((function () {
        $(".fancyMonto").fancybox({
            'title': 'Editar monto de licitación',
            'width': 700,
            'height': 600,
            'autoScale': false,
            'transitionIn': 'fade',
            'transitionOut': 'fade',
            'type': 'iframe',
            'overlayOpacity': 0.9,
            'hideOnOverlayClick': false
        });
        $("#hidden_link").fancybox().trigger('click');
     });
    </script>

    <script type="text/javascript">

        function openPopupFicha(obj) {
            var url = $(obj).attr("href");
            console.log(url);
            radopen(url, "PopupFicha");
        }

        function openPopupCHP(obj) {
            var url = $(obj).attr("href");
            window.open(url, "", "width=850,height=700,scrollbars=yes,resizable=yes");
        }

        function BloquearFicha(titulo, msg) {

            $("#bTitulo").html(titulo);
            $("#lblTextoCuerpo").html(msg);

            $.blockUI({
                message: '', css: {
                    border: 'none',
                    height: '1px',
                    width: '0px',
                    padding: '0px 0px 0px',
                    top: '35%',
                    left: '28%'
                }
            });

            $("#frmABM_Productos").hide();
            alert(msg);

            location.href = location.protocol + '//' + location.hostname + '/portal'
        }

        function cerrarpagina() {
            window.open('', '_parent', '');
            window.close();
            window.event.returnValue = false;
            //return false;
        }


        function cargarEspecialidades() {
            var totRegistros = 0;
            $.ajax({
                type: 'POST',
                url: 'DetailsAcquisition.aspx/ObtenerEspecialidades',
                contentType: "application/json; charset=utf-8",
                async: false,
                datatype: 'json',
                success: function (result) {
                    if (result.d.length > 0) {
                        totRegistros = result.d.length;
                        $("#tblEspecialidades tbody tr td").remove();
                        $.each(result.d, function (i, item) {
                            var dato = item.Descripcion;
                            var datos = dato.split("|");
                            var especialidad = datos[0];
                            var subespecialidad = datos[1];
                            var categoria = datos[2];
                            var id = 'sc_' + item.CodigoProducto + '_';
                            if ($('#tblEspecialidades tbody tr').length == 0) {
                                $('#tblEspecialidades tbody').append('<tr id="' + id + '" ><td>' + especialidad + '</td><td>' + subespecialidad + '</td><td>' + categoria + '</td> </tr>');
                            }
                            else {
                                $('#tblEspecialidades tr:last').after('<tr id="' + id + '" ><td>' + especialidad + '</td><td>' + subespecialidad + '</td><td>' + categoria + '</td> </tr>');
                            }
                        });

                    }
                },
                error: function (xhr, textStatus, exceptionThrown) {
                    var obj = JSON.parse(xhr.responseText);
                    alert(obj.data);
                    return null;
                }
            });

            if (totRegistros > 0) {
                $('#tblEspecialidades').DataTable({
                    "paging": (totRegistros <= 5) ? false : true,
                    "bSort": false,
                    "bFilter": false,
                    "bInfo": false,
                    "bLengthChange": false,
                    "pageLength": 5,
                    "language": {
                        "oPaginate": {
                            "sFirst": "&laquo;&laquo;",
                            "sLast": "&raquo&raquo",
                            "sNext": "&raquo;",
                            "sPrevious": "&laquo;"
                        }
                    }
                });
            }
        }

        function abrirFancyOrg(p_rut, p_clave, p_url, p_sigueLic, p_sessionId, p_seguimiento, p_externalCode, p_intCode) {
            $.fancybox({
                width: '40%',
                height: '60%',
                'autoScale': false,
                'transitionIn': 'none',
                'transitionOut': 'none',
                'type': 'iframe',
                'scrolling': 'no',
                hideOnOverlayClick: false,
                href: '/Portal/LoginOrganizaciones.aspx?rut=' + p_rut + '&clave=' + p_clave + '&url=' + p_url + '&sigueLic=' + p_sigueLic + '&session=' + p_sessionId + '&seguimiento=' + p_seguimiento + '&externalCode=' + p_externalCode + '&intCode=' + p_intCode
            });
        }

        function toContractSheet(idContrato, esPublico, idContratoEncriptado) {
            if (esPublico == "True") {               
                window.opener.location = '/Contratos/Ciudadania/DetalleContrato?qs=' + idContratoEncriptado;
                window.close();
            }
            else {
                window.opener.location = '/Contratos/GestionContratos/DetalleContrato?idContrato=' + idContrato;
                window.close();
            }
        }       

        function toCreateContract(idLicitacion) {            
            window.opener.location = '/Contratos/Comprador/ElaborarFichaDesdeDocumento?idDocumento=' + idLicitacion + '&tipoDocumento=LC';
            window.close();
        }

    </script>


    <script type="text/javascript" src="https://apis.google.com/js/plusone.js"></script>

    <style type="text/css">
        .tituloCriterioIzq {
            text-align: left !important;
        }

        .tituloCriterio {
            text-align: left !important;
        }

        ul li {
            margin-top: 1.8px !important;
        }

        .modal-open {
            overflow: hidden;
        }

        .modal {
            position: fixed;
            top: 0;
            right: 0;
            bottom: 0;
            left: 0;
            z-index: 1050;
            display: none;
            overflow: hidden;
            -webkit-overflow-scrolling: touch;
            outline: 0;
        }

        .modal-dialog {
            position: relative;
            width: auto;
            margin: 10px;
        }

        .modal-content {
            position: relative;
            background-color: #fff;
            -webkit-background-clip: padding-box;
            background-clip: padding-box;
            border: 1px solid #999;
            border: 1px solid rgba(0, 0, 0, .2);
            border-radius: 6px;
            outline: 0;
            -webkit-box-shadow: 0 3px 9px rgba(0, 0, 0, .5);
            box-shadow: 0 3px 9px rgba(0, 0, 0, .5);
        }

        .modal-header {
            min-height: 16.42857143px;
            padding: 15px;
            border-bottom: 1px solid #e5e5e5;
        }

        .modal-title {
            margin: 0;
            line-height: 1.42857143;
        }

        .modal-body {
            position: relative;
            padding: 15px;
        }

        @media (min-width: 768px) {
            .modal-dialog {
                width: 600px;
                margin: 30px auto;
            }

            .modal-content {
                -webkit-box-shadow: 0 5px 15px rgba(0, 0, 0, .5);
                box-shadow: 0 5px 15px rgba(0, 0, 0, .5);
            }

            .modal-sm {
                width: 300px;
            }
        }

        .modal-footer {
            padding: 15px;
            text-align: right;
            border-top: 1px solid #e5e5e5;
        }

        .btn-primary {
            color: #fff;
            background-color: #428bca;
            border-color: #357ebd;
        }

        .btn {
            display: inline-block;
            padding: 6px 12px;
            margin-bottom: 0;
            font-size: 14px;
            font-weight: normal;
            line-height: 1.42857143;
            text-align: center;
            white-space: nowrap;
            vertical-align: middle;
            cursor: pointer;
            -webkit-user-select: none;
            -moz-user-select: none;
            -ms-user-select: none;
            user-select: none;
            background-image: none;
            border: 1px solid transparent;
            border-radius: 4px;
        }

            .btn:focus,
            .btn:active:focus,
            .btn.active:focus {
                outline: thin dotted;
                outline: 5px auto -webkit-focus-ring-color;
                outline-offset: -2px;
            }

            .btn:hover,
            .btn:focus {
                color: #333;
                text-decoration: none;
            }

            .btn:active,
            .btn.active {
                background-image: none;
                outline: 0;
                -webkit-box-shadow: inset 0 3px 5px rgba(0, 0, 0, .125);
                box-shadow: inset 0 3px 5px rgba(0, 0, 0, .125);
            }

        .alert.alerta-info {
            background-color: #E7F0F8;
            border-color: #83b3DA;
        }

        .alert {
            padding: 16px 16px 16px 54px;
            margin: 0 0 10px 0;
            min-height: 53px;
            border-radius: 0;
            border-width: 0 0 0 4px;
            border-style: solid;
        }
    </style>
    
    <!-- Modificación de Ficha Licitación -->
    <style>
        .img-csv img {
            position: absolute;
            display: inline;
            background: #f00;
            width: 25px;
            height: 25px;
            float: right;
            margin: 0 0 0 0;
            z-index: 3;
        }

        .img-api img {
            position: absolute;
            display: inline;
            background: #0f0;
            width: 25px;
            height: 25px;
            float: right;
            margin: 0 0 0 90px;
            z-index: 3;
        }

        .img-ocds img {
            position: absolute;
            display: inline;
            background: #00f;
            width: 25px;
            height: 25px;
            float: right;
            margin: 0 0 0 180px;
            z-index: 3;
        }

        .links-descargas-archivo {
            position: absolute;
            background-color: rgba(255, 247, 228, 0);
            top: 182px;
            left: 50vw;
            margin: 0 0 0 230px;
            z-index: 9999;
            padding: 0px;
            width: 105px;
            height: 25px;
            z-index: 3;
        }

        .img-csv {
            position: relative;
            width: 25px;
            z-index: 3;
        }

        .img-api {
            position: relative;
            width: 25px;
            z-index: 3;
        }

        .img-ocds {
            position: relative;
            width: 25px;
            z-index: 3;
        }
    </style>
    <!-- Popover iconos descarga -->

    <style>
        .popover__title {
        }

        .popover__wrapper {
            position: absolute;
            margin-top: 0px;
            margin-left: 0px;
            display: inline-block;
        }

        .popover__wrapper2 {
            position: absolute;
            margin-top: 0px;
            margin-left: 30px;
            display: inline-block;
        }

        .popover__wrapper3 {
            position: absolute;
            margin-top: 0px;
            margin-left: 60px;
            display: inline-block;
        }


        .popover__content {
            opacity: 0;
            visibility: hidden;
            position: relative;
            z-index: 9999999 !important;
            top: 30px;
            left: -97px !important;
            transform: translate(0,10px);
            background-color: #ffffff;
            padding: 5px 0px;
            border: 1px solid #c5cad2;
            /*box-shadow: 0 2px 5px 0 rgba(0, 0, 0, 0.26);*/
            width: 220px;
            font-family: inherit;
            color: inherit;
        }

            .popover__content:before, .popover__content2:before, .popover__content3:before {
                position: absolute;
                z-index: -1;
                content: '';
                right: calc(50% - 10px);
                top: -8px;
                border-style: solid;
                border-width: 0 10px 10px 10px;
                border-color: transparent transparent #c5cad2 transparent;
                transition-duration: 0.3s;
                transition-property: transform;
            }

        .popover__content2 {
            opacity: 0;
            visibility: hidden;
            position: relative;
            z-index: 9999999 !important;
            top: 30px;
            left: -97px !important;
            transform: translate(0,10px);
            background-color: #ffffff;
            padding: 5px 0px;
            border: 1px solid #c5cad2;
            /*box-shadow: 0 2px 5px 0 rgba(0, 0, 0, 0.26);*/
            width: 220px;
        }


        .popover__content3 {
            opacity: 0;
            visibility: hidden;
            position: relative;
            z-index: 9999999 !important;
            top: 30px;
            left: -97px !important;
            transform: translate(0,10px);
            background-color: #ffffff;
            padding: 5px 0px;
            border: 1px solid #c5cad2;
            /*box-shadow: 0 2px 5px 0 rgba(0, 0, 0, 0.26);*/
            width: 220px;
        }


        .popover__wrapper:hover .popover__content, .popover__wrapper2:hover .popover__content2, .popover__wrapper3:hover .popover__content3 {
            z-index: 999999 !important;
            opacity: 1;
            visibility: visible;
            transform: translate(0,-20px);
            transition: all 0.5s cubic-bezier(0.75, -0.02, 0.2, 0.97);
        }

        .popover__message {
            position: relative;
            width: 200px;
            margin: auto;
            text-align: justify;
            z-index: 999999 !important;
            padding: 5px 0 5px 0 !important;
            font-family: inherit;
            color: inherit;
            font-size: 13px;
            line-height: 16px;
        }

            .popover__message a {
                color: #0667b4;
                text-decoration: none;
                font-weight: 400;
            }
    </style>

<link href="../../Includes/styles/ChileCompra.css" type="text/css" rel="stylesheet" /><script id="ChileCompra" src="/Procurement/Includes/scripts/ChileCompra.js" type="text/javascript"></script><link href="/Procurement/WebResource.axd?d=OIS7CaKxZTe92Q8L0RKIYEXo5lJPeHuW840p1g1kxhFo7sVpAIkNCjrrpnlh1EeLkh1gAku4KGtnMa6q8dbqJW_djuQuZArMst1-m3X_uFZgnjHALGgqA815dWQ1&amp;t=637903994436919470" type="text/css" rel="stylesheet" class="Telerik_stylesheet" /><link href="/Procurement/WebResource.axd?d=86ZWE_2tbdKxTiTiTVSKyWxLQRAAt_cwdObySGeh0iQUxvF8HN_5DgkluObxD0hxEW94p-HJ7pwyDUZ3x6YwAa-pY6YJtRoQApFnoR4TGwk6h6sag38KoX_PVToEWCzm4G8rR5MURZQC-8W0jzbvFBZ_VaE1&amp;t=637903994436919470" type="text/css" rel="stylesheet" class="Telerik_stylesheet" /></head>
<body>
    <form name="frmABM_Productos" method="post" action="./DetailsAcquisition.aspx?qs=HExBybQcp6dmvJhmRUuEkqVjJod83EyleQDUrMofh1xghQ3cJDUqrNtW+Yu5Erpo" id="frmABM_Productos">
<div>
<input type="hidden" name="RadScriptManager1_TSM" id="RadScriptManager1_TSM" value="" />
<input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="" />
<input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="" />
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="/wEPDwUKMTEwMjcyMzI4Nw8WAh4NRW50TGljaXRhY2lvbjLWyAEAAQAAAP////8BAAAAAAAAAAwCAAAARldlYi5Qcm9jdXJlbWVudCwgVmVyc2lvbj0xLjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPW51bGwMAwAAAEFNUC5OZWdvY2lvLCBWZXJzaW9uPTEuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49bnVsbAUBAAAAJVdlYi5Qcm9jdXJlbWVudC5GaWNoYUxpY2l0YWNpb25FbnRpdHlcAAAAClVzZXJFbnRpdHkHX2NvZGlnbw5fY29kaWdvRXh0ZXJubwxfcmVzcG9uc2FibGUMX2ZlY2hhY2llcnJlD19jb250YWRvcmNpZXJyZQpfaW5mb3JtYWRhD19jb2RpZ29UZW1wbGF0ZRRfdGlwb0VzcGVjaWFsaWRhZE1PUBxfZXNwZWNpYWxpZGFkZXNNT1BSZXF1ZXJpZGFzB19ub21icmUNX2NvZGlnb2VzdGFkbwtfdGlwb0VzdGFkbwdfZXN0YWRvDF9kZXNjcmlwY2lvbg9fdGlwb0xpY2l0YWNpb24SX3N1YlRpcG9MaWNpdGFjaW9uFV9jb2RpZ29UaXBvTGljaXRhY2lvbhhfY29kaWdvU3ViVGlwb0xpY2l0YWNpb24dX3N1YlRpcG9MaWNpdGFjaW9uRGVzY3JpcGNpb24TX2NvZGlnb0NvbnZvY2F0b3JpYQ1fY29udm9jYXRvcmlhB19tb25lZGEHX2V0YXBhcw1fZXN0YWRvRXRhcGFzCV9jb250cmF0bxBfY29kaWdvVG9tYVJhem9uGF9jb2RpZ29QdWJsaWNpZGFkT2ZlcnRhcxhfanVzdGlmaWNhY2lvblB1YmxpY2lkYWQcX2p1c3RpZmljYWNpb25SZWFkanVkaWNhY2lvbhVfb3BjaW9uUmVhZGp1ZGljYWNpb24TX2NvZGlnb09yZ2FuaXphY2lvbgxfcmF6b25zb2NpYWwHX3VuaWRhZARfcnV0Cl9kaXJlY2Npb24HX2NvbXVuYQdfcmVnaW9uCV9yZWNsYW1vcwtfZXN0aW1hY2lvbg9fZmluYW5jaWFtaWVudG8RX3Zpc2liaWxpZGFkTW9udG8OX21vbnRvRXN0aW1hZG8bX2p1c3RpZmljYWNpb25Nb250b0VzdGltYWRvDF9vYnNlcnZhY2lvbgpfbW9kYWxpZGFkCV9vcGNpb25lcxZfbm9tYnJlUmVzcG9uc2FibGVQYWdvFV9lbWFpbFJlc3BvbnNhYmxlUGFnbxpfbm9tYnJlUmVzcG9uc2FibGVDb250cmF0bxlfZW1haWxSZXNwb25zYWJsZUNvbnRyYXRvHF90ZWxlZm9ub1Jlc3BvbnNhYmxlQ29udHJhdG8bX3Byb2hpYmljaW9uc3ViY29udHJhdGFjaW9uEF9zdWJjb250cmF0YWNpb24RX2R1cmFjaW9uQ29udHJhdG8PX3RpZW1wb0NvbnRyYXRvH19qdXN0aWZpY2FjaW9uQ29udHJhdG9SZW5vdmFibGUYX29wdGlvbkNvbnRyYXRvUmVub3ZhYmxlG19qdXN0aWZpY2FjaW9uRXh0aWVuZGVQbGF6bwVfZXNMUw9fZXNQdWJsaWNvTW9udG8WX2NhbnRpZGFkZmVjaGFzVXN1YXJpbxNfdGllbmVGZWNoYXNVc3VhcmlvC19lcnJvckZpY2hhCV9lc3RhZG9DUw9fRXh0ZW5zaW9uUGxhem8RX1JlZ2xhbWVudG9BY3Rpdm8GX2VzTW9wD19lc0NvbnRyYXRvT2JyYRFib29sRXNPZmVydGFDaWVnYRtib29sRXNBcnF1aXRlY3R1cmFVcmJhbmlzbW8GX2l0ZW1zDV9hbnRlY2VkZW50ZXMLX3JlcXVpc2l0b3MKX2NyaXRlcmlvcwxfY3JpdGVyaW9zTFMKX2dhcmFudGlhcwpfY2xhdXN1bGFzDl9vYnNlcnZhY2lvbmVzB19mZWNoYXMJX2ZlY2hhc0xTDl9mZWNoYXNVc3VhcmlvCV9lc1ZhbGlkYQtfZXNCYXNlVGlwbxZfX1ZlcmlmaWNhSGFiaWxpZGFkQ0hQFV9UaXBvRHVyYWNpb25Db250cmF0bxdfdGllbXBvRHVyYWNpb25Db250cmF0bx1fVW5pZGFkVGllbXBvRHVyYWNpb25Db250cmF0bxVfVW5pZGFkVGllbXBvQ29udHJhdG8WX1ZhbG9yVGllbXBvUmVub3ZhY2lvbhhfUGVyaW9kb1RpZW1wb1Jlbm92YWNpb24MX0VzUmVub3ZhYmxlBAABAQEAAQAAAAEABAEBAQQAAAEAAQEAAAAAAAEBAAEBAQEBAQEBAQEEAQEBAQQBAQEBAQEEAAABAAEAAAAAAQAAAAAAAAADBAQDAwMDBAQEAwAAAAEBAQEBAQEnTVAuTmVnb2Npby5DaGlsZUNvbXByYVdlYi5FbnRpdGllcy5Vc2VyAwAAAAgICAgBCCdNUC5OZWdvY2lvLlV0aWxzLkFwcEVudW1zK1JGQlN0YXR1c0VudW0DAAAAN01QLk5lZ29jaW8uVXRpbHMuQXBwRW51bXMrUHJvY3VyZW1lbnRQcm9jZXNzU3ViVHlwZUVudW0DAAAACAgICAgICAgISU1QLk5lZ29jaW8uQ2hpbGVDb21wcmFXZWIuVXRpbHMuQXBwQ29uc3RhbnRzRW51bUZpY2hhTGlnaHQrVmFsb3JSZXF1aXNpdG8DAAAASE1QLk5lZ29jaW8uQ2hpbGVDb21wcmFXZWIuVXRpbHMuQXBwQ29uc3RhbnRzRW51bUZpY2hhTGlnaHQrT3BjaW9uZXNQYWdvcwMAAABKTVAuTmVnb2Npby5DaGlsZUNvbXByYVdlYi5VdGlscy5BcHBDb25zdGFudHNFbnVtRmljaGFMaWdodCtTdWJDb250cmF0YWNpb24DAAAACAgIAQEIAQgICAEBAQGWAVN5c3RlbS5Db2xsZWN0aW9ucy5HZW5lcmljLkxpc3RgMVtbV2ViLlByb2N1cmVtZW50LkZpY2hhSXRlbUxpY2l0YWNpb25FbnRpdHksIFdlYi5Qcm9jdXJlbWVudCwgVmVyc2lvbj0xLjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPW51bGxdXTFXZWIuUHJvY3VyZW1lbnQuRmljaGFMaWNpdGFjaW9uQW50ZWNlZGVudGVzRW50aXR5AgAAAChXZWIuUHJvY3VyZW1lbnQuRmljaGFMaWNpdGFjaW9uUmVxdWlzaXRvAgAAAJkBU3lzdGVtLkNvbGxlY3Rpb25zLkdlbmVyaWMuTGlzdGAxW1tXZWIuUHJvY3VyZW1lbnQuRW50aXRpZXMuQXdhcmRDcml0ZXJpYUVudGl0eSwgV2ViLlByb2N1cmVtZW50LCBWZXJzaW9uPTEuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49bnVsbF1dmQFTeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYy5MaXN0YDFbW1dlYi5Qcm9jdXJlbWVudC5FbnRpdGllcy5Bd2FyZENyaXRlcmlhRW50aXR5LCBXZWIuUHJvY3VyZW1lbnQsIFZlcnNpb249MS4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1udWxsXV2PAVN5c3RlbS5Db2xsZWN0aW9ucy5HZW5lcmljLkxpc3RgMVtbV2ViLlByb2N1cmVtZW50LkVudGl0aWVzLkd1YXJhbnRlZSwgV2ViLlByb2N1cmVtZW50LCBWZXJzaW9uPTEuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49bnVsbF1dkgFTeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYy5MaXN0YDFbW1dlYi5Qcm9jdXJlbWVudC5FbnRpdGllcy5DbGF1c2VFbnRpdHksIFdlYi5Qcm9jdXJlbWVudCwgVmVyc2lvbj0xLjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPW51bGxdXTRXZWIuUHJvY3VyZW1lbnQuRW50aXRpZXMuTGVnYWxQcmVjZWRlbnRDb21tZW50RW50aXR5AgAAACZXZWIuUHJvY3VyZW1lbnQuRmVjaGFzTGljaXRhY2lvbkVudGl0eQIAAAAoV2ViLlByb2N1cmVtZW50LkZlY2hhc0xpY2l0YWNpb25MU0VudGl0eQIAAACeAVN5c3RlbS5Db2xsZWN0aW9ucy5HZW5lcmljLkxpc3RgMVtbV2ViLlByb2N1cmVtZW50LkVudGl0aWVzLkRhdGVzRGVmaW5lZEJ5VXNlckVudGl0eSwgV2ViLlByb2N1cmVtZW50LCBWZXJzaW9uPTEuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49bnVsbF1dAQEBAgAAAArxYIkABgQAAAAMMjE3OS0zMC1MUDIyBgUAAABOQ09SUCBBRE1JTklTVFJBVElWQSBERUwgUE9ERVIgSlVESUNJQUwsIENvcnAuIEFkbS4gZGVsIFBvZGVyIEp1ZGljaWFsIC0gVGVtdWNvCg8AAAAGBgAAAAVGYWxzZf////8AAAAAAAYHAAAAMFVOSUZJQ0FDSU9OIERFIEVNUEFMTUVTIEVESUZJQ0lPUyBQT0RFUiBKVURJQ0lBTAUAAAAF+P///ydNUC5OZWdvY2lvLlV0aWxzLkFwcEVudW1zK1JGQlN0YXR1c0VudW0BAAAAB3ZhbHVlX18ACAMAAAAFAAAABgkAAAAJUHVibGljYWRhBgoAAADBAVVOSUZJQ0FDSU9OIERFIEVNUEFMTUVTIEVESUZJQ0lPUyBERSBDT1JURSBBUEVMQUNJT05FUywgSlVaR0FETyBERSBHQVJBTlTDjUEgWSBUUklCVU5BTCBERSBKVUlDSU8gT1JBTCBFTiBMTyBQRU5BTCBERSBURU1VQ08gUEFSQSBPUFRBUiBBIFRBUklGQSBERSBDTElFTlRFIExJQlJFIFBBUkEgU1VNSU5JU1RSTyBERSBFTEVDVFJJQ0lEQUQGCwAAABdSRkJfUFJPQ0VTU19UWVBFX1BVQkxJQwX0////N01QLk5lZ29jaW8uVXRpbHMuQXBwRW51bXMrUHJvY3VyZW1lbnRQcm9jZXNzU3ViVHlwZUVudW0BAAAAB3ZhbHVlX18ACAMAAAADAAAAAQAAAAMAAAAGDQAAABZSRkJfUFJPQ0VTU19TVUJUWVBFX0xQAQAAAAoGDgAAAAxQZXNvIENoaWxlbm8BAAAAAAAAAAAAAAAAAAAAAQAAAAYPAAAAAAYQAAAAogRTaSBlbCByZXNwZWN0aXZvIGFkanVkaWNhdGFyaW8gc2UgZGVzaXN0ZSBkZSBzdSBvZmVydGEsIG5vIGVudHJlZ2EgbG9zIGFudGVjZWRlbnRlcyBsZWdhbGVzIHBhcmEgY29udHJhdGFyIHkvbyBsYSBnYXJhbnTDrWEgZGUgZmllbCBjdW1wbGltaWVudG8sIG5vIGZpcm1hIGVsIGNvbnRyYXRvIG8gbm8gc2UgaW5zY3JpYmUgZW4gQ2hpbGVwcm92ZWVkb3JlcyBlbiBsb3MgcGxhem9zIHF1ZSBzZSBlc3RhYmxlY2VuIGVuIGxhcyBwcmVzZW50ZXMgYmFzZXMsIGxhIGVudGlkYWQgbGljaXRhbnRlIHBvZHLDoSBkZWphciBzaW4gZWZlY3RvIGxhIGFkanVkaWNhY2nDs24geSBzZWxlY2Npb25hciBhbCBvZmVyZW50ZSBxdWUsIGRlIGFjdWVyZG8gYWwgcmVzdWx0YWRvIGRlIGxhIGV2YWx1YWNpw7NuIGxlIHNpZ2EgZW4gcHVudGFqZSwgeSBhc8OtIHN1Y2VzaXZhbWVudGUsIGEgbWVub3MgcXVlLCBkZSBhY3VlcmRvIGEgbG9zIGludGVyZXNlcyBkZWwgc2VydmljaW8sIHNlIGVzdGltZSBjb252ZW5pZW50ZSBkZWNsYXJhciBkZXNpZXJ0YSBsYSBsaWNpdGFjacOzbi4BAAAABhEAAAAEMzE3NAYSAAAAJkNPUlAgQURNSU5JU1RSQVRJVkEgREVMIFBPREVSIEpVRElDSUFMBhMAAAAmQ29ycC4gQWRtLiBkZWwgUG9kZXIgSnVkaWNpYWwgLSBUZW11Y28GFAAAAAw2MC4zMDEuMDAxLTkGFQAAAA9DQVVQT0xJQ0FOIDEwNzcGFgAAAAZUZW11Y28GFwAAABlSZWdpw7NuIGRlIGxhIEFyYXVjYW7DrWEgBhgAAAACMjcGGQAAAC1SRkJfRVNUSU1BVElPTl9UWVBFX0JBU0VfRVNUSU1BVElPTl9BVkFJTEFCTEUJDwAAAAXl////SU1QLk5lZ29jaW8uQ2hpbGVDb21wcmFXZWIuVXRpbHMuQXBwQ29uc3RhbnRzRW51bUZpY2hhTGlnaHQrVmFsb3JSZXF1aXNpdG8BAAAAB3ZhbHVlX18ACAMAAAAAAAAABhwAAAAINzE2Njk1MzQJDwAAAAkPAAAABh4AAAAjUkZCX0NPTlRSQUNUX1BBWU1FTlRfTUVUSE9EXzMwX0RBWVMF4f///0hNUC5OZWdvY2lvLkNoaWxlQ29tcHJhV2ViLlV0aWxzLkFwcENvbnN0YW50c0VudW1GaWNoYUxpZ2h0K09wY2lvbmVzUGFnb3MBAAAAB3ZhbHVlX18ACAMAAAABAAAABiAAAAAPUEFUUklDSUEgTVXDkU9aBiEAAAAPUEFNVU5PWkBQSlVELkNMBiIAAAAZQ0xBVURJTyBTT0JBUlpPIE5BVkFSUkVURQYjAAAAEUNFU09CQVJaT0BQSlVELkNMBiQAAAAONTYtNDUtMjIzNTQyNS0JDwAAAAXa////Sk1QLk5lZ29jaW8uQ2hpbGVDb21wcmFXZWIuVXRpbHMuQXBwQ29uc3RhbnRzRW51bUZpY2hhTGlnaHQrU3ViQ29udHJhdGFjaW9uAQAAAAd2YWx1ZV9fAAgDAAAAAAAAAAAAAAAAAAAACQ8AAAAAAAAACQ8AAAAAAAEAAAABCgEAAAAAAAAAAQAAAAAAAAAJJwAAAAkoAAAACSkAAAAJKgAAAAkrAAAACSwAAAAJLQAAAAkuAAAACS8AAAAJMAAAAAkxAAAAAQAACQ8AAAAJDwAAAAYzAAAAFVJGQl9USU1FX1BFUklPRF9IT1VSUwY0AAAAFVJGQl9USU1FX1BFUklPRF9IT1VSUwY1AAAAATAJDwAAAAkGAAAABCcAAACWAVN5c3RlbS5Db2xsZWN0aW9ucy5HZW5lcmljLkxpc3RgMVtbV2ViLlByb2N1cmVtZW50LkZpY2hhSXRlbUxpY2l0YWNpb25FbnRpdHksIFdlYi5Qcm9jdXJlbWVudCwgVmVyc2lvbj0xLjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPW51bGxdXQMAAAAGX2l0ZW1zBV9zaXplCF92ZXJzaW9uBAAAK1dlYi5Qcm9jdXJlbWVudC5GaWNoYUl0ZW1MaWNpdGFjaW9uRW50aXR5W10CAAAACAgJOAAAAAEAAAABAAAABSgAAAAxV2ViLlByb2N1cmVtZW50LkZpY2hhTGljaXRhY2lvbkFudGVjZWRlbnRlc0VudGl0eQUAAAAQX2FkbWluaXN0cmF0aXZvcwlfdGVjbmljb3MLX2Vjb25vbWljb3MRX3RlY25pY29zUHJpdmFkb3MRX3RlY25pY29zUHVibGljb3MDAwMDA50BU3lzdGVtLkNvbGxlY3Rpb25zLkdlbmVyaWMuTGlzdGAxW1tXZWIuUHJvY3VyZW1lbnQuRW50aXRpZXMuQW50ZWNlZGVudGVPZmVydGFFbnRpdHksIFdlYi5Qcm9jdXJlbWVudCwgVmVyc2lvbj0xLjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPW51bGxdXZ0BU3lzdGVtLkNvbGxlY3Rpb25zLkdlbmVyaWMuTGlzdGAxW1tXZWIuUHJvY3VyZW1lbnQuRW50aXRpZXMuQW50ZWNlZGVudGVPZmVydGFFbnRpdHksIFdlYi5Qcm9jdXJlbWVudCwgVmVyc2lvbj0xLjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPW51bGxdXZ0BU3lzdGVtLkNvbGxlY3Rpb25zLkdlbmVyaWMuTGlzdGAxW1tXZWIuUHJvY3VyZW1lbnQuRW50aXRpZXMuQW50ZWNlZGVudGVPZmVydGFFbnRpdHksIFdlYi5Qcm9jdXJlbWVudCwgVmVyc2lvbj0xLjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPW51bGxdXZ0BU3lzdGVtLkNvbGxlY3Rpb25zLkdlbmVyaWMuTGlzdGAxW1tXZWIuUHJvY3VyZW1lbnQuRW50aXRpZXMuQW50ZWNlZGVudGVPZmVydGFFbnRpdHksIFdlYi5Qcm9jdXJlbWVudCwgVmVyc2lvbj0xLjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPW51bGxdXZ0BU3lzdGVtLkNvbGxlY3Rpb25zLkdlbmVyaWMuTGlzdGAxW1tXZWIuUHJvY3VyZW1lbnQuRW50aXRpZXMuQW50ZWNlZGVudGVPZmVydGFFbnRpdHksIFdlYi5Qcm9jdXJlbWVudCwgVmVyc2lvbj0xLjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPW51bGxdXQIAAAAJOQAAAAk6AAAACTsAAAAJPAAAAAk9AAAABSkAAAAoV2ViLlByb2N1cmVtZW50LkZpY2hhTGljaXRhY2lvblJlcXVpc2l0bwUAAAAJX2p1cmlkaWNhCF9uYXR1cmFsEl9kb2N1bWVudG9KdXJpZGljbxFfZG9jdW1lbnRvTmF0dXJhbA5fcmVxdWlzaXRvc0NIUAMDAwMDmgFTeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYy5MaXN0YDFbW1dlYi5Qcm9jdXJlbWVudC5FbnRpdGllcy5MZWdhbFByZWNlZGVudEVudGl0eSwgV2ViLlByb2N1cmVtZW50LCBWZXJzaW9uPTEuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49bnVsbF1dmgFTeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYy5MaXN0YDFbW1dlYi5Qcm9jdXJlbWVudC5FbnRpdGllcy5MZWdhbFByZWNlZGVudEVudGl0eSwgV2ViLlByb2N1cmVtZW50LCBWZXJzaW9uPTEuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49bnVsbF1dmgFTeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYy5MaXN0YDFbW1dlYi5Qcm9jdXJlbWVudC5FbnRpdGllcy5MZWdhbFByZWNlZGVudEVudGl0eSwgV2ViLlByb2N1cmVtZW50LCBWZXJzaW9uPTEuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49bnVsbF1dmgFTeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYy5MaXN0YDFbW1dlYi5Qcm9jdXJlbWVudC5FbnRpdGllcy5MZWdhbFByZWNlZGVudEVudGl0eSwgV2ViLlByb2N1cmVtZW50LCBWZXJzaW9uPTEuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49bnVsbF1dmgFTeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYy5MaXN0YDFbW1dlYi5Qcm9jdXJlbWVudC5FbnRpdGllcy5MZWdhbFByZWNlZGVudEVudGl0eSwgV2ViLlByb2N1cmVtZW50LCBWZXJzaW9uPTEuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49bnVsbF1dAgAAAAk+AAAACT8AAAAJQAAAAAlBAAAACUIAAAAEKgAAAJkBU3lzdGVtLkNvbGxlY3Rpb25zLkdlbmVyaWMuTGlzdGAxW1tXZWIuUHJvY3VyZW1lbnQuRW50aXRpZXMuQXdhcmRDcml0ZXJpYUVudGl0eSwgV2ViLlByb2N1cmVtZW50LCBWZXJzaW9uPTEuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49bnVsbF1dAwAAAAZfaXRlbXMFX3NpemUIX3ZlcnNpb24EAAAuV2ViLlByb2N1cmVtZW50LkVudGl0aWVzLkF3YXJkQ3JpdGVyaWFFbnRpdHlbXQIAAAAICAlDAAAABAAAAAQAAAABKwAAACoAAAAJRAAAAAAAAAAAAAAABCwAAACPAVN5c3RlbS5Db2xsZWN0aW9ucy5HZW5lcmljLkxpc3RgMVtbV2ViLlByb2N1cmVtZW50LkVudGl0aWVzLkd1YXJhbnRlZSwgV2ViLlByb2N1cmVtZW50LCBWZXJzaW9uPTEuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49bnVsbF1dAwAAAAZfaXRlbXMFX3NpemUIX3ZlcnNpb24EAAAkV2ViLlByb2N1cmVtZW50LkVudGl0aWVzLkd1YXJhbnRlZVtdAgAAAAgICUUAAAACAAAAAgAAAAQtAAAAkgFTeXN0ZW0uQ29sbGVjdGlvbnMuR2VuZXJpYy5MaXN0YDFbW1dlYi5Qcm9jdXJlbWVudC5FbnRpdGllcy5DbGF1c2VFbnRpdHksIFdlYi5Qcm9jdXJlbWVudCwgVmVyc2lvbj0xLjAuMC4wLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPW51bGxdXQMAAAAGX2l0ZW1zBV9zaXplCF92ZXJzaW9uBAAAJ1dlYi5Qcm9jdXJlbWVudC5FbnRpdGllcy5DbGF1c2VFbnRpdHlbXQIAAAAICAlGAAAABQAAAAUAAAAMRwAAAD5NUC5VdGlsLCBWZXJzaW9uPTEuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49bnVsbAUuAAAANFdlYi5Qcm9jdXJlbWVudC5FbnRpdGllcy5MZWdhbFByZWNlZGVudENvbW1lbnRFbnRpdHkHAAAABl9yYmhJZAhfcmJoQ29kZRdfcmJoTGVnYWxSZWNvcmRDb21tZW50cxhfcmJoT2JzZXJ2YXRpb25DaGVja1RleHQWX3JiaE9ic2VydmF0aW9uQ29tbWVudAtfU3RlcFN0YXR1cwRfdXJsAAABAQEEAQgIQU1QLlV0aWwuVmF0ZXNGcmFtZXdvcmsuV2l6YXJkLldpemFyZEVudW1zK1dpemFyZFN0ZXBEYXRhU3RhdGVFbnVtRwAAAAIAAAAAAAAAAAAAAAkPAAAACQ8AAAAJDwAAAAW3////QU1QLlV0aWwuVmF0ZXNGcmFtZXdvcmsuV2l6YXJkLldpemFyZEVudW1zK1dpemFyZFN0ZXBEYXRhU3RhdGVFbnVtAQAAAAd2YWx1ZV9fAAhHAAAAAAAAAAoFLwAAACZXZWIuUHJvY3VyZW1lbnQuRmVjaGFzTGljaXRhY2lvbkVudGl0eQ4AAAAMX1B1YmxpY2FjaW9uEF9DaWVycmVJZG9uZWlkYWQHX0luaWNpbwRfRmluFl9QdWJsaWNhY2lvblJlc3B1ZXN0YXMHX0NpZXJyZRRfQWN0b0FwZXJ0dXJhVGVjbmljYRZfQWN0b0FwZXJ0dXJhRWNvbm9taWNhDV9BZGp1ZGljYWNpb24VX0VzdGltYWRhQWRqdWRpY2FjaW9uDl9Tb3BvcnRlRmlzaWNvEV9UaWVtcG9FdmFsdWFjaW9uF19VbmlkYWRUaWVtcG9FdmFsdWFjaW9uDl9GaXJtYUNvbnRyYXRvAQEBAQEBAQEBAQEBAQECAAAABkoAAAATMjQtMDYtMjAyMiAyMTo1MjozMAoGSwAAABMyNC0wNi0yMDIyIDIzOjAxOjAwBkwAAAATMDctMDctMjAyMiAxNTowMDowMAZNAAAAEzEzLTA3LTIwMjIgMTc6MDA6MDAGTgAAABMyMC0wNy0yMDIyIDE0OjAwOjAwBk8AAAATMjEtMDctMjAyMiAxNDowMDowMAZQAAAAEzIxLTA3LTIwMjIgMTQ6MDA6MDAGUQAAABMxNi0wOC0yMDIyIDE3OjAwOjAwBlIAAAATMTYtMDgtMjAyMiAxNzowMDowMAkPAAAACQ8AAAAGVAAAABVSRkJfVElNRV9QRVJJT0RfSE9VUlMJDwAAAAUwAAAAKFdlYi5Qcm9jdXJlbWVudC5GZWNoYXNMaWNpdGFjaW9uTFNFbnRpdHkbAAAAEF9jaWVycmVJZG9uZWlkYWQPX3ByZVB1YmxpY2FjaW9uF19wdWJsaWNhY2lvblJlc3B1ZXN0YUlUCV9pbmljaW9MUwZfZmluTFMSX2RpYUZlY2hhUHJlQ2llcnJlE19ob3JhRmVjaGFQcmVDaWVycmUQX2luaWNpb1ByZWd1bnRhcxNfaG9yYUluaWNpb1ByZWd1bnRhDV9maW5QcmVndW50YXMRX2hvcmFGaW5QcmVndW50YXMWX3B1YmxpY2FjaW9uUmVzcHVlc3RhcxpfaG9yYVB1YmxpY2FjaW9uUmVzcHVlc3Rhcw5fY2llcnJlT2ZlcnRhcxJfaG9yYUNpZXJyZU9mZXJ0YXMJX2FwZXJ0dXJhDV9ob3JhQXBlcnR1cmEVX2VzdGltYWRhQWRqdWRpY2FjaW9uFl9lc3RpbWFkYUZpcm1hQ29udHJhdG8RX2hvcmFBZGp1ZGljYWNpb24OX3NvcG9ydGVGaXNpY28TX2RpYUluaWNpb0lkb25laWRhZBRfaG9yYUluaWNpb0lkb25laWRhZBJfZGlhRmluYWxJZG9uZWlkYWQTX2hvcmFGaW5hbElkb25laWRhZBdfZGlhUmVzcHVlc3Rhc0lkb25laWRhZBhfaG9yYVJlc3B1ZXN0YXNJZG9uZWlkYWQBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQECAAAACgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKCgoKBDEAAACeAVN5c3RlbS5Db2xsZWN0aW9ucy5HZW5lcmljLkxpc3RgMVtbV2ViLlByb2N1cmVtZW50LkVudGl0aWVzLkRhdGVzRGVmaW5lZEJ5VXNlckVudGl0eSwgV2ViLlByb2N1cmVtZW50LCBWZXJzaW9uPTEuMC4wLjAsIEN1bHR1cmU9bmV1dHJhbCwgUHVibGljS2V5VG9rZW49bnVsbF1dAwAAAAZfaXRlbXMFX3NpemUIX3ZlcnNpb24EAAAzV2ViLlByb2N1cmVtZW50LkVudGl0aWVzLkRhdGVzRGVmaW5lZEJ5VXNlckVudGl0eVtdAgAAAAgICVYAAAABAAAAAQAAAAc4AAAAAAEAAAAEAAAABClXZWIuUHJvY3VyZW1lbnQuRmljaGFJdGVtTGljaXRhY2lvbkVudGl0eQIAAAAJVwAAAA0DBDkAAACdAVN5c3RlbS5Db2xsZWN0aW9ucy5HZW5lcmljLkxpc3RgMVtbV2ViLlByb2N1cmVtZW50LkVudGl0aWVzLkFudGVjZWRlbnRlT2ZlcnRhRW50aXR5LCBXZWIuUHJvY3VyZW1lbnQsIFZlcnNpb249MS4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1udWxsXV0DAAAABl9pdGVtcwVfc2l6ZQhfdmVyc2lvbgQAADJXZWIuUHJvY3VyZW1lbnQuRW50aXRpZXMuQW50ZWNlZGVudGVPZmVydGFFbnRpdHlbXQIAAAAICAlYAAAAAQAAAAEAAAABOgAAADkAAAAJWQAAAAAAAAAAAAAAATsAAAA5AAAACVoAAAABAAAAAQAAAAE8AAAAOQAAAAlZAAAAAAAAAAAAAAABPQAAADkAAAAJWQAAAAAAAAAAAAAABD4AAACaAVN5c3RlbS5Db2xsZWN0aW9ucy5HZW5lcmljLkxpc3RgMVtbV2ViLlByb2N1cmVtZW50LkVudGl0aWVzLkxlZ2FsUHJlY2VkZW50RW50aXR5LCBXZWIuUHJvY3VyZW1lbnQsIFZlcnNpb249MS4wLjAuMCwgQ3VsdHVyZT1uZXV0cmFsLCBQdWJsaWNLZXlUb2tlbj1udWxsXV0DAAAABl9pdGVtcwVfc2l6ZQhfdmVyc2lvbgQAAC9XZWIuUHJvY3VyZW1lbnQuRW50aXRpZXMuTGVnYWxQcmVjZWRlbnRFbnRpdHlbXQIAAAAICAlcAAAACAAAAAgAAAABPwAAAD4AAAAJXQAAAAgAAAAIAAAAAUAAAAA+AAAACV4AAAAFAAAABQAAAAFBAAAAPgAAAAlfAAAAAgAAAAIAAAABQgAAAD4AAAAJYAAAAAQAAAAEAAAAB0MAAAAAAQAAAAQAAAAELFdlYi5Qcm9jdXJlbWVudC5FbnRpdGllcy5Bd2FyZENyaXRlcmlhRW50aXR5AgAAAAlhAAAACWIAAAAJYwAAAAlkAAAAB0QAAAAAAQAAAAAAAAAELFdlYi5Qcm9jdXJlbWVudC5FbnRpdGllcy5Bd2FyZENyaXRlcmlhRW50aXR5AgAAAAdFAAAAAAEAAAAEAAAABCJXZWIuUHJvY3VyZW1lbnQuRW50aXRpZXMuR3VhcmFudGVlAgAAAAllAAAACWYAAAANAgdGAAAAAAEAAAAIAAAABCVXZWIuUHJvY3VyZW1lbnQuRW50aXRpZXMuQ2xhdXNlRW50aXR5AgAAAAlnAAAACWgAAAAJaQAAAAlqAAAACWsAAAANAwdWAAAAAAEAAAAEAAAABDFXZWIuUHJvY3VyZW1lbnQuRW50aXRpZXMuRGF0ZXNEZWZpbmVkQnlVc2VyRW50aXR5AgAAAAlsAAAADQMFVwAAAClXZWIuUHJvY3VyZW1lbnQuRmljaGFJdGVtTGljaXRhY2lvbkVudGl0eQYAAAAHX25vbWJyZQ9fY29kaWdvUHJvZHVjdG8MX2Rlc2NyaXBjaW9uB191bmlkYWQJX2NhbnRpZGFkB19udW1lcm8BAQEBAAEJAgAAAAZtAAAAOkluc3RhbGFjacOzbiBvIHNlcnZpY2lvIGRlIHNpc3RlbWFzIGRlIGVuZXJnw61hIGVsw6ljdHJpY2EGbgAAAAg3MjEwMjIwMQZvAAAAwgFVTklGSUNBQ0lPTiBERSBFTVBBTE1FUyBFRElGSUNJT1MgREUgQ09SVEUgQVBFTEFDSU9ORVMsIEpVWkdBRE8gREUgR0FSQU5Uw41BIFkgVFJJQlVOQUwgREUgSlVJQ0lPIE9SQUwgRU4gTE8gUEVOQUwgREUgVEVNVUNPIFBBUkEgT1BUQVIgQSBUQVJJRkEgREUgQ0xJRU5URSBMSUJSRSBQQVJBDQpTVU1JTklTVFJPIERFIEVMRUNUUklDSURBRAZwAAAABkdsb2JhbAEAAAAAAAAABnEAAAABMQdYAAAAAAEAAAAEAAAABDBXZWIuUHJvY3VyZW1lbnQuRW50aXRpZXMuQW50ZWNlZGVudGVPZmVydGFFbnRpdHkCAAAACXIAAAANAwdZAAAAAAEAAAAAAAAABDBXZWIuUHJvY3VyZW1lbnQuRW50aXRpZXMuQW50ZWNlZGVudGVPZmVydGFFbnRpdHkCAAAAB1oAAAAAAQAAAAQAAAAEMFdlYi5Qcm9jdXJlbWVudC5FbnRpdGllcy5BbnRlY2VkZW50ZU9mZXJ0YUVudGl0eQIAAAAJcwAAAA0DB1wAAAAAAQAAAAgAAAAELVdlYi5Qcm9jdXJlbWVudC5FbnRpdGllcy5MZWdhbFByZWNlZGVudEVudGl0eQIAAAAJdAAAAAl1AAAACXYAAAAJdwAAAAl4AAAACXkAAAAJegAAAAl7AAAAB10AAAAAAQAAAAgAAAAELVdlYi5Qcm9jdXJlbWVudC5FbnRpdGllcy5MZWdhbFByZWNlZGVudEVudGl0eQIAAAAJfAAAAAl9AAAACX4AAAAJfwAAAAmAAAAACYEAAAAJggAAAAmDAAAAB14AAAAAAQAAAAgAAAAELVdlYi5Qcm9jdXJlbWVudC5FbnRpdGllcy5MZWdhbFByZWNlZGVudEVudGl0eQIAAAAJhAAAAAmFAAAACYYAAAAJhwAAAAmIAAAADQMHXwAAAAABAAAABAAAAAQtV2ViLlByb2N1cmVtZW50LkVudGl0aWVzLkxlZ2FsUHJlY2VkZW50RW50aXR5AgAAAAmJAAAACYoAAAANAgdgAAAAAAEAAAAEAAAABC1XZWIuUHJvY3VyZW1lbnQuRW50aXRpZXMuTGVnYWxQcmVjZWRlbnRFbnRpdHkCAAAACYsAAAAJjAAAAAmNAAAACY4AAAAFYQAAACxXZWIuUHJvY3VyZW1lbnQuRW50aXRpZXMuQXdhcmRDcml0ZXJpYUVudGl0eQ8AAAAGX3JiYUlEDF9yYmFTb3VyY2VJRAtfcmJhUkZCQ29kZQhfcmJhTmFtZQxfcmJhRGF0YVR5cGUJX3JiYVNjb3BlDl9yYmFQZXJjZW50YWdlDV9yYmFJc0NoZWNrZWQLX3JiYUNvbW1lbnQKX3JiYVR5cGVDUwhfcmJzTmFtZQhfZHR5TmFtZQxfcmJhTmFtZUkxOG4MX3Jic05hbWVJMThuBF91cmwAAAABAAAAAgEAAQEBAQEICAgICAYIAgAAAAEAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAgEZACgkPAAAAAAAAAAaQAAAAB1RFQ05JQ08KCgoKAWIAAABhAAAAAgAAAAAAAAAAAAAACgAAAAAAAAAAAAAAAAAAREAKCQ8AAAAAAAAABpIAAAAJRUNPTk9NSUNPCgoKCgFjAAAAYQAAAAMAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAACRACgkPAAAAAAAAAAaUAAAAC1BBVFJJTU9OSUFMCgoKCgFkAAAAYQAAAAQAAAAAAAAAAAAAAAoAAAAAAAAAAAAAAAAAABRACgkPAAAAAAAAAAaWAAAADEZPUk1BTElEQURFUwoKCgoFZQAAACJXZWIuUHJvY3VyZW1lbnQuRW50aXRpZXMuR3VhcmFudGVlGgAAAAVpbnRJZAtpbnRTZXF1ZW5jZQ9pbnREb2N1bWVudFR5cGUSaW50RG9jdW1lbnRTdWJUeXBlGnN0ckRlc2NyaXB0aW9uRG9jdW1lbnRUeXBlDnN0ckJlbmVmaWNpYXJ5CWRibEFtb3VudA1zdHJBbW91bnRUeXBlGHN0ckRlc2NyaXB0aW9uQW1vdW50VHlwZQtzdHJDdXJyZW5jeRZzdHJEZXNjcmlwdGlvbkN1cnJlbmN5EWRhdEV4cGlyYXRpb25EYXRlEXN0ckV4cGlyYXRpb25EYXRlCnN0ckNvbW1lbnQOc3RyRGVzY3JpcHRpb24Oc3RyUmVzdGl0dXRpb24QaW50R3VhcmFudGVlVHlwZQ5pbnRJbnN0aXR1dGlvbhJpbnRHdWFyYW50ZWVOdW1iZXIPc3RyT3JnYW5pemF0aW9uCmJsbklzQmFzaXMIaW50QmlkSUQOaW50UmVmZXJlbmNlSUQQc3RyR3VhcmFudGVlVHlwZRlzdHJHdWFyYW50ZWVEb2N1bWVudFR5cGVzEHN0ckd1YXJhbnRlZU5hbWUAAAAAAQEAAQEBAQABAQEBAAABAQAAAAEBAQgCCAgGDQgIAQgIAgAAAKGQVgAAAAAAAAAAAAAGlwAAAAVWYWNpbwaYAAAALUNPUlBPUkFDSU9OIEFETUlOSVNUUkFUSVZBIERFTCBQT0RFUiBKVURJQ0lBTAAAAACAhB5BBpkAAAABMAoGmgAAAANDTFAGmwAAAAxQZXNvIENoaWxlbm8AQKOrLsjaCAoGnAAAAEhFbiBnYXJhbnTDrWEgZGUgbGEgc2VyaWVkYWQgZGUgbGEgb2ZlcnRhIGxpY2l0YWNpw7NuIElEIE7CsCAyMTc5LTMwLUxQMjIJDwAAAAaeAAAAmgVSZXNwZWN0byBkZSBsb3Mgb2ZlcmVudGVzIG5vIGFkanVkaWNhZG9zLCBsZXMgc2Vyw6EgZGV2dWVsdGEgYSBjb250YXIgZGVsIGTDrWEgc3Vic2lndWllbnRlIGEgbGEgZmVjaGEgZGUgZmlybWEgZGVsIGNvbnRyYXRvLg0KUmVzcGVjdG8gZGVsIG9mZXJlbnRlIGFkanVkaWNhZG8sIGxlIHNlcsOhIGRldnVlbHRhIGNvbnRyYSBsYSBwcmVzZW50YWNpw7NuIGRlIGxhIEdhcmFudMOtYSBkZSBGaWVsIHkgT3BvcnR1bm8gQ3VtcGxpbWllbnRvIGRlbCBDb250cmF0by4NCkVuIGNhc28gZGUgb2ZlcnRhcyBpbmFkbWlzaWJsZXMsIGxhIGRldm9sdWNpw7NuIHNlIHJlYWxpemFyw6EgYSBjb250YXIgZGUgbGEgZmVjaGEgZGUgcHVibGljYWNpw7NuIGRlIGxhIGFkanVkaWNhY2nDs24gZW4gZWwgcG9ydGFsLg0KTGEgcmVzdGl0dWNpw7NuIGRlIGxhIGdhcmFudMOtYSBkZSBzZXJpZWRhZCBkZSBsYSBvZmVydGEgc2UgZWZlY3R1YXLDoSBlbiBsYXMgb2ZpY2luYXMgZGUgbGEgQWRtaW5pc3RyYWNpw7NuIFpvbmFsIGRlIFRlbXVjbyB1YmljYWRhIGVuIEF2LiBDYXVwb2xpY8OhbiBOwrAxMDc3LCBwaXNvIDMsIG9maWNpbmEgMzAyLCBlbiBob3JhcmlvIGRlIGx1bmVzIGEganVldmVzIGRlIDg6MDAgYSAxNzowMCBob3JhcywgeSB2aWVybmVzIGRlIDg6MDAgYSAxNjowMCBob3Jhcy4AAAAAAAAAAAafAAAAATEKAAAAAAAAAAAABqAAAAAhR2FyYW50w61hcyBkZSBTZXJpZWRhZCBkZSBPZmVydGFzBqEAAAALMTE7MTs2OzU7NzsJDwAAAAFmAAAAZQAAAKqQVgAAAAAAAAAAAAAGowAAAAVWYWNpbwakAAAALUNPUlBPUkFDSU9OIEFETUlOSVNUUkFUSVZBIERFTCBQT0RFUiBKVURJQ0lBTAAAAAAAACRABqUAAAABMQoGpgAAAANDTFAGpwAAAAElAMAYGxeI3AgKBqgAAAB5UGFyYSBnYXJhbnRpemFyIGVsIGZpZWwgY3VtcGxpbWllbnRvIHkgY29ycmVjdGEgZWplY3VjacOzbiBkZSBsYXMgb2JyYXMgZGVsIGNvbnRyYXRvIGxpY2l0YWNpw7NuIHDDumJsaWNhIElEIDIxNzktMzAtTFAyMgkPAAAABqoAAAAdQSBsYSBmZWNoYSBkZSBzdSB2ZW5jaW1pZW50by4AAAAAAAAAAAarAAAAATIKAAAAAAAAAAAABqwAAAAqR2FyYW50w61hIGZpZWwgZGUgQ3VtcGxpbWllbnRvIGRlIENvbnRyYXRvBq0AAAACMTsJDwAAAAVnAAAAJVdlYi5Qcm9jdXJlbWVudC5FbnRpdGllcy5DbGF1c2VFbnRpdHkGAAAABl9yYmNJRAtfcmJjUkZCQ29kZQxfcmJjU2VxdWVuY2UJX3JiY1RpdGxlD19yYmNEZXNjcmlwdGlvbgRfdXJsAAAAAQEBCAgIAgAAACC31QDxYIkAAAAAAAavAAAAFlJlc29sdWNpw7NuIGRlIEVtcGF0ZXMGsAAAAAtTRUdVTiBCQVNFUwoBaAAAAGcAAAAht9UA8WCJAAAAAAAGsQAAAEFNZWNhbmlzbW8gcGFyYSBzb2x1Y2nDs24gZGUgY29uc3VsdGFzIHJlc3BlY3RvIGEgbGEgYWRqdWRpY2FjacOzbgayAAAAC1NFR1VOIEJBU0VTCgFpAAAAZwAAACK31QDxYIkAAAAAAAazAAAAUkFjcmVkaXRhY2nDs24gZGUgY3VtcGxpbWllbnRvIGRlIHJlbXVuZXJhY2lvbmVzIG8gY290aXphY2lvbmVzIGRlIHNlZ3VyaWRhZCBzb2NpYWwGtAAAAAtTRUdVTiBCQVNFUwoBagAAAGcAAAAjt9UA8WCJAAAAAAAGtQAAADhQcmVzZW50YWNpw7NuIGRlIGFudGVjZWRlbnRlcyBvbWl0aWRvcyBwb3IgbG9zIG9mZXJlbnRlcwa2AAAAC1NFR1VOIEJBU0VTCgFrAAAAZwAAACS31QDxYIkAAAAAAAa3AAAAE1BhY3RvIGRlIGludGVncmlkYWQGuAAAAIAiRWwgb2ZlcmVudGUgZGVjbGFyYSBxdWUsIHBvciBlbCBzJm9hY3V0ZTtsbyBoZWNobyBkZSBwYXJ0aWNpcGFyIGVuIGxhIHByZXNlbnRlIGxpY2l0YWNpJm9hY3V0ZTtuLCBhY2VwdGEgZXhwcmVzYW1lbnRlIGVsIHByZXNlbnRlIHBhY3RvIGRlIGludGVncmlkYWQsIG9ibGlnJmFhY3V0ZTtuZG9zZSBhIGN1bXBsaXIgY29uIHRvZGFzIHkgY2FkYSB1bmEgZGUgbGFzIGVzdGlwdWxhY2lvbmVzIHF1ZSBjb250ZW5pZGFzIGVsIG1pc21vLCBzaW4gcGVyanVpY2lvIGRlIGxhcyBxdWUgc2Ugc2UmbnRpbGRlO2FsZW4gZW4gZWwgcmVzdG8gZGUgbGFzIGJhc2VzIGRlIGxpY2l0YWNpJm9hY3V0ZTtuIHkgZGVtJmFhY3V0ZTtzIGRvY3VtZW50b3MgaW50ZWdyYW50ZXMuIEVzcGVjaWFsbWVudGUsIGVsIG9mZXJlbnRlIGFjZXB0YSBlbCBzdW1pbmlzdHJhciB0b2RhIGxhIGluZm9ybWFjaSZvYWN1dGU7biB5IGRvY3VtZW50YWNpJm9hY3V0ZTtuIHF1ZSBzZWEgY29uc2lkZXJhZGEgbmVjZXNhcmlhIHkgZXhpZ2lkYSBkZSBhY3VlcmRvIGEgbGFzIHByZXNlbnRlcyBiYXNlcyBkZSBsaWNpdGFjaSZvYWN1dGU7biwgYXN1bWllbmRvIGV4cHJlc2FtZW50ZSBsb3Mgc2lndWllbnRlcyBjb21wcm9taXNvczogPGJyIC8+DQoxLi0gRWwgb2ZlcmVudGUgc2UgY29tcHJvbWV0ZSBhIHJlc3BldGFyIGxvcyBkZXJlY2hvcyBmdW5kYW1lbnRhbGVzIGRlIHN1cyB0cmFiYWphZG9yZXMsIGVudGVuZGkmZWFjdXRlO25kb3NlIHBvciAmZWFjdXRlO3N0b3MgbG9zIGNvbnNhZ3JhZG9zIGVuIGxhIENvbnN0aXR1Y2kmb2FjdXRlO24gUG9sJmlhY3V0ZTt0aWNhIGRlIGxhIFJlcCZ1YWN1dGU7YmxpY2EgZW4gc3UgYXJ0JmlhY3V0ZTtjdWxvIDE5LCBuJnVhY3V0ZTttZXJvcyAxJm9yZG07LCA0Jm9yZG07LCA1Jm9yZG07LCA2Jm9yZG07LCAxMiZvcmRtOywgeSAxNiZvcmRtOywgZW4gY29uZm9ybWlkYWQgYWwgYXJ0JmlhY3V0ZTtjdWxvIDQ4NSBkZWwgYyZvYWN1dGU7ZGlnbyBkZWwgdHJhYmFqby4gIEFzaW1pc21vLCBlbCBvZmVyZW50ZSBzZSBjb21wcm9tZXRlIGEgcmVzcGV0YXIgbG9zIGRlcmVjaG9zIGh1bWFub3MsIGxvIHF1ZSBzaWduaWZpY2EgcXVlIGRlYmUgZXZpdGFyIGRhciBsdWdhciBvIGNvbnRyaWJ1aXIgYSBlZmVjdG9zIGFkdmVyc29zIGVuIGxvcyBkZXJlY2hvcyBodW1hbm9zIG1lZGlhbnRlIHN1cyBhY3RpdmlkYWRlcywgcHJvZHVjdG9zIG8gc2VydmljaW9zLCB5IHN1YnNhbmFyIGVzb3MgZWZlY3RvcyBjdWFuZG8gc2UgcHJvZHV6Y2FuLCBkZSBhY3VlcmRvIGEgbG9zIFByaW5jaXBpb3MgUmVjdG9yZXMgZGUgRGVyZWNob3MgSHVtYW5vcyB5IEVtcHJlc2FzIGRlIE5hY2lvbmVzIFVuaWRhcy48YnIgLz4NCjIuLUVsIG9mZXJlbnRlIHNlIG9ibGlnYSBhIG5vIG9mcmVjZXIgbmkgY29uY2VkZXIsIG5pIGludGVudGFyIG9mcmVjZXIgbyBjb25jZWRlciwgc29ib3Jub3MsIHJlZ2Fsb3MsIHByZW1pb3MsIGQmYWFjdXRlO2RpdmFzIG8gcGFnb3MsIGN1YWxxdWllcmEgZnVlc2Ugc3UgdGlwbywgbmF0dXJhbGV6YSB5L28gbW9udG8sIGEgbmluZyZ1YWN1dGU7biBmdW5jaW9uYXJpbyBwJnVhY3V0ZTtibGljbyBlbiByZWxhY2kmb2FjdXRlO24gY29uIHN1IG9mZXJ0YSwgY29uIGVsIHByb2Nlc28gZGUgbGljaXRhY2kmb2FjdXRlO24gcCZ1YWN1dGU7YmxpY2EsIG5pIGNvbiBsYSBlamVjdWNpJm9hY3V0ZTtuIGRlICZlYWN1dGU7bCBvIGxvcyBjb250cmF0b3MgcXVlIGV2ZW50dWFsbWVudGUgc2UgZGVyaXZlbiBkZSBsYSBtaXNtYSwgbmkgdGFtcG9jbyBhIG9mcmVjZXJsYXMgbyBjb25jZWRlcmxhcyBhIHRlcmNlcmFzIHBlcnNvbmFzIHF1ZSBwdWRpZXNlbiBpbmZsdWlyIGRpcmVjdGEgbyBpbmRpcmVjdGFtZW50ZSBlbiBlbCBwcm9jZXNvIGxpY2l0YXRvcmlvLCBlbiBzdSB0b21hIGRlIGRlY2lzaW9uZXMgbyBlbiBsYSBwb3N0ZXJpb3IgYWRqdWRpY2FjaSZvYWN1dGU7biB5IGVqZWN1Y2kmb2FjdXRlO24gZGVsIG8gbG9zIGNvbnRyYXRvcyBxdWUgZGUgZWxsbyBzZSBkZXJpdmVuLjxiciAvPg0KMy4tIEVsIG9mZXJlbnRlIHNlIG9ibGlnYSBhIG5vIGludGVudGFyIG5pIGVmZWN0dWFyIGFjdWVyZG9zIG8gcmVhbGl6YXIgbmVnb2NpYWNpb25lcywgYWN0b3MgbyBjb25kdWN0YXMgcXVlIHRlbmdhbiBwb3Igb2JqZXRvIGluZmx1aXIgbyBhZmVjdGFyIGRlIGN1YWxxdWllciBmb3JtYSBsYSBsaWJyZSBjb21wZXRlbmNpYSwgY3VhbHF1aWVyYSBmdWVzZSBsYSBjb25kdWN0YSBvIGFjdG8gZXNwZWMmaWFjdXRlO2ZpY28sIHkgZXNwZWNpYWxtZW50ZSwgYXF1ZWxsb3MgYWN1ZXJkb3MsIG5lZ29jaWFjaW9uZXMsIGFjdG9zIG8gY29uZHVjdGFzIGRlIHRpcG8gbyBuYXR1cmFsZXphIGNvbHVzaXZhLCBlbiBjdWFscXVpZXIgZGUgc3VzIHRpcG9zIG8gZm9ybWFzLjxiciAvPg0KNC4tIEVsIG9mZXJlbnRlIHNlIG9ibGlnYSBhIHJldmlzYXIgeSB2ZXJpZmljYXIgdG9kYSBsYSBpbmZvcm1hY2kmb2FjdXRlO24geSBkb2N1bWVudGFjaSZvYWN1dGU7biwgcXVlIGRlYmEgcHJlc2VudGFyIHBhcmEgZWZlY3RvcyBkZWwgcHJlc2VudGUgcHJvY2VzbyBsaWNpdGF0b3JpbywgdG9tYW5kbyB0b2RhcyBsYXMgbWVkaWRhcyBxdWUgc2VhbiBuZWNlc2FyaWFzIHBhcmEgYXNlZ3VyYXIgbGEgdmVyYWNpZGFkLCBpbnRlZ3JpZGFkLCBsZWdhbGlkYWQsIGNvbnNpc3RlbmNpYSwgcHJlY2lzaSZvYWN1dGU7biB5IHZpZ2VuY2lhIGRlIGxhIG1pc21hLg0KNS4tIEVsIG9mZXJlbnRlIHNlIG9ibGlnYSBhIGFqdXN0YXIgc3UgYWN0dWFyIHkgY3VtcGxpciBjb24gbG9zIHByaW5jaXBpb3MgZGUgbGVnYWxpZGFkLCAmZWFjdXRlO3RpY2EsIG1vcmFsLCBidWVuYXMgY29zdHVtYnJlcyB5IHRyYW5zcGFyZW5jaWEgZW4gZWwgcHJlc2VudGUgcHJvY2VzbyBsaWNpdGF0b3Jpby4NCjYuLSBFbCBvZmVyZW50ZSBtYW5pZmllc3RhLCBnYXJhbnRpemEgeSBhY2VwdGEgcXVlIGNvbm9jZSB5IHJlc3BldGFyJmFhY3V0ZTsgbGFzIHJlZ2xhcyB5IGNvbmRpY2lvbmVzIGVzdGFibGVjaWRhcyBlbiBsYXMgYmFzZXMgZGUgbGljaXRhY2kmb2FjdXRlO24sIHN1cyBkb2N1bWVudG9zIGludGVncmFudGVzIHkgJmVhY3V0ZTtsIG8gbG9zIGNvbnRyYXRvcyBxdWUgZGUgZWxsb3Mgc2UgZGVyaXZhc2UuPGJyIC8+DQo3Li0gRWwgb2ZlcmVudGUgc2Ugb2JsaWdhIHkgYWNlcHRhIGFzdW1pciwgbGFzIGNvbnNlY3VlbmNpYXMgeSBzYW5jaW9uZXMgcHJldmlzdGFzIGVuIGVzdGFzIGJhc2VzIGRlIGxpY2l0YWNpJm9hY3V0ZTtuLCBhcyZpYWN1dGU7IGNvbW8gZW4gbGEgbGVnaXNsYWNpJm9hY3V0ZTtuIHkgbm9ybWF0aXZhIHF1ZSBzZWFuIGFwbGljYWJsZXMgYSBsYSBtaXNtYS48YnIgLz4NCjguLSBFbCBvZmVyZW50ZSByZWNvbm9jZSB5IGRlY2xhcmEgcXVlIGxhIG9mZXJ0YSBwcmVzZW50YWRhIGVuIGVsIHByb2Nlc28gbGljaXRhdG9yaW8gZXMgdW5hIHByb3B1ZXN0YSBzZXJpYSwgY29uIGluZm9ybWFjaSZvYWN1dGU7biBmaWRlZGlnbmEgeSBlbiB0JmVhY3V0ZTtybWlub3MgdCZlYWN1dGU7Y25pY29zIHkgZWNvbiZvYWN1dGU7bWljb3MgYWp1c3RhZG9zIGEgbGEgcmVhbGlkYWQsIHF1ZSBhc2VndXJlbiBsYSBwb3NpYmlsaWRhZCBkZSBjdW1wbGlyIGNvbiBsYSBtaXNtYSBlbiBsYXMgY29uZGljaW9uZXMgeSBvcG9ydHVuaWRhZCBvZmVydGFkYXMuPGJyIC8+DQo5Li0gRWwgb2ZlcmVudGUgc2Ugb2JsaWdhIGEgdG9tYXIgdG9kYXMgbGFzIG1lZGlkYXMgcXVlIGZ1ZXNlbiBuZWNlc2FyaWFzIHBhcmEgcXVlIGxhcyBvYmxpZ2FjaW9uZXMgYW50ZXJpb3JtZW50ZSBzZSZudGlsZGU7YWxhZGFzIHNlYW4gYXN1bWlkYXMgeSBjYWJhbG1lbnRlIGN1bXBsaWRhcyBwb3Igc3VzIGVtcGxlYWRvcyB5L28gZGVwZW5kaWVudGVzIHkvbyBhc2Vzb3JlcyB5L28gYWdlbnRlcyB5IGVuIGdlbmVyYWwsIHRvZGFzIGxhcyBwZXJzb25hcyBjb24gcXVlICZlYWN1dGU7c3RlIG8gJmVhY3V0ZTtzdG9zIHNlIHJlbGFjaW9uZW4gZGlyZWN0YSBvIGluZGlyZWN0YW1lbnRlIGVuIHZpcnR1ZCBvIGNvbW8gZWZlY3RvIGRlIGxhIHByZXNlbnRlIGxpY2l0YWNpJm9hY3V0ZTtuLCBpbmNsdWlkb3Mgc3VzIHN1YmNvbnRyYXRpc3RhcywgaGFjaSZlYWN1dGU7bmRvc2UgcGxlbmFtZW50ZSByZXNwb25zYWJsZSBkZSBsYXMgY29uc2VjdWVuY2lhcyBkZSBzdSBpbmZyYWNjaSZvYWN1dGU7biwgc2luIHBlcmp1aWNpbyBkZSBsYXMgcmVzcG9uc2FiaWxpZGFkZXMgaW5kaXZpZHVhbGVzIHF1ZSB0YW1iaSZlYWN1dGU7biBwcm9jZWRpZXNlbiB5L28gZnVlc2VuIGRldGVybWluYWRhcyBwb3IgbG9zIG9yZ2FuaXNtb3MgY29ycmVzcG9uZGllbnRlcy4KBWwAAAAxV2ViLlByb2N1cmVtZW50LkVudGl0aWVzLkRhdGVzRGVmaW5lZEJ5VXNlckVudGl0eQkAAAAFaW50SUQHaW50Q29kZQdzdHJOYW1lC2RhdERhdGVUaW1lB3N0ckRhdGUHc3RyVGltZQZzdHJVcmwJaW50RGlhc0NTCXN0ckhvcmFDcwAAAQABAQEAAQgIDQgCAAAAAQAAAPFgiQAGuQAAACtWSVNJVEEgVEVSUkVOTyBPQkxJR0FUT1JJQSBTRUdVTiBDUk9OT0dSQU1BAAAAAAAAAAAGugAAABMwNC0wNy0yMDIyIDE1OjAwOjAwCgoAAAAABrsAAAABMAVyAAAAMFdlYi5Qcm9jdXJlbWVudC5FbnRpdGllcy5BbnRlY2VkZW50ZU9mZXJ0YUVudGl0eRMAAAAFaW50SUQLaW50U291cmNlSWQKaW50UkZCQ29kZRBpbnRSZXF1aXNpdGVUeXBlCHN0clRpdGxlEnN0clRpdGxlVHJhbnNsYXRlZApzdHJDb21tZW50C2ludFNlcXVlbmNlDGJsbklzQ2tlY2tlZAZzdHJVcmwLYmxuSXNBY3RpdmUSc3RyQ29kZUFudGVjZWRlbnRlDGludElEQWRqdW50bw5zdHJDb2RlQWRqdW50bxVzdHJEZXNjcmlwdGlvbkFkanVudG8WaW50RG9jdW1lbnRUeXBlQWRqdW50bxlpbnREb2N1bWVudFN1YlR5cGVBZGp1bnRvDnN0ck5hbWVBZGp1bnRvGHN0clNvdXJjZUZpbGVOYW1lQWRqdW50bwAAAAABAQEAAAEAAQABAQAAAQEICAgICAEBCAgIAgAAAGsQdAEAAAAA8WCJAAMAAAAJDwAAAAoGvQAAABZBTkVYT1MgQURNSU5JU1RSQVRJVk9TAQAAAAAKAAoAAAAABr4AAAABMQoAAAAAAAAAAAoKAXMAAAByAAAAbhB0AQAAAADxYIkABQAAAAkPAAAACgbAAAAAEUFORVhPUyBFQ09OT01JQ09TAQAAAAAKAAoAAAAABsEAAAABMQoAAAAAAAAAAAoKBXQAAAAtV2ViLlByb2N1cmVtZW50LkVudGl0aWVzLkxlZ2FsUHJlY2VkZW50RW50aXR5DAAAAAZfcmxySUQbX3JsckxlZ2FsUmVjb3JkVHlwZVNlcXVlbmNlE19ybHJMZWdhbFJlY29yZFR5cGUUX3JsckxlZ2FsUmVjb3JkVmFsdWUUX3JsckxlZ2FsUmVjb3JkVGl0bGUaX3JsckxlZ2FsUmVjb3JkRGVzY3JpcHRpb24VX3JsckxlZ2FsUmVjb3JkU291cmNlF19ybHJMZWdhbFJlY29yZElzQWN0aXZlFl9ybHJMZWdhbFJlY29yZERlZmF1bHQTX3JsckxlZ2FsUmVjb3JkSGVscBNfcmxyTGVnYWxSZWNvcmRDb2RlBF91cmwAAAAAAQEBAAABAAEICAgIAQEIAgAAAAkAAAABAAAADQAAAAAAAAAGwgAAAB5Db25kZW5hcyBwb3IgZGVsaXRvIGRlIGNvaGVjaG8GwwAAAH9IYWJlciBzaWRvIGNvbmRlbmFkbyBwb3IgY3VhbHF1aWVyYSBkZSBsb3MgZGVsaXRvcyBkZSBjb2hlY2hvIGNvbnRlbXBsYWRvcyBlbiBlbCB0w610dWxvIFYgZGVsIExpYnJvIFNlZ3VuZG8gZGVsIEPDs2RpZ28gUGVuYWwuCgAACgAAAAAKAXUAAAB0AAAACgAAAAIAAAANAAAAAAAAAAbEAAAAEkRldWRhcyB0cmlidXRhcmlhcwbFAAAAiANSZWdpc3RyYXIgdW5hIG8gbcOhcyBkZXVkYXMgdHJpYnV0YXJpYXMgcG9yIHVuIG1vbnRvIHRvdGFsIHN1cGVyaW9yIGEgNTAwIFVUTSBwb3IgbcOhcyBkZSB1biBhw7FvLCBvIHN1cGVyaW9yIGEgMjAwIFVUTSBlIGluZmVyaW9yIGEgNTAwIFVUTSBwb3IgdW4gcGVyw61vZG8gc3VwZXJpb3IgYSAyIGHDsW9zLCBzaW4gcXVlIGV4aXN0YSB1biBjb252ZW5pbyBkZSBwYWdvIHZpZ2VudGUuIEVuIGNhc28gZGUgZW5jb250cmFyc2UgcGVuZGllbnRlIGp1aWNpbyBzb2JyZSBsYSBlZmVjdGl2aWRhZCBkZSBsYSBkZXVkYSwgZXN0YSBpbmhhYmlsaWRhZCByZWdpcsOhIHVuYSB2ZXogcXVlIHNlIGVuY3VlbnRyZSBmaXJtZSBvIGVqZWN1dG9yaWFkYSBsYSByZXNwZWN0aXZhIHJlc29sdWNpw7NuLgoAAAoAAAAACgF2AAAAdAAAAAsAAAADAAAADQAAAAAAAAAGxgAAACBEZXVkYXMgcHJldmlzaW9uYWxlcyB5IGxhYm9yYWxlcwbHAAAAqAFSZWdpc3RyYXIgZGV1ZGFzIHByZXZpc2lvbmFsZXMgbyBkZSBzYWx1ZCBwb3IgbcOhcyBkZSAxMiBtZXNlcyBwb3Igc3VzIHRyYWJhamFkb3JlcyBkZXBlbmRpZW50ZXMsIGxvIHF1ZSBzZSBhY3JlZGl0YXLDoSBtZWRpYW50ZSBjZXJ0aWZpY2FkbyBkZSBsYSBhdXRvcmlkYWQgY29tcGV0ZW50ZS4KAAAKAAAAAAoBdwAAAHQAAAAMAAAABAAAAA0AAAAAAAAABsgAAAAwU2VudGVuY2lhIHBvciBwcmVzZW50YWNpw7NuIGRlIGRvY3VtZW50b3MgZmFsc29zBskAAACJAUxhIHByZXNlbnRhY2nDs24gYWwgUmVnaXN0cm8gTmFjaW9uYWwgZGUgUHJvdmVlZG9yZXMgZGUgdW5vIG8gbcOhcyBkb2N1bWVudG9zIGZhbHNvcywgZGVjbGFyYWRvIGFzw60gcG9yIHNlbnRlbmNpYSBqdWRpY2lhbCBlamVjdXRvcmlhZGEuCgAACgAAAAAKAXgAAAB0AAAADQAAAAUAAAANAAAAAAAAAAbKAAAAGERldWRhcyBFc3RhZG8gZGUgcXVpZWJyYQbLAAAARkhhYmVyIHNpZG8gZGVjbGFyYWRvIGVuIHF1aWVicmEgcG9yIHJlc29sdWNpw7NuIGp1ZGljaWFsIGVqZWN1dG9yaWFkYS4KAAAKAAAAAAoBeQAAAHQAAAAOAAAABgAAAA0AAAAAAAAABswAAAAnU3VzcGVuc2nDs24gbyBlbGltaW5hY2nDs24gZGVsIHJlZ2lzdHJvBs0AAACHAUhhYmVyIHNpZG8gZWxpbWluYWRvIG8gZW5jb250cmFyc2Ugc3VzcGVuZGlkbyBkZWwgUmVnaXN0cm8gTmFjaW9uYWwgZGUgUHJvdmVlZG9yZXMgcG9yIHJlc29sdWNpw7NuIGZ1bmRhZGEgZGUgbGEgRGlyZWNjacOzbiBkZSBDb21wcmFzLgoAAAoAAAAACgF6AAAAdAAAAA8AAAAHAAAADQAAAAAAAAAGzgAAAFdDb25kZW5hcyBwb3IgcHLDoWN0aWNhcyBhbnRpc2luZGljYWxlcyBvIGluZnJhY2Npw7NuIGEgbG9zIGRlcmVjaG9zIGRlIGxvcyB0cmFiYWphZG9yZXMGzwAAAG1IYWJlciBzaWRvIGNvbmRlbmFkbyBwb3IgcHLDoWN0aWNhcyBhbnRpc2luZGljYWxlcyBvIGluZnJhY2Npw7NuIGEgbG9zIGRlcmVjaG9zIGZ1bmRhbWVudGFsZXMgZGVsIHRyYWJhamFkb3IuCgAACgAAAAAKAXsAAAB0AAAAEAAAAAgAAAANAAAAAAAAAAbQAAAAbEhhYmVyIHNpZG8gY29uZGVuYWRvIHBvciBwcsOhY3RpY2FzIGFudGlzaW5kaWNhbGVzIG8gaW5mcmFjY2nDs24gYSBsb3MgZGVyZWNob3MgZnVuZGFtZW50YWxlcyBkZWwgdHJhYmFqYWRvcgbRAAAAaVJlZ2lzdHJhciBjb25kZW5hcyBhc29jaWFkYXMgYSByZXNwb25zYWJpbGlkYWQgcGVuYWwganVyw61kaWNhIChpbmN1bXBsaW1pZW50byBhcnTDrWN1bG8gMTAsIExleSAyMC4zOTMpLgoAAAoAAAAACgF8AAAAdAAAAAEAAAABAAAADAAAAAAAAAAG0gAAAB5Db25kZW5hcyBwb3IgZGVsaXRvIGRlIGNvaGVjaG8G0wAAAH9IYWJlciBzaWRvIGNvbmRlbmFkbyBwb3IgY3VhbHF1aWVyYSBkZSBsb3MgZGVsaXRvcyBkZSBjb2hlY2hvIGNvbnRlbXBsYWRvcyBlbiBlbCB0w610dWxvIFYgZGVsIExpYnJvIFNlZ3VuZG8gZGVsIEPDs2RpZ28gUGVuYWwuCgAACgAAAAAKAX0AAAB0AAAAAgAAAAIAAAAMAAAAAAAAAAbUAAAAEkRldWRhcyB0cmlidXRhcmlhcwbVAAAAiANSZWdpc3RyYXIgdW5hIG8gbcOhcyBkZXVkYXMgdHJpYnV0YXJpYXMgcG9yIHVuIG1vbnRvIHRvdGFsIHN1cGVyaW9yIGEgNTAwIFVUTSBwb3IgbcOhcyBkZSB1biBhw7FvLCBvIHN1cGVyaW9yIGEgMjAwIFVUTSBlIGluZmVyaW9yIGEgNTAwIFVUTSBwb3IgdW4gcGVyw61vZG8gc3VwZXJpb3IgYSAyIGHDsW9zLCBzaW4gcXVlIGV4aXN0YSB1biBjb252ZW5pbyBkZSBwYWdvIHZpZ2VudGUuIEVuIGNhc28gZGUgZW5jb250cmFyc2UgcGVuZGllbnRlIGp1aWNpbyBzb2JyZSBsYSBlZmVjdGl2aWRhZCBkZSBsYSBkZXVkYSwgZXN0YSBpbmhhYmlsaWRhZCByZWdpcsOhIHVuYSB2ZXogcXVlIHNlIGVuY3VlbnRyZSBmaXJtZSBvIGVqZWN1dG9yaWFkYSBsYSByZXNwZWN0aXZhIHJlc29sdWNpw7NuLgoAAAoAAAAACgF+AAAAdAAAAAMAAAADAAAADAAAAAAAAAAG1gAAACBEZXVkYXMgcHJldmlzaW9uYWxlcyB5IGxhYm9yYWxlcwbXAAAAqAFSZWdpc3RyYXIgZGV1ZGFzIHByZXZpc2lvbmFsZXMgbyBkZSBzYWx1ZCBwb3IgbcOhcyBkZSAxMiBtZXNlcyBwb3Igc3VzIHRyYWJhamFkb3JlcyBkZXBlbmRpZW50ZXMsIGxvIHF1ZSBzZSBhY3JlZGl0YXLDoSBtZWRpYW50ZSBjZXJ0aWZpY2FkbyBkZSBsYSBhdXRvcmlkYWQgY29tcGV0ZW50ZS4KAAAKAAAAAAoBfwAAAHQAAAAEAAAABAAAAAwAAAAAAAAABtgAAAAwU2VudGVuY2lhIHBvciBwcmVzZW50YWNpw7NuIGRlIGRvY3VtZW50b3MgZmFsc29zBtkAAACJAUxhIHByZXNlbnRhY2nDs24gYWwgUmVnaXN0cm8gTmFjaW9uYWwgZGUgUHJvdmVlZG9yZXMgZGUgdW5vIG8gbcOhcyBkb2N1bWVudG9zIGZhbHNvcywgZGVjbGFyYWRvIGFzw60gcG9yIHNlbnRlbmNpYSBqdWRpY2lhbCBlamVjdXRvcmlhZGEuCgAACgAAAAAKAYAAAAB0AAAABQAAAAUAAAAMAAAAAAAAAAbaAAAAGERldWRhcyBFc3RhZG8gZGUgcXVpZWJyYQbbAAAARkhhYmVyIHNpZG8gZGVjbGFyYWRvIGVuIHF1aWVicmEgcG9yIHJlc29sdWNpw7NuIGp1ZGljaWFsIGVqZWN1dG9yaWFkYS4KAAAKAAAAAAoBgQAAAHQAAAAGAAAABgAAAAwAAAAAAAAABtwAAAAnU3VzcGVuc2nDs24gbyBlbGltaW5hY2nDs24gZGVsIHJlZ2lzdHJvBt0AAACHAUhhYmVyIHNpZG8gZWxpbWluYWRvIG8gZW5jb250cmFyc2Ugc3VzcGVuZGlkbyBkZWwgUmVnaXN0cm8gTmFjaW9uYWwgZGUgUHJvdmVlZG9yZXMgcG9yIHJlc29sdWNpw7NuIGZ1bmRhZGEgZGUgbGEgRGlyZWNjacOzbiBkZSBDb21wcmFzLgoAAAoAAAAACgGCAAAAdAAAAAcAAAAHAAAADAAAAAAAAAAG3gAAAFdDb25kZW5hcyBwb3IgcHLDoWN0aWNhcyBhbnRpc2luZGljYWxlcyBvIGluZnJhY2Npw7NuIGEgbG9zIGRlcmVjaG9zIGRlIGxvcyB0cmFiYWphZG9yZXMG3wAAAG1IYWJlciBzaWRvIGNvbmRlbmFkbyBwb3IgcHLDoWN0aWNhcyBhbnRpc2luZGljYWxlcyBvIGluZnJhY2Npw7NuIGEgbG9zIGRlcmVjaG9zIGZ1bmRhbWVudGFsZXMgZGVsIHRyYWJhamFkb3IuCgAACgAAAAAKAYMAAAB0AAAACAAAAAgAAAAMAAAAAAAAAAbgAAAAbEhhYmVyIHNpZG8gY29uZGVuYWRvIHBvciBwcsOhY3RpY2FzIGFudGlzaW5kaWNhbGVzIG8gaW5mcmFjY2nDs24gYSBsb3MgZGVyZWNob3MgZnVuZGFtZW50YWxlcyBkZWwgdHJhYmFqYWRvcgbhAAAAaVJlZ2lzdHJhciBjb25kZW5hcyBhc29jaWFkYXMgYSByZXNwb25zYWJpbGlkYWQgcGVuYWwganVyw61kaWNhIChpbmN1bXBsaW1pZW50byBhcnTDrWN1bG8gMTAsIExleSAyMC4zOTMpLgoAAAoAAAAACgGEAAAAdAAAAJ5OiA4AAAAABQAAAAAAAAAG4gAAACBMZWdhbFJlY29yZC5TdXBwbHlfTmF0dXJhbF9UZXh0MQoG4wAAAAItMQAACgAAAAAKAYUAAAB0AAAAn06IDgAAAAAHAAAAAAAAAAbkAAAAJ0xlZ2FsUmVjb3JkX0NvbnRyYWN0ZWRfT2JsaWdhdG9yeV9UZXh0NAoG5QAAAAItMQAACgAAAAAKAYYAAAB0AAAAoE6IDgAAAAAHAAAAAAAAAAbmAAAAIExlZ2FsUmVjb3JkLlN1cHBseV9KdXJpZGljX1RleHQzCgbnAAAAAi0xAAAKAAAAAAoBhwAAAHQAAAChTogOAAAAAAcAAAAAAAAABugAAAAkTGVnYWxSZWNvcmQuQ29udHJhY3RlZF9KdXJpZGljX1RleHQ1CgbpAAAAAi0xAAAKAAAAAAoBiAAAAHQAAACjTogOAAAAAAcAAAAAAAAABuoAAAAkTGVnYWxSZWNvcmQuQ29udHJhY3RlZF9KdXJpZGljX1RleHQ3CgbrAAAAAi0xAAAKAAAAAAoBiQAAAHQAAACcTogOAAAAAAQAAAAAAAAABuwAAAAgTGVnYWxSZWNvcmQuU3VwcGx5X05hdHVyYWxfVGV4dDEKBu0AAAACLTEAAAoAAAAACgGKAAAAdAAAAJ1OiA4AAAAABgAAAAAAAAAG7gAAACdMZWdhbFJlY29yZF9Db250cmFjdGVkX09ibGlnYXRvcnlfVGV4dDQKBu8AAAACLTEAAAoAAAAACgGLAAAAdAAAAAAAAAAAAAAACAAAAAEAAAAKCgoAAAoAAAAACgGMAAAAdAAAAAAAAAAAAAAACQAAAAEAAAAKCgoAAAoAAAAACgGNAAAAdAAAAAAAAAAAAAAACgAAAAEAAAAKCgoAAAoAAAAACgGOAAAAdAAAAAAAAAAAAAAACwAAAAEAAAAKCgoAAAoAAAAACgsWAgIDD2QWSgIEDxQrAAIUKwADDxYCHhdFbmFibGVBamF4U2tpblJlbmRlcmluZ2hkZGQQFgFmFgEUKwADDxYCHwFoZGRkDxYBZhYBBXJUZWxlcmlrLldlYi5VSS5SYWRXaW5kb3csIFRlbGVyaWsuV2ViLlVJLCBWZXJzaW9uPTIwMTAuMy4xMjE1LjIwLCBDdWx0dXJlPW5ldXRyYWwsIFB1YmxpY0tleVRva2VuPTEyMWZhZTc4MTY1YmEzZDQWAmYPFCsAAw8WAh8BaGRkZGQCBg8WAh4HVmlzaWJsZWdkAgcPFgIfAmhkAggPZBYWAgEPDxYCHgRUZXh0BQxMaWNpdGFjacOzbiBkZAICDw8WAh8DBQRJRDogZGQCAw8PFgIfAwUMMjE3OS0zMC1MUDIyZGQCBQ8PFgIfAwUwVU5JRklDQUNJT04gREUgRU1QQUxNRVMgRURJRklDSU9TIFBPREVSIEpVRElDSUFMZGQCBw8PFgIfAwUhUmVzcG9uc2FibGUgZGUgZXN0YSBsaWNpdGFjacOzbjogZGQCCA8PFgIfAwVOQ09SUCBBRE1JTklTVFJBVElWQSBERUwgUE9ERVIgSlVESUNJQUwsIENvcnAuIEFkbS4gZGVsIFBvZGVyIEp1ZGljaWFsIC0gVGVtdWNvZGQCCg8PFgIfAwURRmVjaGEgZGUgQ2llcnJlOiBkZAILDw8WAh8DBRMyMC0wNy0yMDIyIDE0OjAwOjAwZGQCDQ8PFgIfAwUvUmVjbGFtb3MgcmVjaWJpZG9zIHBvciBpbmN1bXBsaXIgcGxhem8gZGUgcGFnbzpkZAIPDw8WAh8DBQIyN2RkAhEPDxYCHwMFngJFc3RlIG7Dum1lcm8gaW5kaWNhIGxvcyByZWNsYW1vcyByZWNpYmlkb3MgcG9yIGVzdGEgaW5zdGl0dWNpw7NuIGRlc2RlIGxvcyDDumx0aW1vcyA8c3Ryb25nPjEyIG1lc2VzIGhhc3RhIGVsIGTDrWEgZGUgYXllci48L3N0cm9uZz4gUmVjdWVyZGUgaW50ZXJwcmV0YXIgZXN0YSBpbmZvcm1hY2nDs24gY29uc2lkZXJhbmRvIGxhIGNhbnRpZGFkIGRlIGxpY2l0YWNpb25lcyB5IMOzcmRlbmVzIGRlIGNvbXByYSBxdWUgZXN0YSBpbnN0aXR1Y2nDs24gZ2VuZXJhIGVuIGVsIE1lcmNhZG8gUMO6YmxpY28uZGQCCQ9kFgQCAQ9kFgICAQ9kFgICAQ8PZBYEHgVjbGFzcwUJb2ZlcnRhckZCHgRocmVmBUIvUG9ydGFsL0xvZ2luRmljaGFMaWNpdGFjaW9uLmFzcHg/cmJoQ29kZT13ZGlWOUYrWmZFZUtieXh6UjZBRFdnPT1kAgMPZBYEAgEPDxYCHwMFD0Rlc2NhcmdhciBmaWNoYWRkAgMPDxYCHwJoZGQCCg9kFgJmD2QWBGYPZBYCAgEPDxYCHghJbWFnZVVybAU6fi9JbmNsdWRlcy9pbWFnZXMvRmljaGFMaWdodC9pY29ub3NfZXN0YWRvcy9wdWJsaWNhZGFzLnBuZ2RkAgEPZBYCAgEPZBYCZg9kFgICAQ9kFgICAQ8PFgIfAwUCMTVkZAILD2QWAmYPZBYIAgEPZBYCAgEPD2QWBB8EBQlvZmVydGFyRkIfBQV9L1BvcnRhbC9Mb2dpbkZpY2hhTGljaXRhY2lvbi5hc3B4P3FzPUhFeEJ5YlFjcDZkbXZKaG1SVXVFa2hkM2JhQ2FXck1yUFZ5RkV3cFA0WFR1VEZYWXVPQzhmSFVuMGtTYk1BUEdCaUZCc0VITStURU91eEhJcUI0YVhnPT1kAgMPFgQeBnRhcmdldAUGX2JsYW5rHwUFtQFodHRwOi8vd3d3LmZhY2Vib29rLmNvbS9zaGFyZXIucGhwP3U9aHR0cDovL3d3dy5tZXJjYWRvcHVibGljby5jbC9Qcm9jdXJlbWVudC9Nb2R1bGVzL1JGQi9EZXRhaWxzQWNxdWlzaXRpb24uYXNweD9xcz1IRXhCeWJRY3A2ZG12SmhtUlV1RWtxVmpKb2Q4M0V5bGVRRFVyTW9maDF4Z2hRM2NKRFVxck50VytZdTVFcnBvZAIFDxYEHwcFBl9ibGFuax8FBfsBaHR0cDovL3R3aXR0ZXIuY29tL3NoYXJlP3VybD1odHRwJTNhJTJmJTJmd3d3Lm1lcmNhZG9wdWJsaWNvLmNsJTJmUHJvY3VyZW1lbnQlMmZNb2R1bGVzJTJmUkZCJTJmRGV0YWlsc0FjcXVpc2l0aW9uLmFzcHglM2ZxcyUzZEhFeEJ5YlFjcDZkbXZKaG1SVXVFa3FWakpvZDgzRXlsZVFEVXJNb2ZoMXhnaFEzY0pEVXFyTnRXJTJiWXU1RXJwbyZhbXA7dGV4dD1VTklGSUNBQ0lPTitERStFTVBBTE1FUytFRElGSUNJT1MrUE9ERVIrSlVESUNJQUxkAgcPFgIfBQXjAW1haWx0bzo/c3ViamVjdD1VTklGSUNBQ0lPTiBERSBFTVBBTE1FUyBFRElGSUNJT1MgUE9ERVIgSlVESUNJQUwgMjE3OS0zMC1MUDIyJmJvZHk9aHR0cDovL3d3dy5tZXJjYWRvcHVibGljby5jbC9Qcm9jdXJlbWVudC9Nb2R1bGVzL1JGQi9EZXRhaWxzQWNxdWlzaXRpb24uYXNweD9xcz1IRXhCeWJRY3A2ZG12SmhtUlV1RWtxVmpKb2Q4M0V5bGVRRFVyTW9maDF4Z2hRM2NKRFVxck50VytZdTVFcnBvZAIPDw9kFgQfBAUFZmFuY3kfBQVtaHR0cHM6Ly93d3cubWVyY2Fkb3B1YmxpY28uY2wvaG9tZS9Db250ZW5pZG9zL1JlY2xhbW9zP3ZhckFtYmllbnRlPTEmcmJoRXh0ZXJuYWxDb2RlPTRKSG5rYnoybkMyL2dvTkh0Q1RBN0E9PWQCEA8PZBYEHwQFBWZhbmN5HwUFbWh0dHBzOi8vd3d3Lm1lcmNhZG9wdWJsaWNvLmNsL2hvbWUvQ29udGVuaWRvcy9SZWNsYW1vcz92YXJBbWJpZW50ZT0xJnJiaEV4dGVybmFsQ29kZT00Skhua2J6Mm5DMi9nb05IdENUQTdBPT1kAhEPD2QWAh4HT25DbGljawWGBG9wZW4oJy4uL0F0dGFjaG1lbnQvVmlld0F0dGFjaG1lbnQuYXNweD9lbmM9Y1huMmlpbUVqeXB3SGpoUGZNNlZBJTJmbU5yWTVHRmtTb2lWOCUyYks5WDR3ZjM0JTJmSiUyYlFQMW5vJTJid3pJM1lNYW85c0RMdUxDVEh3alhJSDR2eDlocmJjTWxMcUhmT29rcFdDYzQ4eWR4MHFUQkxiWWRVUk9nMXRrcmROWTZwekxaWXFOOU52aXlaUHBDeDdlTEpYUnZ4MjdrbEJodzhKNHZsbW9sUTFnaGxxc29uczkwVzVMY1h5dnh5SXU4dHA3c1Y2azhGZG5xWUk4THhLSVF4ckFmWmQ2MmNTRCUyYjNVNDQ3QzJrUlAzNUlDME9nJTJialNucUpCRDRlb3R3aW92VWdJemx1OFZtZkxvRG80MWNLeHV5Z3p0TCUyZmI3YmlFUUhqaXMzaWtKdXhzJTJiOHhqJTJic1FQZDhzZTRFYWVLMFI1Y2c0TnZjZycsJ01lcmNhZG9QdWJsaWNvJywgJ3dpZHRoPTg1MCwgaGVpZ2h0PTcwMCwgc3RhdHVzPXllcywgc2Nyb2xsYmFycz15ZXMsIGxlZnQ9MCwgdG9wPTAsIHJlc2l6YWJsZT15ZXMnKTt3aW5kb3cuZXZlbnQucmV0dXJuVmFsdWU9ZmFsc2U7ZAISDw8WBB8GBUMuLi8uLi9JbmNsdWRlcy9pbWFnZXMvRmljaGFMaWdodC9pY19saWNpdGFjaW9uX2Jsb3EvcHJlZ3VudGFzX2IucG5nHgdFbmFibGVkaBYGHwQFBWZhbmN5HwUFcS9Gb3Jvcy9Nb2R1bGVzL0ZOb3JtYWwvUG9wVXBzL1B1YmxpY1ZpZXcuYXNweD9xcz1IRXhCeWJRY3A2ZG12SmhtUlV1RWtqM1JBcXE5b1VCYUQ1R2JKU3V0UWJLbnBLYmZrMnR1MjlBVzRKS3plWmpBHgZjdXJzb3IFB2RlZmF1bHRkAhQPZBYCAgEPD2QWBB8EBQVmYW5jeR8FBWAvcHJvY3VyZW1lbnQvbW9kdWxlcy9yZmIvc2hvd2hpc3RvcnkuYXNweD9yYmhjb2RlPTkwMDMyNDkmcnN0VHlwZT0tMSZxcz1MUHpCQ291N3ZHMStQWTZrUGFRdFhRPT1kAhUPDxYEHwYFQi4uLy4uL0luY2x1ZGVzL2ltYWdlcy9GaWNoYUxpZ2h0L2ljX2xpY2l0YWNpb25fYmxvcS9hcGVydHVyYV9iLnBuZx8JaGRkAhYPFgIeBXN0eWxlBQ1kaXNwbGF5Om5vbmU7FgICAQ8PZBYEHwQFBWZhbmN5HwUFai9Qcm9jdXJlbWVudC9Nb2R1bGVzL1JGQi9TdGVwc1Byb2Nlc3NBd2FyZC9QcmV2aWV3VGVjaG5pY2FsT3BlbmluZ1Jlc3VsdHMuYXNweD9xcz1BVWJpL1FiZmZucnhidkMvNlQvcjRnPT1kAhcPDxYEHwYFQS4uLy4uL0luY2x1ZGVzL2ltYWdlcy9GaWNoYUxpZ2h0L2ljX2xpY2l0YWNpb25fYmxvcS9pYy0zMmJsb3EucG5nHwloZGQCGA9kFgICAQ8PFgQfBgVBLi4vLi4vSW5jbHVkZXMvaW1hZ2VzL0ZpY2hhTGlnaHQvaWNfbGljaXRhY2lvbl9ibG9xL2ljLTI1YmxvcS5wbmcfCWhkZAIZD2QWAgIBDw8WBB8GBUEuLi8uLi9JbmNsdWRlcy9pbWFnZXMvRmljaGFMaWdodC9pY19saWNpdGFjaW9uX2Jsb3EvaWMtMjdibG9xLnBuZx8JaGRkAhoPFgQfCwUNZGlzcGxheTpub25lOx8CaBYCAgEPD2QWBB8EBQxjdWFkcm9PZmVydGEfBQVfL1Byb2N1cmVtZW50L01vZHVsZXMvUkZCL1N0ZXBzUHJvY2Vzc0F3YXJkL1ByZXZpZXdEZXNlcnRpb25BY3QuYXNweD9xcz1BVWJpL1FiZmZucnhidkMvNlQvcjRnPT1kAhsPDxYEHwYFQS4uLy4uL0luY2x1ZGVzL2ltYWdlcy9GaWNoYUxpZ2h0L2ljX2xpY2l0YWNpb25fYmxvcS9pYy0yNmJsb3EucG5nHwloZGQCHA8PFgQfBgVBLi4vLi4vSW5jbHVkZXMvaW1hZ2VzL0ZpY2hhTGlnaHQvaWNfbGljaXRhY2lvbl9ibG9xL2ljLTMxYmxvcS5wbmcfCWhkZAIdDw8WAh8CaGRkAh4PDxYEHwYFRi4uLy4uL0luY2x1ZGVzL2ltYWdlcy9GaWNoYUxpZ2h0L2ljb25vc19saWNpdGFjaW9uL2dlb2Nncl9pbmFjdGl2by5wbmcfCWhkZAIhD2QWAgIBDw8WAh8DBTRObyBoYXkgZXNwZWNpYWxpZGFkZXMgcmVxdWVyaWRhcyBwYXJhIGxhIGxpY2l0YWNpw7NuZGQCIg8PFgIfAwUVUHJvZHVjdG9zIG8gc2VydmljaW9zZGQCIw88KwARAwAPFgQeC18hRGF0YUJvdW5kZx4LXyFJdGVtQ291bnQCAWQBEBYAFgAWAAwUKwAAFgJmD2QWBmYPDxYCHwJoZGQCAQ9kFgJmD2QWDAIBDw8WAh8DBQExZGQCAw8PFgIfAwU6SW5zdGFsYWNpw7NuIG8gc2VydmljaW8gZGUgc2lzdGVtYXMgZGUgZW5lcmfDrWEgZWzDqWN0cmljYWRkAgUPDxYCHwMFATFkZAIHDw8WAh8DBQZHbG9iYWxkZAILDw8WAh8DBQg3MjEwMjIwMWRkAg0PDxYCHwMFwgFVTklGSUNBQ0lPTiBERSBFTVBBTE1FUyBFRElGSUNJT1MgREUgQ09SVEUgQVBFTEFDSU9ORVMsIEpVWkdBRE8gREUgR0FSQU5Uw41BIFkgVFJJQlVOQUwgREUgSlVJQ0lPIE9SQUwgRU4gTE8gUEVOQUwgREUgVEVNVUNPIFBBUkEgT1BUQVIgQSBUQVJJRkEgREUgQ0xJRU5URSBMSUJSRSBQQVJBDQpTVU1JTklTVFJPIERFIEVMRUNUUklDSURBRGRkAgIPDxYCHwJoZGQCJg9kFipmDw8WAh8DBRZDb250ZW5pZG8gZGUgbGFzIGJhc2VzZGQCAQ8PFgIfAwUDMS4gZGQCAg8PFgIfAwUiQ2FyYWN0ZXLDrXN0aWNhcyBkZSBsYSBsaWNpdGFjacOzbmRkAgMPDxYCHwMFAzIuIGRkAgQPDxYCHwMFFE9yZ2FuaXNtbyBkZW1hbmRhbnRlZGQCBQ8PFgIfAwUDMy4gZGQCBg8PFgIfAwUPRXRhcGFzIHkgcGxhem9zZGQCBw8PFgIfAwUDNC4gZGQCCA8PFgIfAwUmQW50ZWNlZGVudGVzIHBhcmEgaW5jbHVpciBlbiBsYSBvZmVydGFkZAIJDw8WAh8DBQM1LiBkZAIKDw8WAh8DBTFSZXF1aXNpdG9zIHBhcmEgY29udHJhdGFyIGFsIHByb3ZlZWRvciBhZGp1ZGljYWRvZGQCCw8PFgIfAwUDNi4gZGQCDA8PFgIfAwUYQ3JpdGVyaW9zIGRlIGV2YWx1YWNpw7NuZGQCDQ8PFgIfAwUDNy4gZGQCDg8PFgIfAwUfTW9udG9zIHkgZHVyYWNpw7NuIGRlbCBjb250cmF0b2RkAg8PDxYCHwMFAzguIGRkAhAPDxYCHwMFFUdhcmFudMOtYXMgcmVxdWVyaWRhc2RkAhEPDxYCHwMFAzkuIGRkAhIPDxYCHwMFK1JlcXVlcmltaWVudG9zIHTDqWNuaWNvcyB5IG90cmFzIGNsw6F1c3VsYXNkZAITDw8WAh8DBQQxMC4gZGQCFA8PFgIfAwUdRGF0b3MgY29tcGxlbWVudGFyaW9zIEFuZXhvIDRkZAInDxYCHwJoZAIpD2QWJgIBDw8WAh8DBSUxLiBDYXJhY3RlcsOtc3RpY2FzIGRlIGxhIGxpY2l0YWNpw7NuZGQCAw8PFgIfAwUZTm9tYnJlIGRlIGxhIGxpY2l0YWNpw7NuOmRkAgUPDxYCHwMFMFVOSUZJQ0FDSU9OIERFIEVNUEFMTUVTIEVESUZJQ0lPUyBQT0RFUiBKVURJQ0lBTGRkAgcPDxYCHwMFB0VzdGFkbzpkZAIJDw8WAh8DBQlQdWJsaWNhZGFkZAILDw8WAh8DBQ1EZXNjcmlwY2nDs246ZGQCDQ8PFgIfAwXBAVVOSUZJQ0FDSU9OIERFIEVNUEFMTUVTIEVESUZJQ0lPUyBERSBDT1JURSBBUEVMQUNJT05FUywgSlVaR0FETyBERSBHQVJBTlTDjUEgWSBUUklCVU5BTCBERSBKVUlDSU8gT1JBTCBFTiBMTyBQRU5BTCBERSBURU1VQ08gUEFSQSBPUFRBUiBBIFRBUklGQSBERSBDTElFTlRFIExJQlJFIFBBUkEgU1VNSU5JU1RSTyBERSBFTEVDVFJJQ0lEQURkZAIPDw8WAh8DBRRUaXBvIGRlIGxpY2l0YWNpw7NuOmRkAhEPDxYCHwMFVlDDumJsaWNhLUxpY2l0YWNpw7NuIFDDumJsaWNhIGlndWFsIG8gc3VwZXJpb3IgYSAxLjAwMCBVVE0gZSBpbmZlcmlvciBhIDIuMDAwIFVUTSAoTFApZGQCFQ8PFgIfAwUVVGlwbyBkZSBjb252b2NhdG9yaWE6ZGQCFw8PFgIfAwUHQUJJRVJUT2RkAiMPDxYCHwMFB01vbmVkYTpkZAIlDw8WAh8DBQxQZXNvIENoaWxlbm9kZAInDw8WAh8DBR9FdGFwYXMgZGVsIHByb2Nlc28gZGUgYXBlcnR1cmE6ZGQCKQ8PFgIfAwUJVW5hIEV0YXBhZGQCKw9kFgICAQ8PFgIfAwUIQ29udHJhdG9kZAItD2QWBAIBDw8WAh8DBSBUb21hIGRlIHJhesOzbiBwb3IgQ29udHJhbG9yw61hOmRkAgMPDxYCHwMFK05vIHJlcXVpZXJlIFRvbWEgZGUgUmF6w7NuIHBvciBDb250cmFsb3LDrWFkZAIvDw8WAh8DBSBQdWJsaWNpZGFkIGRlIG9mZXJ0YXMgdMOpY25pY2FzOmRkAjEPDxYCHwMFbExhcyBvZmVydGFzIHTDqWNuaWNhcyBzZXLDoW4gZGUgcMO6YmxpY28gY29ub2NpbWllbnRvIHVuYSB2ZXogcmVhbGl6YWRhIGxhIGFwZXJ0dXJhIHTDqWNuaWNhIGRlIGxhcyBvZmVydGFzLmRkAisPZBYcAgEPDxYCHwMFFzIuIE9yZ2FuaXNtbyBkZW1hbmRhbnRlZGQCAw8PFgIfAwUOUmF6w7NuIHNvY2lhbDpkZAIFDw8WAh8DBSZDT1JQIEFETUlOSVNUUkFUSVZBIERFTCBQT0RFUiBKVURJQ0lBTGRkAgcPDxYCHwMFEVVuaWRhZCBkZSBjb21wcmE6ZGQCCQ8PFgIfAwUmQ29ycC4gQWRtLiBkZWwgUG9kZXIgSnVkaWNpYWwgLSBUZW11Y29kZAILDw8WAh8DBQdSLlUuVC46ZGQCDQ8PFgIfAwUMNjAuMzAxLjAwMS05ZGQCDw8PFgIfAwULRGlyZWNjacOzbjpkZAIRDw8WAh8DBQ9DQVVQT0xJQ0FOIDEwNzdkZAITDw8WAh8CaGRkAhUPDxYCHwMFB0NvbXVuYTpkZAIXDw8WAh8DBQZUZW11Y29kZAIZDw8WAh8DBShSZWdpw7NuIGVuIHF1ZSBzZSBnZW5lcmEgbGEgbGljaXRhY2nDs246ZGQCGw8PFgIfAwUZUmVnacOzbiBkZSBsYSBBcmF1Y2Fuw61hIGRkAi0PZBY0Zg8PFgIfAwUSMy4gRXRhcGFzIHkgcGxhem9zZGQCAQ8WAh8LBSp0ZXh0LWFsaWduOmNlbnRlciAhaW1wb3J0YW50O2Rpc3BsYXk6bm9uZTtkAgIPFgQfBAUNYm9yZGVfdGFibGEwMB8LBRJ0ZXh0LWFsaWduOmNlbnRlcjsWBAIBDw8WAh8DBStGZWNoYSBkZSBjaWVycmUgZGUgcmVjZXBjacOzbiBkZSBsYSBvZmVydGE6ZGQCAw8PFgIfAwUTMjAtMDctMjAyMiAxNDowMDowMGRkAgMPDxYCHwMFFkZlY2hhIGRlIFB1YmxpY2FjacOzbjpkZAIEDw8WAh8DBRMyNC0wNi0yMDIyIDIxOjUyOjMwZGQCBQ8PFgIfAwUaRmVjaGEgaW5pY2lvIGRlIHByZWd1bnRhczpkZAIGDw8WAh8DBRMyNC0wNi0yMDIyIDIzOjAxOjAwZGQCBw8PFgIfAwUZRmVjaGEgZmluYWwgZGUgcHJlZ3VudGFzOmRkAggPDxYCHwMFEzA3LTA3LTIwMjIgMTU6MDA6MDBkZAIJDw8WAh8DBSRGZWNoYSBkZSBwdWJsaWNhY2nDs24gZGUgcmVzcHVlc3RhczpkZAIKDw8WAh8DBRMxMy0wNy0yMDIyIDE3OjAwOjAwZGQCCw8PFgIfAwUjRmVjaGEgZGUgYWN0byBkZSBhcGVydHVyYSB0w6ljbmljYTpkZAIMDw8WAh8DBRMyMS0wNy0yMDIyIDE0OjAwOjAwZGQCDQ9kFgQCAQ8PFgIfAwUzRmVjaGEgZGUgYWN0byBkZSBhcGVydHVyYSBlY29uw7NtaWNhIChyZWZlcmVuY2lhbCk6ZGQCAw8PFgIfAwUTMjEtMDctMjAyMiAxNDowMDowMGRkAg4PZBYEAgEPDxYCHwMFF0ZlY2hhIGRlIEFkanVkaWNhY2nDs246ZGQCAw8PFgIfAwUTMTYtMDgtMjAyMiAxNzowMDowMGRkAg8PFgIfAmhkAhAPFgIfCwUNZGlzcGxheTpub25lO2QCEQ8WAh8LBQ1kaXNwbGF5Om5vbmU7ZAISDxYCHwsFDWRpc3BsYXk6bm9uZTtkAhMPZBYEAgEPDxYCHwMFIkZlY2hhIGRlIGVudHJlZ2EgZW4gc29wb3J0ZSBmaXNpY29kZAIDDw8WAh8DBRNObyBoYXkgaW5mb3JtYWNpw7NuZGQCFA9kFgQCAQ8PFgIfAwUjRmVjaGEgZXN0aW1hZGEgZGUgZmlybWEgZGUgY29udHJhdG9kZAIDDw8WAh8DBRNObyBoYXkgaW5mb3JtYWNpw7NuZGQCFQ9kFgQCAQ8PFgIfAwUpVGllbXBvIGVzdGltYWRvIGRlIGV2YWx1YWNpw7NuIGRlIG9mZXJ0YXNkZAIDDw8WAh8DBRNObyBoYXkgaW5mb3JtYWNpw7NuZGQCFg9kFgICAQ8PFgQfCWgfAmhkZAIXD2QWAgIBDw8WAh8DBYsDDQogICAgPGI+RXh0ZW5zacOzbiBhdXRvbcOhdGljYSBkZWwgcGxhem8gZGUgb2ZlcnRhczo8L2I+PC9icj48L2JyPg0KICAgIFNlIGVzdGFibGVjacOzIHBhcmEgZXN0YSBsaWNpdGFjacOzbiBxdWU6ICJTaSBhIGxhIGZlY2hhIGRlIHJlY2VwY2nDs24gZGUgb2ZlcnRhcywgc2UgaGFuIHJlY2liaWRvIDIgbyBtZW5vcyBwcm9wdWVzdGFzLCA8Yj5lbCBwbGF6byBkZSBjaWVycmUgc2UgYW1wbGlhcsOhIGF1dG9tw6F0aWNhbWVudGUgZW4gMiBkw61hcyBow6FiaWxlczwvYj4sIHBvciB1bmEgc29sYSB2ZXosIGJham8gbGFzIGNvbmRpY2lvbmVzIGVzdGFibGVjaWRhcyBlbiBlbCBhcnTDrWN1bG8gMjUsIGluY2lzbyBvY3Rhdm8sIGRlbCBSZWdsYW1lbnRvIGRlIGxhIGxleSAxOS44ODYuIg0KICBkZAIYDxYCHwJnZAIZD2QWAgIBDzwrABEDAA8WBB8MZx8NAgFkARAWABYAFgAMFCsAABYCZg9kFgZmDw8WAh8CaGRkAgEPZBYCZg9kFgoCAQ8PFgIfAwUrVklTSVRBIFRFUlJFTk8gT0JMSUdBVE9SSUEgU0VHVU4gQ1JPTk9HUkFNQWRkAgMPDxYCHwMFEzA0LTA3LTIwMjIgMTU6MDA6MDBkZAIFDw8WAh8DBQEwZGQCBw8PFgIfAwUBMGRkAgkPDxYCHwMFEzA0LTA3LTIwMjIgMTU6MDA6MDBkZAICDw8WAh8CaGRkAi4PZBYEZg8PFgIfAwUpNC4gQW50ZWNlZGVudGVzIHBhcmEgaW5jbHVpciBlbiBsYSBvZmVydGFkZAICD2QWDGYPDxYCHwMFGkRvY3VtZW50b3MgQWRtaW5pc3RyYXRpdm9zZGQCAQ88KwARAwAPFgQfDGcfDQIBZAEQFgAWABYADBQrAAAWAmYPZBYGZg8PFgIfAmhkZAIBD2QWAmYPZBYMAgEPDxYCHwMFBTEuLSAgZGQCAw8PFgIfA2VkZAIFDw8WAh8DBRZBTkVYT1MgQURNSU5JU1RSQVRJVk9TZGQCBw8PFgIfAwUBMWRkAgkPDxYCHwMFCDI0MzgzNTk1ZGQCCw9kFgRmD2QWAgIBDw8WBB4PQ29tbWFuZEFyZ3VtZW50BQExHwJnFgQfBAUMZmFuY3lBZGp1bnRvHwUFsQQuLi9BdHRhY2htZW50L1ZlckFudGVjZWRlbnRlcy5hc3B4P2VuYz0wMVR2UEglMmZnb0IxTVBucGtxWUFlZTVsZ3c1a1lWSDJZbXp3eERtS3pUYk5jSFpuJTJiS0xXNTh6bDVyZUJJQktBN2wwJTJmSHU1UXpvNndWJTJiJTJmUVV3cDF5VWlUdzFlTmdaekdmbXIwb1Y4VGJrQkVJdFVZNVJXc0pheFN1REdDR0twcjlCbWF3JTJiSXJZMzhkYjdCRURlMktDQkdIMmxLZmZUalNHUUZRQ29CdXczZHlQTGFUMW4wZUZJNTBiV3hoRnRxTVU4SktENkE3OHdGSnVWRUlhQUdWb3VqU1EyJTJiWll3M3hEc25OWVJkQ2VOTTBhTmVFQm5tNm90RDNldTFhZ1VUeE0yTXI4YldVQjBmQnRpM1RoQSUyZkV2ZnpqY3pHOXUlMmZtZkYzNmQycEFxVlRLQldJYmNyTWtLVVF0b3YxWUd2WDVQZHliQXJCU0x3WmNyTTVybHRKcHRQNjhTQ2h2RGRCb1RkS2NhbFhScnp6RkxpJTJicW91NlA3UU5IQkdCaXNvZmhzYzI2RGYyaUFtQWJhbUIxQmRGT3pjZ3FKYk9aJTJmSVI5U1FVRUtxdURhaVQ2NEk1RENqT3RFMm9zdGwlMmJRd0piYUNhcTdqamxQODdERmtYTjREeHplRmUlMmJ1cmJuJTJiVXJSQ0FONWhMNUJsSmFQTjQlM2RkAgEPZBYCAgEPDxYEHw4FATEfAmcWBB8EBQxmYW5jeUFkanVudG8fBQWxBC4uL0F0dGFjaG1lbnQvVmVyQW50ZWNlZGVudGVzLmFzcHg/ZW5jPTAxVHZQSCUyZmdvQjFNUG5wa3FZQWVlNWxndzVrWVZIMlltend4RG1LelRiTmNIWm4lMmJLTFc1OHpsNXJlQklCS0E3bDAlMmZIdTVRem82d1YlMmIlMmZRVXdwMXlVaVR3MWVOZ1p6R2ZtcjBvVjhUYmtCRUl0VVk1UldzSmF4U3VER0NHS3ByOUJtYXclMmJJclkzOGRiN0JFRGUyS0NCR0gybEtmZlRqU0dRRlFDb0J1dzNkeVBMYVQxbjBlRkk1MGJXeGhGdHFNVThKS0Q2QTc4d0ZKdVZFSWFBR1ZvdWpTUTIlMmJaWXczeERzbk5ZUmRDZU5NMGFOZUVCbm02b3REM2V1MWFnVVR4TTJNcjhiV1VCMGZCdGkzVGhBJTJmRXZmempjekc5dSUyZm1mRjM2ZDJwQXFWVEtCV0liY3JNa0tVUXRvdjFZR3ZYNVBkeWJBckJTTHdaY3JNNXJsdEpwdFA2OFNDaHZEZEJvVGRLY2FsWFJyenpGTGklMmJxb3U2UDdRTkhCR0Jpc29maHNjMjZEZjJpQW1BYmFtQjFCZEZPemNncUpiT1olMmZJUjlTUVVFS3F1RGFpVDY0STVEQ2pPdEUyb3N0bCUyYlF3SmJhQ2FxN2pqbFA4N0RGa1hONER4emVGZSUyYnVyYm4lMmJVclJDQU41aEw1QmxKYVBONCUzZGQCAg8PFgIfAmhkZAICDw8WAh8DBS1ObyBoYXkgaW5mb3JtYWNpw7NuIGRlIEFudGVjZWRlbnRlcyBUw6ljbmljb3NkZAIDDzwrABEDAA8WAh8CaGQBEBYAFgAWAAwUKwAAZAIEDw8WAh8DBRZEb2N1bWVudG9zIEVjb27Ds21pY29zZGQCBQ88KwARAwAPFgQfDGcfDQIBZAEQFgAWABYADBQrAAAWAmYPZBYGZg8PFgIfAmhkZAIBD2QWAmYPZBYKAgEPDxYCHwMFBDEuLSBkZAIDDw8WAh8DBRFBTkVYT1MgRUNPTk9NSUNPU2RkAgUPDxYCHwMFATFkZAIHDw8WAh8DBQgyNDM4MzU5OGRkAgkPZBYEZg9kFgICAQ8PFgQfDgUBMR8CZxYEHwQFDGZhbmN5QWRqdW50bx8FBcMELi4vQXR0YWNobWVudC9WZXJBbnRlY2VkZW50ZXMuYXNweD9lbmM9NGloUjdzV25jbXZXYzhFWEh1SmlWVm4lMmJrZ2VScmd3b1QzemUxeWxJMnJEJTJmJTJmY0VsMyUyYjJ6aEdJZXBMZ0lBZzJRZHlEUVlPdCUyYmlHc3dYTG1ZY0tUTmpxWXFWV0JlbUFCWlNma3hpNktDZTRwWU5QaXNaeDlMa2VLT0lPcm9DNkRPYm9xJTJienNaaHZQJTJmUmZjbWE0dk0lMmJQeXB6QjNBM3V1Tk9pN2JQJTJiJTJiUkNDRFBKUm1jWEIyNzAlMmJMNUxKMkJ1SzYlMmJKYTl5YlhmMHh6S2lVZzk4cW5ZWjcxckVYMGVYNzQlMmY5MkFKM3JvJTJia0w0MVNTYmlTSnZiWDd1JTJiVFZLdWVWU1pxVW8lMmJuQUIwdTlYSHZRbUtyeE43OG03T3pBTzUzeko1TVh2ZDFmYVdqY3UlMmJHNjYwVUxIaVVpZ2NXNU5oV2RhaDZNZHNHcThiUm9PanVNaUhFVFJXZFBydGpBdmZ1QkU5SldWUEZjODJzbmlHMjZXTGIlMmZRRGd0R3JpWUVSNG9rY21iUGZYcnkwODlyYjRwVTNXTFhhMUFWJTJia1lsSjl4NU5ydXAxVHBXWEVzYW1mSmtVJTJiTXpRamhoZ2hLdkRPNmo4JTJmN2RSVmFUVEw1YlhUd09WOCUyYkhHVjdySiUyZlladERhVjBwSEx6Y0sxcDI5RkpvJTNkZAIBD2QWAgIBDw8WBB8OBQExHwJnFgQfBAUMZmFuY3lBZGp1bnRvHwUFwwQuLi9BdHRhY2htZW50L1ZlckFudGVjZWRlbnRlcy5hc3B4P2VuYz00aWhSN3NXbmNtdldjOEVYSHVKaVZWbiUyYmtnZVJyZ3dvVDN6ZTF5bEkyckQlMmYlMmZjRWwzJTJiMnpoR0llcExnSUFnMlFkeURRWU90JTJiaUdzd1hMbVljS1ROanFZcVZXQmVtQUJaU2ZreGk2S0NlNHBZTlBpc1p4OUxrZUtPSU9yb0M2RE9ib3ElMmJ6c1podlAlMmZSZmNtYTR2TSUyYlB5cHpCM0EzdXVOT2k3YlAlMmIlMmJSQ0NEUEpSbWNYQjI3MCUyYkw1TEoyQnVLNiUyYkphOXliWGYweHpLaVVnOThxbllaNzFyRVgwZVg3NCUyZjkyQUozcm8lMmJrTDQxU1NiaVNKdmJYN3UlMmJUVkt1ZVZTWnFVbyUyYm5BQjB1OVhIdlFtS3J4Tjc4bTdPekFPNTN6SjVNWHZkMWZhV2pjdSUyYkc2NjBVTEhpVWlnY1c1TmhXZGFoNk1kc0dxOGJSb09qdU1pSEVUUldkUHJ0akF2ZnVCRTlKV1ZQRmM4MnNuaUcyNldMYiUyZlFEZ3RHcmlZRVI0b2tjbWJQZlhyeTA4OXJiNHBVM1dMWGExQVYlMmJrWWxKOXg1TnJ1cDFUcFdYRXNhbWZKa1UlMmJNelFqaGhnaEt2RE82ajglMmY3ZFJWYVRUTDViWFR3T1Y4JTJiSEdWN3JKJTJmWVp0RGFWMHBITHpjSzFwMjlGSm8lM2RkAgIPDxYCHwJoZGQCMA9kFhYCAQ8PFgIfAwU0NS4gUmVxdWlzaXRvcyBwYXJhIGNvbnRyYXRhciBhbCBwcm92ZWVkb3IgYWRqdWRpY2Fkb2RkAgMPDxYCHwMFD1BlcnNvbmEgbmF0dXJhbGRkAgUPDxYCHwMFiAFFbmNvbnRyYXJzZSBow6FiaWwgZW4gZWwgUmVnaXN0cm8gZGUgUHJvdmVlZG9yZXMsIHJlZ2lzdHJvIHF1ZSB2ZXJpZmljYXLDoSBOTyBoYWJlciBpbmN1cnJpZG8gZW4gbGFzIHNpZ3VpZW50ZXMgY2F1c2FsZXMgZGUgaW5oYWJpbGlkYWQ6ZGQCBw88KwARAwAPFgQfDGcfDQIIZAEQFgAWABYADBQrAAAWAmYPZBYUZg8PFgIfAmhkZAIBD2QWAmYPZBYEAgEPDxYCHwMFATFkZAIFDw8WAh8DBX9IYWJlciBzaWRvIGNvbmRlbmFkbyBwb3IgY3VhbHF1aWVyYSBkZSBsb3MgZGVsaXRvcyBkZSBjb2hlY2hvIGNvbnRlbXBsYWRvcyBlbiBlbCB0w610dWxvIFYgZGVsIExpYnJvIFNlZ3VuZG8gZGVsIEPDs2RpZ28gUGVuYWwuZGQCAg9kFgJmD2QWBAIBDw8WAh8DBQEyZGQCBQ8PFgIfAwWIA1JlZ2lzdHJhciB1bmEgbyBtw6FzIGRldWRhcyB0cmlidXRhcmlhcyBwb3IgdW4gbW9udG8gdG90YWwgc3VwZXJpb3IgYSA1MDAgVVRNIHBvciBtw6FzIGRlIHVuIGHDsW8sIG8gc3VwZXJpb3IgYSAyMDAgVVRNIGUgaW5mZXJpb3IgYSA1MDAgVVRNIHBvciB1biBwZXLDrW9kbyBzdXBlcmlvciBhIDIgYcOxb3MsIHNpbiBxdWUgZXhpc3RhIHVuIGNvbnZlbmlvIGRlIHBhZ28gdmlnZW50ZS4gRW4gY2FzbyBkZSBlbmNvbnRyYXJzZSBwZW5kaWVudGUganVpY2lvIHNvYnJlIGxhIGVmZWN0aXZpZGFkIGRlIGxhIGRldWRhLCBlc3RhIGluaGFiaWxpZGFkIHJlZ2lyw6EgdW5hIHZleiBxdWUgc2UgZW5jdWVudHJlIGZpcm1lIG8gZWplY3V0b3JpYWRhIGxhIHJlc3BlY3RpdmEgcmVzb2x1Y2nDs24uZGQCAw9kFgJmD2QWBAIBDw8WAh8DBQEzZGQCBQ8PFgIfAwWoAVJlZ2lzdHJhciBkZXVkYXMgcHJldmlzaW9uYWxlcyBvIGRlIHNhbHVkIHBvciBtw6FzIGRlIDEyIG1lc2VzIHBvciBzdXMgdHJhYmFqYWRvcmVzIGRlcGVuZGllbnRlcywgbG8gcXVlIHNlIGFjcmVkaXRhcsOhIG1lZGlhbnRlIGNlcnRpZmljYWRvIGRlIGxhIGF1dG9yaWRhZCBjb21wZXRlbnRlLmRkAgQPZBYCZg9kFgQCAQ8PFgIfAwUBNGRkAgUPDxYCHwMFiQFMYSBwcmVzZW50YWNpw7NuIGFsIFJlZ2lzdHJvIE5hY2lvbmFsIGRlIFByb3ZlZWRvcmVzIGRlIHVubyBvIG3DoXMgZG9jdW1lbnRvcyBmYWxzb3MsIGRlY2xhcmFkbyBhc8OtIHBvciBzZW50ZW5jaWEganVkaWNpYWwgZWplY3V0b3JpYWRhLmRkAgUPZBYCZg9kFgQCAQ8PFgIfAwUBNWRkAgUPDxYCHwMFRkhhYmVyIHNpZG8gZGVjbGFyYWRvIGVuIHF1aWVicmEgcG9yIHJlc29sdWNpw7NuIGp1ZGljaWFsIGVqZWN1dG9yaWFkYS5kZAIGD2QWAmYPZBYEAgEPDxYCHwMFATZkZAIFDw8WAh8DBYcBSGFiZXIgc2lkbyBlbGltaW5hZG8gbyBlbmNvbnRyYXJzZSBzdXNwZW5kaWRvIGRlbCBSZWdpc3RybyBOYWNpb25hbCBkZSBQcm92ZWVkb3JlcyBwb3IgcmVzb2x1Y2nDs24gZnVuZGFkYSBkZSBsYSBEaXJlY2Npw7NuIGRlIENvbXByYXMuZGQCBw9kFgJmD2QWBAIBDw8WAh8DBQE3ZGQCBQ8PFgIfAwVtSGFiZXIgc2lkbyBjb25kZW5hZG8gcG9yIHByw6FjdGljYXMgYW50aXNpbmRpY2FsZXMgbyBpbmZyYWNjacOzbiBhIGxvcyBkZXJlY2hvcyBmdW5kYW1lbnRhbGVzIGRlbCB0cmFiYWphZG9yLmRkAggPZBYCZg9kFgQCAQ8PFgIfAwUBOGRkAgUPDxYCHwMFaVJlZ2lzdHJhciBjb25kZW5hcyBhc29jaWFkYXMgYSByZXNwb25zYWJpbGlkYWQgcGVuYWwganVyw61kaWNhIChpbmN1bXBsaW1pZW50byBhcnTDrWN1bG8gMTAsIExleSAyMC4zOTMpLmRkAgkPDxYCHwJoZGQCCQ8PFgIfAwUaRG9jdW1lbnRvcyBwZXJzb25hIG5hdHVyYWxkZAILDzwrABEDAA8WBB8MZx8NAgJkARAWABYAFgAMFCsAABYCZg9kFghmDw8WAh8CaGRkAgEPZBYCZg9kFgYCAQ8PFgIfAwUuLSBGb3RvY29waWEgTGVnYWxpemFkYSBkZSBDw6lkdWxhIGRlIElkZW50aWRhZGRkAgMPDxYCHwMFATRkZAIFDw8WAh8DBQItMWRkAgIPZBYCZg9kFgYCAQ8PFgIfAwX8Ai0gRGVjbGFyYWNpw7NuIGp1cmFkYSBhY3JlZGl0YW5kbyBxdWUgbm8gc2UgZW5jdWVudHJhIGFmZWN0byBhbCBhcnQuIDQgaW5jaXNvIDYgZGUgbGEgbGV5IDE5Ljg4NiwgZW4gZWwgY3VhbCBzZSBlc3RhYmxlY2UgcXVlICJuaW5nw7puIMOzcmdhbm8gZGUgbGEgYWRtaW5pc3RyYWNpw7NuIGRlbCBFc3RhZG8gcG9kcsOhIHN1c2NyaWJpciBjb250cmF0b3MgYWRtaW5pc3RyYXRpdm9zIGRlIHByb3Zpc2nDs24gZGUgYmllbmVzIHkgc2VydmljaW9zIGNvbiBsb3MgZnVuY2lvbmFyaW9zIGRpcmVjdGl2b3MgZGVsIG1pc21vIMOzcmdhbm8gbyBlbXByZXNhLCBuaSBjb24gcGVyc29uYXMgdW5pZGFzIGEgZWxsb3MgcG9yIGxvcyB2w61uY3Vsb3MgZGUgcGFyZW50ZXNjby4iZGQCAw8PFgIfAwUBNmRkAgUPDxYCHwMFAi0xZGQCAw8PFgIfAmhkZAINDw8WAh8DBRFQZXJzb25hIGp1csOtZGljYWRkAg8PDxYCHwMFiAFFbmNvbnRyYXJzZSBow6FiaWwgZW4gZWwgUmVnaXN0cm8gZGUgUHJvdmVlZG9yZXMsIHJlZ2lzdHJvIHF1ZSB2ZXJpZmljYXLDoSBOTyBoYWJlciBpbmN1cnJpZG8gZW4gbGFzIHNpZ3VpZW50ZXMgY2F1c2FsZXMgZGUgaW5oYWJpbGlkYWQ6ZGQCEQ88KwARAwAPFgQfDGcfDQIIZAEQFgAWABYADBQrAAAWAmYPZBYUZg8PFgIfAmhkZAIBD2QWAmYPZBYEAgEPDxYCHwMFATFkZAIFDw8WAh8DBX9IYWJlciBzaWRvIGNvbmRlbmFkbyBwb3IgY3VhbHF1aWVyYSBkZSBsb3MgZGVsaXRvcyBkZSBjb2hlY2hvIGNvbnRlbXBsYWRvcyBlbiBlbCB0w610dWxvIFYgZGVsIExpYnJvIFNlZ3VuZG8gZGVsIEPDs2RpZ28gUGVuYWwuZGQCAg9kFgJmD2QWBAIBDw8WAh8DBQEyZGQCBQ8PFgIfAwWIA1JlZ2lzdHJhciB1bmEgbyBtw6FzIGRldWRhcyB0cmlidXRhcmlhcyBwb3IgdW4gbW9udG8gdG90YWwgc3VwZXJpb3IgYSA1MDAgVVRNIHBvciBtw6FzIGRlIHVuIGHDsW8sIG8gc3VwZXJpb3IgYSAyMDAgVVRNIGUgaW5mZXJpb3IgYSA1MDAgVVRNIHBvciB1biBwZXLDrW9kbyBzdXBlcmlvciBhIDIgYcOxb3MsIHNpbiBxdWUgZXhpc3RhIHVuIGNvbnZlbmlvIGRlIHBhZ28gdmlnZW50ZS4gRW4gY2FzbyBkZSBlbmNvbnRyYXJzZSBwZW5kaWVudGUganVpY2lvIHNvYnJlIGxhIGVmZWN0aXZpZGFkIGRlIGxhIGRldWRhLCBlc3RhIGluaGFiaWxpZGFkIHJlZ2lyw6EgdW5hIHZleiBxdWUgc2UgZW5jdWVudHJlIGZpcm1lIG8gZWplY3V0b3JpYWRhIGxhIHJlc3BlY3RpdmEgcmVzb2x1Y2nDs24uZGQCAw9kFgJmD2QWBAIBDw8WAh8DBQEzZGQCBQ8PFgIfAwWoAVJlZ2lzdHJhciBkZXVkYXMgcHJldmlzaW9uYWxlcyBvIGRlIHNhbHVkIHBvciBtw6FzIGRlIDEyIG1lc2VzIHBvciBzdXMgdHJhYmFqYWRvcmVzIGRlcGVuZGllbnRlcywgbG8gcXVlIHNlIGFjcmVkaXRhcsOhIG1lZGlhbnRlIGNlcnRpZmljYWRvIGRlIGxhIGF1dG9yaWRhZCBjb21wZXRlbnRlLmRkAgQPZBYCZg9kFgQCAQ8PFgIfAwUBNGRkAgUPDxYCHwMFiQFMYSBwcmVzZW50YWNpw7NuIGFsIFJlZ2lzdHJvIE5hY2lvbmFsIGRlIFByb3ZlZWRvcmVzIGRlIHVubyBvIG3DoXMgZG9jdW1lbnRvcyBmYWxzb3MsIGRlY2xhcmFkbyBhc8OtIHBvciBzZW50ZW5jaWEganVkaWNpYWwgZWplY3V0b3JpYWRhLmRkAgUPZBYCZg9kFgQCAQ8PFgIfAwUBNWRkAgUPDxYCHwMFRkhhYmVyIHNpZG8gZGVjbGFyYWRvIGVuIHF1aWVicmEgcG9yIHJlc29sdWNpw7NuIGp1ZGljaWFsIGVqZWN1dG9yaWFkYS5kZAIGD2QWAmYPZBYEAgEPDxYCHwMFATZkZAIFDw8WAh8DBYcBSGFiZXIgc2lkbyBlbGltaW5hZG8gbyBlbmNvbnRyYXJzZSBzdXNwZW5kaWRvIGRlbCBSZWdpc3RybyBOYWNpb25hbCBkZSBQcm92ZWVkb3JlcyBwb3IgcmVzb2x1Y2nDs24gZnVuZGFkYSBkZSBsYSBEaXJlY2Npw7NuIGRlIENvbXByYXMuZGQCBw9kFgJmD2QWBAIBDw8WAh8DBQE3ZGQCBQ8PFgIfAwVtSGFiZXIgc2lkbyBjb25kZW5hZG8gcG9yIHByw6FjdGljYXMgYW50aXNpbmRpY2FsZXMgbyBpbmZyYWNjacOzbiBhIGxvcyBkZXJlY2hvcyBmdW5kYW1lbnRhbGVzIGRlbCB0cmFiYWphZG9yLmRkAggPZBYCZg9kFgQCAQ8PFgIfAwUBOGRkAgUPDxYCHwMFaVJlZ2lzdHJhciBjb25kZW5hcyBhc29jaWFkYXMgYSByZXNwb25zYWJpbGlkYWQgcGVuYWwganVyw61kaWNhIChpbmN1bXBsaW1pZW50byBhcnTDrWN1bG8gMTAsIExleSAyMC4zOTMpLmRkAgkPDxYCHwJoZGQCEw8PFgIfAwUcRG9jdW1lbnRvcyBwZXJzb25hIGp1csOtZGljYWRkAhUPPCsAEQMADxYEHwxnHw0CBWQBEBYAFgAWAAwUKwAAFgJmD2QWDmYPDxYCHwJoZGQCAQ9kFgJmD2QWBgIBDw8WAh8DBSwtIEZvdG9jb3BpYSBMZWdhbGl6YWRhIGRlbCBSdXQgZGUgbGEgRW1wcmVzYWRkAgMPDxYCHwMFATVkZAIFDw8WAh8DBQItMWRkAgIPZBYCZg9kFgYCAQ8PFgIfAwX8Ai0gRGVjbGFyYWNpw7NuIGp1cmFkYSBhY3JlZGl0YW5kbyBxdWUgbm8gc2UgZW5jdWVudHJhIGFmZWN0byBhbCBhcnQuIDQgaW5jaXNvIDYgZGUgbGEgbGV5IDE5Ljg4NiwgZW4gZWwgY3VhbCBzZSBlc3RhYmxlY2UgcXVlICJuaW5nw7puIMOzcmdhbm8gZGUgbGEgYWRtaW5pc3RyYWNpw7NuIGRlbCBFc3RhZG8gcG9kcsOhIHN1c2NyaWJpciBjb250cmF0b3MgYWRtaW5pc3RyYXRpdm9zIGRlIHByb3Zpc2nDs24gZGUgYmllbmVzIHkgc2VydmljaW9zIGNvbiBsb3MgZnVuY2lvbmFyaW9zIGRpcmVjdGl2b3MgZGVsIG1pc21vIMOzcmdhbm8gbyBlbXByZXNhLCBuaSBjb24gcGVyc29uYXMgdW5pZGFzIGEgZWxsb3MgcG9yIGxvcyB2w61uY3Vsb3MgZGUgcGFyZW50ZXNjby4iZGQCAw8PFgIfAwUBN2RkAgUPDxYCHwMFAi0xZGQCAw9kFgJmD2QWBgIBDw8WAh8DBSgtIENlcnRpZmljYWRvIGRlIFZpZ2VuY2lhIGRlIGxhIFNvY2llZGFkZGQCAw8PFgIfAwUBN2RkAgUPDxYCHwMFAi0xZGQCBA9kFgJmD2QWBgIBDw8WAh8DBVItIDxmb250IGNvbG9yPScjQ0MwMDMzJz4oMSk8L2ZvbnQ+IENlcnRpZmljYWRvIGRlIEJvbGV0w61uIGRlIEluZm9ybWVzIENvbWVyY2lhbGVzZGQCAw8PFgIfAwUBN2RkAgUPDxYCHwMFAi0xZGQCBQ9kFgJmD2QWBgIBDw8WAh8DBUwtIDxmb250IGNvbG9yPScjQ0MwMDMzJz4oMSk8L2ZvbnQ+IENlcnRpZmljYWRvIGRlIFF1aWVicmFzL0NvbnZlbmlvIEp1ZGljaWFsZGQCAw8PFgIfAwUBN2RkAgUPDxYCHwMFAi0xZGQCBg8PFgIfAmhkZAIyD2QWBmYPDxYCHwMFGzYuIENyaXRlcmlvcyBkZSBldmFsdWFjacOzbmRkAgIPPCsAEQMADxYEHwxnHw0CBGQBEBYDZgIBAgIWAxQrAAUWAh4KSGVhZGVyVGV4dAUFw410ZW1kFgYeD0hvcml6b250YWxBbGlnbgsqKVN5c3RlbS5XZWIuVUkuV2ViQ29udHJvbHMuSG9yaXpvbnRhbEFsaWduAR4IQ3NzQ2xhc3MFEXRpdHVsb0NyaXRlcmlvSXpxHgRfIVNCAoKABGRkFCsABRYCHw8FDU9ic2VydmFjaW9uZXNkFgYfEAsrBAEfEQUOdGl0dWxvQ3JpdGVyaW8fEgKCgARkZBQrAAUWAh8PBQxQb25kZXJhY2nDs25kFgYfEAsrBAEfEQURdGl0dWxvQ3JpdGVyaW9EZXIfEgKCgARkZBYDAgYCBgIGDBQrAAAWAmYPZBYKAgEPZBYGZg9kFgQCAQ8PFgIfAwUBMWRkAgMPDxYCHwMFB1RFQ05JQ09kZAIBD2QWAgIBDw8WAh8DZWRkAgIPZBYCAgEPDxYCHwMFAzQ1JRYCHgVTdHlsZQU2dGV4dC1hbGlnbjpjZW50ZXI7dmVydGljYWwtYWxpZ246dG9wO2ZvbnQtd2VpZ2h0OmJvbGQ7ZAICD2QWBmYPZBYEAgEPDxYCHwMFATJkZAIDDw8WAh8DBQlFQ09OT01JQ09kZAIBD2QWAgIBDw8WAh8DZWRkAgIPZBYCAgEPDxYCHwMFAzQwJRYCHxMFNnRleHQtYWxpZ246Y2VudGVyO3ZlcnRpY2FsLWFsaWduOnRvcDtmb250LXdlaWdodDpib2xkO2QCAw9kFgZmD2QWBAIBDw8WAh8DBQEzZGQCAw8PFgIfAwULUEFUUklNT05JQUxkZAIBD2QWAgIBDw8WAh8DZWRkAgIPZBYCAgEPDxYCHwMFAzEwJRYCHxMFNnRleHQtYWxpZ246Y2VudGVyO3ZlcnRpY2FsLWFsaWduOnRvcDtmb250LXdlaWdodDpib2xkO2QCBA9kFgZmD2QWBAIBDw8WAh8DBQE0ZGQCAw8PFgIfAwUMRk9STUFMSURBREVTZGQCAQ9kFgICAQ8PFgIfA2VkZAICD2QWAgIBDw8WAh8DBQI1JRYCHxMFNnRleHQtYWxpZ246Y2VudGVyO3ZlcnRpY2FsLWFsaWduOnRvcDtmb250LXdlaWdodDpib2xkO2QCBQ8PFgIfAmhkZAIFDzwrABECARAWABYAFgAMFCsAAGQCNA9kFh5mDw8WAh8DBSI3LiBNb250b3MgeSBkdXJhY2nDs24gZGVsIGNvbnRyYXRvZGQCAQ9kFgQCAQ8PFgIfAwUWRXN0aW1hY2nDs24gZW4gYmFzZSBhOmRkAgMPDxYCHwMFFlByZXN1cHVlc3RvIERpc3BvbmlibGVkZAICDw8WAh8DBRlGdWVudGUgZGUgZmluYW5jaWFtaWVudG86ZGQCAw8PFgIfAwUTTm8gaGF5IGluZm9ybWFjacOzbmRkAgQPFgIfCwUNZGlzcGxheTpub25lOxYCAgUPZBYCAgEPDxYEHwloHwJoZGQCBQ8WAh8CaBYCZg9kFgICAQ8PFgIfAwUhSnVzdGlmaWNhY2nDs24gZGVsIG1vbnRvIGVzdGltYWRvZGQCBw9kFgRmD2QWAgIBDw8WAh8DBRlDb250cmF0byBjb24gUmVub3ZhY2nDs246ZGQCAQ9kFgICAQ8PFgIfAwUCTk9kZAIIDxYCHwJoFgJmD2QWAgIBDw8WAh8DBRtKdXN0aWZpY2FjacOzbiBSZW5vdmFjacOzbjpkZAIJD2QWBAIBD2QWBGYPZBYCAgEPDxYCHwMFDU9ic2VydmFjaW9uZXNkZAIBD2QWAgIBDw8WAh8DBRFTaW4gb2JzZXJ2YWNpb25lc2RkAgMPFgIfAmhkAgoPZBYEAgEPFgIfAmgWAmYPZBYCAgEPDxYCHwMFFUR1cmFjacOzbiBkZSBDb250cmF0b2RkAgMPFgIfAmgWAmYPZBYCAgEPDxYCHwMFE1RpZW1wbyBkZWwgQ29udHJhdG9kZAILD2QWCgIBDw8WAh8DBQ9QbGF6b3MgZGUgcGFnbzpkZAIDDw8WAh8DBTQzMCBkw61hcyBjb250cmEgbGEgcmVjZXBjacOzbiBjb25mb3JtZSBkZSBsYSBmYWN0dXJhZGQCBQ9kFgRmD2QWAgIBDw8WAh8DBSRKdXN0aWZpY2FjacOzbiBwYWdvIE1heW9yIGEgMzAgZMOtYXNkZAIBD2QWAgIBDw8WAh8DBRJTaW4gSnVzdGlmaWNhY2nDs25kZAIHDw8WAh8DBRFPcGNpb25lcyBkZSBwYWdvOmRkAgkPDxYCHwMFGlRyYW5zZmVyZW5jaWEgRWxlY3Ryw7NuaWNhZGQCDA9kFggCAQ8PFgIfAwUeTm9tYnJlIGRlIHJlc3BvbnNhYmxlIGRlIHBhZ286ZGQCAw8PFgIfAwUPUEFUUklDSUEgTVXDkU9aZGQCBQ8PFgIfAwUeZS1tYWlsIGRlIHJlc3BvbnNhYmxlIGRlIHBhZ286ZGQCBw8PFgIfAwUPUEFNVU5PWkBQSlVELkNMZGQCDQ8WAh8CaBYMAgEPDxYCHwMFIk5vbWJyZSBkZSByZXNwb25zYWJsZSBkZSBjb250cmF0bzpkZAIDDw8WAh8DBRlDTEFVRElPIFNPQkFSWk8gTkFWQVJSRVRFZGQCBQ8PFgIfAwUiZS1tYWlsIGRlIHJlc3BvbnNhYmxlIGRlIGNvbnRyYXRvOmRkAgcPDxYCHwMFEUNFU09CQVJaT0BQSlVELkNMZGQCCQ8PFgIfAwUmVGVsw6lmb25vIGRlIHJlc3BvbnNhYmxlIGRlbCBjb250cmF0bzpkZAILDw8WAh8DBQ41Ni00NS0yMjM1NDI1LWRkAg4PDxYCHwMFIVByb2hpYmljacOzbiBkZSBzdWJjb250cmF0YWNpw7NuOmRkAg8PDxYCHwMFG1NlIHBlcm1pdGUgc3ViY29udHJhdGFjacOzbmRkAjYPZBYEZg8PFgIfAwUYOC4gR2FyYW50w61hcyByZXF1ZXJpZGFzZGQCBA9kFgICAQ88KwARAwAPFgQfDGcfDQICZAEQFgAWABYADBQrAAAWAmYPZBYIZg8PFgIfAmhkZAIBD2QWAmYPZBYiZg8PFgQfAwUhR2FyYW50w61hcyBkZSBTZXJpZWRhZCBkZSBPZmVydGFzHwJnZGQCAQ8PFgIfAwUSVGlwbyBkZSBkb2N1bWVudG86ZGQCAg8PFgQfAwUFVmFjaW8fAmgWAh8LBQ1kaXNwbGF5Om5vbmU7ZAIDDw8WAh8DBXhQw7NsaXphIGRlIFNlZ3VybyBFbGVjdHLDs25pY28gbyBCb2xldGEgZGUgR2FyYW50w61hIG8gQ2VydGlmaWNhZG8gZGUgRmlhbnphIGEgbGEgVmlzdGEgbyBWYWxlIFZpc3RhIG8gUMOzbGl6YSBkZSBTZWd1cm9kZAIEDw8WAh8DBQ1CZW5lZmljaWFyaW86ZGQCBQ8PFgIfAwUtQ09SUE9SQUNJT04gQURNSU5JU1RSQVRJVkEgREVMIFBPREVSIEpVRElDSUFMZGQCBg8PFgIfAwUVRmVjaGEgZGUgdmVuY2ltaWVudG86ZGQCBw8PFgIfAwUKMTctMTEtMjAyMmRkAggPDxYCHwMFBk1vbnRvOmRkAgkPDxYCHwMFBjUwMDAwMGRkAgoPDxYCHwMFDFBlc28gQ2hpbGVub2RkAgsPDxYCHwMFDURlc2NyaXBjacOzbjpkZAIMDw8WAh8DBRNObyBoYXkgaW5mb3JtYWNpw7NuZGQCDQ8PFgIfAwUGR2xvc2E6ZGQCDg8PFgIfAwVIRW4gZ2FyYW50w61hIGRlIGxhIHNlcmllZGFkIGRlIGxhIG9mZXJ0YSBsaWNpdGFjacOzbiBJRCBOwrAgMjE3OS0zMC1MUDIyZGQCDw8PFgIfAwUkRm9ybWEgeSBvcG9ydHVuaWRhZCBkZSByZXN0aXR1Y2nDs246ZGQCEA8PFgIfAwWaBVJlc3BlY3RvIGRlIGxvcyBvZmVyZW50ZXMgbm8gYWRqdWRpY2Fkb3MsIGxlcyBzZXLDoSBkZXZ1ZWx0YSBhIGNvbnRhciBkZWwgZMOtYSBzdWJzaWd1aWVudGUgYSBsYSBmZWNoYSBkZSBmaXJtYSBkZWwgY29udHJhdG8uDQpSZXNwZWN0byBkZWwgb2ZlcmVudGUgYWRqdWRpY2FkbywgbGUgc2Vyw6EgZGV2dWVsdGEgY29udHJhIGxhIHByZXNlbnRhY2nDs24gZGUgbGEgR2FyYW50w61hIGRlIEZpZWwgeSBPcG9ydHVubyBDdW1wbGltaWVudG8gZGVsIENvbnRyYXRvLg0KRW4gY2FzbyBkZSBvZmVydGFzIGluYWRtaXNpYmxlcywgbGEgZGV2b2x1Y2nDs24gc2UgcmVhbGl6YXLDoSBhIGNvbnRhciBkZSBsYSBmZWNoYSBkZSBwdWJsaWNhY2nDs24gZGUgbGEgYWRqdWRpY2FjacOzbiBlbiBlbCBwb3J0YWwuDQpMYSByZXN0aXR1Y2nDs24gZGUgbGEgZ2FyYW50w61hIGRlIHNlcmllZGFkIGRlIGxhIG9mZXJ0YSBzZSBlZmVjdHVhcsOhIGVuIGxhcyBvZmljaW5hcyBkZSBsYSBBZG1pbmlzdHJhY2nDs24gWm9uYWwgZGUgVGVtdWNvIHViaWNhZGEgZW4gQXYuIENhdXBvbGljw6FuIE7CsDEwNzcsIHBpc28gMywgb2ZpY2luYSAzMDIsIGVuIGhvcmFyaW8gZGUgbHVuZXMgYSBqdWV2ZXMgZGUgODowMCBhIDE3OjAwIGhvcmFzLCB5IHZpZXJuZXMgZGUgODowMCBhIDE2OjAwIGhvcmFzLmRkAgIPZBYCZg9kFiJmDw8WBB8DBSpHYXJhbnTDrWEgZmllbCBkZSBDdW1wbGltaWVudG8gZGUgQ29udHJhdG8fAmdkZAIBDw8WAh8DBRJUaXBvIGRlIGRvY3VtZW50bzpkZAICDw8WBB8DBQVWYWNpbx8CaBYCHwsFDWRpc3BsYXk6bm9uZTtkAgMPDxYCHwMFE0JvbGV0YSBkZSBHYXJhbnTDrWFkZAIEDw8WAh8DBQ1CZW5lZmljaWFyaW86ZGQCBQ8PFgIfAwUtQ09SUE9SQUNJT04gQURNSU5JU1RSQVRJVkEgREVMIFBPREVSIEpVRElDSUFMZGQCBg8PFgIfAwUVRmVjaGEgZGUgdmVuY2ltaWVudG86ZGQCBw8PFgIfAwUKMDktMDYtMjAyNGRkAggPDxYCHwMFBk1vbnRvOmRkAgkPDxYCHwMFAjEwZGQCCg8PFgIfAwUBJWRkAgsPDxYCHwMFDURlc2NyaXBjacOzbjpkZAIMDw8WAh8DBRNObyBoYXkgaW5mb3JtYWNpw7NuZGQCDQ8PFgIfAwUGR2xvc2E6ZGQCDg8PFgIfAwV5UGFyYSBnYXJhbnRpemFyIGVsIGZpZWwgY3VtcGxpbWllbnRvIHkgY29ycmVjdGEgZWplY3VjacOzbiBkZSBsYXMgb2JyYXMgZGVsIGNvbnRyYXRvIGxpY2l0YWNpw7NuIHDDumJsaWNhIElEIDIxNzktMzAtTFAyMmRkAg8PDxYCHwMFJEZvcm1hIHkgb3BvcnR1bmlkYWQgZGUgcmVzdGl0dWNpw7NuOmRkAhAPDxYCHwMFHUEgbGEgZmVjaGEgZGUgc3UgdmVuY2ltaWVudG8uZGQCAw8PFgIfAmhkZAI4D2QWBmYPDxYCHwMFLjkuIFJlcXVlcmltaWVudG9zIHTDqWNuaWNvcyB5IG90cmFzIGNsw6F1c3VsYXNkZAIBD2QWBAIBDw8WAh8DBRxDbMOhdXN1bGEgZGUgUmVhZGp1ZGljYWNpw7NuZGQCAw8PFgIfAwWiBFNpIGVsIHJlc3BlY3Rpdm8gYWRqdWRpY2F0YXJpbyBzZSBkZXNpc3RlIGRlIHN1IG9mZXJ0YSwgbm8gZW50cmVnYSBsb3MgYW50ZWNlZGVudGVzIGxlZ2FsZXMgcGFyYSBjb250cmF0YXIgeS9vIGxhIGdhcmFudMOtYSBkZSBmaWVsIGN1bXBsaW1pZW50bywgbm8gZmlybWEgZWwgY29udHJhdG8gbyBubyBzZSBpbnNjcmliZSBlbiBDaGlsZXByb3ZlZWRvcmVzIGVuIGxvcyBwbGF6b3MgcXVlIHNlIGVzdGFibGVjZW4gZW4gbGFzIHByZXNlbnRlcyBiYXNlcywgbGEgZW50aWRhZCBsaWNpdGFudGUgcG9kcsOhIGRlamFyIHNpbiBlZmVjdG8gbGEgYWRqdWRpY2FjacOzbiB5IHNlbGVjY2lvbmFyIGFsIG9mZXJlbnRlIHF1ZSwgZGUgYWN1ZXJkbyBhbCByZXN1bHRhZG8gZGUgbGEgZXZhbHVhY2nDs24gbGUgc2lnYSBlbiBwdW50YWplLCB5IGFzw60gc3VjZXNpdmFtZW50ZSwgYSBtZW5vcyBxdWUsIGRlIGFjdWVyZG8gYSBsb3MgaW50ZXJlc2VzIGRlbCBzZXJ2aWNpbywgc2UgZXN0aW1lIGNvbnZlbmllbnRlIGRlY2xhcmFyIGRlc2llcnRhIGxhIGxpY2l0YWNpw7NuLmRkAgQPPCsAEQMADxYEHwxnHw0CBWQBEBYAFgAWAAwUKwAAFgJmD2QWDmYPDxYCHwJoZGQCAQ9kFgJmD2QWBGYPDxYCHwMFFlJlc29sdWNpw7NuIGRlIEVtcGF0ZXNkZAIBDw8WAh8DBQtTRUdVTiBCQVNFU2RkAgIPZBYCZg9kFgRmDw8WAh8DBUFNZWNhbmlzbW8gcGFyYSBzb2x1Y2nDs24gZGUgY29uc3VsdGFzIHJlc3BlY3RvIGEgbGEgYWRqdWRpY2FjacOzbmRkAgEPDxYCHwMFC1NFR1VOIEJBU0VTZGQCAw9kFgJmD2QWBGYPDxYCHwMFUkFjcmVkaXRhY2nDs24gZGUgY3VtcGxpbWllbnRvIGRlIHJlbXVuZXJhY2lvbmVzIG8gY290aXphY2lvbmVzIGRlIHNlZ3VyaWRhZCBzb2NpYWxkZAIBDw8WAh8DBQtTRUdVTiBCQVNFU2RkAgQPZBYCZg9kFgRmDw8WAh8DBThQcmVzZW50YWNpw7NuIGRlIGFudGVjZWRlbnRlcyBvbWl0aWRvcyBwb3IgbG9zIG9mZXJlbnRlc2RkAgEPDxYCHwMFC1NFR1VOIEJBU0VTZGQCBQ9kFgJmD2QWBmYPDxYCHwMFE1BhY3RvIGRlIGludGVncmlkYWRkZAIBDw8WAh8DBYAiRWwgb2ZlcmVudGUgZGVjbGFyYSBxdWUsIHBvciBlbCBzJm9hY3V0ZTtsbyBoZWNobyBkZSBwYXJ0aWNpcGFyIGVuIGxhIHByZXNlbnRlIGxpY2l0YWNpJm9hY3V0ZTtuLCBhY2VwdGEgZXhwcmVzYW1lbnRlIGVsIHByZXNlbnRlIHBhY3RvIGRlIGludGVncmlkYWQsIG9ibGlnJmFhY3V0ZTtuZG9zZSBhIGN1bXBsaXIgY29uIHRvZGFzIHkgY2FkYSB1bmEgZGUgbGFzIGVzdGlwdWxhY2lvbmVzIHF1ZSBjb250ZW5pZGFzIGVsIG1pc21vLCBzaW4gcGVyanVpY2lvIGRlIGxhcyBxdWUgc2Ugc2UmbnRpbGRlO2FsZW4gZW4gZWwgcmVzdG8gZGUgbGFzIGJhc2VzIGRlIGxpY2l0YWNpJm9hY3V0ZTtuIHkgZGVtJmFhY3V0ZTtzIGRvY3VtZW50b3MgaW50ZWdyYW50ZXMuIEVzcGVjaWFsbWVudGUsIGVsIG9mZXJlbnRlIGFjZXB0YSBlbCBzdW1pbmlzdHJhciB0b2RhIGxhIGluZm9ybWFjaSZvYWN1dGU7biB5IGRvY3VtZW50YWNpJm9hY3V0ZTtuIHF1ZSBzZWEgY29uc2lkZXJhZGEgbmVjZXNhcmlhIHkgZXhpZ2lkYSBkZSBhY3VlcmRvIGEgbGFzIHByZXNlbnRlcyBiYXNlcyBkZSBsaWNpdGFjaSZvYWN1dGU7biwgYXN1bWllbmRvIGV4cHJlc2FtZW50ZSBsb3Mgc2lndWllbnRlcyBjb21wcm9taXNvczogPGJyIC8+DQoxLi0gRWwgb2ZlcmVudGUgc2UgY29tcHJvbWV0ZSBhIHJlc3BldGFyIGxvcyBkZXJlY2hvcyBmdW5kYW1lbnRhbGVzIGRlIHN1cyB0cmFiYWphZG9yZXMsIGVudGVuZGkmZWFjdXRlO25kb3NlIHBvciAmZWFjdXRlO3N0b3MgbG9zIGNvbnNhZ3JhZG9zIGVuIGxhIENvbnN0aXR1Y2kmb2FjdXRlO24gUG9sJmlhY3V0ZTt0aWNhIGRlIGxhIFJlcCZ1YWN1dGU7YmxpY2EgZW4gc3UgYXJ0JmlhY3V0ZTtjdWxvIDE5LCBuJnVhY3V0ZTttZXJvcyAxJm9yZG07LCA0Jm9yZG07LCA1Jm9yZG07LCA2Jm9yZG07LCAxMiZvcmRtOywgeSAxNiZvcmRtOywgZW4gY29uZm9ybWlkYWQgYWwgYXJ0JmlhY3V0ZTtjdWxvIDQ4NSBkZWwgYyZvYWN1dGU7ZGlnbyBkZWwgdHJhYmFqby4gIEFzaW1pc21vLCBlbCBvZmVyZW50ZSBzZSBjb21wcm9tZXRlIGEgcmVzcGV0YXIgbG9zIGRlcmVjaG9zIGh1bWFub3MsIGxvIHF1ZSBzaWduaWZpY2EgcXVlIGRlYmUgZXZpdGFyIGRhciBsdWdhciBvIGNvbnRyaWJ1aXIgYSBlZmVjdG9zIGFkdmVyc29zIGVuIGxvcyBkZXJlY2hvcyBodW1hbm9zIG1lZGlhbnRlIHN1cyBhY3RpdmlkYWRlcywgcHJvZHVjdG9zIG8gc2VydmljaW9zLCB5IHN1YnNhbmFyIGVzb3MgZWZlY3RvcyBjdWFuZG8gc2UgcHJvZHV6Y2FuLCBkZSBhY3VlcmRvIGEgbG9zIFByaW5jaXBpb3MgUmVjdG9yZXMgZGUgRGVyZWNob3MgSHVtYW5vcyB5IEVtcHJlc2FzIGRlIE5hY2lvbmVzIFVuaWRhcy48YnIgLz4NCjIuLUVsIG9mZXJlbnRlIHNlIG9ibGlnYSBhIG5vIG9mcmVjZXIgbmkgY29uY2VkZXIsIG5pIGludGVudGFyIG9mcmVjZXIgbyBjb25jZWRlciwgc29ib3Jub3MsIHJlZ2Fsb3MsIHByZW1pb3MsIGQmYWFjdXRlO2RpdmFzIG8gcGFnb3MsIGN1YWxxdWllcmEgZnVlc2Ugc3UgdGlwbywgbmF0dXJhbGV6YSB5L28gbW9udG8sIGEgbmluZyZ1YWN1dGU7biBmdW5jaW9uYXJpbyBwJnVhY3V0ZTtibGljbyBlbiByZWxhY2kmb2FjdXRlO24gY29uIHN1IG9mZXJ0YSwgY29uIGVsIHByb2Nlc28gZGUgbGljaXRhY2kmb2FjdXRlO24gcCZ1YWN1dGU7YmxpY2EsIG5pIGNvbiBsYSBlamVjdWNpJm9hY3V0ZTtuIGRlICZlYWN1dGU7bCBvIGxvcyBjb250cmF0b3MgcXVlIGV2ZW50dWFsbWVudGUgc2UgZGVyaXZlbiBkZSBsYSBtaXNtYSwgbmkgdGFtcG9jbyBhIG9mcmVjZXJsYXMgbyBjb25jZWRlcmxhcyBhIHRlcmNlcmFzIHBlcnNvbmFzIHF1ZSBwdWRpZXNlbiBpbmZsdWlyIGRpcmVjdGEgbyBpbmRpcmVjdGFtZW50ZSBlbiBlbCBwcm9jZXNvIGxpY2l0YXRvcmlvLCBlbiBzdSB0b21hIGRlIGRlY2lzaW9uZXMgbyBlbiBsYSBwb3N0ZXJpb3IgYWRqdWRpY2FjaSZvYWN1dGU7biB5IGVqZWN1Y2kmb2FjdXRlO24gZGVsIG8gbG9zIGNvbnRyYXRvcyBxdWUgZGUgZWxsbyBzZSBkZXJpdmVuLjxiciAvPg0KMy4tIEVsIG9mZXJlbnRlIHNlIG9ibGlnYSBhIG5vIGludGVudGFyIG5pIGVmZWN0dWFyIGFjdWVyZG9zIG8gcmVhbGl6YXIgbmVnb2NpYWNpb25lcywgYWN0b3MgbyBjb25kdWN0YXMgcXVlIHRlbmdhbiBwb3Igb2JqZXRvIGluZmx1aXIgbyBhZmVjdGFyIGRlIGN1YWxxdWllciBmb3JtYSBsYSBsaWJyZSBjb21wZXRlbmNpYSwgY3VhbHF1aWVyYSBmdWVzZSBsYSBjb25kdWN0YSBvIGFjdG8gZXNwZWMmaWFjdXRlO2ZpY28sIHkgZXNwZWNpYWxtZW50ZSwgYXF1ZWxsb3MgYWN1ZXJkb3MsIG5lZ29jaWFjaW9uZXMsIGFjdG9zIG8gY29uZHVjdGFzIGRlIHRpcG8gbyBuYXR1cmFsZXphIGNvbHVzaXZhLCBlbiBjdWFscXVpZXIgZGUgc3VzIHRpcG9zIG8gZm9ybWFzLjxiciAvPg0KNC4tIEVsIG9mZXJlbnRlIHNlIG9ibGlnYSBhIHJldmlzYXIgeSB2ZXJpZmljYXIgdG9kYSBsYSBpbmZvcm1hY2kmb2FjdXRlO24geSBkb2N1bWVudGFjaSZvYWN1dGU7biwgcXVlIGRlYmEgcHJlc2VudGFyIHBhcmEgZWZlY3RvcyBkZWwgcHJlc2VudGUgcHJvY2VzbyBsaWNpdGF0b3JpbywgdG9tYW5kbyB0b2RhcyBsYXMgbWVkaWRhcyBxdWUgc2VhbiBuZWNlc2FyaWFzIHBhcmEgYXNlZ3VyYXIgbGEgdmVyYWNpZGFkLCBpbnRlZ3JpZGFkLCBsZWdhbGlkYWQsIGNvbnNpc3RlbmNpYSwgcHJlY2lzaSZvYWN1dGU7biB5IHZpZ2VuY2lhIGRlIGxhIG1pc21hLg0KNS4tIEVsIG9mZXJlbnRlIHNlIG9ibGlnYSBhIGFqdXN0YXIgc3UgYWN0dWFyIHkgY3VtcGxpciBjb24gbG9zIHByaW5jaXBpb3MgZGUgbGVnYWxpZGFkLCAmZWFjdXRlO3RpY2EsIG1vcmFsLCBidWVuYXMgY29zdHVtYnJlcyB5IHRyYW5zcGFyZW5jaWEgZW4gZWwgcHJlc2VudGUgcHJvY2VzbyBsaWNpdGF0b3Jpby4NCjYuLSBFbCBvZmVyZW50ZSBtYW5pZmllc3RhLCBnYXJhbnRpemEgeSBhY2VwdGEgcXVlIGNvbm9jZSB5IHJlc3BldGFyJmFhY3V0ZTsgbGFzIHJlZ2xhcyB5IGNvbmRpY2lvbmVzIGVzdGFibGVjaWRhcyBlbiBsYXMgYmFzZXMgZGUgbGljaXRhY2kmb2FjdXRlO24sIHN1cyBkb2N1bWVudG9zIGludGVncmFudGVzIHkgJmVhY3V0ZTtsIG8gbG9zIGNvbnRyYXRvcyBxdWUgZGUgZWxsb3Mgc2UgZGVyaXZhc2UuPGJyIC8+DQo3Li0gRWwgb2ZlcmVudGUgc2Ugb2JsaWdhIHkgYWNlcHRhIGFzdW1pciwgbGFzIGNvbnNlY3VlbmNpYXMgeSBzYW5jaW9uZXMgcHJldmlzdGFzIGVuIGVzdGFzIGJhc2VzIGRlIGxpY2l0YWNpJm9hY3V0ZTtuLCBhcyZpYWN1dGU7IGNvbW8gZW4gbGEgbGVnaXNsYWNpJm9hY3V0ZTtuIHkgbm9ybWF0aXZhIHF1ZSBzZWFuIGFwbGljYWJsZXMgYSBsYSBtaXNtYS48YnIgLz4NCjguLSBFbCBvZmVyZW50ZSByZWNvbm9jZSB5IGRlY2xhcmEgcXVlIGxhIG9mZXJ0YSBwcmVzZW50YWRhIGVuIGVsIHByb2Nlc28gbGljaXRhdG9yaW8gZXMgdW5hIHByb3B1ZXN0YSBzZXJpYSwgY29uIGluZm9ybWFjaSZvYWN1dGU7biBmaWRlZGlnbmEgeSBlbiB0JmVhY3V0ZTtybWlub3MgdCZlYWN1dGU7Y25pY29zIHkgZWNvbiZvYWN1dGU7bWljb3MgYWp1c3RhZG9zIGEgbGEgcmVhbGlkYWQsIHF1ZSBhc2VndXJlbiBsYSBwb3NpYmlsaWRhZCBkZSBjdW1wbGlyIGNvbiBsYSBtaXNtYSBlbiBsYXMgY29uZGljaW9uZXMgeSBvcG9ydHVuaWRhZCBvZmVydGFkYXMuPGJyIC8+DQo5Li0gRWwgb2ZlcmVudGUgc2Ugb2JsaWdhIGEgdG9tYXIgdG9kYXMgbGFzIG1lZGlkYXMgcXVlIGZ1ZXNlbiBuZWNlc2FyaWFzIHBhcmEgcXVlIGxhcyBvYmxpZ2FjaW9uZXMgYW50ZXJpb3JtZW50ZSBzZSZudGlsZGU7YWxhZGFzIHNlYW4gYXN1bWlkYXMgeSBjYWJhbG1lbnRlIGN1bXBsaWRhcyBwb3Igc3VzIGVtcGxlYWRvcyB5L28gZGVwZW5kaWVudGVzIHkvbyBhc2Vzb3JlcyB5L28gYWdlbnRlcyB5IGVuIGdlbmVyYWwsIHRvZGFzIGxhcyBwZXJzb25hcyBjb24gcXVlICZlYWN1dGU7c3RlIG8gJmVhY3V0ZTtzdG9zIHNlIHJlbGFjaW9uZW4gZGlyZWN0YSBvIGluZGlyZWN0YW1lbnRlIGVuIHZpcnR1ZCBvIGNvbW8gZWZlY3RvIGRlIGxhIHByZXNlbnRlIGxpY2l0YWNpJm9hY3V0ZTtuLCBpbmNsdWlkb3Mgc3VzIHN1YmNvbnRyYXRpc3RhcywgaGFjaSZlYWN1dGU7bmRvc2UgcGxlbmFtZW50ZSByZXNwb25zYWJsZSBkZSBsYXMgY29uc2VjdWVuY2lhcyBkZSBzdSBpbmZyYWNjaSZvYWN1dGU7biwgc2luIHBlcmp1aWNpbyBkZSBsYXMgcmVzcG9uc2FiaWxpZGFkZXMgaW5kaXZpZHVhbGVzIHF1ZSB0YW1iaSZlYWN1dGU7biBwcm9jZWRpZXNlbiB5L28gZnVlc2VuIGRldGVybWluYWRhcyBwb3IgbG9zIG9yZ2FuaXNtb3MgY29ycmVzcG9uZGllbnRlcy5kZAICD2QWAmYPZBYCAgEPFgIfAmhkAgYPDxYCHwJoZGQCPA8PZBYCHwgFLndpbmRvdy5jbG9zZSgpO3dpbmRvdy5ldmVudC5yZXR1cm5WYWx1ZT1mYWxzZTtkGA4FC2dydlByb2R1Y3RvDzwrAAwBCAIBZAURZ3J2QWRtaW5pc3RyYXRpdm8PPCsADAMGFQEISXNBY3RpdmUHFCsAARQrAAFmCAIBZAULZ3J2SnVyaWRpY2EPPCsADAEIAgFkBQxncnZDcml0ZXJpb3MPPCsADAEIAgFkBQpncnZOYXR1cmFsDzwrAAwBCAIBZAUWZ3J2RG9jdW1lbnRvc0p1cmlkaWNvcw88KwAMAQgCAWQFDGdydkdhcmFudGlhcw88KwAMAQgCAWQFDmdydkNyaXRlcmlvc0xTD2dkBR5fX0NvbnRyb2xzUmVxdWlyZVBvc3RCYWNrS2V5X18WHAURUmFkV2luZG93TWFuYWdlcjEFClBvcHVwRmljaGEFC2lidG5PZmVydGFyBQ5pYnRTZWd1aW1pZW50bwUGYnRuQ1NWBQZidG5BUEkFB2J0bk9DRFMFC2ltZ0FkanVudG9zBRZpbWdQcmVndW50YXNMaWNpdGFjaW9uBQxpbWdIaXN0b3JpYWwFFmltZ0FwZXJ0dXJhRWxlY3Ryb25pY2EFEmltZ0FwZXJ0dXJhVGVjbmljYQUPaW1nQ3VhZHJvT2ZlcnRhBRNpbWdBY2xhcmFjaW9uT2ZlcnRhBQ9pbWdBZGp1ZGljYWNpb24FDmltZ09yZGVuQ29tcHJhBQtpbWdSZWdpc3RybwUkZ3J2QWRtaW5pc3RyYXRpdm8kY3RsMDIkZ3J2RGVzY2FyZ2FyBShncnZBZG1pbmlzdHJhdGl2byRjdGwwMiRncnZEZXNjYXJnYXJMaW5rBR9ncnZFY29ub21pY28kY3RsMDIkZ3J2RGVzY2FyZ2FyBSNncnZFY29ub21pY28kY3RsMDIkZ3J2RGVzY2FyZ2FyTGluawUIYnRuQ2xvc2UFEGltZ0RvY3VtZW50QW5leHgFF2ltZ1ZpZXdIaXN0b3J5U2lnbmF0dXJlBQppbWdIaXN0b3J5BQ5JbWdDb250cmF0b29sZAUYaW1hVmlld1ByZXZpZXdNYWtlUmF6b24wBQZpbWdQREYFEGdydkZlY2hhc1VzdWFyaW8PPCsADAEIAgFkBRZncnZEb2N1bWVudG9zTmF0dXJhbGVzDzwrAAwBCAIBZAUKZ3J2VGVjbmljbw9nZAUMZ3J2RWNvbm9taWNvDzwrAAwBCAIBZAUZZ3J2UmVxdWVyaW1pZW50b3NUZWNuaWNvcw88KwAMAQgCAWT0v04nzR8IILerOy+t2g+w82bVyQ==" />
</div>

<script type="text/javascript">
//<![CDATA[
var theForm = document.forms['frmABM_Productos'];
if (!theForm) {
    theForm = document.frmABM_Productos;
}
function __doPostBack(eventTarget, eventArgument) {
    if (!theForm.onsubmit || (theForm.onsubmit() != false)) {
        theForm.__EVENTTARGET.value = eventTarget;
        theForm.__EVENTARGUMENT.value = eventArgument;
        theForm.submit();
    }
}
//]]>
</script>


<script src="/Procurement/WebResource.axd?d=SqZa8GYeN-voTRZ-GMsb11KKLzsM4GjYxTGAXg23ajVoLdblDojATKR_7aSBdwvGYc1HUN_gkQjb5mtE0&amp;t=637814545746327080" type="text/javascript"></script>


<script src="/Procurement/Telerik.Web.UI.WebResource.axd?_TSM_HiddenField_=RadScriptManager1_TSM&amp;compress=1&amp;_TSM_CombinedScripts_=%3b%3bSystem.Web.Extensions%2c+Version%3d4.0.0.0%2c+Culture%3dneutral%2c+PublicKeyToken%3d31bf3856ad364e35%3aen-US%3a9ddf364d-d65d-4f01-a69e-8b015049e026%3aea597d4b%3ab25378d2%3bTelerik.Web.UI%2c+Version%3d2010.3.1215.20%2c+Culture%3dneutral%2c+PublicKeyToken%3d121fae78165ba3d4%3aen-US%3ac7e43360-cbc8-4666-85f6-c5101371c559%3a16e4e7cd%3a874f8ea2%3af7645509%3a24ee1bba%3af46195d3%3a19620875%3a490a9d4e%3abd8f85e4" type="text/javascript"></script>
<script type="text/javascript">
//<![CDATA[
if (typeof(Sys) === 'undefined') throw new Error('ASP.NET Ajax client-side framework failed to load.');
//]]>
</script>

<div>

	<input type="hidden" name="__VIEWSTATEGENERATOR" id="__VIEWSTATEGENERATOR" value="13285B56" />
</div>
        <input type="hidden" name="HddienLinkGeoCgrViewer" id="HddienLinkGeoCgrViewer" value="https://www.contraloria.cl/opencgrapp/sisgeobPasarela/chileCompraViewer?" />

        <input type="hidden" name="hidEsPublico" id="hidEsPublico" value="True" />
        <input type="hidden" name="hidCryptedConId" id="hidCryptedConId" />

        <div class="modal-dialog" id="divPrimerMensaje" style="display: none; cursor: default">
            <div class="modal-content">
                <div class="modal-header">
                    <h4 class="modal-title"><b id="bTitulo"></b></h4>
                </div>
                <div class="modal-body">
                    <label id="lblTextoCuerpo"></label>
                    <br />
                    <br />
                    <br />
                </div>
                <div class="modal-footer">
                    <button id="btnAceptarPopUp" type="button" class="btn btn-primary" onclick="cerrarpagina();">Aceptar</button>
                </div>
            </div>
        </div>

        <script type="text/javascript">
//<![CDATA[
Sys.WebForms.PageRequestManager._initialize('RadScriptManager1', 'frmABM_Productos', [], [], [], 90, '');
//]]>
</script>

        <div id="RadWindowManager1" style="display:none;">
	<!-- 2010.3.1215.20 --><div id="PopupFicha" style="display:none;">
		<div id="PopupFicha_C">

		</div><input id="PopupFicha_ClientState" name="PopupFicha_ClientState" type="hidden" />
	</div><div id="RadWindowManager1_alerttemplate" style="display:none;">
		<div class="rwDialogPopup radalert">			
			<div class="rwDialogText">
			{1}				
			</div>
			
			<div>
				<a  onclick="$find('{0}').close();"
				class="rwPopupButton" href="javascript:void(0);">
					<span class="rwOuterSpan">
						<span class="rwInnerSpan">##LOC[OK]##</span>
					</span>
				</a>				
			</div>
		</div>
		</div><div id="RadWindowManager1_prompttemplate" style="display:none;">
		 <div class="rwDialogPopup radprompt">			
			    <div class="rwDialogText">
			    {1}				
			    </div>		
			    <div>
				    <script type="text/javascript">
				    function RadWindowprompt_detectenter(id, ev, input)
				    {							
					    if (!ev) ev = window.event;                
					    if (ev.keyCode == 13)
					    {															        
					        var but = input.parentNode.parentNode.getElementsByTagName("A")[0];					        
					        if (but)
						    {							
							    if (but.click) but.click();
							    else if (but.onclick)
							    {
							        but.focus(); var click = but.onclick; but.onclick = null; if (click) click.call(but);							 
							    }
						    }
					       return false;
					    } 
					    else return true;
				    }	 
				    </script>
				    <input title="Eneter Value" onkeydown="return RadWindowprompt_detectenter('{0}', event, this);" type="text"  class="rwDialogInput" value="{2}" />
			    </div>
			    <div>
				    <a onclick="$find('{0}').close(this.parentNode.parentNode.getElementsByTagName('input')[0].value);"				
					    class="rwPopupButton" href="javascript:void(0);" ><span class="rwOuterSpan"><span class="rwInnerSpan">##LOC[OK]##</span></span></a>
				    <a onclick="$find('{0}').close(null);" class="rwPopupButton"  href="javascript:void(0);"><span class="rwOuterSpan"><span class="rwInnerSpan">##LOC[Cancel]##</span></span></a>
			    </div>
		    </div>				       
		</div><div id="RadWindowManager1_confirmtemplate" style="display:none;">
		<div class="rwDialogPopup radconfirm">			
			<div class="rwDialogText">
			{1}				
			</div>						
			<div>
				<a onclick="$find('{0}').close(true);"  class="rwPopupButton" href="javascript:void(0);" ><span class="rwOuterSpan"><span class="rwInnerSpan">##LOC[OK]##</span></span></a>
				<a onclick="$find('{0}').close(false);" class="rwPopupButton"  href="javascript:void(0);"><span class="rwOuterSpan"><span class="rwInnerSpan">##LOC[Cancel]##</span></span></a>
			</div>
		</div>		
		</div><input id="RadWindowManager1_ClientState" name="RadWindowManager1_ClientState" type="hidden" />
</div>
        <div style="text-align: center">
            <div id="divGeneralError" class="contError" style="display: none; width: 631px;">
                <span id="lblMensajeError" class="cssmensaje"></span>
            </div>
            <a id="anchor"></a>
        </div>

        
        <div class="FichaLight">
            
            <div id="top1" class="box_a_pie">
                <img id="top_fondo" alt="" src="../../Includes/images/FichaLight/top_fondo.png" style="height:37px;width:762px;border-width:0px;" />
            </div>
            

            <div id="box_a2">
                <div id="box_a_text_00">
                    <span id="lblLicitacion" class="texto01">Licitación </span><span id="lblID" class="texto03">ID: </span><span id="lblNumLicitacion" class="texto02">2179-30-LP22</span>
                    <div id="box_a_text_00a">
                        <span id="lblNombreLicitacion" class="texto04">UNIFICACION DE EMPALMES EDIFICIOS PODER JUDICIAL</span>
                    </div>
                    <div id="box_a_text_00b">
                        <span id="lblResponsableTitulo" class="texto03">Responsable de esta licitación: </span><span id="lblResponsable" class="texto02">CORP ADMINISTRATIVA DEL PODER JUDICIAL, Corp. Adm. del Poder Judicial - Temuco</span>
                    </div>
                    <div id="box_a_text_00c">
                        <span id="lblFechaCierreTitulo" class="texto03">Fecha de Cierre: </span><span id="lblCierre" class="texto02">20-07-2022 14:00:00</span>
                    </div>
                    <div style="border: 1px solid white;">
                        <span id="lblFicha2TituloReclamo" class="texto03">Reclamos recibidos por incumplir plazo de pago:</span>
                        <span id="lblFicha2Reclamo" class="texto02">27</span>
                        <div id="tabla2_texto" class="alert alerta-info">
                            <span id="lblFicha2MensajeReclamo" class="texto09">Este número indica los reclamos recibidos por esta institución desde los últimos <strong>12 meses hasta el día de ayer.</strong> Recuerde interpretar esta información considerando la cantidad de licitaciones y órdenes de compra que esta institución genera en el Mercado Público.</span>
                        </div>
                    </div>
                </div>
                <div id="caja_ofertar">
                    <div id="boton_ofertar">
                        <a id="Ofertar">
                            <input type="image" name="ibtnOfertar" id="ibtnOfertar" onmouseover="this.src=&#39;../../Includes/images/FichaLight/icofertar-press.png&#39;;" onmouseout="this.src=&#39;../../Includes/images/FichaLight/icofertar.png&#39;;" class="ofertarFB" href="/Portal/LoginFichaLicitacion.aspx?rbhCode=wdiV9F+ZfEeKbyxzR6ADWg==" src="../../Includes/images/FichaLight/icofertar.png" style="height:53px;width:48px;border-width:0px;" />
                        </a>
                    </div>
                    <div id="caja_descargar00">
                        <a id="descargar_pdf" class="lnkFicha" href="javascript:__doPostBack(&#39;descargar_pdf&#39;,&#39;&#39;)">Descargar ficha</a>
                        
                    </div>
                </div>
                <div style="border: 1px solid white;">
                    <table class="tabla_estado_fecha2" border="0">
	<tr>
		<td width="40px">
                                <img id="imgEstado" src="../../Includes/images/FichaLight/iconos_estados/publicadas.png" style="border-width:0px;" /></td>
		<td style="width: 280px; margin-top: 0px; vertical-align: text-top; padding-top: 0px">
                                <table id="caja_fecha" class="td_caja_tiempo" cellpadding="0" cellspacing="0">
			<tr>
				<td style="vertical-align: middle;">
                                            <img src="../../Includes/images/FichaLight/reloj.png" style="padding-left: 5px; padding-bottom: 5px;" alt="" /></td>
				<td style="float: left; vertical-align: middle; width: 320px; height: 18px; margin-left: 4px; padding: 3px;">Faltan
                                            <span id="lblContadorCierre">15</span>
                                            días para que cierre esta licitación.</td>
			</tr>
		</table>
		
                            </td>
	</tr>
</table>

                    
                    <table class="box_redes2">
                        <tr>
                            <td>
                                <table id="redes2">
                                    <tr class="texto05">
	<td>
                                            <table>
                                                <tr>
                                                    <td class="img"><a id="lnkSeguimiento">
                                                        <input type="image" name="ibtSeguimiento" id="ibtSeguimiento" class="ofertarFB" href="/Portal/LoginFichaLicitacion.aspx?qs=HExBybQcp6dmvJhmRUuEkhd3baCaWrMrPVyFEwpP4XTuTFXYuOC8fHUn0kSbMAPGBiFBsEHM+TEOuxHIqB4aXg==" src="../../Includes/images/FichaLight/ic_00.png" style="height:23px;width:23px;border-width:0px;" /></a></td>
                                                    <td class="img"><a href="http://www.facebook.com/sharer.php?u=http://www.mercadopublico.cl/Procurement/Modules/RFB/DetailsAcquisition.aspx?qs=HExBybQcp6dmvJhmRUuEkqVjJod83EyleQDUrMofh1xghQ3cJDUqrNtW+Yu5Erpo" id="lnkFace" target="_blank">
                                                        <img src="../../Includes/images/FichaLight/ic_01.png" width="22" height="22" alt="" /></a></td>
                                                    <td class="img"><a href="http://twitter.com/share?url=http%3a%2f%2fwww.mercadopublico.cl%2fProcurement%2fModules%2fRFB%2fDetailsAcquisition.aspx%3fqs%3dHExBybQcp6dmvJhmRUuEkqVjJod83EyleQDUrMofh1xghQ3cJDUqrNtW%2bYu5Erpo&amp;text=UNIFICACION+DE+EMPALMES+EDIFICIOS+PODER+JUDICIAL" id="lnkTwitter" target="_blank">
                                                        <img src="../../Includes/images/FichaLight/ic_02.png" width="22" height="22" alt="" /></a></td>
                                                    <td class="img">
                                                        <script type="text/javascript">
                                                            window.___gcfg = { lang: 'es' };

                                                            (function () {
                                                                var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
                                                                po.src = 'https://apis.google.com/js/plusone.js';
                                                                var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
                                                            })();
                                                        </script>
                                                        <g:plusone annotation="none"></g:plusone>
                                                    </td>
                                                    <td class="img"><a href="mailto:?subject=UNIFICACION DE EMPALMES EDIFICIOS PODER JUDICIAL 2179-30-LP22&body=http://www.mercadopublico.cl/Procurement/Modules/RFB/DetailsAcquisition.aspx?qs=HExBybQcp6dmvJhmRUuEkqVjJod83EyleQDUrMofh1xghQ3cJDUqrNtW+Yu5Erpo" id="lnkMail">
                                                        <img src="../../Includes/images/FichaLight/ic_04.png" width="27" height="23" alt="" /></a></td>

                                                </tr>
                                            </table>
                                        </td>
</tr>

                                    <tr>
                                        <td>
                                            <table class="links-descargas-archivo">
                                                <tr>
                                                    <td class="img-csv popover__wrapper">
                                                        <input type="image" name="btnCSV" id="btnCSV" class="popover__title" src="../../Includes/images/FichaLight/csv.png" style="height:25px;width:25px;border-width:0px;" />

                                                        <div id="tipCSV" class="push popover__content">
                                                            <p class="popover__message">
                                                                Descarga los datos de esta licitación en <strong>formato CSV</strong>.
                                                    <a href="http://api.mercadopublico.cl/modules/Licitacion.aspx" target="_blank" class="a-link-intool">Más información</a>.
                                                            </p>
                                                        </div>

                                                    </td>

                                                    <td class="img-api popover__wrapper2">
                                                        <input type="image" name="btnAPI" id="btnAPI" class="popover__title" src="../../Includes/images/FichaLight/api.png" style="height:25px;width:25px;border-width:0px;" />

                                                        <div id="tipAPI" class="push popover__content2">
                                                            <p class="popover__message">
                                                                Descarga los datos de esta licitación en <strong>formato JSON</strong>. Más información en  
                                                    <a href="http://api.mercadopublico.cl/" target="_blank" class="a-link-intool">API Mercado Público</a>.
                                                            </p>
                                                        </div>

                                                    </td>

                                                    <td class="img-ocds popover__wrapper3">
                                                        <input type="image" name="btnOCDS" id="btnOCDS" class="popover__title" src="../../Includes/images/FichaLight/ocds.png" style="height:25px;width:25px;border-width:0px;" />

                                                        <div id="tipOCDS" class="push popover__content3">
                                                            <p class="popover__message">
                                                                Descarga los datos de esta licitación en <strong>formato OCDS</strong>. Conoce el estandar en el     
                                                    <a href="http://standard.open-contracting.org/latest/es/" target="_blank" class="a-link-intool">Sitio Oficial OCDS</a>.
                                                            </p>
                                                        </div>

                                                    </td>

                                                </tr>
                                            </table>
                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>

                        <tr>
                            <td>
                                <table class="texto05" id="tabla_nomegusta">
                                    <tr>
                                        <td id="td_nomegusta" style="vertical-align: middle !important;">
                                            <a href="https://ayuda.mercadopublico.cl/reclamosodenuncias/reclamoaOOPP/" target="_blank">
                                                <img alt="Dejar un reclamo sobre esta licitación" src="../../Includes/images/FichaLight/nomegusta.png" border="0" style="border-width: 0px" onmouseover="this.src='../../Includes/images/FichaLight/nomegusta_sobre.png';" onmouseout="this.src='../../Includes/images/FichaLight/nomegusta.png';" />

                                            </a>
                                            </td>
                                        <td id="td_nomegusta" style="margin-top: 10px; vertical-align: middle !important;">

                                            <a href="https://ayuda.mercadopublico.cl/reclamosodenuncias/reclamoaOOPP/" target="_blank">
                                                <img alt="Dejar un reclamo sobre esta licitación" src="../../Includes/images/FichaLight/reclamo.png" border="0" style="border-width: 0px" onmouseover="this.src='../../Includes/images/FichaLight/reclamo.png';" onmouseout="this.src='../../Includes/images/FichaLight/reclamo.png';" />
                                            </a>
                                            

                                        </td>
                                    </tr>
                                </table>
                            </td>
                        </tr>
                    </table>
                    
                </div>
            </div>
            <div class="box_a_pie">
                <img src="../../Includes/images/FichaLight/pie_fondo.png" width="762" height="37" alt="" />
            </div>
            <div class="box_a_pie">
                <img src="../../Includes/images/FichaLight/top_fondo.png" width="762" height="37" alt="" />
            </div>
            <div id="box_b">
                <div id="caja_iconos_licitacion">
                    <div class="caja_iconos02">
                        <div id="alerta"></div>
                        <div class="iconos00">
                            <input type="image" name="imgAdjuntos" id="imgAdjuntos" src="../../Includes/images/FichaLight/iconos_licitacion/ic-21.png" onclick="open(&#39;../Attachment/ViewAttachment.aspx?enc=cXn2iimEjypwHjhPfM6VA%2fmNrY5GFkSoiV8%2bK9X4wf34%2fJ%2bQP1no%2bwzI3YMao9sDLuLCTHwjXIH4vx9hrbcMlLqHfOokpWCc48ydx0qTBLbYdUROg1tkrdNY6pzLZYqN9NviyZPpCx7eLJXRvx27klBhw8J4vlmolQ1ghlqsons90W5LcXyvxyIu8tp7sV6k8FdnqYI8LxKIQxrAfZd62cSD%2b3U447C2kRP35IC0Og%2bjSnqJBD4eotwiovUgIzlu8VmfLoDo41cKxuygztL%2fb7biEQHjis3ikJuxs%2b8xj%2bsQPd8se4EaeK0R5cg4Nvcg&#39;,&#39;MercadoPublico&#39;, &#39;width=850, height=700, status=yes, scrollbars=yes, left=0, top=0, resizable=yes&#39;);window.event.returnValue=false;" style="border-width:0px;width: 43; height: 60;" />
                        </div>
                    </div>
                    <div class="caja_iconos02">
                        <div></div>
                        <div class="iconos00">
                            <input type="image" name="imgPreguntasLicitacion" id="imgPreguntasLicitacion" disabled="disabled" alt="" class="fancy" href="/Foros/Modules/FNormal/PopUps/PublicView.aspx?qs=HExBybQcp6dmvJhmRUuEkj3RAqq9oUBaD5GbJSutQbKnpKbfk2tu29AW4JKzeZjA" cursor="default" src="../../Includes/images/FichaLight/ic_licitacion_bloq/preguntas_b.png" style="border-width:0px;width: 45; height: 56;" />
                        </div>
                    </div>
                    
                    <div id="divHistorial" class="caja_iconos00a">
                        <div class="iconos00">
                            <input type="image" name="imgHistorial" id="imgHistorial" alt="" class="fancy" href="/procurement/modules/rfb/showhistory.aspx?rbhcode=9003249&amp;rstType=-1&amp;qs=LPzBCou7vG1+PY6kPaQtXQ==" src="../../Includes/images/FichaLight/iconos_licitacion/ic-24.png" style="border-width:0px;width: 42; height: 56;" />
                        </div>
                    </div>
                    <div class="caja_iconos02">
                        <div class="iconos00">
                            <input type="image" name="imgAperturaElectronica" id="imgAperturaElectronica" disabled="disabled" alt="" src="../../Includes/images/FichaLight/ic_licitacion_bloq/apertura_b.png" style="border-width:0px;" />
                        </div>
                    </div>
                    <div id="divAperturaTecnica" class="caja_iconos02" style="display:none;">
                        <div class="iconos00">
                            <input type="image" name="imgAperturaTecnica" id="imgAperturaTecnica" alt="" class="fancy" href="/Procurement/Modules/RFB/StepsProcessAward/PreviewTechnicalOpeningResults.aspx?qs=AUbi/QbffnrxbvC/6T/r4g==" src="../../Includes/images/FichaLight/iconos_licitacion/apertura-46.png" style="border-width:0px;width: 18; height: 57;" />
                        </div>
                    </div>


                    <div class="caja_iconos02">
                        <div class="iconos00">
                            <input type="image" name="imgCuadroOferta" id="imgCuadroOferta" disabled="disabled" alt="" src="../../Includes/images/FichaLight/ic_licitacion_bloq/ic-32bloq.png" style="border-width:0px;width: 46; height: 58;" />
                        </div>
                    </div>
                    <div id="divAclaracionOferta" class="caja_iconos00a">
                        <div class="iconos00">
                            <input type="image" name="imgAclaracionOferta" id="imgAclaracionOferta" disabled="disabled" alt="" src="../../Includes/images/FichaLight/ic_licitacion_bloq/ic-25bloq.png" style="border-width:0px;width: 46; height: 57;" />
                        </div>
                    </div>
                    <div id="divAdjudicacion" class="caja_iconos02">
                        <div class="iconos00">
                            <input type="image" name="imgAdjudicacion" id="imgAdjudicacion" disabled="disabled" alt="" src="../../Includes/images/FichaLight/ic_licitacion_bloq/ic-27bloq.png" style="border-width:0px;width: 41; height: 60;" />
                        </div>
                    </div>
                    
                    <div class="caja_iconos02b" style="padding-left: 4px;">
                        <div class="iconos00">
                            <input type="image" name="imgOrdenCompra" id="imgOrdenCompra" disabled="disabled" alt="" src="../../Includes/images/FichaLight/ic_licitacion_bloq/ic-26bloq.png" style="border-width:0px;width: 41; height: 60;" />
                        </div>
                    </div>
                    <div class="caja_iconos02b">
                        <div class="iconos00">
                            <input type="image" name="imgRegistro" id="imgRegistro" disabled="disabled" alt="" src="../../Includes/images/FichaLight/ic_licitacion_bloq/ic-31bloq.png" style="border-width:0px;" />
                        </div>
                    </div>
                    <div class="caja_iconos02">
                        <div class="iconos00">
                            
                            
                        </div>
                    </div>
                    <div class="caja_iconos02">
                        <div class="iconos00">
                            
                        </div>
                    </div>
                </div>

            </div>
            

            <div class="box_a_pie">
                <img src="../../Includes/images/FichaLight/pie_peq_fondo.png" width="762" height="37" alt="" />
            </div>
            <div class="box_a_pie">
                <img src="../../Includes/images/FichaLight/top_fondo.png" width="762" height="37" alt="" />
            </div>
            <div id="box_c">
                
                
                <div>
                    <span id="lblProductoTitulo" class="texto05">Productos o servicios</span>
                </div>
                <div class="caja_ficha00">
                    <div>
	<table cellspacing="0" border="0" id="grvProducto" style="width:100%;border-collapse:collapse;">
		<tr>
			<td style="width:100%;">

                                    <table width="100%" border="0" cellpadding="0" cellspacing="2">
                                        <tr>
                                            <td width="2%" valign="top" align="right">
                                                <div>
                                                    <span id="grvProducto_ctl02_lblNumero" class="texto10">1</span>
                                                </div>
                                            </td>

                                            <td>
                                                <div class="tabla_ficha00">
                                                    <table width="640" cellpadding="0" cellspacing="0" class="borde_tabla00">
                                                        <tr>
                                                            <td width="532" style="padding: 5px 5px 0px 5px;">
                                                                <span id="grvProducto_ctl02_lblProducto" class="texto05">Instalación o servicio de sistemas de energía eléctrica</span></td>
                                                            <td width="126" rowspan="2">
                                                                <span id="grvProducto_ctl02_lblCantidad" class="texto09">1</span>
                                                                <span id="grvProducto_ctl02_lblUnidad" class="texto09">Global</span></td>
                                                        </tr>
                                                        <tr>
                                                            <td style="padding: 5px;">
                                                                <span id="grvProducto_ctl02_lblTituloCategoria" class="texto09">Cod:</span>
                                                                <span id="grvProducto_ctl02_lblCategoria" class="texto09">72102201</span></td>
                                                        </tr>
                                                        <tr>
                                                            <td class="borde_tabla02">
                                                                <span id="grvProducto_ctl02_lblDescripcion" class="texto09">UNIFICACION DE EMPALMES EDIFICIOS DE CORTE APELACIONES, JUZGADO DE GARANTÍA Y TRIBUNAL DE JUICIO ORAL EN LO PENAL DE TEMUCO PARA OPTAR A TARIFA DE CLIENTE LIBRE PARA
SUMINISTRO DE ELECTRICIDAD</span></td>
                                                            <td class="borde_tabla02">&nbsp;</td>
                                                        </tr>
                                                    </table>
                                                </div>

                                            </td>
                                        </tr>
                                        <tr>
                                            <td colspan="2">
                                                <br />
                                            </td>

                                        </tr>

                                    </table>
                                </td>
		</tr>
	</table>
</div>
                    <input type="hidden" name="MostrarEspecialidades" id="MostrarEspecialidades" />
                    
                </div>
            </div>
            <div class="box_a_pie">
                <img src="../../Includes/images/FichaLight/pie_fondo.png" width="762" height="37">
            </div>
            <a name="contenidoentero"></a>
            <div id="box_ficha_1">
                <div id="box_ficha_a">
                    <div id="titulo_ficha00" class="texto08">
                        <span id="lblTituloFicha" class="texto05">Contenido de las bases</span>
                    </div>
                    <table class="caja_contenido">
                        <tr>
                            <td>
                                <ul id="caja_contenido_a" style="width: 357px;">
                                    <li>
                                        <span id="lblNumeroFicha1" class="link">1. </span><a><span id="lblTitulo1" class="link_activado" onclick="javascript:mostrarPaso(1);">Características de la licitación</span></a></li>
                                    <li>
                                        <span id="lblNumeroFicha2" class="link">2. </span><a><span id="lblTitulo2" class="link" onclick="javascript:mostrarPaso(2);">Organismo demandante</span></a></li>
                                    <li>
                                        <span id="lblNumeroFicha3" class="link">3. </span><a><span id="lblTitulo3" class="link" onclick="javascript:mostrarPaso(3);">Etapas y plazos</span></a></li>
                                    <li>
                                        <span id="lblNumeroFicha4" class="link">4. </span><a><span id="lblTitulo4" class="link" onclick="javascript:mostrarPaso(4);">Antecedentes para incluir en la oferta</span></a></li>
                                    <li>
                                        <span id="lblNumeroFicha5" class="link">5. </span><a><span id="lblTitulo5" class="link" onclick="javascript:mostrarPaso(5);">Requisitos para contratar al proveedor adjudicado</span></a></li>
                                </ul>
                            </td>
                            <td>
                                <ul id="caja_contenido_b" style="width: 300px; margin-left: 21px;">
                                    <li>
                                        <span id="lblNumeroFicha6" class="link">6. </span><a><span id="lblTitulo6" class="link" onclick="javascript:mostrarPaso(6);">Criterios de evaluación</span></a></li>
                                    <li>
                                        <span id="lblNumeroFicha7" class="link">7. </span><a><span id="lblTitulo7" class="link" onclick="javascript:mostrarPaso(7);">Montos y duración del contrato</span></a></li>
                                    <li>
                                        <span id="lblNumeroFicha8" class="link">8. </span><a><span id="lblTitulo8" class="link" onclick="javascript:mostrarPaso(8);">Garantías requeridas</span></a></li>
                                    <li>
                                        <span id="lblNumeroFicha9" class="link">9. </span><a><span id="lblTitulo9" class="link" onclick="javascript:mostrarPaso(9);">Requerimientos técnicos y otras cláusulas</span></a></li>
                                    
                                </ul>
                            </td>
                        </tr>
                    </table>
                </div>
                
                <div id="caja_bt_vertodo">
                    <div class="caja_bt00">
                        <img src="../../Includes/images/FichaLight/parte00.png" width="343" height="44" alt="" />
                    </div>
                    <a>
                        <div class="caja_bt00">
                            <img src="../../Includes/images/FichaLight/bt_ver.png" border="0" width="81" height="44" onmouseover="this.src='../../Includes/images/FichaLight/bt_ver_sobre.png';" onclick="javascript:mostrarTodo();" onmouseout="this.src='../../Includes/images/FichaLight/bt_ver.png';" style="border: 0pt none;" alt="" />
                        </div>
                        <div class="caja_bt00">
                            <img src="../../Includes/images/FichaLight/parte02.png" width="341" height="44" alt="" />
                        </div>
                    </a>
                </div>
                <div class="box_ficha">
                    <div id="Ficha1" class="ficha">
                        <div class="titulo_ficha01">
                            <span id="lblFicha1" class="titulo00">1. Características de la licitación</span>
                        </div>
                        <div class="tabla_ficha_00">
                            <div class="contenedor_00">
                                <div class="row_a">
                                    <div class="cell_a">
                                        <span id="lblFicha1TituloNombre" class="texto05">Nombre de la licitación:</span>
                                    </div>
                                    <div class="cell_a">
                                        <span id="lblFicha1Nombre" class="texto09">UNIFICACION DE EMPALMES EDIFICIOS PODER JUDICIAL</span>
                                    </div>
                                </div>
                            </div>
                            <div class="contenedor_00">
                                <div class="row_a">
                                    <div class="cell_a">
                                        <span id="lblFicha1TituloEstado" class="texto05">Estado:</span>
                                    </div>
                                    <div class="cell_a">
                                        <span id="lblFicha1Estado" class="texto09">Publicada</span>
                                    </div>
                                </div>
                            </div>
                            <div class="contenedor_00">
                                <div class="row_a">
                                    <div class="cell_a">
                                        <span id="lblFicha1TituloDescripcion" class="texto05">Descripción:</span>
                                    </div>
                                    <div class="cell_a">
                                        <span id="lblFicha1Descripcion" class="texto09">UNIFICACION DE EMPALMES EDIFICIOS DE CORTE APELACIONES, JUZGADO DE GARANTÍA Y TRIBUNAL DE JUICIO ORAL EN LO PENAL DE TEMUCO PARA OPTAR A TARIFA DE CLIENTE LIBRE PARA SUMINISTRO DE ELECTRICIDAD</span>
                                    </div>
                                </div>
                            </div>
                            <div class="contenedor_00">
                                <div class="row_a">
                                    <div class="cell_a">
                                        <span id="lblFicha1TituloTipo" class="texto05">Tipo de licitación:</span>
                                    </div>
                                    <div class="cell_a">
                                        <span id="lblFicha1Tipo" class="texto09">Pública-Licitación Pública igual o superior a 1.000 UTM e inferior a 2.000 UTM (LP)</span>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="contenedor_00">
                                <div class="row_a">
                                    <div class="cell_a">
                                        <span id="lblFicha1TituloConvocatoria" class="texto05">Tipo de convocatoria:</span>
                                    </div>
                                    <div class="cell_a">
                                        <span id="lblFicha1Convocatoria" class="texto09">ABIERTO</span>
                                    </div>
                                </div>
                            </div>
                            
                            
                            
                            
                            
                            <div class="contenedor_00">
                                <div class="row_a">
                                    <div class="cell_a">
                                        <span id="lblFicha1TituloMoneda" class="texto05">Moneda:</span>
                                    </div>
                                    <div class="cell_a">
                                        <span id="lblFicha1Moneda" class="texto09">Peso Chileno</span>
                                    </div>
                                </div>
                            </div>
                            <div class="contenedor_00">
                                <div class="row_a">
                                    <div class="cell_a">
                                        <span id="lblFicha1TituloEtapas" class="texto05">Etapas del proceso de apertura:</span>
                                    </div>
                                    <div class="cell_a">
                                        <span id="lblFicha1Etapas" class="texto09">Una Etapa</span>
                                    </div>
                                </div>
                            </div>
                            
                            <div id="divTomaRazonInfo" class="contenedor_00">
                                <div class="row_a">
                                    <div class="cell_a">
                                        <span id="lblFicha1TituloTR" class="texto05">Toma de razón por Contraloría:</span>
                                    </div>
                                    <div class="cell_a">
                                        <span id="lblFicha1TR" class="texto09">No requiere Toma de Razón por Contraloría</span>
                                    </div>
                                </div>
                            </div>
                            <div class="contenedor_sep">
                                <img src="../../Includes/images/FichaLight/separacion00.png" width="646" height="1" alt="" />
                            </div>
                            <div class="contenedor_00">
                                <div class="row_a">
                                    <div class="cell_a">
                                        <span id="lblFicha1TituloPublicidad" class="texto05">Publicidad de ofertas técnicas:</span>
                                    </div>
                                    <div class="cell_a">
                                        <span id="lblFicha1Publicidad" class="texto09">Las ofertas técnicas serán de público conocimiento una vez realizada la apertura técnica de las ofertas.</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div id="bt_subir1" style="width: 701px; margin-bottom: 18px;" align="right">
                        <a href="#contenidoentero" class="subir">Subir</a>
                    </div>

                    <div id="Ficha2" class="ficha">
                        <div class="titulo_ficha01 titulo00">
                            <span id="lblFicha2" class="titulo00">2. Organismo demandante</span>
                        </div>
                        <div class="tabla_ficha_00">
                            <div class="contenedor_00">
                                <div class="row_a">
                                    <div class="cell_a">
                                        <span id="lblFicha2TituloRazon" class="texto05">Razón social:</span>
                                    </div>
                                    <div class="cell_a">
                                        <span id="lblFicha2Razon" class="texto09">CORP ADMINISTRATIVA DEL PODER JUDICIAL</span>
                                    </div>
                                </div>
                            </div>
                            <div class="contenedor_00">
                                <div class="row_a">
                                    <div class="cell_a">
                                        <span id="lblFicha2TituloUnidad" class="texto05">Unidad de compra:</span>
                                    </div>
                                    <div class="cell_a">
                                        <span id="lblFicha2Unidad" class="texto09">Corp. Adm. del Poder Judicial - Temuco</span>
                                    </div>
                                </div>
                            </div>
                            <div class="contenedor_00">
                                <div class="row_a">
                                    <div class="cell_a">
                                        <span id="lblFicha2TituloRUT" class="texto05">R.U.T.:</span>
                                    </div>
                                    <div class="cell_a">
                                        <span id="lblFicha2RUT" class="texto09">60.301.001-9</span>
                                    </div>
                                </div>
                            </div>
                            <div class="contenedor_00">
                                <div class="row_a">
                                    <div class="cell_a">
                                        <span id="lblFicha2TituloDireccion" class="texto05">Dirección:</span>
                                    </div>
                                    <div class="cell_a">
                                        <span id="lblFicha2Direccion" class="texto09">CAUPOLICAN 1077</span>
                                        
                                    </div>
                                </div>
                            </div>
                            <div class="contenedor_00">
                                <div class="row_a">
                                    <div class="cell_a">
                                        <span id="lblFicha2TituloComuna" class="texto05">Comuna:</span>
                                    </div>
                                    <div class="cell_a">
                                        <span id="lblFicha2Comuna" class="texto09">Temuco</span>
                                    </div>
                                </div>
                            </div>
                            <div class="contenedor_00">
                                <div class="row_a">
                                    <div class="cell_a">
                                        <span id="lblFicha2TituloRegion" class="texto05">Región en que se genera la licitación:</span>
                                    </div>
                                    <div class="cell_a">
                                        <span id="lblFicha2Region" class="texto09">Región de la Araucanía </span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div id="bt_subir2" style="width: 701px; margin-bottom: 18px;" align="right">
                        <a href="#contenidoentero" class="subir">Subir</a>
                    </div>

                    <div id="Ficha3" class="ficha">
                        <div class="titulo_ficha01">
                            <span id="lblFicha3" class="titulo00">3. Etapas y plazos</span>
                        </div>
                        <div class="tabla_ficha_00">
                            <div id="CierreIdoneidad" class="contenedor_00" style="text-align:center !important;display:none;">
                                <div>
                                    <div>
                                        
                                        
                                    </div>
                                </div>
                            </div>
                            <div id="Cierre" class="borde_tabla00" style="text-align:center;">
                                <div>
                                    <div>
                                        <span id="lblFicha3TituloCierre" class="texto05">Fecha de cierre de recepción de la oferta:</span>
                                        <span id="lblFicha3Cierre" class="texto09">20-07-2022 14:00:00</span>
                                    </div>
                                </div>
                            </div>
                            <div class="contenedor_00">
                                <div class="row_a">
                                    <div class="cell_a">
                                        <span id="lblFicha3TituloPublicacion" class="texto05">Fecha de Publicación:</span>
                                        <span id="lblFicha3Publicacion" class="texto09">24-06-2022 21:52:30</span>
                                    </div>
                                </div>
                            </div>
                            <div class="contenedor_00">
                                <div class="row_a">
                                    <div class="cell_a">
                                        <span id="lblFicha3TituloInicio" class="texto05">Fecha inicio de preguntas:</span>
                                        <span id="lblFicha3Inicio" class="texto09">24-06-2022 23:01:00</span>
                                    </div>
                                </div>
                            </div>
                            <div class="contenedor_00">
                                <div class="row_a">
                                    <div class="cell_a">
                                        <span id="lblFicha3TituloFin" class="texto05">Fecha final de preguntas:</span>
                                        <span id="lblFicha3Fin" class="texto09">07-07-2022 15:00:00</span>
                                    </div>
                                </div>
                            </div>
                            <div class="contenedor_00">
                                <div class="row_a">
                                    <div class="cell_a">
                                        <span id="lblFicha3TituloPublicacionRespuestas" class="texto05">Fecha de publicación de respuestas:</span>
                                        <span id="lblFicha3PublicacionRespuestas" class="texto09">13-07-2022 17:00:00</span>
                                    </div>
                                </div>
                            </div>
                            <div class="contenedor_00">
                                <div class="row_a">
                                    <div class="cell_a">
                                        <span id="lblFicha3TituloActoAperturaTecnica" class="texto05">Fecha de acto de apertura técnica:</span>
                                        <span id="lblFicha3ActoAperturaTecnica" class="texto09">21-07-2022 14:00:00</span>
                                    </div>
                                </div>
                            </div>
                            <div id="AperturaEconomica" class="contenedor_00">
                                <div class="row_a">
                                    <div class="cell_a">
                                        <span id="lblFicha3TituloActoAperturaEconomica" class="texto05">Fecha de acto de apertura económica (referencial):</span>
                                        <span id="lblFicha3ActoAperturaEconomica" class="texto09">21-07-2022 14:00:00</span>
                                    </div>
                                </div>
                            </div>
                            <div id="divFechaAdjInfo" class="contenedor_00">
                                <div class="row_a">
                                    <div class="cell_a">
                                        <span id="lblFicha3TituloAdjudicacion" class="texto05">Fecha de Adjudicación:</span>
                                        <span id="lblFicha3Adjudicacion" class="texto09">16-08-2022 17:00:00</span>
                                    </div>
                                </div>
                            </div>
                            
                            <div id="InicioPreguntasLS" class="contenedor_00" style="display:none;">
                                <div class="row_a">
                                    <div class="cell_a">
                                        
                                        
                                    </div>
                                </div>
                            </div>
                            <div id="FinalPreguntasLS" class="contenedor_00" style="display:none;">
                                <div class="row_a">
                                    <div class="cell_a">
                                        
                                        
                                    </div>
                                </div>
                            </div>
                            <div id="PublicacionRespuestasLS" class="contenedor_00" style="display:none;">
                                <div class="row_a">
                                    <div class="cell_a">
                                        
                                        
                                    </div>
                                </div>
                            </div>
                            <div id="SoporteFisico" class="contenedor_00">
                                <div class="row_a">
                                    <div class="cell_a">
                                        <span id="lblFicha3TituloSoporteFisico" class="texto05">Fecha de entrega en soporte fisico</span>
                                        <span id="lblFicha3SoporteFisico" class="texto09">No hay información</span>
                                    </div>
                                </div>
                            </div>
                            <div id="FirmaContrato" class="contenedor_00">
                                <div class="row_a">
                                    <div class="cell_a">
                                        <span id="lblFicha3TituloFirmaContrato" class="texto05">Fecha estimada de firma de contrato</span>
                                        <span id="lblFicha3FirmaContrato" class="texto09">No hay información</span>
                                    </div>
                                </div>
                            </div>
                            <div id="EvaluacionOfertas" class="contenedor_00">
                                <div class="row_a">
                                    <div class="cell_a">
                                        <span id="lblFicha3TituloEvaluacionOfertas" class="texto05">Tiempo estimado de evaluación de ofertas</span>
                                        <span id="lblFicha3EvaluacionOfertas" class="texto09">No hay información</span>
                                    </div>
                                </div>
                            </div>
                            <div class="contenedor_sep">
                                <img src="../../Includes/images/FichaLight/separacion00.png" width="646" height="1" alt="" />
                            </div>
                            <div id="btnEditarFechas" class="fancybox" style="width: 640px; margin-bottom: 18px;" align="right">
                                

                            </div>
                            <div id="sepFechasUsuario" class="contenedor_sep">
                                <img src="../../Includes/images/FichaLight/separacion00.png" width="646" height="1" alt="" />
                            </div>
                            <div id="FechasUsuario" class="contenedor_00">
                                <div>
	<table cellspacing="0" border="0" id="grvFechasUsuario" style="width:100%;border-collapse:collapse;">
		<tr>
			<td style="width:100%;">
                                                <div class="cell_a">
                                                    <span id="grvFechasUsuario_ctl02_lblFicha3TituloFechaUsuario" class="texto05">VISITA TERRENO OBLIGATORIA SEGUN CRONOGRAMA</span>
                                                    <span id="grvFechasUsuario_ctl02_lblFicha3FechaUsuario" class="texto09">04-07-2022 15:00:00</span>
                                                    
                                                    
                                                    
                                                </div>
                                            </td>
		</tr>
	</table>
</div>
                            </div>
                        </div>
                    </div>

                    <div id="bt_subir3" style="width: 701px; margin-bottom: 18px;" align="right">
                        <a href="#contenidoentero" class="subir">Subir</a>
                    </div>

                    <div id="Ficha4" class="ficha">

                        <div class="titulo_ficha01">
                            <span id="lblFicha4" class="titulo00">4. Antecedentes para incluir en la oferta</span>
                        </div>

                        <div class="tabla_ficha_00">
                            
                            <div id="IdAntecedentes">
                                
                                    <div class="contenedor_00">
                                        <div class="row_a">
                                            <span style="font-size: 12px; color: #333333;">Adicionalmente, todos los proveedores para ofertar en esta licitación, deberán obligatoriamente confirmar y firmar electrónicamente la Declaración Jurada de Requisitos para Ofertar.</span>
                                        </div>
                                    </div>
                                    <div class="contenedor_sep">
                                        <img src="../../Includes/images/FichaLight/separacion00.png" width="646" height="1" alt="" />
                                    </div>
                                    
                                <div class="contenedor_00">
                                    <div class="row_a">
                                        <span id="lblAdministrativo" style="font-size: 12px; color: #333333; line-height: 30px;">Documentos Administrativos</span>
                                        <div>
	<table cellspacing="0" border="0" id="grvAdministrativo" style="width:100%;border-collapse:collapse;">
		<tr>
			<td style="width:100%;">
                                                        <table width="655" cellpadding="0" cellspacing="0" border="0">
                                                            <tr valign="top">
                                                                <td width="635" valign="top">
                                                                    <span id="grvAdministrativo_ctl02_lblNumero" style="font-size: 12px; color: #333333; font-weight: bold;">1.-  </span>
                                                                    <span id="grvAdministrativo_ctl02_lblTitulo" class="texto09a1"></span>
                                                                    <span id="grvAdministrativo_ctl02_lblDescripcion" class="texto09a1">ANEXOS ADMINISTRATIVOS</span>
                                                                    
                                                                    
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td align="right">
                                                                    <table cellpadding="0" cellspacing="0" border="0">
                                                                        <tr id="grvAdministrativo_ctl02_descargar_tb4">
				<td>
                                                                                <input type="image" name="grvAdministrativo$ctl02$grvDescargar" id="grvAdministrativo_ctl02_grvDescargar" border="0" onmouseover="this.src=&#39;../../Includes/images/FichaLight/bt_bajar_no.png&#39;;" onmouseout="this.src=&#39;../../Includes/images/FichaLight/bt_bajar_si.png&#39;;" class="fancyAdjunto" href="../Attachment/VerAntecedentes.aspx?enc=01TvPH%2fgoB1MPnpkqYAee5lgw5kYVH2YmzwxDmKzTbNcHZn%2bKLW58zl5reBIBKA7l0%2fHu5Qzo6wV%2b%2fQUwp1yUiTw1eNgZzGfmr0oV8TbkBEItUY5RWsJaxSuDGCGKpr9Bmaw%2bIrY38db7BEDe2KCBGH2lKffTjSGQFQCoBuw3dyPLaT1n0eFI50bWxhFtqMU8JKD6A78wFJuVEIaAGVoujSQ2%2bZYw3xDsnNYRdCeNM0aNeEBnm6otD3eu1agUTxM2Mr8bWUB0fBti3ThA%2fEvfzjczG9u%2fmfF36d2pAqVTKBWIbcrMkKUQtov1YGvX5PdybArBSLwZcrM5rltJptP68SChvDdBoTdKcalXRrzzFLi%2bqou6P7QNHBGBisofhsc26Df2iAmAbamB1BdFOzcgqJbOZ%2fIR9SQUEKquDaiT64I5DCjOtE2ostl%2bQwJbaCaq7jjlP87DFkXN4DxzeFe%2burbn%2bUrRCAN5hL5BlJaPN4%3d" src="../../Includes/images/FichaLight/bt_bajar_si.png" style="border-width:0px;" />
                                                                            </td>
				<td id="grvAdministrativo_ctl02_boton_descarga_tb4">
                                                                                <input type="image" name="grvAdministrativo$ctl02$grvDescargarLink" id="grvAdministrativo_ctl02_grvDescargarLink" border="0" onmouseover="this.src=&#39;../../Includes/images/FichaLight/descargar.png&#39;;" onmouseout="this.src=&#39;../../Includes/images/FichaLight/descargar.png&#39;;" class="fancyAdjunto" href="../Attachment/VerAntecedentes.aspx?enc=01TvPH%2fgoB1MPnpkqYAee5lgw5kYVH2YmzwxDmKzTbNcHZn%2bKLW58zl5reBIBKA7l0%2fHu5Qzo6wV%2b%2fQUwp1yUiTw1eNgZzGfmr0oV8TbkBEItUY5RWsJaxSuDGCGKpr9Bmaw%2bIrY38db7BEDe2KCBGH2lKffTjSGQFQCoBuw3dyPLaT1n0eFI50bWxhFtqMU8JKD6A78wFJuVEIaAGVoujSQ2%2bZYw3xDsnNYRdCeNM0aNeEBnm6otD3eu1agUTxM2Mr8bWUB0fBti3ThA%2fEvfzjczG9u%2fmfF36d2pAqVTKBWIbcrMkKUQtov1YGvX5PdybArBSLwZcrM5rltJptP68SChvDdBoTdKcalXRrzzFLi%2bqou6P7QNHBGBisofhsc26Df2iAmAbamB1BdFOzcgqJbOZ%2fIR9SQUEKquDaiT64I5DCjOtE2ostl%2bQwJbaCaq7jjlP87DFkXN4DxzeFe%2burbn%2bUrRCAN5hL5BlJaPN4%3d" src="../../Includes/images/FichaLight/descargar.png" style="border-width:0px;padding-right: 20px" />
                                                                            </td>
			</tr>
			
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                    </td>
		</tr>
	</table>
</div>
                                    </div>
                                </div>

                                <div class="contenedor_sep">
                                    <img src="../../Includes/images/FichaLight/separacion00.png" width="646" height="1" alt="" />
                                </div>

                                
                                <div class="contenedor_00">
                                    <div class="row_a">
                                        <span id="lblTecnico" style="font-size: 12px; color: #333333; line-height: 30px;">No hay información de Antecedentes Técnicos</span>
                                        
                                    </div>
                                </div>

                                <div class="contenedor_sep">
                                    <img src="../../Includes/images/FichaLight/separacion00.png" width="646" height="1" alt="" />
                                </div>

                                
                                <div class="contenedor_00">
                                    <div class="row_a">
                                        <span id="lblEconomico" style="font-size: 12px; color: #333333; line-height: 30px;">Documentos Económicos</span>
                                        <div>
	<table cellspacing="0" border="0" id="grvEconomico" style="width:100%;border-collapse:collapse;">
		<tr>
			<td style="width:100%;">
                                                        <table width="655" cellpadding="0" cellspacing="0" border="0">
                                                            <tr>
                                                                <td valign="top">
                                                                    <span id="grvEconomico_ctl02_lblNumero" style="font-size: 12px; color: #333333; font-weight: bold;">1.- </span>
                                                                    <span id="grvEconomico_ctl02_lblDescripcion" class="texto09a1">ANEXOS ECONOMICOS</span>
                                                                    
                                                                    
                                                                </td>
                                                            </tr>
                                                            <tr>
                                                                <td align="right">
                                                                    <table cellpadding="0" cellspacing="0" border="0">
                                                                        <tr id="grvEconomico_ctl02_descargar_tb4">
				<td>
                                                                                <input type="image" name="grvEconomico$ctl02$grvDescargar" id="grvEconomico_ctl02_grvDescargar" border="0" onmouseover="this.src=&#39;../../Includes/images/FichaLight/bt_bajar_no.png&#39;;" onmouseout="this.src=&#39;../../Includes/images/FichaLight/bt_bajar_si.png&#39;;" class="fancyAdjunto" href="../Attachment/VerAntecedentes.aspx?enc=4ihR7sWncmvWc8EXHuJiVVn%2bkgeRrgwoT3ze1ylI2rD%2f%2fcEl3%2b2zhGIepLgIAg2QdyDQYOt%2biGswXLmYcKTNjqYqVWBemABZSfkxi6KCe4pYNPisZx9LkeKOIOroC6DOboq%2bzsZhvP%2fRfcma4vM%2bPypzB3A3uuNOi7bP%2b%2bRCCDPJRmcXB270%2bL5LJ2BuK6%2bJa9ybXf0xzKiUg98qnYZ71rEX0eX74%2f92AJ3ro%2bkL41SSbiSJvbX7u%2bTVKueVSZqUo%2bnAB0u9XHvQmKrxN78m7OzAO53zJ5MXvd1faWjcu%2bG660ULHiUigcW5NhWdah6MdsGq8bRoOjuMiHETRWdPrtjAvfuBE9JWVPFc82sniG26WLb%2fQDgtGriYER4okcmbPfXry089rb4pU3WLXa1AV%2bkYlJ9x5Nrup1TpWXEsamfJkU%2bMzQjhhghKvDO6j8%2f7dRVaTTL5bXTwOV8%2bHGV7rJ%2fYZtDaV0pHLzcK1p29FJo%3d" src="../../Includes/images/FichaLight/bt_bajar_si.png" style="border-width:0px;" />
                                                                            </td>
				<td id="grvEconomico_ctl02_boton_descarga_tb4">
                                                                                <input type="image" name="grvEconomico$ctl02$grvDescargarLink" id="grvEconomico_ctl02_grvDescargarLink" border="0" onmouseover="this.src=&#39;../../Includes/images/FichaLight/descargar.png&#39;;" onmouseout="this.src=&#39;../../Includes/images/FichaLight/descargar.png&#39;;" class="fancyAdjunto" href="../Attachment/VerAntecedentes.aspx?enc=4ihR7sWncmvWc8EXHuJiVVn%2bkgeRrgwoT3ze1ylI2rD%2f%2fcEl3%2b2zhGIepLgIAg2QdyDQYOt%2biGswXLmYcKTNjqYqVWBemABZSfkxi6KCe4pYNPisZx9LkeKOIOroC6DOboq%2bzsZhvP%2fRfcma4vM%2bPypzB3A3uuNOi7bP%2b%2bRCCDPJRmcXB270%2bL5LJ2BuK6%2bJa9ybXf0xzKiUg98qnYZ71rEX0eX74%2f92AJ3ro%2bkL41SSbiSJvbX7u%2bTVKueVSZqUo%2bnAB0u9XHvQmKrxN78m7OzAO53zJ5MXvd1faWjcu%2bG660ULHiUigcW5NhWdah6MdsGq8bRoOjuMiHETRWdPrtjAvfuBE9JWVPFc82sniG26WLb%2fQDgtGriYER4okcmbPfXry089rb4pU3WLXa1AV%2bkYlJ9x5Nrup1TpWXEsamfJkU%2bMzQjhhghKvDO6j8%2f7dRVaTTL5bXTwOV8%2bHGV7rJ%2fYZtDaV0pHLzcK1p29FJo%3d" src="../../Includes/images/FichaLight/descargar.png" style="border-width:0px;padding-right: 20px" />
                                                                            </td>
			</tr>
			
                                                                    </table>
                                                                </td>
                                                            </tr>
                                                        </table>
                                                    </td>
		</tr>
	</table>
</div>
                                    </div>
                                </div>
                            </div>
                            
                        </div>
                    </div>

                    <div id="bt_subir4" style="width: 701px; margin-bottom: 18px;" align="right">
                        <a href="#contenidoentero" class="subir">Subir</a>
                    </div>

                    <div id="Ficha5" class="ficha">
                        <div class="titulo_ficha01">
                            <span id="lblFicha5" class="titulo00">5. Requisitos para contratar al proveedor adjudicado</span>
                        </div>
                        <div class="tabla_ficha_00">
                            <div class="contenedor_00">
                                <div class="row_a">
                                    <span id="lblNatural" style="font-size: 12px; color: #333333; line-height: 30px; font-weight: bolder;">Persona natural</span><br />
                                    <span id="lblNaturalCHP" style="font-size: 12px; color: #333333; font-family: Verdana, regular;">Encontrarse hábil en el Registro de Proveedores, registro que verificará NO haber incurrido en las siguientes causales de inhabilidad:</span><br />
                                    <br />
                                    <div>
	<table cellspacing="0" border="0" id="grvNatural" style="width:100%;border-collapse:collapse;">
		<tr>
			<td style="width:100%;">
                                                    <table width="620" cellpadding="0" cellspacing="0" border="0">
                                                        <tr>
                                                            <td width="620">
                                                                <span id="grvNatural_ctl02_lblNumero" Class="texto09a" style="font-weight: bold;">1</span>
                                                                <span id="grvNatural_ctl02_Label1" Class="texto09a" style="font-weight: bold;">.-</span>
                                                                <span id="grvNatural_ctl02_lblDescripcion" class="texto09a">Haber sido condenado por cualquiera de los delitos de cohecho contemplados en el título V del Libro Segundo del Código Penal.</span>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td>&nbsp;</td>
                                                        </tr>
                                                    </table>
                                                </td>
		</tr><tr>
			<td style="width:100%;">
                                                    <table width="620" cellpadding="0" cellspacing="0" border="0">
                                                        <tr>
                                                            <td width="620">
                                                                <span id="grvNatural_ctl03_lblNumero" Class="texto09a" style="font-weight: bold;">2</span>
                                                                <span id="grvNatural_ctl03_Label1" Class="texto09a" style="font-weight: bold;">.-</span>
                                                                <span id="grvNatural_ctl03_lblDescripcion" class="texto09a">Registrar una o más deudas tributarias por un monto total superior a 500 UTM por más de un año, o superior a 200 UTM e inferior a 500 UTM por un período superior a 2 años, sin que exista un convenio de pago vigente. En caso de encontrarse pendiente juicio sobre la efectividad de la deuda, esta inhabilidad regirá una vez que se encuentre firme o ejecutoriada la respectiva resolución.</span>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td>&nbsp;</td>
                                                        </tr>
                                                    </table>
                                                </td>
		</tr><tr>
			<td style="width:100%;">
                                                    <table width="620" cellpadding="0" cellspacing="0" border="0">
                                                        <tr>
                                                            <td width="620">
                                                                <span id="grvNatural_ctl04_lblNumero" Class="texto09a" style="font-weight: bold;">3</span>
                                                                <span id="grvNatural_ctl04_Label1" Class="texto09a" style="font-weight: bold;">.-</span>
                                                                <span id="grvNatural_ctl04_lblDescripcion" class="texto09a">Registrar deudas previsionales o de salud por más de 12 meses por sus trabajadores dependientes, lo que se acreditará mediante certificado de la autoridad competente.</span>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td>&nbsp;</td>
                                                        </tr>
                                                    </table>
                                                </td>
		</tr><tr>
			<td style="width:100%;">
                                                    <table width="620" cellpadding="0" cellspacing="0" border="0">
                                                        <tr>
                                                            <td width="620">
                                                                <span id="grvNatural_ctl05_lblNumero" Class="texto09a" style="font-weight: bold;">4</span>
                                                                <span id="grvNatural_ctl05_Label1" Class="texto09a" style="font-weight: bold;">.-</span>
                                                                <span id="grvNatural_ctl05_lblDescripcion" class="texto09a">La presentación al Registro Nacional de Proveedores de uno o más documentos falsos, declarado así por sentencia judicial ejecutoriada.</span>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td>&nbsp;</td>
                                                        </tr>
                                                    </table>
                                                </td>
		</tr><tr>
			<td style="width:100%;">
                                                    <table width="620" cellpadding="0" cellspacing="0" border="0">
                                                        <tr>
                                                            <td width="620">
                                                                <span id="grvNatural_ctl06_lblNumero" Class="texto09a" style="font-weight: bold;">5</span>
                                                                <span id="grvNatural_ctl06_Label1" Class="texto09a" style="font-weight: bold;">.-</span>
                                                                <span id="grvNatural_ctl06_lblDescripcion" class="texto09a">Haber sido declarado en quiebra por resolución judicial ejecutoriada.</span>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td>&nbsp;</td>
                                                        </tr>
                                                    </table>
                                                </td>
		</tr><tr>
			<td style="width:100%;">
                                                    <table width="620" cellpadding="0" cellspacing="0" border="0">
                                                        <tr>
                                                            <td width="620">
                                                                <span id="grvNatural_ctl07_lblNumero" Class="texto09a" style="font-weight: bold;">6</span>
                                                                <span id="grvNatural_ctl07_Label1" Class="texto09a" style="font-weight: bold;">.-</span>
                                                                <span id="grvNatural_ctl07_lblDescripcion" class="texto09a">Haber sido eliminado o encontrarse suspendido del Registro Nacional de Proveedores por resolución fundada de la Dirección de Compras.</span>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td>&nbsp;</td>
                                                        </tr>
                                                    </table>
                                                </td>
		</tr><tr>
			<td style="width:100%;">
                                                    <table width="620" cellpadding="0" cellspacing="0" border="0">
                                                        <tr>
                                                            <td width="620">
                                                                <span id="grvNatural_ctl08_lblNumero" Class="texto09a" style="font-weight: bold;">7</span>
                                                                <span id="grvNatural_ctl08_Label1" Class="texto09a" style="font-weight: bold;">.-</span>
                                                                <span id="grvNatural_ctl08_lblDescripcion" class="texto09a">Haber sido condenado por prácticas antisindicales o infracción a los derechos fundamentales del trabajador.</span>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td>&nbsp;</td>
                                                        </tr>
                                                    </table>
                                                </td>
		</tr><tr>
			<td style="width:100%;">
                                                    <table width="620" cellpadding="0" cellspacing="0" border="0">
                                                        <tr>
                                                            <td width="620">
                                                                <span id="grvNatural_ctl09_lblNumero" Class="texto09a" style="font-weight: bold;">8</span>
                                                                <span id="grvNatural_ctl09_Label1" Class="texto09a" style="font-weight: bold;">.-</span>
                                                                <span id="grvNatural_ctl09_lblDescripcion" class="texto09a">Registrar condenas asociadas a responsabilidad penal jurídica (incumplimiento artículo 10, Ley 20.393).</span>
                                                            </td>
                                                        </tr>
                                                        <tr>
                                                            <td>&nbsp;</td>
                                                        </tr>
                                                    </table>
                                                </td>
		</tr>
	</table>
</div>
                                </div>
                            </div>
                            <div class="contenedor_00">
                                <div class="row_a">
                                    <span id="lblDocumentosNaturales" style="font-size: 12px; color: #333333; font-weight: bolder;">Documentos persona natural</span>
                                    <div>
	<table cellspacing="0" border="0" id="grvDocumentosNaturales" style="width:100%;border-collapse:collapse;">
		<tr style="height:3px;">
			<td style="width:100%;">
                                                    <span id="grvDocumentosNaturales_ctl02_lblDocumento" class="texto09a" ReadOnly="true">- Fotocopia Legalizada de Cédula de Identidad</span>
                                                    
                                                    
                                                </td>
		</tr><tr style="height:3px;">
			<td style="width:100%;">
                                                    <span id="grvDocumentosNaturales_ctl03_lblDocumento" class="texto09a" ReadOnly="true">- Declaración jurada acreditando que no se encuentra afecto al art. 4 inciso 6 de la ley 19.886, en el cual se establece que "ningún órgano de la administración del Estado podrá suscribir contratos administrativos de provisión de bienes y servicios con los funcionarios directivos del mismo órgano o empresa, ni con personas unidas a ellos por los vínculos de parentesco."</span>
                                                    
                                                    
                                                </td>
		</tr>
	</table>
</div>
                                </div>
                            </div>
                            <div class="contenedor_sep">
                                <img src="../../Includes/images/FichaLight/separacion00.png" width="646" height="1" alt="" />
                            </div>
                            <div class="contenedor_00">
                                <div class="row_a">
                                    <span id="lblJuridica" style="font-size: 12px; color: #333333; line-height: 30px; font-weight: bolder;">Persona jurídica</span><br />
                                    <span id="lblJuridicaCHP" style="font-size: 12px; color: #333333; font-family: Verdana, regular;">Encontrarse hábil en el Registro de Proveedores, registro que verificará NO haber incurrido en las siguientes causales de inhabilidad:</span>
                                    <div>
	<table cellspacing="0" border="0" id="grvJuridica" style="width:100%;border-collapse:collapse;">
		<tr>
			<td style="width:100%;">
                                                    <table width="620" cellpadding="0" cellspacing="0" border="0">
                                                        
                                                        <tr>
                                                            <td width="620">
                                                                <span id="grvJuridica_ctl02_lblNumero" Class="texto09a" style="font-weight: bold;">1</span>
                                                                <span id="grvJuridica_ctl02_Label1" Class="texto09a" style="font-weight: bold;">.-</span>
                                                                <span id="grvJuridica_ctl02_lblDescripcion" class="texto09a">Haber sido condenado por cualquiera de los delitos de cohecho contemplados en el título V del Libro Segundo del Código Penal.</span>
                                                            </td>
                                                        </tr>
                                                        <br />
                                                    </table>
                                                </td>
		</tr><tr>
			<td style="width:100%;">
                                                    <table width="620" cellpadding="0" cellspacing="0" border="0">
                                                        
                                                        <tr>
                                                            <td width="620">
                                                                <span id="grvJuridica_ctl03_lblNumero" Class="texto09a" style="font-weight: bold;">2</span>
                                                                <span id="grvJuridica_ctl03_Label1" Class="texto09a" style="font-weight: bold;">.-</span>
                                                                <span id="grvJuridica_ctl03_lblDescripcion" class="texto09a">Registrar una o más deudas tributarias por un monto total superior a 500 UTM por más de un año, o superior a 200 UTM e inferior a 500 UTM por un período superior a 2 años, sin que exista un convenio de pago vigente. En caso de encontrarse pendiente juicio sobre la efectividad de la deuda, esta inhabilidad regirá una vez que se encuentre firme o ejecutoriada la respectiva resolución.</span>
                                                            </td>
                                                        </tr>
                                                        <br />
                                                    </table>
                                                </td>
		</tr><tr>
			<td style="width:100%;">
                                                    <table width="620" cellpadding="0" cellspacing="0" border="0">
                                                        
                                                        <tr>
                                                            <td width="620">
                                                                <span id="grvJuridica_ctl04_lblNumero" Class="texto09a" style="font-weight: bold;">3</span>
                                                                <span id="grvJuridica_ctl04_Label1" Class="texto09a" style="font-weight: bold;">.-</span>
                                                                <span id="grvJuridica_ctl04_lblDescripcion" class="texto09a">Registrar deudas previsionales o de salud por más de 12 meses por sus trabajadores dependientes, lo que se acreditará mediante certificado de la autoridad competente.</span>
                                                            </td>
                                                        </tr>
                                                        <br />
                                                    </table>
                                                </td>
		</tr><tr>
			<td style="width:100%;">
                                                    <table width="620" cellpadding="0" cellspacing="0" border="0">
                                                        
                                                        <tr>
                                                            <td width="620">
                                                                <span id="grvJuridica_ctl05_lblNumero" Class="texto09a" style="font-weight: bold;">4</span>
                                                                <span id="grvJuridica_ctl05_Label1" Class="texto09a" style="font-weight: bold;">.-</span>
                                                                <span id="grvJuridica_ctl05_lblDescripcion" class="texto09a">La presentación al Registro Nacional de Proveedores de uno o más documentos falsos, declarado así por sentencia judicial ejecutoriada.</span>
                                                            </td>
                                                        </tr>
                                                        <br />
                                                    </table>
                                                </td>
		</tr><tr>
			<td style="width:100%;">
                                                    <table width="620" cellpadding="0" cellspacing="0" border="0">
                                                        
                                                        <tr>
                                                            <td width="620">
                                                                <span id="grvJuridica_ctl06_lblNumero" Class="texto09a" style="font-weight: bold;">5</span>
                                                                <span id="grvJuridica_ctl06_Label1" Class="texto09a" style="font-weight: bold;">.-</span>
                                                                <span id="grvJuridica_ctl06_lblDescripcion" class="texto09a">Haber sido declarado en quiebra por resolución judicial ejecutoriada.</span>
                                                            </td>
                                                        </tr>
                                                        <br />
                                                    </table>
                                                </td>
		</tr><tr>
			<td style="width:100%;">
                                                    <table width="620" cellpadding="0" cellspacing="0" border="0">
                                                        
                                                        <tr>
                                                            <td width="620">
                                                                <span id="grvJuridica_ctl07_lblNumero" Class="texto09a" style="font-weight: bold;">6</span>
                                                                <span id="grvJuridica_ctl07_Label1" Class="texto09a" style="font-weight: bold;">.-</span>
                                                                <span id="grvJuridica_ctl07_lblDescripcion" class="texto09a">Haber sido eliminado o encontrarse suspendido del Registro Nacional de Proveedores por resolución fundada de la Dirección de Compras.</span>
                                                            </td>
                                                        </tr>
                                                        <br />
                                                    </table>
                                                </td>
		</tr><tr>
			<td style="width:100%;">
                                                    <table width="620" cellpadding="0" cellspacing="0" border="0">
                                                        
                                                        <tr>
                                                            <td width="620">
                                                                <span id="grvJuridica_ctl08_lblNumero" Class="texto09a" style="font-weight: bold;">7</span>
                                                                <span id="grvJuridica_ctl08_Label1" Class="texto09a" style="font-weight: bold;">.-</span>
                                                                <span id="grvJuridica_ctl08_lblDescripcion" class="texto09a">Haber sido condenado por prácticas antisindicales o infracción a los derechos fundamentales del trabajador.</span>
                                                            </td>
                                                        </tr>
                                                        <br />
                                                    </table>
                                                </td>
		</tr><tr>
			<td style="width:100%;">
                                                    <table width="620" cellpadding="0" cellspacing="0" border="0">
                                                        
                                                        <tr>
                                                            <td width="620">
                                                                <span id="grvJuridica_ctl09_lblNumero" Class="texto09a" style="font-weight: bold;">8</span>
                                                                <span id="grvJuridica_ctl09_Label1" Class="texto09a" style="font-weight: bold;">.-</span>
                                                                <span id="grvJuridica_ctl09_lblDescripcion" class="texto09a">Registrar condenas asociadas a responsabilidad penal jurídica (incumplimiento artículo 10, Ley 20.393).</span>
                                                            </td>
                                                        </tr>
                                                        <br />
                                                    </table>
                                                </td>
		</tr>
	</table>
</div>
                                </div>
                            </div>
                            <br />
                            <div class="contenedor_00">
                                <div class="row_a">
                                    <span id="lblDocumentosJuridicos" style="font-size: 12px; color: #333333; font-weight: bolder;">Documentos persona jurídica</span>
                                    
                                    <div>
	<table cellspacing="0" border="0" id="grvDocumentosJuridicos" style="width:100%;border-collapse:collapse;">
		<tr style="height:3px;">
			<td style="width:100%;">
                                                    <span id="grvDocumentosJuridicos_ctl02_lblDocumento" class="texto09a" ReadOnly="true">- Fotocopia Legalizada del Rut de la Empresa</span>
                                                    
                                                    
                                                </td>
		</tr><tr style="height:3px;">
			<td style="width:100%;">
                                                    <span id="grvDocumentosJuridicos_ctl03_lblDocumento" class="texto09a" ReadOnly="true">- Declaración jurada acreditando que no se encuentra afecto al art. 4 inciso 6 de la ley 19.886, en el cual se establece que "ningún órgano de la administración del Estado podrá suscribir contratos administrativos de provisión de bienes y servicios con los funcionarios directivos del mismo órgano o empresa, ni con personas unidas a ellos por los vínculos de parentesco."</span>
                                                    
                                                    
                                                </td>
		</tr><tr style="height:3px;">
			<td style="width:100%;">
                                                    <span id="grvDocumentosJuridicos_ctl04_lblDocumento" class="texto09a" ReadOnly="true">- Certificado de Vigencia de la Sociedad</span>
                                                    
                                                    
                                                </td>
		</tr><tr style="height:3px;">
			<td style="width:100%;">
                                                    <span id="grvDocumentosJuridicos_ctl05_lblDocumento" class="texto09a" ReadOnly="true">- <font color='#CC0033'>(1)</font> Certificado de Boletín de Informes Comerciales</span>
                                                    
                                                    
                                                </td>
		</tr><tr style="height:3px;">
			<td style="width:100%;">
                                                    <span id="grvDocumentosJuridicos_ctl06_lblDocumento" class="texto09a" ReadOnly="true">- <font color='#CC0033'>(1)</font> Certificado de Quiebras/Convenio Judicial</span>
                                                    
                                                    
                                                </td>
		</tr>
	</table>
</div>
                                </div>
                            </div>
                            
                            <div class="contenedor_00">
                                <div class="row_a">
                                    <table>
                                        <tr>
                                            <td>
                                                </td>
                                        </tr>
                                        <tr>
                                            <td>
                                                </td>
                                            <td>
                                                </td>
                                        </tr>
                                        <tr>
                                            <td>
                                                </td>
                                            <td>
                                                </td>
                                        </tr>
                                        <tr>
                                            <td>
                                                </td>
                                            <td>
                                                </td>
                                        </tr>
                                    </table>
                                </div>
                            </div>

                        </div>
                    </div>

                    <div id="bt_subir5" style="width: 701px; margin-bottom: 18px;" align="right">
                        <a href="#contenidoentero" class="subir">Subir</a>
                    </div>

                    <div id="Ficha6" class="ficha">
                        <div class="titulo_ficha01">
                            <span id="lblFicha6" class="titulo00">6. Criterios de evaluación</span>
                        </div>
                        <div class="tabla_ficha_00">
                            
                            <div class="contenedor_00">
                                
                                <div>
	<table cellspacing="0" rules="rows" border="0" border="1" id="grvCriterios" style="width:100%;border-collapse:collapse;">
		<tr style="border-color:#999999;border-width:1px;border-style:Solid;">
			<th class="tituloCriterioIzq" align="left" scope="col">Ítem</th><th class="tituloCriterio" align="left" scope="col">Observaciones</th><th class="tituloCriterioDer" align="left" scope="col">Ponderación</th>
		</tr><tr class="estiloSeparador" style="height:50px;">
			<td style="width:45%;">
                                                <span id="grvCriterios_ctl02_lblNumero" class="criterios" style="vertical-align: top; font-size: 11px; color: #333333; font-weight: bolder;">1</span>
                                                <span id="grvCriterios_ctl02_lblNombreCriterio" class="criterios" style="vertical-align: top; width: 100%">TECNICO</span>
                                            </td><td style="width:45%;">
                                                <span id="grvCriterios_ctl02_lblObservaciones" class="criterios" style="vertical-align: top; padding-left: 5px;"></span>
                                            </td><td>
                                                <span id="grvCriterios_ctl02_lblPonderacion" class="criterioPorcentaje" style="text-align:center;vertical-align:top;font-weight:bold;">45%</span>
                                            </td>
		</tr><tr class="estiloSeparador" style="height:50px;">
			<td style="width:45%;">
                                                <span id="grvCriterios_ctl03_lblNumero" class="criterios" style="vertical-align: top; font-size: 11px; color: #333333; font-weight: bolder;">2</span>
                                                <span id="grvCriterios_ctl03_lblNombreCriterio" class="criterios" style="vertical-align: top; width: 100%">ECONOMICO</span>
                                            </td><td style="width:45%;">
                                                <span id="grvCriterios_ctl03_lblObservaciones" class="criterios" style="vertical-align: top; padding-left: 5px;"></span>
                                            </td><td>
                                                <span id="grvCriterios_ctl03_lblPonderacion" class="criterioPorcentaje" style="text-align:center;vertical-align:top;font-weight:bold;">40%</span>
                                            </td>
		</tr><tr class="estiloSeparador" style="height:50px;">
			<td style="width:45%;">
                                                <span id="grvCriterios_ctl04_lblNumero" class="criterios" style="vertical-align: top; font-size: 11px; color: #333333; font-weight: bolder;">3</span>
                                                <span id="grvCriterios_ctl04_lblNombreCriterio" class="criterios" style="vertical-align: top; width: 100%">PATRIMONIAL</span>
                                            </td><td style="width:45%;">
                                                <span id="grvCriterios_ctl04_lblObservaciones" class="criterios" style="vertical-align: top; padding-left: 5px;"></span>
                                            </td><td>
                                                <span id="grvCriterios_ctl04_lblPonderacion" class="criterioPorcentaje" style="text-align:center;vertical-align:top;font-weight:bold;">10%</span>
                                            </td>
		</tr><tr class="estiloSeparador" style="height:50px;">
			<td style="width:45%;">
                                                <span id="grvCriterios_ctl05_lblNumero" class="criterios" style="vertical-align: top; font-size: 11px; color: #333333; font-weight: bolder;">4</span>
                                                <span id="grvCriterios_ctl05_lblNombreCriterio" class="criterios" style="vertical-align: top; width: 100%">FORMALIDADES</span>
                                            </td><td style="width:45%;">
                                                <span id="grvCriterios_ctl05_lblObservaciones" class="criterios" style="vertical-align: top; padding-left: 5px;"></span>
                                            </td><td>
                                                <span id="grvCriterios_ctl05_lblPonderacion" class="criterioPorcentaje" style="text-align:center;vertical-align:top;font-weight:bold;">5%</span>
                                            </td>
		</tr>
	</table>
</div>
                                <br />
                                
                                
                                <div>

</div>
                            </div>
                            
                        </div>
                    </div>

                    <div id="bt_subir6" style="width: 701px; margin-bottom: 18px;" align="right">
                        <a href="#contenidoentero" class="subir">Subir</a>
                    </div>

                    <div id="Ficha7" class="ficha">
                        <div class="titulo_ficha01">
                            <span id="lblFicha7" class="titulo00">7. Montos y duración del contrato</span>
                        </div>
                        <div class="tabla_ficha_00">
                            <table>
                                <div id="divEstimacion">
                                    <tr>
                                        <td style="padding: 4px; width: 280px;">
                                            <span id="lblFicha7TituloEstimacion" class="texto05">Estimación en base a:</span>
                                        </td>
                                        <td class="cell_a">
                                            <span id="lblFicha7Estimacion" class="texto09">Presupuesto Disponible</span>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td colspan="2" class="contenedor_sep">
                                            <img src="../../Includes/images/FichaLight/separacion00.png" width="646" height="1" />
                                        </td>
                                    </tr>
                                </div>
                                
                                <tr>
                                    <td style="padding: 4px;">
                                        <span id="lblFicha7TituloFinanciamiento" class="texto05">Fuente de financiamiento:</span>
                                    </td>
                                    <td class="cell_a">
                                        <span id="lblFicha7Financiamiento" class="texto09">No hay información</span>
                                    </td>
                                </tr>
                                <tr>
                                    <div id="monto" style="display:none;">
                                        <td style="padding: 4px;">
                                            
                                        </td>
                                        <td class="cell_a">
                                            
                                            <div style="width: 640px; margin-bottom: 18px;" align="left">
                                                
                                            </div> 
                                        </td>
                                    </div>
                                </tr>
                                <tr>   
                                    <td></td>
                                    <td> <div style="float:left;">
                                    </div>
                                    </td>
                                </tr>
                                
                                <tr id="SeparadorfilaContratoRenovable">
	<td colspan="2" class="contenedor_sep">
                                        <img src="../../Includes/images/FichaLight/separacion00.png" width="646" height="1" />
                                    </td>
</tr>

                                <tr id="filaContratoRenovable">
	<td style="padding: 4px;">
                                        <span id="lblFicha7TituloContratoRenovacion" class="texto05">Contrato con Renovación:</span>
                                    </td>
	<td class="cell_a">
                                        <span id="lblFicha7ContratoRenovacion" class="texto09">NO</span>
                                    </td>
</tr>

                                
                                <tr>
                                    <td colspan="2" class="contenedor_sep">
                                        <img src="../../Includes/images/FichaLight/separacion00.png" width="646" height="1" />
                                    </td>
                                </tr>
                                <div id="divObservaciones">
                                    <tr id="filaObservaciones">
	<td style="padding: 4px;">
                                            <span id="lblFicha7TituloObservacion" class="texto05">Observaciones</span>
                                        </td>
	<td class="cell_a">
                                            <span id="lblFicha7Observacion" class="texto09">Sin observaciones</span>
                                        </td>
</tr>

                                    
                                </div>
                                <div id="divDuracionContrato">
                                    
                                    
                                    <tr>
                                        <td colspan="2" class="contenedor_sep">
                                            <img src="../../Includes/images/FichaLight/separacion00.png" width="646" height="1" />
                                        </td>
                                    </tr>
                                </div>
                                <div id="divPlazos">
                                    <tr>
                                        <td style="padding: 4px;">
                                            <span id="lblFicha7TituloPlazos" class="texto05">Plazos de pago:</span>
                                        </td>
                                        <td class="cell_a">
                                            <span id="lblFicha7Plazos" class="texto09">30 días contra la recepción conforme de la factura</span>
                                        </td>
                                    </tr>
                                    
                                    <tr>
                                        <td style="padding: 4px;">
                                            <span id="lblFicha7TituloOpciones" class="texto05">Opciones de pago:</span>
                                        </td>
                                        <td class="cell_a">
                                            <span id="lblFicha7Opciones" class="texto09">Transferencia Electrónica</span>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td colspan="2" class="contenedor_sep">
                                            <img src="../../Includes/images/FichaLight/separacion00.png" width="646" height="1" />
                                        </td>
                                    </tr>
                                </div>
                                <div id="divResponsablePago">
                                    <tr>
                                        <td style="padding: 4px;">
                                            <span id="lblFicha7TituloNombreResponsablePago" class="texto05">Nombre de responsable de pago:</span>
                                        </td>
                                        <td class="cell_a">
                                            <span id="lblFicha7NombreResponsablePago" class="texto09">PATRICIA MUÑOZ</span>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td style="padding: 4px;">
                                            <span id="lblFicha7TituloEmailResponsablePago" class="texto05">e-mail de responsable de pago:</span>
                                        </td>
                                        <td class="cell_a">
                                            <span id="lblFicha7EmailResponsablePago" class="texto09">PAMUNOZ@PJUD.CL</span>
                                        </td>
                                    </tr>
                                    <tr>
                                        <td colspan="2" class="contenedor_sep">
                                            <img src="../../Includes/images/FichaLight/separacion00.png" width="646" height="1" />
                                        </td>
                                    </tr>
                                </div>
                                
                                <tr>
                                    <td style="padding: 4px;">
                                        <span id="lblFicha7TituloSubcontratacion" class="texto05">Prohibición de subcontratación:</span>
                                    </td>
                                    <td class="cell_a">
                                        <span id="lblFicha7Subcontratacion" class="texto09">Se permite subcontratación</span>
                                    </td>
                                </tr>
                            </table>
                        </div>

                    </div>

                    <div id="bt_subir7" style="width: 701px; margin-bottom: 18px;" align="right">
                        <a href="#contenidoentero" class="subir">Subir</a>
                    </div>

                    <div id="Ficha8" class="ficha">
                        <div class="titulo_ficha01">
                            <span id="lblFicha8" class="titulo00">8. Garantías requeridas</span>
                        </div>

                        <div style="margin-bottom: 10px;">
                            
                            <input type="hidden" name="hdModReglamento" id="hdModReglamento" value="false" />
                            <div id="divGrillaGarantias" class="">
                                <div>
	<table cellspacing="10" border="0" id="grvGarantias" style="width:100%;">
		<tr>
			<td>
                                                &nbsp;&nbsp;&nbsp;
                                        <span id="grvGarantias_ctl02_lblFicha8TituloTipoGarantia" class="texto05" style="display:inline-block;height:25px;">Garantías de Seriedad de Ofertas</span>

                                                <table class="tabla_ficha_00" border="0" cellpadding="0" cellspacing="0" width="100%">
                                                    
                                                    <tr>
                                                        <td style="padding: 4px;">
                                                            <span id="grvGarantias_ctl02_lblFicha8TituloBeneficiario" class="texto05">Beneficiario:</span>
                                                        </td>
                                                        <td class="cell_a">
                                                            <span id="grvGarantias_ctl02_lblFicha8Beneficiario" class="texto09">CORPORACION ADMINISTRATIVA DEL PODER JUDICIAL</span>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td style="padding: 4px;">
                                                            <span id="grvGarantias_ctl02_lblFicha8TituloFechaVencimiento" class="texto05">Fecha de vencimiento:</span>
                                                        </td>
                                                        <td class="cell_a">
                                                            <span id="grvGarantias_ctl02_lblFicha8FechaVencimiento" class="texto09">17-11-2022</span>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td style="padding: 4px;">
                                                            <span id="grvGarantias_ctl02_lblFicha8TituloMonto" class="texto05">Monto:</span>
                                                        </td>
                                                        <td class="cell_a">
                                                            <span id="grvGarantias_ctl02_lblFicha8Monto" class="texto09">500000</span>
                                                            <span id="grvGarantias_ctl02_lblFicha8TipoMoneda" class="texto09">Peso Chileno</span>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td class="contenedor_sep" colspan="2">
                                                            <img src="../../Includes/images/FichaLight/separacion00.png" width="646" height="1" alt="" />
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td style="padding: 4px;">
                                                            <span id="grvGarantias_ctl02_lblFicha8TituloDescripcion" class="texto05">Descripción:</span>
                                                        </td>
                                                        <td class="cell_a">
                                                            <span id="grvGarantias_ctl02_lblFicha8Descripcion" class="texto09">No hay información</span>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td class="contenedor_sep" colspan="2">
                                                            <img src="../../Includes/images/FichaLight/separacion00.png" width="646" height="1" alt="" />
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td style="padding: 4px;">
                                                            <span id="grvGarantias_ctl02_lblFicha8TituloGlosa" class="texto05">Glosa:</span>
                                                        </td>
                                                        <td class="cell_a">
                                                            <span id="grvGarantias_ctl02_lblFicha8Glosa" class="texto09">En garantía de la seriedad de la oferta licitación ID N° 2179-30-LP22</span>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td class="contenedor_sep" colspan="2">
                                                            <img src="../../Includes/images/FichaLight/separacion00.png" width="646" height="1" alt="" />
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td style="padding: 4px; width: 250px">
                                                            <span id="grvGarantias_ctl02_lblFicha8TituloRestitucion" class="texto05">Forma y oportunidad de restitución:</span>
                                                        </td>
                                                        <td class="cell_a">
                                                            <span id="grvGarantias_ctl02_lblFicha8Restitucion" class="texto09">Respecto de los oferentes no adjudicados, les será devuelta a contar del día subsiguiente a la fecha de firma del contrato.
Respecto del oferente adjudicado, le será devuelta contra la presentación de la Garantía de Fiel y Oportuno Cumplimiento del Contrato.
En caso de ofertas inadmisibles, la devolución se realizará a contar de la fecha de publicación de la adjudicación en el portal.
La restitución de la garantía de seriedad de la oferta se efectuará en las oficinas de la Administración Zonal de Temuco ubicada en Av. Caupolicán N°1077, piso 3, oficina 302, en horario de lunes a jueves de 8:00 a 17:00 horas, y viernes de 8:00 a 16:00 horas.</span>
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
		</tr><tr>
			<td>
                                                &nbsp;&nbsp;&nbsp;
                                        <span id="grvGarantias_ctl03_lblFicha8TituloTipoGarantia" class="texto05" style="display:inline-block;height:25px;">Garantía fiel de Cumplimiento de Contrato</span>

                                                <table class="tabla_ficha_00" border="0" cellpadding="0" cellspacing="0" width="100%">
                                                    
                                                    <tr>
                                                        <td style="padding: 4px;">
                                                            <span id="grvGarantias_ctl03_lblFicha8TituloBeneficiario" class="texto05">Beneficiario:</span>
                                                        </td>
                                                        <td class="cell_a">
                                                            <span id="grvGarantias_ctl03_lblFicha8Beneficiario" class="texto09">CORPORACION ADMINISTRATIVA DEL PODER JUDICIAL</span>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td style="padding: 4px;">
                                                            <span id="grvGarantias_ctl03_lblFicha8TituloFechaVencimiento" class="texto05">Fecha de vencimiento:</span>
                                                        </td>
                                                        <td class="cell_a">
                                                            <span id="grvGarantias_ctl03_lblFicha8FechaVencimiento" class="texto09">09-06-2024</span>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td style="padding: 4px;">
                                                            <span id="grvGarantias_ctl03_lblFicha8TituloMonto" class="texto05">Monto:</span>
                                                        </td>
                                                        <td class="cell_a">
                                                            <span id="grvGarantias_ctl03_lblFicha8Monto" class="texto09">10</span>
                                                            <span id="grvGarantias_ctl03_lblFicha8TipoMoneda" class="texto09">%</span>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td class="contenedor_sep" colspan="2">
                                                            <img src="../../Includes/images/FichaLight/separacion00.png" width="646" height="1" alt="" />
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td style="padding: 4px;">
                                                            <span id="grvGarantias_ctl03_lblFicha8TituloDescripcion" class="texto05">Descripción:</span>
                                                        </td>
                                                        <td class="cell_a">
                                                            <span id="grvGarantias_ctl03_lblFicha8Descripcion" class="texto09">No hay información</span>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td class="contenedor_sep" colspan="2">
                                                            <img src="../../Includes/images/FichaLight/separacion00.png" width="646" height="1" alt="" />
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td style="padding: 4px;">
                                                            <span id="grvGarantias_ctl03_lblFicha8TituloGlosa" class="texto05">Glosa:</span>
                                                        </td>
                                                        <td class="cell_a">
                                                            <span id="grvGarantias_ctl03_lblFicha8Glosa" class="texto09">Para garantizar el fiel cumplimiento y correcta ejecución de las obras del contrato licitación pública ID 2179-30-LP22</span>
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td class="contenedor_sep" colspan="2">
                                                            <img src="../../Includes/images/FichaLight/separacion00.png" width="646" height="1" alt="" />
                                                        </td>
                                                    </tr>
                                                    <tr>
                                                        <td style="padding: 4px; width: 250px">
                                                            <span id="grvGarantias_ctl03_lblFicha8TituloRestitucion" class="texto05">Forma y oportunidad de restitución:</span>
                                                        </td>
                                                        <td class="cell_a">
                                                            <span id="grvGarantias_ctl03_lblFicha8Restitucion" class="texto09">A la fecha de su vencimiento.</span>
                                                        </td>
                                                    </tr>
                                                </table>
                                            </td>
		</tr>
	</table>
</div>
                            </div>
                            
                        </div>
                    </div>

                    <div id="bt_subir8" style="width: 701px; margin-bottom: 18px;" align="right">
                        <a href="#contenidoentero" class="subir">Subir</a>
                    </div>

                    <div id="Ficha9" style="padding-bottom: 10px;">
                        <div class="titulo_ficha01">
                            <span id="lblFicha9" class="titulo00">9. Requerimientos técnicos y otras cláusulas</span>
                        </div>
                        <div class="tabla_ficha_00">
                            <div class="contenedor_00">
                                <div class="row_a">
                                    <div id="divReadjudicacion" class="contenedor_00">
                                        <div class="row_a">
                                            <span id="lblFichaTituloReadjudicacion" style="font-size: 12px; color: #333333; font-weight: bolder;">Cláusula de Readjudicación</span><br />
                                        </div>
                                        <div class="row_a">
                                            <div>
                                                <span id="lblFichaReadjudicacion" class="texto09a">Si el respectivo adjudicatario se desiste de su oferta, no entrega los antecedentes legales para contratar y/o la garantía de fiel cumplimiento, no firma el contrato o no se inscribe en Chileproveedores en los plazos que se establecen en las presentes bases, la entidad licitante podrá dejar sin efecto la adjudicación y seleccionar al oferente que, de acuerdo al resultado de la evaluación le siga en puntaje, y así sucesivamente, a menos que, de acuerdo a los intereses del servicio, se estime conveniente declarar desierta la licitación.</span>
                                            </div>
                                        </div>
                                    </div>
                                    <img src="../../Includes/images/FichaLight/separacion00.png" id="imagenSeparadoraReadjudicacion" width="646" height="1" style="padding: 10px 0 10px 0" />
                                    
                                    <div>
	<table cellspacing="0" border="0" id="grvRequerimientosTecnicos" style="width:100%;border-collapse:collapse;">
		<tr>
			<td style="width:100%;">
                                                    <table width="655" cellpadding="0" cellspacing="0" border="0">
                                                        

                                                        <tr>
                                                            <td valign="top">
                                                                <span id="grvRequerimientosTecnicos_ctl02_lblTitulo" style="font-size: 12px; color: #333333; font-weight: bolder;">Resolución de Empates</span></td>
                                                        </tr>
                                                        
                                                        <tr>
                                                            <td width="635">
                                                                <span id="grvRequerimientosTecnicos_ctl02_lblDescripcion" class="texto09a" style="vertical-align: top;">SEGUN BASES</span>
                                                            </td>
                                                        </tr>
                                                        <tr id="grvRequerimientosTecnicos_ctl02_sepRequerimiento" class="contenedor_sep">
				<td>
                                                                <img src="../../Includes/images/FichaLight/separacion00.png" id="grvRequerimientosTecnicos_ctl02_imagenSeparadora" width="646" height="1" style="padding: 10px 0 10px 0" />
                                                            </td>
			</tr>
			
                                                    </table>
                                                </td>
		</tr><tr>
			<td style="width:100%;">
                                                    <table width="655" cellpadding="0" cellspacing="0" border="0">
                                                        

                                                        <tr>
                                                            <td valign="top">
                                                                <span id="grvRequerimientosTecnicos_ctl03_lblTitulo" style="font-size: 12px; color: #333333; font-weight: bolder;">Mecanismo para solución de consultas respecto a la adjudicación</span></td>
                                                        </tr>
                                                        
                                                        <tr>
                                                            <td width="635">
                                                                <span id="grvRequerimientosTecnicos_ctl03_lblDescripcion" class="texto09a" style="vertical-align: top;">SEGUN BASES</span>
                                                            </td>
                                                        </tr>
                                                        <tr id="grvRequerimientosTecnicos_ctl03_sepRequerimiento" class="contenedor_sep">
				<td>
                                                                <img src="../../Includes/images/FichaLight/separacion00.png" id="grvRequerimientosTecnicos_ctl03_imagenSeparadora" width="646" height="1" style="padding: 10px 0 10px 0" />
                                                            </td>
			</tr>
			
                                                    </table>
                                                </td>
		</tr><tr>
			<td style="width:100%;">
                                                    <table width="655" cellpadding="0" cellspacing="0" border="0">
                                                        

                                                        <tr>
                                                            <td valign="top">
                                                                <span id="grvRequerimientosTecnicos_ctl04_lblTitulo" style="font-size: 12px; color: #333333; font-weight: bolder;">Acreditación de cumplimiento de remuneraciones o cotizaciones de seguridad social</span></td>
                                                        </tr>
                                                        
                                                        <tr>
                                                            <td width="635">
                                                                <span id="grvRequerimientosTecnicos_ctl04_lblDescripcion" class="texto09a" style="vertical-align: top;">SEGUN BASES</span>
                                                            </td>
                                                        </tr>
                                                        <tr id="grvRequerimientosTecnicos_ctl04_sepRequerimiento" class="contenedor_sep">
				<td>
                                                                <img src="../../Includes/images/FichaLight/separacion00.png" id="grvRequerimientosTecnicos_ctl04_imagenSeparadora" width="646" height="1" style="padding: 10px 0 10px 0" />
                                                            </td>
			</tr>
			
                                                    </table>
                                                </td>
		</tr><tr>
			<td style="width:100%;">
                                                    <table width="655" cellpadding="0" cellspacing="0" border="0">
                                                        

                                                        <tr>
                                                            <td valign="top">
                                                                <span id="grvRequerimientosTecnicos_ctl05_lblTitulo" style="font-size: 12px; color: #333333; font-weight: bolder;">Presentación de antecedentes omitidos por los oferentes</span></td>
                                                        </tr>
                                                        
                                                        <tr>
                                                            <td width="635">
                                                                <span id="grvRequerimientosTecnicos_ctl05_lblDescripcion" class="texto09a" style="vertical-align: top;">SEGUN BASES</span>
                                                            </td>
                                                        </tr>
                                                        <tr id="grvRequerimientosTecnicos_ctl05_sepRequerimiento" class="contenedor_sep">
				<td>
                                                                <img src="../../Includes/images/FichaLight/separacion00.png" id="grvRequerimientosTecnicos_ctl05_imagenSeparadora" width="646" height="1" style="padding: 10px 0 10px 0" />
                                                            </td>
			</tr>
			
                                                    </table>
                                                </td>
		</tr><tr>
			<td style="width:100%;">
                                                    <table width="655" cellpadding="0" cellspacing="0" border="0">
                                                        

                                                        <tr>
                                                            <td valign="top">
                                                                <span id="grvRequerimientosTecnicos_ctl06_lblTitulo" style="font-size: 12px; color: #333333; font-weight: bolder;">Pacto de integridad</span></td>
                                                        </tr>
                                                        
                                                        <tr>
                                                            <td width="635">
                                                                <span id="grvRequerimientosTecnicos_ctl06_lblDescripcion" class="texto09a" style="vertical-align: top;">El oferente declara que, por el s&oacute;lo hecho de participar en la presente licitaci&oacute;n, acepta expresamente el presente pacto de integridad, oblig&aacute;ndose a cumplir con todas y cada una de las estipulaciones que contenidas el mismo, sin perjuicio de las que se se&ntilde;alen en el resto de las bases de licitaci&oacute;n y dem&aacute;s documentos integrantes. Especialmente, el oferente acepta el suministrar toda la informaci&oacute;n y documentaci&oacute;n que sea considerada necesaria y exigida de acuerdo a las presentes bases de licitaci&oacute;n, asumiendo expresamente los siguientes compromisos: <br />
1.- El oferente se compromete a respetar los derechos fundamentales de sus trabajadores, entendi&eacute;ndose por &eacute;stos los consagrados en la Constituci&oacute;n Pol&iacute;tica de la Rep&uacute;blica en su art&iacute;culo 19, n&uacute;meros 1&ordm;, 4&ordm;, 5&ordm;, 6&ordm;, 12&ordm;, y 16&ordm;, en conformidad al art&iacute;culo 485 del c&oacute;digo del trabajo.  Asimismo, el oferente se compromete a respetar los derechos humanos, lo que significa que debe evitar dar lugar o contribuir a efectos adversos en los derechos humanos mediante sus actividades, productos o servicios, y subsanar esos efectos cuando se produzcan, de acuerdo a los Principios Rectores de Derechos Humanos y Empresas de Naciones Unidas.<br />
2.-El oferente se obliga a no ofrecer ni conceder, ni intentar ofrecer o conceder, sobornos, regalos, premios, d&aacute;divas o pagos, cualquiera fuese su tipo, naturaleza y/o monto, a ning&uacute;n funcionario p&uacute;blico en relaci&oacute;n con su oferta, con el proceso de licitaci&oacute;n p&uacute;blica, ni con la ejecuci&oacute;n de &eacute;l o los contratos que eventualmente se deriven de la misma, ni tampoco a ofrecerlas o concederlas a terceras personas que pudiesen influir directa o indirectamente en el proceso licitatorio, en su toma de decisiones o en la posterior adjudicaci&oacute;n y ejecuci&oacute;n del o los contratos que de ello se deriven.<br />
3.- El oferente se obliga a no intentar ni efectuar acuerdos o realizar negociaciones, actos o conductas que tengan por objeto influir o afectar de cualquier forma la libre competencia, cualquiera fuese la conducta o acto espec&iacute;fico, y especialmente, aquellos acuerdos, negociaciones, actos o conductas de tipo o naturaleza colusiva, en cualquier de sus tipos o formas.<br />
4.- El oferente se obliga a revisar y verificar toda la informaci&oacute;n y documentaci&oacute;n, que deba presentar para efectos del presente proceso licitatorio, tomando todas las medidas que sean necesarias para asegurar la veracidad, integridad, legalidad, consistencia, precisi&oacute;n y vigencia de la misma.
5.- El oferente se obliga a ajustar su actuar y cumplir con los principios de legalidad, &eacute;tica, moral, buenas costumbres y transparencia en el presente proceso licitatorio.
6.- El oferente manifiesta, garantiza y acepta que conoce y respetar&aacute; las reglas y condiciones establecidas en las bases de licitaci&oacute;n, sus documentos integrantes y &eacute;l o los contratos que de ellos se derivase.<br />
7.- El oferente se obliga y acepta asumir, las consecuencias y sanciones previstas en estas bases de licitaci&oacute;n, as&iacute; como en la legislaci&oacute;n y normativa que sean aplicables a la misma.<br />
8.- El oferente reconoce y declara que la oferta presentada en el proceso licitatorio es una propuesta seria, con informaci&oacute;n fidedigna y en t&eacute;rminos t&eacute;cnicos y econ&oacute;micos ajustados a la realidad, que aseguren la posibilidad de cumplir con la misma en las condiciones y oportunidad ofertadas.<br />
9.- El oferente se obliga a tomar todas las medidas que fuesen necesarias para que las obligaciones anteriormente se&ntilde;aladas sean asumidas y cabalmente cumplidas por sus empleados y/o dependientes y/o asesores y/o agentes y en general, todas las personas con que &eacute;ste o &eacute;stos se relacionen directa o indirectamente en virtud o como efecto de la presente licitaci&oacute;n, incluidos sus subcontratistas, haci&eacute;ndose plenamente responsable de las consecuencias de su infracci&oacute;n, sin perjuicio de las responsabilidades individuales que tambi&eacute;n procediesen y/o fuesen determinadas por los organismos correspondientes.</span>
                                                            </td>
                                                        </tr>
                                                        <tr id="grvRequerimientosTecnicos_ctl06_sepRequerimiento" class="contenedor_sep">
				<td>
                                                                
                                                            </td>
			</tr>
			
                                                    </table>
                                                </td>
		</tr>
	</table>
</div>
                                </div>
                            </div>
                        </div>
                    </div>

                    <div id="bt_subir9" style="width: 701px; margin-bottom: 18px;" align="right">
                        <a href="#contenidoentero" class="subir">Subir</a>
                    </div>

                    
                    <br />
                </div>
                <div id="pie_abajo">
                    <img src="../../Includes/images/FichaLight/pie_fondo.png" width="762" height="37">
                </div>
                <div style="text-align: right; width: 620; padding-right: 19px; padding-bottom: 15px">
                    <input type="image" name="btnClose" id="btnClose" onmouseover="this.src=&#39;../../Includes/images/FichaLight/cerrar_sobre.png&#39;;" onmouseout="this.src=&#39;../../Includes/images/FichaLight/cerrar.png&#39;;" border="0" src="../../Includes/images/FichaLight/cerrar.png" onclick="window.close();window.event.returnValue=false;" style="border-width:0px;border: 0pt none;" />
                </div>
            </div>
            <input type="hidden" name="IndicadorEsMOP" id="IndicadorEsMOP" value="0" />
            
        </div>

        <div class="FichaAntigua">
            <table width="631px" style="height: 100%;" align="center">
                <tr>
                    <td valign="top" colspan="3">
                        <table width="631px" border="0" align="center" cellpadding="0" cellspacing="0">
                            <tr>
                                <td>
                                    <div class="adquisicionTitulo">
                                        <table>
                                            <tr>
                                                <td>
                                                    <span id="Span1">
                                                        <span id="lblTitlePage"></span><span id="lblTitleNumberAq"></span>
                                                    </span>
                                                    <span id="lblTitleNameAq"></span>
                                                    <br />
                                                    <span id="lblFechaCierreAq" class="cssDetailAdquisitionSubtitle"></span>
                                                    <br />
                                                    <br />
                                                    
                                                    <div style="font-size: 12px; width: 100%; background: #FFFFCC; padding: 10px 20px">
                                                        <span id="lblresponsabilidad"></span>
                                                    </div>
                                                    <br />
                                                                                
                                                </td>
                                                
                                            </tr>
                                        </table>
                                    </div>
                                </td>
                                <td>&nbsp;
                                </td>
                            </tr>

                        </table>
                    </td>
                </tr>
                <tr>
                    <td style="width: 45%">
                        <table border="0" cellpadding="0" cellspacing="0" align="center" width="315px" style="height: 280px;">
                            <tr>
                                <td>
                                    <img src="../../Includes/Images/menu_sup.jpg" alt="" style="vertical-align: bottom; width: 315px" />
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <table width="315px" cellpadding="0" cellspacing="0" border="0" style="height: 280px;"
                                        class="TableDetailAdquisition">
                                        <tr>
                                            <td align="center" class="adquisicionTitulo" style="height: 30px;">
                                                <span id="lblTituloContenidos"></span>
                                            </td>
                                        </tr>
                                        <tr>
                                            <td style="vertical-align: top;">
                                                <table cellpadding="0" cellspacing="0" border="0">
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                    
                                                </table>
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <img src="../../Includes/Images/menu_inf.jpg" alt="" style="width: 315px; vertical-align: top;" />
                                </td>
                            </tr>
                        </table>
                    </td>
                    <td style="width: 10%">&nbsp;&nbsp;&nbsp;&nbsp;
                    </td>
                    <td style="width: 45%">
                        <table border="0" cellpadding="0" cellspacing="0" align="center" width="315px" style="height: 250px;">
                            <tr>
                                <td>
                                    <img src="../../Includes/Images/menu_sup.jpg" alt="" style="vertical-align: bottom; width: 315px" />
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <table width="315px" style="height: 280px;" cellpadding="0" cellspacing="0" border="0"
                                        class="TableDetailAdquisition">
                                        <tr style="vertical-align: top; height: 25px;">
                                            <td align="center" class="adquisicionTitulo">
                                                <span id="lblTituloDocumentacion"></span>
                                            </td>
                                        </tr>
                                        <tr style="vertical-align: top; height: 175px;">
                                            <td style="vertical-align: top; padding-left: 30px;">
                                                <input type="image" name="imgDocumentAnexx" id="imgDocumentAnexx" class="cssIconoFichaDigital" src="../../Includes/images/Ficha/adjunto.gif" style="border-width:0px;" />
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                
                                                <input type="image" name="imgViewHistorySignature" id="imgViewHistorySignature" class="cssIconoFichaDigital" src="../../Includes/images/Ficha/historico_firmas.gif" style="border-width:0px;" />
                                                <input type="image" name="imgHistory" id="imgHistory" class="cssIconoFichaDigital" src="../../Includes/images/Ficha/historial.gif" style="border-width:0px;" />

                                                
                                                
                                                
                                                <input type="image" name="ImgContratoold" id="ImgContratoold" class="cssIconoFichaDigital" src="../../Includes/images/Ficha/ver_contratos.gif" style="border-width:0px;" />

                                                
                                                
                                                
                                                
                                                
                                                &nbsp;<input type="image" name="imaViewPreviewMakeRazon0" id="imaViewPreviewMakeRazon0" class="cssIconoFichaDigital" src="../../Includes/images/Ficha/certificado.gif" style="border-width:0px;" />
                                            </td>
                                        </tr>
                                    </table>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    <img src="../../Includes/Images/menu_inf.jpg" alt="" style="width: 315px; vertical-align: top" />
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
            </table>
            <table width="631px" border="0" align="center" cellpadding="0" cellspacing="0">
                <tr>
                    <td style="width: 100%">

                        <table id="tblContenedor" cellspacing="0" cellpadding="0" border="0" width="100%">
                            <!-- PASO 10: PRODUCTOS Y SERVICIOS-->
                            <tr>
                                <td style="width: 100%">
                                    <div class="cssFwkLabelTitleAzulSinUnderLine">
                                        <table width="100%">
                                            <tr>
                                                <td>
                                                    <span id="lblPrincipalTitleS10"></span>
                                                </td>
                                                <td align="right">
                                                    <input type="image" name="imgPDF" id="imgPDF" class="cssIconoFichaDigital" src="../../Includes/images/Ficha/pdf.gif" style="border-width:0px;" />
                                                </td>
                                            </tr>
                                        </table>
                                    </div>
                                    

                                </td>
                            </tr>
                        </table>
                        <br />
                        <div class="cssFwkLabelTitleAzulSinUnderLine">
                            
                        </div>
                        
                        <br />
                        <table id="tableFichaElectronica" border="0">

</table>
                        <div class="gralTitulos">
                            <span id="lblTitle"></span>
                        </div>

                        <table width="100%">
                            <tr id="trBack">
	<td style="width: 100%">
                                    <input type="submit" name="btnBack" value="" id="btnBack" class="cssBtnVolver" />
                                </td>
</tr>

                        </table>
                        <div id="blanket" style="display: none;">
                        </div>
                        <div id="popUpDiv" style="display: none; width: 500px;">
                            <table>
                                <tr>
                                    <td>
                                        
                                    </td>
                                    <td style="vertical-align: top">&nbsp; <b><a id="hpClose" href="#" onclick="popup('popUpDiv')" style="font-size: 20px; color: #000000;">x</a></b>
                                    </td>
                                </tr>
                            </table>
                            <div id="divButton" style="display: none">
                            </div>
                            <br />
                            <br />
                            <br />
                        </div>
                        <input type="hidden" name="HdnEnvironment" id="HdnEnvironment" />
                        <input type="hidden" name="HdnNumberAq" id="HdnNumberAq" />
        </div>
    

<script type="text/javascript">
//<![CDATA[
Sys.Application.add_init(function() {
    $create(Telerik.Web.UI.RadWindow, {"_dockMode":false,"behaviors":20,"clientStateFieldID":"PopupFicha_ClientState","enableShadow":true,"formID":"frmABM_Productos","height":"700px","iconUrl":"","minimizeIconUrl":"","modal":true,"name":"PopupFicha","showContentDuringLoad":false,"skin":"Sitefinity","visibleStatusbar":false,"width":"850px"}, null, null, $get("PopupFicha"));
});
Sys.Application.add_init(function() {
    $create(Telerik.Web.UI.RadWindowManager, {"clientStateFieldID":"RadWindowManager1_ClientState","enableShadow":true,"formID":"frmABM_Productos","iconUrl":"","minimizeIconUrl":"","modal":true,"name":"RadWindowManager1","skin":"Sitefinity","windowControls":"['PopupFicha']"}, null, {"child":"PopupFicha"}, $get("RadWindowManager1"));
});
//]]>
</script>
</form>

    

</body>
<script type="text/javascript">
    var Mostrar = $("#MostrarEspecialidades").val();
    if (Mostrar = "1") { cargarEspecialidades(); }
</script>
</html>
<script type="text/javascript">
    
    function mostrarPaso(paso) {
        var topePasos = CalcularTopePasos();
        for (i = 1; i <= topePasos; i++) {
            $("#lblTitulo" + i).removeClass("link_activado");
            if (i == 1) {
                $("#lblTitulo" + i).addClass("link");
            }
            $("#Ficha" + i).fadeOut();
            $("#bt_subir" + i).fadeOut();
        }
        $("#lblTitulo" + paso).addClass("link_activado");
        $("#Ficha" + paso).fadeIn();
        $("#Ficha" + paso).focus();
    }

    function mostrarTodo() {
        var topePasos = CalcularTopePasos();
        for (i = 1; i <= topePasos; i++) {
            $("#Ficha" + i).show();
            $("#bt_subir" + i).show();
        }
    }

    function cerrarVentana() {
        $.fancybox.close()
    }

    function CalcularTopePasos() {
        var mop = $("#IndicadorEsMOP").val();
        var topePasos = 0;
        if (mop = "1") topePasos = 4;
        if (mop = "0") topePasos = 10;
        return topePasos;
    }

</script>
