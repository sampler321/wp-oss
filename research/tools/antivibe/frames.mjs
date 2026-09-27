import { chromium } from 'playwright';
const b = await chromium.launch(); const p = await b.newPage();
for (const url of process.argv.slice(2)) {
 try { await p.goto(url,{waitUntil:'domcontentloaded',timeout:40000}); await p.waitForTimeout(6000);} catch(e){}
 const f = await p.$$eval('iframe', fs=>fs.map(f=>f.src));
 console.log(url, '=>', f.join(' , '));
}
await b.close();
