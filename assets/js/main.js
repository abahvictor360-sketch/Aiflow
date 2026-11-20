/* Aiflow — interactions & motion */
(() => {
  const $ = (s, r = document) => r.querySelector(s);
  const $$ = (s, r = document) => [...r.querySelectorAll(s)];
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const store = {
    get(k) { try { return JSON.parse(localStorage.getItem(k)); } catch { return null; } },
    set(k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch {} },
    del(k) { try { localStorage.removeItem(k); } catch {} },
  };

  /* ---- Page load / transition curtain ---- */
  const ready = () => requestAnimationFrame(() => document.body.classList.add('loaded'));
  if (document.readyState === 'complete') ready(); else addEventListener('load', ready);
  setTimeout(ready, 1200);
  addEventListener('pageshow', e => { if (e.persisted) document.body.classList.remove('leaving'); });
  document.addEventListener('click', e => {
    const a = e.target.closest('a[href]');
    if (!a || e.metaKey || e.ctrlKey || e.shiftKey || a.target === '_blank') return;
    const url = new URL(a.href, location.href);
    if (url.origin !== location.origin || url.pathname === location.pathname || a.hasAttribute('download')) return;
    e.preventDefault();
    document.body.classList.remove('menu-open');
    document.body.classList.add('leaving');
    setTimeout(() => { location.href = url.href; }, reduce ? 0 : 450);
  });

  /* ---- Nav ---- */
  const navWrap = $('.nav-wrap'), progress = $('.progress');
  const onScroll = () => {
    const y = scrollY;
    navWrap && navWrap.classList.toggle('scrolled', y > 20);
    if (progress) {
      const h = document.documentElement.scrollHeight - innerHeight;
      progress.style.width = (h > 0 ? (y / h) * 100 : 0) + '%';
    }
  };
  addEventListener('scroll', onScroll, { passive: true }); onScroll();
  $('.burger')?.addEventListener('click', () => document.body.classList.toggle('menu-open'));
  const page = document.body.dataset.page;
  $$('.nav-links a, .mobile-menu a').forEach(a => { if (a.dataset.page === page) a.classList.add('active'); });

  /* Reflect auth state in nav */
  const user = store.get('aiflow_user');
  if (user) $$('[data-auth-link]').forEach(a => { a.textContent = 'Dashboard'; a.href = 'dashboard.html'; });

  /* ---- Split headline words ---- */
  $$('.split-words').forEach(el => {
    const walk = node => {
      [...node.childNodes].forEach(n => {
        if (n.nodeType === 3) {
          const frag = document.createDocumentFragment();
          n.textContent.split(/(\s+)/).forEach(part => {
            if (!part) return;
            if (/^\s+$/.test(part)) { frag.append(' '); return; }
            const w = document.createElement('span'); w.className = 'w';
            const i = document.createElement('span'); i.textContent = part; w.append(i); frag.append(w);
          });
          n.replaceWith(frag);
        } else if (n.nodeType === 1 && n.tagName !== 'BR') walk(n);
      });
    };
    walk(el);
    $$('.w > span', el).forEach((s, i) => s.style.transitionDelay = (i * 0.07) + 's');
  });

  /* ---- Reveal on scroll ---- */
  const io = new IntersectionObserver(entries => {
    entries.forEach(en => { if (en.isIntersecting) { en.target.classList.add('in'); io.unobserve(en.target); } });
  }, { threshold: 0.14, rootMargin: '0px 0px -40px 0px' });
  $$('.reveal, .reveal-l, .reveal-r, .reveal-scale, .split-words').forEach(el => io.observe(el));

  /* ---- Counters ---- */
  const cio = new IntersectionObserver(entries => {
    entries.forEach(en => {
      if (!en.isIntersecting) return;
      const el = en.target; cio.unobserve(el);
      const to = parseFloat(el.dataset.count), dec = (el.dataset.count.split('.')[1] || '').length;
      const pre = el.dataset.prefix || '', suf = el.dataset.suffix || '';
      const t0 = performance.now(), dur = 1800;
      const tick = t => {
        const p = Math.min(1, (t - t0) / dur), e = 1 - Math.pow(1 - p, 4);
        el.textContent = pre + (to * e).toLocaleString(undefined, { minimumFractionDigits: dec, maximumFractionDigits: dec }) + suf;
        if (p < 1) requestAnimationFrame(tick);
      };
      requestAnimationFrame(tick);
    });
  }, { threshold: 0.5 });
  $$('[data-count]').forEach(el => cio.observe(el));

  /* ---- Typing agent prompt ---- */
  const typed = $('.typed');
  if (typed) {
    const items = JSON.parse(typed.dataset.items);
    const list = $('.agent-list');
    let i = 0;
    const type = async () => {
      const text = items[i % items.length];
      for (let c = 0; c <= text.length; c++) { typed.textContent = text.slice(0, c); await new Promise(r => setTimeout(r, 38)); }
      await new Promise(r => setTimeout(r, 1700));
      for (let c = text.length; c >= 0; c--) { typed.textContent = text.slice(0, c); await new Promise(r => setTimeout(r, 16)); }
      i++;
      if (list) {
        const rest = items.filter((_, k) => k !== i % items.length).slice(0, 5);
        list.innerHTML = rest.map(t => `<li>${t}</li>`).join('');
      }
      type();
    };
    type();
  }

  /* ---- Magnetic buttons ---- */
  if (!reduce && matchMedia('(hover: hover)').matches) {
    $$('.btn, .magnetic').forEach(b => {
      b.addEventListener('mousemove', e => {
        const r = b.getBoundingClientRect();
        b.style.transform = `translate(${(e.clientX - r.left - r.width / 2) * .18}px, ${(e.clientY - r.top - r.height / 2) * .3}px)`;
      });
      b.addEventListener('mouseleave', () => b.style.transform = '');
    });
    /* Spotlight cards */
    $$('.spot').forEach(c => c.addEventListener('mousemove', e => {
      const r = c.getBoundingClientRect();
      c.style.setProperty('--mx', (e.clientX - r.left) + 'px'); c.style.setProperty('--my', (e.clientY - r.top) + 'px');
    }));
    /* Cursor glow */
    const g = $('.cursor-glow');
    if (g) addEventListener('mousemove', e => { g.style.left = e.clientX + 'px'; g.style.top = e.clientY + 'px'; }, { passive: true });
    /* Hero parallax */
    const hv = $('.hero-visual');
    if (hv) {
      const img = $('img', hv), halo = $('.hero-halo', hv);
      addEventListener('mousemove', e => {
        const x = e.clientX / innerWidth - .5, y = e.clientY / innerHeight - .5;
        img.style.translate = `${x * -18}px ${y * -12}px`;
        if (halo) halo.style.translate = `${x * 30}px ${y * 24}px`;
      }, { passive: true });
    }
    /* Tilt */
    $$('.tilt').forEach(t => {
      t.addEventListener('mousemove', e => {
        const r = t.getBoundingClientRect(), x = (e.clientX - r.left) / r.width - .5, y = (e.clientY - r.top) / r.height - .5;
        t.style.transform = `perspective(900px) rotateY(${x * 8}deg) rotateX(${y * -8}deg)`;
      });
      t.addEventListener('mouseleave', () => t.style.transform = '');
    });
  }

  /* ---- Scroll parallax ---- */
  const px = $$('[data-parallax]');
  if (px.length && !reduce) {
    const run = () => {
      px.forEach(el => {
        const r = el.getBoundingClientRect(), s = parseFloat(el.dataset.parallax);
        el.style.transform = `translateY(${(r.top + r.height / 2 - innerHeight / 2) * s}px)`;
      });
      requestAnimationFrame(run);
    };
    run();
  }

  /* ---- Tabs ---- */
  $$('[data-tabs]').forEach(group => {
    const btns = $$('button', group), id = group.dataset.tabs;
    btns.forEach(b => b.addEventListener('click', () => {
      btns.forEach(x => x.classList.toggle('on', x === b));
      $$(`[data-panel^="${id}:"]`).forEach(p => p.classList.toggle('on', p.dataset.panel === `${id}:${b.dataset.tab}`));
    }));
  });

  /* ---- Pricing toggle ---- */
  const tg = $('[data-billing]');
  if (tg) {
    $$('button', tg).forEach(b => b.addEventListener('click', () => {
      $$('button', tg).forEach(x => x.classList.toggle('on', x === b));
      const yearly = b.dataset.mode === 'yearly';
      $$('[data-month]').forEach(p => {
        const v = yearly ? p.dataset.year : p.dataset.month;
        p.style.opacity = 0; p.style.transform = 'translateY(-8px)';
        setTimeout(() => { p.firstChild.textContent = v; p.style.opacity = 1; p.style.transform = ''; }, 200);
      });
    }));
    $$('[data-month]').forEach(p => p.style.transition = 'opacity .25s, transform .25s');
  }

  /* ---- Toast ---- */
  const toast = msg => {
    let t = $('.toast');
    if (!t) { t = document.createElement('div'); t.className = 'toast glass'; document.body.append(t); }
    t.textContent = msg; t.classList.add('show');
    clearTimeout(t._h); t._h = setTimeout(() => t.classList.remove('show'), 3200);
  };
  window.aiflowToast = toast;

  /* ---- Newsletter / contact ---- */
  $$('form[data-simple]').forEach(f => f.addEventListener('submit', e => {
    e.preventDefault();
    const bad = $$('[required]', f).filter(i => !i.value.trim() || (i.type === 'email' && !/^\S+@\S+\.\S+$/.test(i.value)));
    $$('.input', f).forEach(i => i.classList.remove('err'));
    if (bad.length) { bad.forEach(i => i.classList.add('err')); toast('Please complete the highlighted fields.'); return; }
    f.reset(); toast(f.dataset.simple);
  }));

  /* ---- Auth ---- */
  const auth = $('#auth-form');
  if (auth) {
    let mode = new URLSearchParams(location.search).get('mode') === 'signup' ? 'signup' : 'login';
    const setMode = m => {
      mode = m;
      $$('.auth-switch button').forEach(b => b.classList.toggle('on', b.dataset.mode === m));
      $$('[data-only]').forEach(el => el.hidden = el.dataset.only !== m);
      $('#auth-title').textContent = m === 'login' ? 'Welcome back' : 'Create your account';
      $('#auth-sub').textContent = m === 'login' ? 'Sign in to manage your AI agents.' : 'Start your 14-day free trial. No card required.';
      $('#auth-submit span').textContent = m === 'login' ? 'Sign in' : 'Create account';
      $('#name').required = m === 'signup';
    };
    $$('.auth-switch button').forEach(b => b.addEventListener('click', () => setMode(b.dataset.mode)));
    setMode(mode);
    $('.pw-wrap button')?.addEventListener('click', e => {
      const i = $('#password'); i.type = i.type === 'password' ? 'text' : 'password';
      e.currentTarget.textContent = i.type === 'password' ? 'Show' : 'Hide';
    });
    auth.addEventListener('submit', e => {
      e.preventDefault();
      const email = $('#email'), pw = $('#password'), name = $('#name');
      const errs = [];
      $$('.input', auth).forEach(i => i.classList.remove('err'));
      $$('.err-msg', auth).forEach(m => m.textContent = '');
      const fail = (el, msg) => { el.classList.add('err'); el.closest('.field').querySelector('.err-msg').textContent = msg; errs.push(el); };
      if (mode === 'signup' && name.value.trim().length < 2) fail(name, 'Please enter your full name.');
      if (!/^\S+@\S+\.\S+$/.test(email.value)) fail(email, 'Enter a valid work email.');
      if (pw.value.length < 8) fail(pw, 'Password must be at least 8 characters.');
      if (errs.length) return;
      const btn = $('#auth-submit');
      btn.disabled = true; btn.querySelector('.ico').innerHTML = '<div class="spinner"></div>';
      setTimeout(() => {
        const n = mode === 'signup' ? name.value.trim() : (store.get('aiflow_profile')?.email === email.value ? store.get('aiflow_profile').name : email.value.split('@')[0]);
        store.set('aiflow_user', { name: n, email: email.value });
        if (mode === 'signup') store.set('aiflow_profile', { name: n, email: email.value });
        toast(mode === 'signup' ? 'Account created — welcome to Aiflow!' : 'Signed in successfully.');
        setTimeout(() => { document.body.classList.add('leaving'); setTimeout(() => location.href = 'dashboard.html', 450); }, 700);
      }, 1100);
    });
    $$('.sso button').forEach(b => b.addEventListener('click', () => {
      store.set('aiflow_user', { name: 'Guest', email: 'guest@aiflow.ai' });
      toast(`Connecting with ${b.textContent.trim()}…`);
      setTimeout(() => { document.body.classList.add('leaving'); setTimeout(() => location.href = 'dashboard.html', 450); }, 900);
    }));
    $('#forgot')?.addEventListener('click', e => { e.preventDefault(); toast('Password reset link sent — check your inbox.'); });
  }

  /* ---- Dashboard ---- */
  if (page === 'dashboard') {
    const u = store.get('aiflow_user');
    if (!u) { location.replace('login.html'); return; }
    $$('[data-user-name]').forEach(el => el.textContent = u.name.split(' ')[0]);
    $$('[data-user-initial]').forEach(el => el.textContent = u.name[0].toUpperCase());
    $$('[data-logout]').forEach(b => b.addEventListener('click', e => {
      e.preventDefault(); store.del('aiflow_user'); document.body.classList.add('leaving'); setTimeout(() => location.href = 'index.html', 450);
    }));
    $$('.agent-row [data-toggle]').forEach(b => b.addEventListener('click', () => {
      const p = b.closest('.agent-row').querySelector('.pill');
      const on = p.classList.toggle('idle'); p.textContent = on ? 'Paused' : 'Running';
      b.textContent = on ? 'Resume' : 'Pause'; toast(on ? 'Agent paused' : 'Agent resumed');
    }));
    const live = $('[data-live]');
    if (live) setInterval(() => { live.textContent = (parseInt(live.textContent.replace(/,/g, '')) + Math.ceil(Math.random() * 7)).toLocaleString(); }, 1400);
  }

  /* Year */
  $$('[data-year]').forEach(el => el.textContent = new Date().getFullYear());
})();
