import { chromium } from 'playwright';
const url = process.argv[2]; const scroll = +(process.argv[3]||3);
const b = await chromium.launch(); const p = await b.newPage({viewport:{width:1440,height:900}});
try { await p.goto(url,{waitUntil:'domcontentloaded',timeout:40000}); await p.waitForLoadState('networkidle',{timeout:10000}).catch(()=>{});
for (let i=0;i<scroll;i++){ await p.mouse.wheel(0,4000); await p.waitForTimeout(1200);} } catch(e){console.log('ERR',e.message.split('\n')[0]);}
const links = await p.$$eval('a[href]', as=>as.map(a=>a.href+' | '+(a.innerText||'').replace(/\s+/g,' ').trim().slice(0,80)));
console.log([...new Set(links)].join('\n'));
await b.close();
