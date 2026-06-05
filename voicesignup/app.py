import streamlit as st
import sqlite3
import hashlib
import json

DB_PATH = "users.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute("""CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL)""")
        conn.commit()

def hash_pw(p):
    return hashlib.sha256(p.encode()).hexdigest()

def verify_user(u, p):
    with sqlite3.connect(DB_PATH) as conn:
        res = conn.execute("SELECT password FROM users WHERE username=?", (u,)).fetchone()
        return bool(res and res[0] == hash_pw(p))

def register_user(u, p):
    try:
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute("INSERT INTO users (username,password) VALUES (?,?)", (u, hash_pw(p)))
            conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False

init_db()
st.set_page_config(page_title="Voice Auth", page_icon="🎤", layout="centered")

# --- SESSION STATE INITIALIZATION ---
# Added 'logged_in' to handle page routing natively
for k, v in [("username",""), ("password",""), ("msg",""), ("msg_type",""), ("logged_in", False)]:
    if k not in st.session_state:
        st.session_state[k] = v

# --- INCOMING PAYLOAD HANDLING ---
if "voice_payload" in st.query_params:
    try:
        data = json.loads(st.query_params["voice_payload"])
        u = data.get("username","").strip()
        p = data.get("password","").strip()
        action = data.get("action","").lower().strip()
        if u: st.session_state.username = u
        if p: st.session_state.password = p
        
        if action in ["login","log in","signin","sign in"]:
            if verify_user(st.session_state.username, st.session_state.password):
                st.session_state.logged_in = True  # Routing flag
                st.session_state.msg = f"✅ Welcome back, {st.session_state.username}!"
                st.session_state.msg_type = "success"
            else:
                st.session_state.msg = "❌ Wrong username or password."
                st.session_state.msg_type = "error"
                
        elif action in ["register","signup","sign up"]:
            if register_user(st.session_state.username, st.session_state.password):
                st.session_state.logged_in = True  # Routing flag
                st.session_state.msg = f"🎉 Registered & Logged In {st.session_state.username}!"
                st.session_state.msg_type = "success"
            else:
                st.session_state.msg = "⚠️ Username already taken."
                st.session_state.msg_type = "error"
    except:
        pass
    
    # Clear the query parameters to prevent loops on manual page reloads
    st.query_params.clear()
    st.rerun()

# --- ROUTING LOGIC ---
if st.session_state.logged_in:
    # ----------------------------------------------------
    # NEW PAGE VIEW (Renders only after successful Auth)
    # ----------------------------------------------------
    st.title("🚀 Dashboard")
    st.subheader(f"Welcome to your secure space, {st.session_state.username}!")
    
    st.write("You have successfully authenticated using your voice.")
    
    # Dummy data or features for your application's interior page
    st.info("This is a completely brand new view isolated from the login page context.")
    
    # Logout feature to return to the original portal
    if st.button("Log Out", type="primary"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.password = ""
        st.session_state.msg = "Logged out successfully."
        st.session_state.msg_type = "success"
        st.rerun()

else:
    # ----------------------------------------------------
    # ORIGINAL LOGIN VIEW (HTML & Voice Interface)
    # ----------------------------------------------------
    uname = st.session_state.username
    pw    = st.session_state.password
    msg   = st.session_state.msg
    msg_type = st.session_state.msg_type

    msg_html = ""
    if msg:
        c = "#8ed4a8" if msg_type=="success" else "#e08888"
        b = "rgba(106,191,138,.12)" if msg_type=="success" else "rgba(224,92,92,.12)"
        bd = "rgba(106,191,138,.3)" if msg_type=="success" else "rgba(224,92,92,.3)"
        msg_html = f'<div style="background:{b};border:1px solid {bd};color:{c};padding:.7rem 1rem;border-radius:8px;font-size:.85rem;margin-top:1rem;">{msg}</div>'

    HTML = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8"/>
    <style>
      @import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Syne:wght@800&display=swap');
      *{{box-sizing:border-box;margin:0;padding:0;}}
      html,body{{background:#0c0d10;color:#e3e1da;font-family:'DM Mono',monospace;height:100%;}}
      body{{display:flex;align-items:flex-start;justify-content:center;padding:2rem 1rem;}}
      .app{{width:100%;max-width:480px;}}
      h1{{font-family:'Syne',sans-serif;font-size:2.2rem;font-weight:800;color:#f5f0e8;text-align:center;margin-bottom:1.5rem;letter-spacing:-1px;}}
      .card{{background:#111318;border:1px solid #1e2028;border-radius:14px;padding:1.5rem;margin-bottom:1rem;}}
      .field{{margin-bottom:1rem;}}
      .field:last-child{{margin-bottom:0;}}
      .field-label{{font-size:.65rem;letter-spacing:.15em;text-transform:uppercase;color:#555;margin-bottom:.4rem;}}
      .field-value{{background:#0c0d10;border:1px solid #252730;border-radius:8px;padding:.6rem .9rem;font-size:.9rem;color:#aaa;min-height:2.5rem;display:flex;align-items:center;transition:border-color .25s,color .25s;}}
      .field-value.filled{{border-color:#4a7fd4;color:#7ab3ff;font-weight:500;}}
      .orb-section{{display:flex;flex-direction:column;align-items:center;gap:.8rem;padding:1.5rem;}}
      .orb{{width:90px;height:90px;border-radius:50%;background:#1a1c24;border:2px solid #252730;display:flex;align-items:center;justify-content:center;font-size:2.2rem;cursor:pointer;transition:all .2s;user-select:none;-webkit-user-select:none;}}
      .orb:hover{{transform:scale(1.06);border-color:#333;}}
      .orb.idle{{background:#1a1c24;}}
      .orb.listening{{background:#b8922a;border-color:#d4a83a;animation:pulse-gold 1.2s ease-in-out infinite;}}
      .orb.processing{{background:#2a5bb8;border-color:#3a7ad4;animation:pulse-blue 1.2s ease-in-out infinite;}}
      @keyframes pulse-gold{{0%,100%{{box-shadow:0 0 0 0 rgba(184,146,42,.6);}}50%{{box-shadow:0 0 0 20px rgba(184,146,42,0);}}}}
      @keyframes pulse-blue{{0%,100%{{box-shadow:0 0 0 0 rgba(42,91,184,.6);}}50%{{box-shadow:0 0 0 20px rgba(42,91,184,0);}}}}
      .status{{font-size:.72rem;letter-spacing:.1em;text-transform:uppercase;color:#666;text-align:center;}}
      .status.active{{color:#d4a83a;}}
      .transcript{{font-size:.85rem;color:#c8a96e;font-style:italic;text-align:center;min-height:1.4rem;padding:0 .5rem;}}
      .steps{{display:flex;gap:.4rem;justify-content:center;margin-top:.3rem;}}
      .step{{padding:.25rem .7rem;border-radius:20px;font-size:.65rem;letter-spacing:.08em;text-transform:uppercase;background:#1a1c24;color:#444;border:1px solid #252730;transition:all .25s;}}
      .step.current{{background:#2a2200;color:#d4a83a;border-color:#5a4400;}}
      .step.done{{background:#0d1f3a;color:#4a7fd4;border-color:#1a3a6a;}}
      .hint{{font-size:.72rem;color:#444;text-align:center;margin-top:.5rem;}}
      .warn{{background:rgba(200,80,80,.1);border:1px solid rgba(200,80,80,.25);color:#d08888;padding:.6rem .9rem;border-radius:8px;font-size:.78rem;display:none;margin-top:.5rem;}}
    </style>
    </head>
    <body>
    <div class="app">
      <h1>Voice Auth</h1>

      <div class="card">
        <div class="field">
          <div class="field-label">Username</div>
          <div class="field-value {'filled' if uname else ''}" id="fv-u">
            {uname if uname else '<span style="color:#333">—</span>'}
          </div>
        </div>
        <div class="field">
          <div class="field-label">Password</div>
          <div class="field-value {'filled' if pw else ''}" id="fv-p">
            {'●'*min(len(pw),14) if pw else '<span style="color:#333">—</span>'}
          </div>
        </div>
      </div>

      <div class="card orb-section">
        <div class="orb idle" id="orb">🎤</div>
        <div class="status" id="status">Tap to start listening</div>
        <div class="transcript" id="transcript"></div>
        <div class="steps">
          <div class="step {'done' if uname else 'current'}" id="s0">Username</div>
          <div class="step {'done' if pw else ('current' if uname else '')}" id="s1">Password</div>
          <div class="step {'current' if uname and pw else ''}" id="s2">Action</div>
        </div>
        <div class="hint" id="hint">Say username → password → "login" or "register"</div>
      </div>

      {msg_html}
      <div class="warn" id="no-sr">⚠️ Speech not supported. Use Chrome or Edge on desktop.</div>
</div>

    <script>
    (function(){{
      var SR = window.SpeechRecognition || window.webkitSpeechRecognition;
      if (!SR) {{
        document.getElementById('no-sr').style.display='block';
        document.getElementById('orb').textContent='🚫';
        return;
      }}

      var flow = {{
        username: {json.dumps(uname)},
        password: {json.dumps(pw)},
        action: ""
      }};

      var step = flow.username ? (flow.password ? 2 : 1) : 0;
      var listening = false;
      var shouldLoop = false;
      var recog = null;
      var buf = "";

      var orbEl     = document.getElementById('orb');
      var statusEl  = document.getElementById('status');
      var transEl   = document.getElementById('transcript');
      var fvU       = document.getElementById('fv-u');
      var fvP       = document.getElementById('fv-p');
      var s0        = document.getElementById('s0');
      var s1        = document.getElementById('s1');
      var s2        = document.getElementById('s2');
      var hintEl    = document.getElementById('hint');

      var PROMPTS = [
        "Speak your username…",
        "Speak your password…",
        'Say  "login"  or  "register"…'
      ];

      function updateStepUI() {{
        [s0,s1,s2].forEach(function(el,i){{
          el.className = 'step' + (i < step ? ' done' : i===step ? ' current' : '');
        }});
      }}

      function setOrb(state, status) {{
        orbEl.className = 'orb ' + (state||'idle');
        statusEl.className = 'status' + (state==='listening'?' active':'');
        if (status) statusEl.textContent = status;
      }}

      function stopRecog() {{
        listening = false;
        if (recog) {{ try{{recog.stop();}}catch(e){{}} recog=null; }}
      }}

      function processText(raw) {{
        var t = raw.toLowerCase()
                   .replace(/^(um|uh|okay|ok|so|like|hey)\\s+/i,'')
                   .replace(/[.,!?]+$/,'')
                   .trim();
        if (!t) return;

        if (step===0) {{
          t = t.replace(/\\busername\\s+(is\\s+)?/i,'').trim().replace(/\\s+/g,'_');
          if (!t) return;
          flow.username = t;
          fvU.className='field-value filled';
          fvU.textContent = t;
          step=1; buf="";
          updateStepUI();
          setOrb('listening', PROMPTS[1]);
          transEl.textContent='';

        }} else if (step===1) {{
          t = t.replace(/\\b(my\\s+)?password\\s+(is\\s+)?/i,'').trim();
          if (!t) return;
          flow.password = t;
          fvP.className='field-value filled';
          fvP.textContent = '●'.repeat(Math.min(t.length,14));
          step=2; buf="";
          updateStepUI();
          setOrb('listening', PROMPTS[2]);
          transEl.textContent='';

        }} else if (step===2) {{
          if (t.includes('login')||t.includes('log in')||t.includes('sign in')) {{
            flow.action='login';
            finish('Processing login…');
          }} else if (t.includes('register')||t.includes('signup')||t.includes('sign up')) {{
            flow.action='register';
            finish('Processing registration…');
          }} else {{
            transEl.textContent = '"'+raw.trim()+'" — say login or register';
          }}
        }}
      }}

      function finish(msg) {{
        shouldLoop=false;
        setOrb('processing', msg);
        stopRecog();
        setTimeout(function(){{
          var url = new URL(window.location.href);
          url.searchParams.set('voice_payload', JSON.stringify(flow));
          window.location.href = url.toString();
        }}, 350);
      }}

      function launch() {{
        if (listening) return;
        buf = "";
        recog = new SR();
        recog.lang='en-US';
        recog.interimResults=true;
        recog.continuous=false;
        recog.maxAlternatives=1;

        recog.onstart=function(){{ listening=true; }};

        recog.onresult=function(e){{
          buf=''; var interim='';
          for(var i=0;i<e.results.length;i++){{
            if(e.results[i].isFinal) buf+=e.results[i][0].transcript;
            else interim+=e.results[i][0].transcript;
          }}
          transEl.textContent = (buf||interim).trim() ? '"'+(buf||interim).trim()+'"' : '';
        }};

        recog.onerror=function(e){{
          listening=false;
          if((e.error==='no-speech'||e.error==='audio-capture') && shouldLoop){{
            setTimeout(launch,150);
          }} else if(e.error!=='aborted'){{
            shouldLoop=false;
            setOrb('idle','Tap to start listening');
          }}
        }};

        recog.onend=function(){{
          listening=false;
          var captured=buf.trim();
          if(captured){{ processText(captured); buf=""; }}
          if(shouldLoop && step<3) setTimeout(launch,150);
        }};

        try{{ recog.start(); }}catch(e){{ console.warn(e); }}
      }}

      function startSession() {{
        shouldLoop=true;
        step = flow.username ? (flow.password ? 2 : 1) : 0;
        updateStepUI();
        setOrb('listening', PROMPTS[step]);
        launch();
      }}

      orbEl.addEventListener('click',function(){{
        if(listening){{ shouldLoop=false; stopRecog(); setOrb('idle','Tap to start listening'); }}
        else{{ startSession(); }}
      }});

      document.addEventListener('keydown',function(e){{
        if((e.code==='Space'||e.keyCode===32)&&!listening){{
          e.preventDefault();
          startSession();
        }}
      }});

      updateStepUI();
    }})();
</script>
    </body>
    </html>
    """
    st.components.v1.html(HTML, height=620, scrolling=False)