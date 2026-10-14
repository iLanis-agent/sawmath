import json, math

def pos(x): return isinstance(x,(int,float)) and math.isfinite(x) and x>0
def jround(x): return math.floor(x+0.5)
def jsnum(x):
    if isinstance(x,float) and x==int(x): return str(int(x))
    return str(x)
def r2(x): return jround(x*100)/100

def mix_plan(gasGal,ratio):
    if not pos(gasGal) or not pos(ratio): return {"error":"gas and ratio must both be above zero"}
    return {"oilOz":r2(gasGal*128/ratio)}

def render_mix(r,gasGal,ratio):
    return ("Your "+jsnum(gasGal)+(" gallon" if gasGal==1 else " gallons")+" of gas at "+jsnum(ratio)
            +":1 takes "+jsnum(r["oilOz"])+" oz of oil - measure the cap lines, not capfuls.")

FILES={"1/4":"5/32",".325":"3/16","3/8":"7/32",".404":"7/32"}

def file_plan(pitch):
    if pitch not in FILES: return {"error":"pick a chain pitch"}
    return {"file":FILES[pitch],"pitch":pitch}

def render_file(r, *args):
    return ("Your "+r["pitch"]+" pitch chain files with a "+r["file"]
            +" in round file - a labeled norm; the pitch is stamped on the drive link.")

def log_plan(barIn,logIn):
    if not pos(barIn) or not pos(logIn): return {"error":"bar and log must both be above zero"}
    if logIn<=barIn-2: verdict="one pass"
    elif logIn<=barIn*2-4: verdict="two passes, one from each side"
    else: verdict="beyond the bar - a bigger saw or a different plan"
    return {"verdict":verdict}

def render_log(r,barIn,logIn):
    lead=" is " if r["verdict"].startswith("beyond") else " goes in "
    return "Your "+jsnum(barIn)+" in bar against a "+jsnum(logIn)+" in log"+lead+r["verdict"]+"."

cases=[]
def add(tool,args):
    if tool=="mix": r=mix_plan(*args); fn=render_mix
    elif tool=="file": r=file_plan(*args); fn=render_file
    else: r=log_plan(*args); fn=render_log
    case={"tool":tool,"args":args,"result":r}
    if "error" not in r: case["render"]=fn(r,*args)
    cases.append(case)

for a in [(1,50),(2.5,50),(1,40),(5,50),(2,25),(0.5,50),(1,32),(3,50)]:
    add("mix",a)
for a in [("1/4",),(".325",),("3/8",),(".404",)]:
    add("file",a)
for a in [(16,12),(16,28),(18,20),(14,25),(20,36),(16,30),(12,22),(18,33)]:
    add("log",a)
add("mix",[0,50]); add("mix",[1,0]); add("file",[".500"]); add("log",[0,12]); add("log",[16,0])

json.dump(cases,open("expected.json","w"),separators=(",",":"))
print(len(cases),"cases")
