!function(e){function t(t){for(var r,i,c=t[0],u=t[1],l=t[2],s=0,f=[];s<c.length;s++)i=c[s],Object.prototype.hasOwnProperty.call(a,i)&&a[i]&&f.push(a[i][0]),a[i]=0;for(r in u)Object.prototype.hasOwnProperty.call(u,r)&&(e[r]=u[r]);for(p&&p(t);f.length;)f.shift()();return o.push.apply(o,l||[]),n()}function n(){for(var e,t=0;t<o.length;t++){for(var n=o[t],r=!0,c=1;c<n.length;c++){var u=n[c];0!==a[u]&&(r=!1)}r&&(o.splice(t--,1),e=i(i.s=n[0]))}return e}var r={},a={0:0},o=[];function i(t){if(r[t])return r[t].exports;var n=r[t]={i:t,l:!1,exports:{}};return e[t].call(n.exports,n,n.exports,i),n.l=!0,n.exports}i.e=function(e){var t=[],n=a[e];if(0!==n)if(n)t.push(n[2]);else{var r=new Promise((function(t,r){n=a[e]=[t,r]}));t.push(n[2]=r);var o,c=document.createElement("script");c.charset="utf-8",c.timeout=120,i.nc&&c.setAttribute("nonce",i.nc),c.src=function(e){return i.p+""+e+".index_bundle.js"}(e);var u=new Error;o=function(t){c.onerror=c.onload=null,clearTimeout(l);var n=a[e];if(0!==n){if(n){var r=t&&("load"===t.type?"missing":t.type),o=t&&t.target&&t.target.src;u.message="Loading chunk "+e+" failed.\n("+r+": "+o+")",u.name="ChunkLoadError",u.type=r,u.request=o,n[1](u)}a[e]=void 0}};var l=setTimeout((function(){o({type:"timeout",target:c})}),12e4);c.onerror=c.onload=o,document.head.appendChild(c)}return Promise.all(t)},i.m=e,i.c=r,i.d=function(e,t,n){i.o(e,t)||Object.defineProperty(e,t,{enumerable:!0,get:n})},i.r=function(e){"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},i.t=function(e,t){if(1&t&&(e=i(e)),8&t)return e;if(4&t&&"object"==typeof e&&e&&e.__esModule)return e;var n=Object.create(null);if(i.r(n),Object.defineProperty(n,"default",{enumerable:!0,value:e}),2&t&&"string"!=typeof e)for(var r in e)i.d(n,r,function(t){return e[t]}.bind(null,r));return n},i.n=function(e){var t=e&&e.__esModule?function(){return e.default}:function(){return e};return i.d(t,"a",t),t},i.o=function(e,t){return Object.prototype.hasOwnProperty.call(e,t)},i.p="",i.oe=function(e){throw console.error(e),e};var c=window.webpackJsonp=window.webpackJsonp||[],u=c.push.bind(c);c.push=t,c=c.slice();for(var l=0;l<c.length;l++)t(c[l]);var p=u;o.push([392,1]),n()}({392:function(e,t,n){"use strict";n.r(t);var r=n(0),a=n.n(r),o=n(23),i=n.n(o),c=n(84),u=n(18),l=n(95),p=n.n(l),s=n(154),f=n.n(s),d=n(147),m=n.n(d),b=n(85),v=n.n(b),y=n(38),E=n.n(y),h=n(55),A=n.n(h),g=(n(173),n(89));function O(e,t){return function(e){if(Array.isArray(e))return e}(e)||function(e,t){if(!(Symbol.iterator in Object(e)||"[object Arguments]"===Object.prototype.toString.call(e)))return;var n=[],r=!0,a=!1,o=void 0;try{for(var i,c=e[Symbol.iterator]();!(r=(i=c.next()).done)&&(n.push(i.value),!t||n.length!==t);r=!0);}catch(e){a=!0,o=e}finally{try{r||null==c.return||c.return()}finally{if(a)throw o}}return n}(e,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance")}()}var j=Object(r.lazy)((function(){return n.e(4).then(n.bind(null,410))})),_=Object(r.lazy)((function(){return Promise.all([n.e(2),n.e(3)]).then(n.bind(null,415))})),S=Object(r.lazy)((function(){return n.e(5).then(n.bind(null,414))})),T=function(){var e=Object(u.f)(),t=O(Object(r.useState)(1),2),n=t[0],o=t[1],i={1:"/",2:"/etapas",3:"/about"};return Object(r.useEffect)((function(){e.push(i[n])}),[n]),a.a.createElement("div",{className:"show-container"},a.a.createElement(p.a,null,a.a.createElement(m.a,null,a.a.createElement(A.a,{appearance:"inverse"},a.a.createElement(A.a.Header,null,a.a.createElement("a",{href:"#",className:"navbar-brand logo"},"Poker App")),a.a.createElement(A.a.Body,null,a.a.createElement(E.a,{activeKey:n,onSelect:function(e){return o(e)}},a.a.createElement(E.a.Item,{eventKey:1,icon:a.a.createElement(v.a,{icon:"home"})},"Home"),a.a.createElement(E.a.Item,{eventKey:2},"Etapas"),a.a.createElement(E.a.Item,{eventKey:3},"Sobre"))))),a.a.createElement(f.a,null,a.a.createElement(g.b,null,a.a.createElement(r.Suspense,{fallback:a.a.createElement("div",null,"Loading...")},a.a.createElement(u.c,null,a.a.createElement(u.a,{exact:!0,path:"(/pkapp)*/",component:S}),a.a.createElement(u.a,{exact:!0,path:"(/pkapp)*/about",component:j}),a.a.createElement(u.a,{exact:!0,path:"(/pkapp)*/etapas",component:_})))))))};i.a.render(a.a.createElement(c.a,null,a.a.createElement(T,null)),document.getElementById("app"))},89:function(e,t,n){"use strict";n.d(t,"a",(function(){return u}));var r=n(0),a=n.n(r),o=n(90);function i(e,t){return function(e){if(Array.isArray(e))return e}(e)||function(e,t){if(!(Symbol.iterator in Object(e)||"[object Arguments]"===Object.prototype.toString.call(e)))return;var n=[],r=!0,a=!1,o=void 0;try{for(var i,c=e[Symbol.iterator]();!(r=(i=c.next()).done)&&(n.push(i.value),!t||n.length!==t);r=!0);}catch(e){a=!0,o=e}finally{try{r||null==c.return||c.return()}finally{if(a)throw o}}return n}(e,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance")}()}var c={etapaAdmin:{torneio:{},etapa:{},etapa_finalizada:!0,inscritos:[],rebuys:[],finalizacoes:[],vlr_arrecadado:0,vlr_jackpot:0,vlr_prizepool:0},setTorneio:function(){}},u=Object(r.createContext)(c);t.b=function(e){var t=i(Object(r.useReducer)(o.e,c,(function(){var e=localStorage.getItem("pkapp_admin"),t=c;return e&&(t.etapaAdmin=JSON.parse(e)),t})),2),n=t[0],l=t[1];return Object(r.useEffect)((function(){localStorage.setItem("pkapp_admin",JSON.stringify(n.etapaAdmin))}),[n.etapaAdmin]),a.a.createElement(u.Provider,{value:{etapaAdminCtx:n,dispatch_admin:l}},e.children)}},90:function(e,t,n){"use strict";n.d(t,"b",(function(){return r})),n.d(t,"a",(function(){return a})),n.d(t,"d",(function(){return o})),n.d(t,"c",(function(){return i})),n.d(t,"e",(function(){return u}));var r="ETAPA_ADMIN_RESET_TORNEIO",a="ETAPA_ADMIN_RESET_ETAPA",o="ETAPA_ADMIN_SET_TORNEIO",i="ETAPA_ADMIN_SET_ETAPA",c={torneio:{},id_etapa:null,etapa_finalizada:!0,inscritos:[],rebuys:[],finalizacoes:[],vlr_arrecadado:0,vlr_jackpot:0,vlr_prizepool:0},u=function e(t,n){switch(n.type){case"ETAPA_ADMIN_RESET":return c;case o:var u=Object.assign({},t);return u.etapaAdmin=Object.assign({},u.etapaAdmin,{torneio:n.torneio}),u;case r:var l=e(t,{type:a});return l.etapaAdmin=Object.assign({},l.etapaAdmin,{torneio:{}}),l;case i:var p=Object.assign({},t);return p.etapaAdmin=Object.assign({},p.etapaAdmin,{etapa:n.etapa}),p;case a:var s=Object.assign({},t);return s.etapaAdmin=Object.assign({},s.etapaAdmin,{etapa:{}}),s;default:return console.log("adminReducer: Warning default: ",t,n),t}}}});