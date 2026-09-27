import json,re,collections,sys
S=sys.argv[1]; D='/Users/borys/Desktop/wp-oss/research/tools/antivibe/'
s=json.load(open(S+'/summary.json')); sites={x['id']:x for x in json.load(open(D+'sites.json'))}
T=['10Web AI (WordPress)','Bolt','Durable','Lovable','v0']
names=json.load(open(D+'names.json'))
skip={'lucide icons','vite','next','wordpress','elementor','backdrop-blur class','accent hue 200-290 (blue to violet)','closes on CTA/contact band','>=2 chromatic/tinted colours within dE2.5 of Tailwind v3 defaults','near-black text not #000','rating string ("4.9/5", "5.0 ★")'}
rows=[]
for k,a,n,c,m in s['freq']:
  if k in skip or (k.startswith('section:') and k!='section: logos'): continue
  tf=s['tool_freq'][k]; rows.append((a/n, names.get(k,k), a, n, [tf[t] for t in T], c, m))
ta=set(); tac=set()
for l in open(S+'/cl-av.txt'):
  m=re.match(r'S5\s+(\S+?):\d+\s+tier A word', l.strip())
  if m: ta.add(m.group(1).split('/')[-1][:-4])
for l in open(S+'/cl-ctl.txt'):
  m=re.match(r'S5\s+(\S+?):\d+\s+tier A word', l.strip())
  if m: tac.add(m.group(1))
ta.discard('dur-obp')
rows.append((len(ta)/65,'copylint tier-A word in visible copy',len(ta),65,[sum(1 for i in ta if sites[i]['tool']==t) for t in T],len(tac),12))
o=json.load(open(D+'order-manual.json')); o={k:v.split() for k,v in o.items()}
multi={k:v for k,v in o.items() if len([x for x in v if x!='X'])>=4}
def sub(v,p):
  it=iter(v); return all(x in it for x in p)
for label,pred in [('Page ends on a CTA band or contact block (manual, of 47 multi-section pages)',lambda v:v[-1] in('C','K')),('Second block is services/features (manual, of 47)',lambda v:v[1]=='S'),('Testimonials directly before the closing CTA/contact (manual, of 47)',lambda v:v[-1] in ('C','K') and 'T' in v[-3:-1]),('Hero, then services, then testimonials, in that order (manual, of 47)',lambda v:sub(v,['H','S','T']))]:
  ks=[k for k,v in multi.items() if pred(v)]
  rows.append((len(ks)/47,label,len(ks),47,[sum(1 for k in ks if sites[k]['tool']==t) for t in T],None,None))
rows.sort(key=lambda r:-r[0])
print('| Trait (measured) | AI sample | 10Web | Bolt | Durable | Lovable | v0 | Control (hand-built) |')
print('|---|---|---|---|---|---|---|---|')
print('| *n per group* | 65 | 12 | 14 | 7 | 18 | 14 | 12 |')
for _,name,a,n,tt,c,m in rows:
  print(f'| {name} | **{a}/{n}** | ' + ' | '.join(str(x) for x in tt) + ' | ' + (f'{c}/{m}' if c is not None else 'not coded') + ' |')
