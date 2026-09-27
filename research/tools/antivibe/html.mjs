import { chromium } from 'playwright';
const b = await chromium.launch(); const p = await b.newPage();
await p.goto(process.argv[2],{waitUntil:'domcontentloaded',timeout:40000}).catch(()=>{}); await p.waitForTimeout(5000);
console.log(await p.content()); await b.close();
