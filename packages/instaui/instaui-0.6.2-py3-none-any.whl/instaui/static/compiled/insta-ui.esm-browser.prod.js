var ur = Object.defineProperty;
var fr = (e, t, n) => t in e ? ur(e, t, { enumerable: !0, configurable: !0, writable: !0, value: n }) : e[t] = n;
var Y = (e, t, n) => fr(e, typeof t != "symbol" ? t + "" : t, n);
import * as dr from "vue";
import { toRaw as dn, toValue as be, normalizeClass as ut, normalizeStyle as hr, cloneVNode as re, vModelDynamic as pr, vShow as mr, withDirectives as hn, h as J, toDisplayString as pn, withModifiers as gr, resolveDynamicComponent as yr, normalizeProps as vr, TransitionGroup as wr, createTextVNode as _r, unref as H, toRef as me, readonly as Rt, customRef as ye, ref as U, onBeforeUnmount as Er, onMounted as mn, nextTick as Se, getCurrentScope as br, onScopeDispose as Sr, getCurrentInstance as He, watch as G, isRef as Ot, shallowRef as ie, watchEffect as Nt, computed as j, inject as ae, shallowReactive as kr, defineComponent as Z, reactive as Rr, provide as z, onUnmounted as Or, onErrorCaptured as Nr, openBlock as fe, createElementBlock as Ee, createElementVNode as gn, createVNode as Pr, createCommentVNode as ft, mergeProps as de, createBlock as yn, Teleport as Vr, renderSlot as Cr, useAttrs as Ar, Fragment as xr, useSlots as Ke, KeepAlive as $r } from "vue";
let vn;
function Tr(e) {
  vn = e;
}
function dt() {
  return vn;
}
function We() {
  const { queryPath: e, pathParams: t, queryParams: n } = dt();
  return {
    path: e,
    ...t === void 0 ? {} : { params: t },
    ...n === void 0 ? {} : { queryParams: n }
  };
}
function Mt(e, t) {
  Object.entries(e).forEach(([n, r]) => t(r, n));
}
function Ge(e, t) {
  return wn(e, {
    valueFn: t
  });
}
function wn(e, t) {
  const { valueFn: n, keyFn: r } = t;
  return Object.fromEntries(
    Object.entries(e).map(([s, o], i) => [
      r ? r(s, o) : s,
      n(o, s, i)
    ])
  );
}
function Ir(e, t, n) {
  if (Array.isArray(t)) {
    const [s, ...o] = t;
    switch (s) {
      case "!":
        return !e;
      case "+":
        return e + o[0];
      case "~+":
        return o[0] + e;
    }
  }
  const r = Dr(t);
  return e[r];
}
function Dr(e, t) {
  if (typeof e == "string" || typeof e == "number")
    return e;
  if (!Array.isArray(e))
    throw new Error(`Invalid path ${e}`);
  const [n, ...r] = e;
  switch (n) {
    case "bind":
      throw new Error("No bindable function provided");
    default:
      throw new Error(`Invalid flag ${n} in array at ${e}`);
  }
}
function Mr(e, t, n) {
  return t.reduce(
    (r, s) => Ir(r, s),
    e
  );
}
function jr(e, t) {
  return t ? t.reduce((n, r) => n[r], e) : e;
}
const Br = window.structuredClone || ((e) => JSON.parse(JSON.stringify(e)));
function _n(e) {
  if (typeof e == "function")
    return e;
  try {
    return Br(dn(be(e)));
  } catch {
    return e;
  }
}
function Lr(e, t) {
  const n = e.classes;
  if (!n)
    return null;
  if (typeof n == "string")
    return ut(n);
  const { str: r, map: s, bind: o } = n, { bindingGetter: i } = t, c = [];
  return r && c.push(r), s && c.push(
    Ge(
      s,
      (a) => i.getValue(a)
    )
  ), o && c.push(...o.map((a) => i.getValue(a))), ut(c);
}
function Fr(e, t) {
  const n = [], { bindingGetter: r } = t, { dStyle: s = {}, sStyle: o = [] } = e;
  n.push(
    Ge(
      s || {},
      (a) => r.getValue(a)
    )
  ), n.push(
    ...o.map((a) => r.getValue(a))
  );
  const i = hr([e.style || {}, n]);
  return {
    hasStyle: i && Object.keys(i).length > 0,
    styles: i
  };
}
function Wr(e, t, n) {
  const r = [], { dir: s = [] } = t, { bindingGetter: o } = n;
  return s.forEach((i) => {
    const { sys: c, name: a, arg: h, value: u, mf: l } = i;
    if (a === "vmodel") {
      const f = o.getRef(u);
      if (e = re(e, {
        [`onUpdate:${h}`]: (d) => {
          f.value = d;
        }
      }), c === 1) {
        const d = l ? Object.fromEntries(l.map((p) => [p, !0])) : {};
        r.push([pr, f.value, void 0, d]);
      } else
        e = re(e, {
          [h]: f.value
        });
    } else if (a === "vshow") {
      const f = o.getValue(u);
      r.push([mr, f]);
    } else
      console.warn(`Directive ${a} is not supported yet`);
  }), r.length > 0 ? hn(e, r) : e;
}
function Te(e, t) {
  return J(or, {
    config: e,
    vforSetting: t == null ? void 0 : t.vforSetting,
    slotSetting: t == null ? void 0 : t.slotSetting
  });
}
function Ur(e, t, n) {
  if (!e.slots)
    return;
  const r = e.slots ?? {};
  if (t) {
    const c = r[":"];
    if (!c)
      return;
    const { scope: a, items: h } = c;
    return a ? Te(a, {
      buildOptions: n
    }) : h == null ? void 0 : h.map((u) => ve(u, n));
  }
  return wn(r, { keyFn: (c) => c === ":" ? "default" : c, valueFn: (c) => {
    const { usePropId: a, scope: h } = c;
    return h ? (u) => Te(h, {
      buildOptions: n,
      slotSetting: a ? {
        id: a,
        value: u
      } : void 0
    }) : () => {
      var u;
      return (u = c.items) == null ? void 0 : u.map((l) => ve(l, n));
    };
  } });
}
function q(e, t) {
  t = t || {};
  const n = [...Object.keys(t), "__Vue"], r = [...Object.values(t), dr];
  try {
    return new Function(...n, `return (${e})`)(...r);
  } catch (s) {
    throw new Error(s + " in function code: " + e);
  }
}
function Ue(e, t = !0) {
  if (!(typeof e != "object" || e === null)) {
    if (Array.isArray(e)) {
      t && e.forEach((n) => Ue(n, !0));
      return;
    }
    for (const [n, r] of Object.entries(e))
      if (n.startsWith(":"))
        try {
          e[n.slice(1)] = new Function(`return (${r})`)(), delete e[n];
        } catch (s) {
          console.error(
            `Error while converting ${n} attribute to function:`,
            s
          );
        }
      else
        t && Ue(r, !0);
  }
}
function zr(e, t) {
  const n = e.startsWith(":");
  return n && (e = e.slice(1), t = q(t)), { name: e, value: t, isFunc: n };
}
class Hr {
  toString() {
    return "";
  }
}
const Ie = new Hr();
function ke(e) {
  return dn(e) === Ie;
}
function Kr(e, t) {
  var o;
  const n = {}, r = e.props ?? {}, { bindingGetter: s } = t;
  return Ue(r), Mt(e.bProps || {}, (i, c) => {
    const a = s.getValue(i);
    ke(a) || (Ue(a), n[c] = Gr(a, c));
  }), (o = e.proxyProps) == null || o.forEach((i) => {
    const c = s.getValue(i);
    typeof c == "object" && Mt(c, (a, h) => {
      const { name: u, value: l } = zr(h, a);
      n[u] = l;
    });
  }), { ...r, ...n };
}
function Gr(e, t) {
  return t === "innerText" ? pn(e) : e;
}
function Pt(e) {
  return e !== null && typeof e == "object" && e.nodeType === 1 && typeof e.nodeName == "string";
}
class qr {
  async eventSend(t, n) {
    const { fType: r, hKey: s, key: o } = t, i = dt().webServerInfo, c = o !== void 0 ? { key: o } : {}, a = r === "sync" ? i.event_url : i.event_async_url;
    let h = {};
    const u = await fetch(a, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        bind: n,
        hKey: s,
        ...c,
        page: We(),
        ...h
      })
    });
    if (!u.ok)
      throw new Error(`HTTP error! status: ${u.status}`);
    return await u.json();
  }
  async watchSend(t) {
    const { fType: n, key: r } = t.watchConfig, s = dt().webServerInfo, o = n === "sync" ? s.watch_url : s.watch_async_url, i = t.getServerInputs(), c = {
      key: r,
      input: i,
      page: We()
    };
    return await (await fetch(o, {
      method: "POST",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify(c)
    })).json();
  }
}
class Jr {
  async eventSend(t, n) {
    const { fType: r, hKey: s, key: o } = t, i = o !== void 0 ? { key: o } : {};
    let c = {};
    const a = {
      bind: n,
      fType: r,
      hKey: s,
      ...i,
      page: We(),
      ...c
    };
    return await window.pywebview.api.event_call(a);
  }
  async watchSend(t) {
    const { fType: n, key: r } = t.watchConfig, s = t.getServerInputs(), o = {
      key: r,
      input: s,
      fType: n,
      page: We()
    };
    return await window.pywebview.api.watch_call(o);
  }
}
let ht;
function Qr(e) {
  switch (e) {
    case "web":
      ht = new qr();
      break;
    case "webview":
      ht = new Jr();
      break;
  }
}
function En() {
  return ht;
}
function bn(e) {
  const { config: t, bindingGetter: n } = e;
  if (!t)
    return {
      run: () => {
      },
      tryReset: () => {
      }
    };
  const r = t.map((i) => {
    const [c, a, h] = i, u = n.getRef(c);
    function l(f, d) {
      const { type: p, value: g } = d;
      if (p === "const") {
        f.value = g;
        return;
      }
      if (p === "action") {
        const y = Yr(g, n);
        f.value = y;
        return;
      }
    }
    return {
      run: () => l(u, a),
      reset: () => l(u, h)
    };
  });
  return {
    run: () => {
      r.forEach((i) => i.run());
    },
    tryReset: () => {
      r.forEach((i) => i.reset());
    }
  };
}
function Yr(e, t) {
  const { inputs: n = [], code: r } = e, s = q(r), o = n.map((i) => t.getValue(i));
  return s(...o);
}
function jt(e) {
  return e == null;
}
const ue = {
  Ref: 0,
  EventContext: 1,
  Data: 2,
  JsFn: 3,
  ElementRef: 4
}, Bt = {
  const: "c",
  ref: "r",
  range: "n"
}, Ae = {
  Ref: 0,
  RouterAction: 1,
  ElementRefAction: 2,
  JsCode: 3
};
function qe(e, t, n) {
  if (jt(t) || jt(e.values))
    return;
  t = t;
  const r = e.values, s = e.types ?? Array.from({ length: t.length }).fill(0);
  t.forEach((o, i) => {
    const c = s[i];
    if (c === 1)
      return;
    if (o.type === Ae.Ref) {
      if (c === 2) {
        r[i].forEach(([u, l]) => {
          const f = o.ref, d = {
            ...f,
            path: [...f.path ?? [], ...u]
          };
          n.updateValue(d, l);
        });
        return;
      }
      n.updateValue(o.ref, r[i]);
      return;
    }
    if (o.type === Ae.RouterAction) {
      const h = r[i], u = n.getRouter(o.ref)[h.fn];
      u(...h.args);
      return;
    }
    if (o.type === Ae.ElementRefAction) {
      const h = o.ref, u = n.getRef(h).value, l = r[i], { method: f, args: d = [] } = l;
      u[f](...d);
      return;
    }
    if (o.type === Ae.JsCode) {
      const h = r[i];
      if (!h)
        return;
      const u = q(h);
      Promise.resolve(u());
      return;
    }
    const a = n.getRef(o.ref);
    a.value = r[i];
  });
}
class Xr extends Map {
  constructor(t) {
    super(), this.factory = t;
  }
  getOrDefault(t) {
    if (!this.has(t)) {
      const n = this.factory();
      return this.set(t, n), n;
    }
    return super.get(t);
  }
}
function Sn(e) {
  return new Xr(e);
}
const Zr = "on:mounted";
function es(e, t, n) {
  if (!t)
    return e;
  const r = Sn(() => []);
  t.map(([c, a]) => {
    const h = ts(a, n), { eventName: u, handleEvent: l } = is({
      eventName: c,
      info: a,
      handleEvent: h
    });
    r.getOrDefault(u).push(l);
  });
  const s = {};
  for (const [c, a] of r) {
    const h = a.length === 1 ? a[0] : (...u) => a.forEach((l) => Promise.resolve().then(() => l(...u)));
    s[c] = h;
  }
  const { [Zr]: o, ...i } = s;
  return e = re(e, i), o && (e = hn(e, [
    [
      {
        mounted(c) {
          o(c);
        }
      }
    ]
  ])), e;
}
function ts(e, t) {
  if (e.type === "web") {
    const n = ns(e, t);
    return rs(e, n, t);
  } else {
    if (e.type === "vue")
      return os(e, t);
    if (e.type === "js")
      return ss(e, t);
  }
  throw new Error(`unknown event type ${e}`);
}
function ns(e, t) {
  const { inputs: n = [] } = e, { bindingGetter: r } = t;
  return (...s) => n.map(({ value: o, type: i }) => {
    if (i === ue.EventContext) {
      const { path: c } = o;
      if (c.startsWith(":")) {
        const a = c.slice(1);
        return q(a)(...s);
      }
      return jr(s[0], c.split("."));
    }
    return i === ue.Ref ? r.getValue(o) : o;
  });
}
function rs(e, t, n) {
  const { bindingGetter: r } = n;
  async function s(...o) {
    const i = t(...o), c = bn({
      config: e.preSetup,
      bindingGetter: r
    });
    try {
      c.run();
      const a = await En().eventSend(e, i);
      if (!a)
        return;
      qe(a, e.sets, r);
    } finally {
      c.tryReset();
    }
  }
  return s;
}
function ss(e, t) {
  const { sets: n, code: r, inputs: s = [] } = e, { bindingGetter: o } = t, i = q(r);
  function c(...a) {
    const h = s.map(({ value: l, type: f }) => {
      if (f === ue.EventContext) {
        if (l.path.startsWith(":")) {
          const d = l.path.slice(1);
          return q(d)(...a);
        }
        return Mr(a[0], l.path.split("."));
      }
      if (f === ue.Ref)
        return o.getValue(l);
      if (f === ue.Data)
        return l;
      if (f === ue.ElementRef) {
        const d = o.getValue(l);
        return d && (Pt(d) ? d : d.$el);
      }
      if (f === ue.JsFn)
        return o.getValue(l);
      throw new Error(`unknown input type ${f}`);
    }), u = i(...h);
    if (n !== void 0) {
      const f = n.length === 1 ? [u] : u, d = f.map((p) => p === void 0 ? 1 : 0);
      qe(
        { values: f, types: d },
        n,
        o
      );
    }
  }
  return c;
}
function os(e, t) {
  const { code: n, inputs: r = {} } = e, { bindingGetter: s } = t, o = Ge(
    r,
    (a) => a.type !== ue.Data ? s.getRef(a.value) : a.value
  ), i = q(n, o);
  function c(...a) {
    i(...a);
  }
  return c;
}
function is(e) {
  const { eventName: t, info: n, handleEvent: r } = e;
  if (n.type === "vue")
    return {
      eventName: t,
      handleEvent: r
    };
  const { modifier: s = [] } = n;
  if (s.length === 0)
    return {
      eventName: t,
      handleEvent: r
    };
  const o = ["passive", "capture", "once"], i = [], c = [];
  for (const u of s)
    o.includes(u) ? i.push(u[0].toUpperCase() + u.slice(1)) : c.push(u);
  const a = i.length > 0 ? t + i.join("") : t, h = c.length > 0 ? gr(r, c) : r;
  return {
    eventName: a,
    handleEvent: h
  };
}
function as(e, t, n) {
  const { eRef: r } = t, { bindingGetter: s } = n;
  return r ? re(e, { ref: s.getRef(r) }) : e;
}
function cs(e, t) {
  const n = ls(e, t), r = yr(n), s = typeof r == "string", o = Lr(e, t), { styles: i, hasStyle: c } = Fr(e, t), a = Ur(e, s, t), h = Kr(e, t), u = vr(h) || {};
  c && (u.style = i), o && (u.class = o);
  let l = J(r, { ...u }, a);
  return l = es(l, e.events, t), l = as(l, e, t), Wr(l, e, t);
}
function ls(e, t) {
  const { tag: n } = e;
  return typeof n == "string" ? n : t.bindingGetter.getValue(n);
}
function us(e, t) {
  var l, f, d;
  const { fkey: n, tsGroup: r = {}, scope: s } = e, o = !!((l = e.used) != null && l.item), i = !!((f = e.used) != null && f.index), c = !!((d = e.used) != null && d.key), a = [], { sourceInfo: h, iterSource: u } = fs(e, t);
  for (const [p, g, y] of u) {
    const _ = {};
    o && (_.item = {
      value: g,
      id: e.used.item
    }, h && (_.item.sourceInfo = {
      source: h.source,
      type: h.type,
      index: p,
      key: y
    })), i && (_.index = {
      value: p,
      id: e.used.index
    }), c && (_.key = {
      value: y,
      id: e.used.key
    });
    let w = Te(s, {
      buildOptions: t,
      vforSetting: _
    });
    const k = ps(n, { value: g, index: p });
    w = re(w, { key: k }), a.push(w);
  }
  return r && Object.keys(r).length > 0 ? J(wr, r, {
    default: () => a
  }) : a;
}
function fs(e, t) {
  const { type: n, value: r } = e.array, { bindingGetter: s } = t, o = n === Bt.range, i = n === Bt.const || o && typeof r == "number";
  if (o) {
    const { start: c = 0, end: a, step: h = 1 } = r, u = typeof c == "number" ? c : s.getValue(c), l = typeof a == "number" ? a : s.getValue(a), f = typeof h == "number" ? h : s.getValue(h);
    return {
      sourceInfo: void 0,
      iterSource: Lt(u, l, f)
    };
  }
  {
    const c = i ? r : s.getValue(e.array.value);
    if (typeof c == "number")
      return {
        sourceInfo: void 0,
        iterSource: Lt(0, c, 1)
      };
    if (Array.isArray(c)) {
      function* a() {
        for (let h = 0; h < c.length; h++)
          yield [h, c[h]];
      }
      return {
        sourceInfo: i ? void 0 : {
          source: s.getRef(e.array.value),
          type: "array"
        },
        iterSource: a()
      };
    }
    if (typeof c == "object" && c !== null) {
      function* a() {
        let h = 0;
        for (const [u, l] of Object.entries(c))
          yield [h++, l, u];
      }
      return {
        sourceInfo: i ? void 0 : {
          source: s.getRef(e.array.value),
          type: "object"
        },
        iterSource: a()
      };
    }
    if (ke(c))
      return c;
  }
  throw new Error("Not implemented yet");
}
function* Lt(e, t, n = 1) {
  if (n === 0)
    throw new Error("Step cannot be 0");
  let r = 0;
  if (n > 0)
    for (let s = e; s < t; s += n)
      yield [r++, s];
  else
    for (let s = e; s > t; s += n)
      yield [r++, s];
}
const ds = (e) => e, hs = (e, t) => t;
function ps(e, t) {
  const { value: n, index: r } = t, s = ms(e ?? "index");
  return typeof s == "function" ? s(n, r) : e === "item" ? ds(n) : hs(n, r);
}
function ms(e) {
  const t = e.trim();
  if (t === "item" || t === "index")
    return;
  if (e.startsWith(":")) {
    e = e.slice(1);
    try {
      return q(e);
    } catch (r) {
      throw new Error(r + " in function code: " + e);
    }
  }
  const n = `(item, index) => { return ${t}; }`;
  try {
    return q(n);
  } catch (r) {
    throw new Error(r + " in function code: " + n);
  }
}
function gs(e, t) {
  const { on: n, items: r } = e;
  return (typeof n == "boolean" ? n : t.bindingGetter.getValue(n)) ? r == null ? void 0 : r.map((o) => ve(o, t)) : void 0;
}
function ys(e, t) {
  const { cond: n, const: r = 0, cases: s, default: o } = e, c = r === 1 ? n : t.bindingGetter.getValue(n), a = [];
  let h = !1;
  for (const { value: u, items: l = [] } of s || [])
    if (u === c) {
      a.push(...l.map((f) => ve(f, t))), h = !0;
      break;
    }
  return !h && o && o.items && a.push(
    ...o.items.map((u) => ve(u, t))
  ), a;
}
function vs(e, t) {
  const { value: n, r = 0 } = e, s = r === 1 ? t.bindingGetter.getValue(n) : n;
  return _r(s);
}
const ws = /* @__PURE__ */ new Map(
  [
    ["vfor", us],
    ["vif", gs],
    ["match", ys],
    ["content", vs]
  ]
);
function _s(e, t) {
  const n = ws.get(e.tag);
  if (!n)
    throw new Error(`Unknown logic component ${e.tag}`);
  return n(e, t);
}
function ve(e, t) {
  const { type: n } = e;
  if (n === "cp")
    return cs(e, t);
  if (n === "logic")
    return _s(e, t);
  if (n === "scope")
    return Te(e, {
      buildOptions: t
    });
  throw new Error(`Unknown component type ${n}`);
}
function kn(e) {
  return "r" in e;
}
function Vt(e) {
  return br() ? (Sr(e), !0) : !1;
}
function te(e) {
  return typeof e == "function" ? e() : H(e);
}
const Rn = typeof window < "u" && typeof document < "u";
typeof WorkerGlobalScope < "u" && globalThis instanceof WorkerGlobalScope;
const Es = (e) => e != null, bs = Object.prototype.toString, Ss = (e) => bs.call(e) === "[object Object]", De = () => {
};
function ks(e, t) {
  function n(...r) {
    return new Promise((s, o) => {
      Promise.resolve(e(() => t.apply(this, r), { fn: t, thisArg: this, args: r })).then(s).catch(o);
    });
  }
  return n;
}
const On = (e) => e();
function Rs(e = On) {
  const t = U(!0);
  function n() {
    t.value = !1;
  }
  function r() {
    t.value = !0;
  }
  const s = (...o) => {
    t.value && e(...o);
  };
  return { isActive: Rt(t), pause: n, resume: r, eventFilter: s };
}
function pt(e, t = !1, n = "Timeout") {
  return new Promise((r, s) => {
    setTimeout(t ? () => s(n) : r, e);
  });
}
function Nn(e) {
  return He();
}
function Pn(...e) {
  if (e.length !== 1)
    return me(...e);
  const t = e[0];
  return typeof t == "function" ? Rt(ye(() => ({ get: t, set: De }))) : U(t);
}
function Os(e, t, n = {}) {
  const {
    eventFilter: r = On,
    ...s
  } = n;
  return G(
    e,
    ks(
      r,
      t
    ),
    s
  );
}
function Ns(e, t, n = {}) {
  const {
    eventFilter: r,
    ...s
  } = n, { eventFilter: o, pause: i, resume: c, isActive: a } = Rs(r);
  return { stop: Os(
    e,
    t,
    {
      ...s,
      eventFilter: o
    }
  ), pause: i, resume: c, isActive: a };
}
function Ps(e, t) {
  Nn() && Er(e, t);
}
function Vn(e, t = !0, n) {
  Nn() ? mn(e, n) : t ? e() : Se(e);
}
function mt(e, t = !1) {
  function n(l, { flush: f = "sync", deep: d = !1, timeout: p, throwOnTimeout: g } = {}) {
    let y = null;
    const w = [new Promise((k) => {
      y = G(
        e,
        (v) => {
          l(v) !== t && (y ? y() : Se(() => y == null ? void 0 : y()), k(v));
        },
        {
          flush: f,
          deep: d,
          immediate: !0
        }
      );
    })];
    return p != null && w.push(
      pt(p, g).then(() => te(e)).finally(() => y == null ? void 0 : y())
    ), Promise.race(w);
  }
  function r(l, f) {
    if (!Ot(l))
      return n((v) => v === l, f);
    const { flush: d = "sync", deep: p = !1, timeout: g, throwOnTimeout: y } = f ?? {};
    let _ = null;
    const k = [new Promise((v) => {
      _ = G(
        [e, l],
        ([R, A]) => {
          t !== (R === A) && (_ ? _() : Se(() => _ == null ? void 0 : _()), v(R));
        },
        {
          flush: d,
          deep: p,
          immediate: !0
        }
      );
    })];
    return g != null && k.push(
      pt(g, y).then(() => te(e)).finally(() => (_ == null || _(), te(e)))
    ), Promise.race(k);
  }
  function s(l) {
    return n((f) => !!f, l);
  }
  function o(l) {
    return r(null, l);
  }
  function i(l) {
    return r(void 0, l);
  }
  function c(l) {
    return n(Number.isNaN, l);
  }
  function a(l, f) {
    return n((d) => {
      const p = Array.from(d);
      return p.includes(l) || p.includes(te(l));
    }, f);
  }
  function h(l) {
    return u(1, l);
  }
  function u(l = 1, f) {
    let d = -1;
    return n(() => (d += 1, d >= l), f);
  }
  return Array.isArray(te(e)) ? {
    toMatch: n,
    toContains: a,
    changed: h,
    changedTimes: u,
    get not() {
      return mt(e, !t);
    }
  } : {
    toMatch: n,
    toBe: r,
    toBeTruthy: s,
    toBeNull: o,
    toBeNaN: c,
    toBeUndefined: i,
    changed: h,
    changedTimes: u,
    get not() {
      return mt(e, !t);
    }
  };
}
function Vs(e) {
  return mt(e);
}
function Cs(e, t, n) {
  let r;
  Ot(n) ? r = {
    evaluating: n
  } : r = n || {};
  const {
    lazy: s = !1,
    evaluating: o = void 0,
    shallow: i = !0,
    onError: c = De
  } = r, a = U(!s), h = i ? ie(t) : U(t);
  let u = 0;
  return Nt(async (l) => {
    if (!a.value)
      return;
    u++;
    const f = u;
    let d = !1;
    o && Promise.resolve().then(() => {
      o.value = !0;
    });
    try {
      const p = await e((g) => {
        l(() => {
          o && (o.value = !1), d || g();
        });
      });
      f === u && (h.value = p);
    } catch (p) {
      c(p);
    } finally {
      o && f === u && (o.value = !1), d = !0;
    }
  }), s ? j(() => (a.value = !0, h.value)) : h;
}
const Re = Rn ? window : void 0, As = Rn ? window.document : void 0;
function Ct(e) {
  var t;
  const n = te(e);
  return (t = n == null ? void 0 : n.$el) != null ? t : n;
}
function Ft(...e) {
  let t, n, r, s;
  if (typeof e[0] == "string" || Array.isArray(e[0]) ? ([n, r, s] = e, t = Re) : [t, n, r, s] = e, !t)
    return De;
  Array.isArray(n) || (n = [n]), Array.isArray(r) || (r = [r]);
  const o = [], i = () => {
    o.forEach((u) => u()), o.length = 0;
  }, c = (u, l, f, d) => (u.addEventListener(l, f, d), () => u.removeEventListener(l, f, d)), a = G(
    () => [Ct(t), te(s)],
    ([u, l]) => {
      if (i(), !u)
        return;
      const f = Ss(l) ? { ...l } : l;
      o.push(
        ...n.flatMap((d) => r.map((p) => c(u, d, p, f)))
      );
    },
    { immediate: !0, flush: "post" }
  ), h = () => {
    a(), i();
  };
  return Vt(h), h;
}
function xs() {
  const e = U(!1), t = He();
  return t && mn(() => {
    e.value = !0;
  }, t), e;
}
function Cn(e) {
  const t = xs();
  return j(() => (t.value, !!e()));
}
function $s(e, t, n = {}) {
  const { window: r = Re, ...s } = n;
  let o;
  const i = Cn(() => r && "MutationObserver" in r), c = () => {
    o && (o.disconnect(), o = void 0);
  }, a = j(() => {
    const f = te(e), d = (Array.isArray(f) ? f : [f]).map(Ct).filter(Es);
    return new Set(d);
  }), h = G(
    () => a.value,
    (f) => {
      c(), i.value && f.size && (o = new MutationObserver(t), f.forEach((d) => o.observe(d, s)));
    },
    { immediate: !0, flush: "post" }
  ), u = () => o == null ? void 0 : o.takeRecords(), l = () => {
    h(), c();
  };
  return Vt(l), {
    isSupported: i,
    stop: l,
    takeRecords: u
  };
}
function Ts(e, t, n) {
  const {
    immediate: r = !0,
    delay: s = 0,
    onError: o = De,
    onSuccess: i = De,
    resetOnExecute: c = !0,
    shallow: a = !0,
    throwError: h
  } = {}, u = a ? ie(t) : U(t), l = U(!1), f = U(!1), d = ie(void 0);
  async function p(_ = 0, ...w) {
    c && (u.value = t), d.value = void 0, l.value = !1, f.value = !0, _ > 0 && await pt(_);
    const k = typeof e == "function" ? e(...w) : e;
    try {
      const v = await k;
      u.value = v, l.value = !0, i(v);
    } catch (v) {
      if (d.value = v, o(v), h)
        throw v;
    } finally {
      f.value = !1;
    }
    return u.value;
  }
  r && p(s);
  const g = {
    state: u,
    isReady: l,
    isLoading: f,
    error: d,
    execute: p
  };
  function y() {
    return new Promise((_, w) => {
      Vs(f).toBe(!1).then(() => _(g)).catch(w);
    });
  }
  return {
    ...g,
    then(_, w) {
      return y().then(_, w);
    }
  };
}
function Is(e, t = {}) {
  const { window: n = Re } = t, r = Cn(() => n && "matchMedia" in n && typeof n.matchMedia == "function");
  let s;
  const o = U(!1), i = (h) => {
    o.value = h.matches;
  }, c = () => {
    s && ("removeEventListener" in s ? s.removeEventListener("change", i) : s.removeListener(i));
  }, a = Nt(() => {
    r.value && (c(), s = n.matchMedia(te(e)), "addEventListener" in s ? s.addEventListener("change", i) : s.addListener(i), o.value = s.matches);
  });
  return Vt(() => {
    a(), c(), s = void 0;
  }), o;
}
const Be = typeof globalThis < "u" ? globalThis : typeof window < "u" ? window : typeof global < "u" ? global : typeof self < "u" ? self : {}, Le = "__vueuse_ssr_handlers__", Ds = /* @__PURE__ */ Ms();
function Ms() {
  return Le in Be || (Be[Le] = Be[Le] || {}), Be[Le];
}
function An(e, t) {
  return Ds[e] || t;
}
function js(e) {
  return Is("(prefers-color-scheme: dark)", e);
}
function Bs(e) {
  return e == null ? "any" : e instanceof Set ? "set" : e instanceof Map ? "map" : e instanceof Date ? "date" : typeof e == "boolean" ? "boolean" : typeof e == "string" ? "string" : typeof e == "object" ? "object" : Number.isNaN(e) ? "any" : "number";
}
const Ls = {
  boolean: {
    read: (e) => e === "true",
    write: (e) => String(e)
  },
  object: {
    read: (e) => JSON.parse(e),
    write: (e) => JSON.stringify(e)
  },
  number: {
    read: (e) => Number.parseFloat(e),
    write: (e) => String(e)
  },
  any: {
    read: (e) => e,
    write: (e) => String(e)
  },
  string: {
    read: (e) => e,
    write: (e) => String(e)
  },
  map: {
    read: (e) => new Map(JSON.parse(e)),
    write: (e) => JSON.stringify(Array.from(e.entries()))
  },
  set: {
    read: (e) => new Set(JSON.parse(e)),
    write: (e) => JSON.stringify(Array.from(e))
  },
  date: {
    read: (e) => new Date(e),
    write: (e) => e.toISOString()
  }
}, Wt = "vueuse-storage";
function gt(e, t, n, r = {}) {
  var s;
  const {
    flush: o = "pre",
    deep: i = !0,
    listenToStorageChanges: c = !0,
    writeDefaults: a = !0,
    mergeDefaults: h = !1,
    shallow: u,
    window: l = Re,
    eventFilter: f,
    onError: d = (P) => {
      console.error(P);
    },
    initOnMounted: p
  } = r, g = (u ? ie : U)(typeof t == "function" ? t() : t);
  if (!n)
    try {
      n = An("getDefaultStorage", () => {
        var P;
        return (P = Re) == null ? void 0 : P.localStorage;
      })();
    } catch (P) {
      d(P);
    }
  if (!n)
    return g;
  const y = te(t), _ = Bs(y), w = (s = r.serializer) != null ? s : Ls[_], { pause: k, resume: v } = Ns(
    g,
    () => A(g.value),
    { flush: o, deep: i, eventFilter: f }
  );
  l && c && Vn(() => {
    n instanceof Storage ? Ft(l, "storage", L) : Ft(l, Wt, Q), p && L();
  }), p || L();
  function R(P, I) {
    if (l) {
      const F = {
        key: e,
        oldValue: P,
        newValue: I,
        storageArea: n
      };
      l.dispatchEvent(n instanceof Storage ? new StorageEvent("storage", F) : new CustomEvent(Wt, {
        detail: F
      }));
    }
  }
  function A(P) {
    try {
      const I = n.getItem(e);
      if (P == null)
        R(I, null), n.removeItem(e);
      else {
        const F = w.write(P);
        I !== F && (n.setItem(e, F), R(I, F));
      }
    } catch (I) {
      d(I);
    }
  }
  function T(P) {
    const I = P ? P.newValue : n.getItem(e);
    if (I == null)
      return a && y != null && n.setItem(e, w.write(y)), y;
    if (!P && h) {
      const F = w.read(I);
      return typeof h == "function" ? h(F, y) : _ === "object" && !Array.isArray(F) ? { ...y, ...F } : F;
    } else return typeof I != "string" ? I : w.read(I);
  }
  function L(P) {
    if (!(P && P.storageArea !== n)) {
      if (P && P.key == null) {
        g.value = y;
        return;
      }
      if (!(P && P.key !== e)) {
        k();
        try {
          (P == null ? void 0 : P.newValue) !== w.write(g.value) && (g.value = T(P));
        } catch (I) {
          d(I);
        } finally {
          P ? Se(v) : v();
        }
      }
    }
  }
  function Q(P) {
    L(P.detail);
  }
  return g;
}
const Fs = "*,*::before,*::after{-webkit-transition:none!important;-moz-transition:none!important;-o-transition:none!important;-ms-transition:none!important;transition:none!important}";
function Ws(e = {}) {
  const {
    selector: t = "html",
    attribute: n = "class",
    initialValue: r = "auto",
    window: s = Re,
    storage: o,
    storageKey: i = "vueuse-color-scheme",
    listenToStorageChanges: c = !0,
    storageRef: a,
    emitAuto: h,
    disableTransition: u = !0
  } = e, l = {
    auto: "",
    light: "light",
    dark: "dark",
    ...e.modes || {}
  }, f = js({ window: s }), d = j(() => f.value ? "dark" : "light"), p = a || (i == null ? Pn(r) : gt(i, r, o, { window: s, listenToStorageChanges: c })), g = j(() => p.value === "auto" ? d.value : p.value), y = An(
    "updateHTMLAttrs",
    (v, R, A) => {
      const T = typeof v == "string" ? s == null ? void 0 : s.document.querySelector(v) : Ct(v);
      if (!T)
        return;
      const L = /* @__PURE__ */ new Set(), Q = /* @__PURE__ */ new Set();
      let P = null;
      if (R === "class") {
        const F = A.split(/\s/g);
        Object.values(l).flatMap((ee) => (ee || "").split(/\s/g)).filter(Boolean).forEach((ee) => {
          F.includes(ee) ? L.add(ee) : Q.add(ee);
        });
      } else
        P = { key: R, value: A };
      if (L.size === 0 && Q.size === 0 && P === null)
        return;
      let I;
      u && (I = s.document.createElement("style"), I.appendChild(document.createTextNode(Fs)), s.document.head.appendChild(I));
      for (const F of L)
        T.classList.add(F);
      for (const F of Q)
        T.classList.remove(F);
      P && T.setAttribute(P.key, P.value), u && (s.getComputedStyle(I).opacity, document.head.removeChild(I));
    }
  );
  function _(v) {
    var R;
    y(t, n, (R = l[v]) != null ? R : v);
  }
  function w(v) {
    e.onChanged ? e.onChanged(v, _) : _(v);
  }
  G(g, w, { flush: "post", immediate: !0 }), Vn(() => w(g.value));
  const k = j({
    get() {
      return h ? p.value : g.value;
    },
    set(v) {
      p.value = v;
    }
  });
  return Object.assign(k, { store: p, system: d, state: g });
}
function Us(e = {}) {
  const {
    valueDark: t = "dark",
    valueLight: n = ""
  } = e, r = Ws({
    ...e,
    onChanged: (i, c) => {
      var a;
      e.onChanged ? (a = e.onChanged) == null || a.call(e, i === "dark", c, i) : c(i);
    },
    modes: {
      dark: t,
      light: n
    }
  }), s = j(() => r.system.value);
  return j({
    get() {
      return r.value === "dark";
    },
    set(i) {
      const c = i ? "dark" : "light";
      s.value === c ? r.value = "auto" : r.value = c;
    }
  });
}
function zs(e = null, t = {}) {
  var n, r, s;
  const {
    document: o = As,
    restoreOnUnmount: i = (l) => l
  } = t, c = (n = o == null ? void 0 : o.title) != null ? n : "", a = Pn((r = e ?? (o == null ? void 0 : o.title)) != null ? r : null), h = e && typeof e == "function";
  function u(l) {
    if (!("titleTemplate" in t))
      return l;
    const f = t.titleTemplate || "%s";
    return typeof f == "function" ? f(l) : te(f).replace(/%s/g, l);
  }
  return G(
    a,
    (l, f) => {
      l !== f && o && (o.title = u(typeof l == "string" ? l : ""));
    },
    { immediate: !0 }
  ), t.observe && !t.titleTemplate && o && !h && $s(
    (s = o.head) == null ? void 0 : s.querySelector("title"),
    () => {
      o && o.title !== a.value && (a.value = u(o.title));
    },
    { childList: !0 }
  ), Ps(() => {
    if (i) {
      const l = i(c, a.value || "");
      l != null && o && (o.title = l);
    }
  }), a;
}
function xn(e) {
  return e.constructor.name === "AsyncFunction";
}
function $n(e, t, n) {
  const [r] = t;
  switch (r) {
    case "bind":
      return e[ne(t, n)];
    case "!":
      return !e;
    case "+":
      return e + ne(t, n);
    case "~+":
      return ne(t, n) + e;
    case "<":
      return e < ne(t, n);
    case "<=":
      return e <= ne(t, n);
    case ">":
      return e > ne(t, n);
    case ">=":
      return e >= ne(t, n);
    case "==":
      return e == ne(t, n);
    case "!=":
      return e != ne(t, n);
    case "len":
      return e.length;
    default:
      throw new Error(`Invalid flag ${r} in array at ${t}`);
  }
}
function ne(e, t) {
  const [n, r, s] = e, o = () => s && s[0] ? t(r[0]) : r[0];
  switch (n) {
    case "bind":
      return o();
    case "+":
      return o();
    case "~+":
      return o();
    case "<":
      return o();
    case "<=":
      return o();
    case ">":
      return o();
    case ">=":
      return o();
    case "==":
      return o();
    case "!=":
      return o();
    default:
      throw new Error(`Invalid flag ${n} in array at ${e}`);
  }
}
function Hs(e, t, n) {
  return In(t).reduce(
    (r, s) => $n(r, s, n),
    e
  );
}
function Tn(e, t, n, r) {
  In(t).reduce((s, o, i) => {
    if (i === t.length - 1)
      s[ne(o, r)] = n;
    else
      return $n(s, o, r);
  }, e);
}
function In(e) {
  return Ks(e) ? e.map((t) => ["bind", [t]]) : e;
}
function Ks(e) {
  return !Array.isArray(e[0]);
}
function Gs(e, t, n) {
  const { paths: r, getBindableValueFn: s } = t, { paths: o, getBindableValueFn: i } = t;
  return r === void 0 || r.length === 0 ? e : ye(() => ({
    get() {
      try {
        return Hs(
          be(e),
          r,
          s
        );
      } catch {
        return;
      }
    },
    set(c) {
      Tn(
        be(e),
        o || r,
        c,
        i
      );
    }
  }));
}
function Ut(e, t) {
  return !ke(e) && JSON.stringify(t) === JSON.stringify(e);
}
function At(e) {
  if (Ot(e)) {
    const t = e;
    return ye(() => ({
      get() {
        return be(t);
      },
      set(n) {
        const r = be(t);
        Ut(r, n) || (t.value = n);
      }
    }));
  }
  return ye((t, n) => ({
    get() {
      return t(), e;
    },
    set(r) {
      Ut(e, r) || (e = r, n());
    }
  }));
}
function qs(e) {
  const { type: t, key: n, value: r } = e.args;
  return t === "local" ? gt(n, r) : gt(n, r, sessionStorage);
}
const Js = "insta-color-scheme";
function Qs(e) {
  return Us({
    storageKey: Js,
    onChanged(n) {
      n ? (document.documentElement.setAttribute("theme-mode", "dark"), document.documentElement.classList.add("insta-dark")) : (document.documentElement.setAttribute("theme-mode", "light"), document.documentElement.classList.remove("insta-dark"));
    }
  });
}
function Ys(e) {
  return zs();
}
const Xs = /* @__PURE__ */ new Map([
  ["storage", qs],
  ["useDark", Qs],
  ["usePageTitle", Ys]
]);
function Zs(e) {
  const { type: t } = e;
  if (!t)
    throw new Error("Invalid ref type");
  const n = Xs.get(t);
  if (!n)
    throw new Error(`Invalid ref type ${t}`);
  return n(e);
}
function eo(e, t) {
  const { deepCompare: n = !1, type: r } = e;
  if (!r) {
    const { value: s } = e;
    return n ? At(s) : U(s);
  }
  return Zs(e);
}
function to(e, t, n) {
  const { bind: r = {}, code: s, const: o = [] } = e, i = Object.values(r).map((u, l) => o[l] === 1 ? u : t.getRef(u));
  if (xn(new Function(s)))
    return Cs(
      async () => {
        const u = Object.fromEntries(
          Object.keys(r).map((l, f) => [l, i[f]])
        );
        return await q(s, u)();
      },
      null,
      { lazy: !0 }
    );
  const c = Object.fromEntries(
    Object.keys(r).map((u, l) => [u, i[l]])
  ), a = q(s, c);
  return j(a);
}
function no(e) {
  const { init: t, deepEqOnInput: n } = e;
  return n === void 0 ? ie(t ?? Ie) : At(t ?? Ie);
}
function ro(e, t, n) {
  const {
    inputs: r = [],
    code: s,
    slient: o,
    data: i,
    asyncInit: c = null,
    deepEqOnInput: a = 0
  } = e, h = o || Array(r.length).fill(0), u = i || Array(r.length).fill(0), l = r.filter((y, _) => h[_] === 0 && u[_] === 0).map((y) => t.getRef(y));
  function f() {
    return r.map((y, _) => {
      if (u[_] === 1)
        return y;
      const w = t.getValue(y);
      return Pt(w) ? w : _n(w);
    });
  }
  const d = q(s), p = a === 0 ? ie(Ie) : At(Ie), g = { immediate: !0, deep: !0 };
  return xn(d) ? (p.value = c, G(
    l,
    async () => {
      f().some(ke) || (p.value = await d(...f()));
    },
    g
  )) : G(
    l,
    () => {
      const y = f();
      y.some(ke) || (p.value = d(...y));
    },
    g
  ), Rt(p);
}
function so(e, t, n) {
  const s = {
    ref: {
      r: n.getBindIndex(D(e, t.id))
    },
    type: Ae.Ref
  };
  return {
    ...t,
    immediate: !0,
    outputs: [s, ...t.outputs || []]
  };
}
function oo(e) {
  const { watchConfigs: t, computedConfigs: n, bindingGetter: r, sid: s } = e;
  return new io(t, n, r, s);
}
class io {
  constructor(t, n, r, s) {
    Y(this, "taskQueue", []);
    Y(this, "id2TaskMap", /* @__PURE__ */ new Map());
    Y(this, "input2TaskIdMap", Sn(() => []));
    this.bindingGetter = r;
    const o = [], i = (c) => {
      var h;
      const a = new ao(c, r);
      return this.id2TaskMap.set(a.id, a), (h = c.inputs) == null || h.forEach((u, l) => {
        var d, p;
        if (((d = c.data) == null ? void 0 : d[l]) === 0 && ((p = c.slient) == null ? void 0 : p[l]) === 0) {
          const g = u.r;
          this.input2TaskIdMap.getOrDefault(g).push(a.id);
        }
      }), a;
    };
    t == null || t.forEach((c) => {
      const a = i(c);
      o.push(a);
    }), n == null || n.forEach((c) => {
      const a = i(
        so(s, c, r)
      );
      o.push(a);
    }), o.forEach((c) => {
      const {
        deep: a = !0,
        once: h,
        flush: u,
        immediate: l = !0
      } = c.watchConfig, f = {
        immediate: l,
        deep: a,
        once: h,
        flush: u
      }, d = this._getWatchTargets(c);
      G(
        d,
        (p) => {
          p.some(ke) || (c.modify = !0, this.taskQueue.push(new co(c)), this._scheduleNextTick());
        },
        f
      );
    });
  }
  _getWatchTargets(t) {
    if (!t.watchConfig.inputs)
      return [];
    const n = t.slientInputs, r = t.constDataInputs;
    return t.watchConfig.inputs.filter(
      (o, i) => !r[i] && !n[i]
    ).map((o) => this.bindingGetter.getRef(o));
  }
  _scheduleNextTick() {
    Se(() => this._runAllTasks());
  }
  _runAllTasks() {
    const t = this.taskQueue.slice();
    this.taskQueue.length = 0, this._setTaskNodeRelations(t), t.forEach((n) => {
      n.run();
    });
  }
  _setTaskNodeRelations(t) {
    t.forEach((n) => {
      const r = this._findNextNodes(n, t);
      n.appendNextNodes(...r), r.forEach((s) => {
        s.appendPrevNodes(n);
      });
    });
  }
  _findNextNodes(t, n) {
    const r = t.watchTask.watchConfig.outputs;
    if (r && r.length <= 0)
      return [];
    const s = this._getCalculatorTasksByOutput(
      t.watchTask.watchConfig.outputs
    );
    return n.filter(
      (o) => s.has(o.watchTask.id) && o.watchTask.id !== t.watchTask.id
    );
  }
  _getCalculatorTasksByOutput(t) {
    const n = /* @__PURE__ */ new Set();
    return t == null || t.forEach((r) => {
      if (!kn(r.ref))
        throw new Error("Non-var output bindings are not supported.");
      const s = r.ref.r;
      (this.input2TaskIdMap.get(s) || []).forEach((i) => n.add(i));
    }), n;
  }
}
class ao {
  constructor(t, n) {
    Y(this, "modify", !0);
    Y(this, "_running", !1);
    Y(this, "id");
    Y(this, "_runningPromise", null);
    Y(this, "_runningPromiseResolve", null);
    Y(this, "_inputInfos");
    this.watchConfig = t, this.bindingGetter = n, this.id = Symbol(t.debug), this._inputInfos = this.createInputInfos();
  }
  createInputInfos() {
    const { inputs: t = [] } = this.watchConfig, n = this.watchConfig.data || Array.from({ length: t.length }).fill(0), r = this.watchConfig.slient || Array.from({ length: t.length }).fill(0);
    return {
      const_data: n,
      slients: r
    };
  }
  get slientInputs() {
    return this._inputInfos.slients;
  }
  get constDataInputs() {
    return this._inputInfos.const_data;
  }
  getServerInputs() {
    const { const_data: t } = this._inputInfos;
    return this.watchConfig.inputs ? this.watchConfig.inputs.map((n, r) => t[r] === 0 ? this.bindingGetter.getValue(n) : n) : [];
  }
  get running() {
    return this._running;
  }
  get runningPromise() {
    return this._runningPromise;
  }
  /**
   * setRunning
   */
  setRunning() {
    this._running = !0, this._runningPromise = new Promise((t) => {
      this._runningPromiseResolve = t;
    });
  }
  /**
   * taskDone
   */
  taskDone() {
    this._running = !1, this._runningPromiseResolve && (this._runningPromiseResolve(), this._runningPromiseResolve = null);
  }
}
class co {
  /**
   *
   */
  constructor(t) {
    Y(this, "prevNodes", []);
    Y(this, "nextNodes", []);
    Y(this, "_runningPrev", !1);
    this.watchTask = t;
  }
  /**
   * appendPrevNodes
   */
  appendPrevNodes(...t) {
    this.prevNodes.push(...t);
  }
  /**
   *
   */
  appendNextNodes(...t) {
    this.nextNodes.push(...t);
  }
  /**
   * hasNextNodes
   */
  hasNextNodes() {
    return this.nextNodes.length > 0;
  }
  /**
   * run
   */
  async run() {
    if (this.prevNodes.length > 0 && !this._runningPrev)
      try {
        this._runningPrev = !0, await Promise.all(this.prevNodes.map((t) => t.run()));
      } finally {
        this._runningPrev = !1;
      }
    if (this.watchTask.running) {
      await this.watchTask.runningPromise;
      return;
    }
    if (this.watchTask.modify) {
      this.watchTask.modify = !1, this.watchTask.setRunning();
      try {
        await lo(this.watchTask);
      } finally {
        this.watchTask.taskDone();
      }
    }
  }
}
async function lo(e) {
  const { bindingGetter: t } = e, { outputs: n, preSetup: r } = e.watchConfig, s = bn({
    config: r,
    bindingGetter: t
  });
  try {
    s.run(), e.taskDone();
    const o = await En().watchSend(e);
    if (!o)
      return;
    qe(o, n, t);
  } finally {
    s.tryReset();
  }
}
function uo(e, t) {
  const {
    on: n,
    code: r,
    immediate: s,
    deep: o,
    once: i,
    flush: c,
    bind: a = {},
    onData: h,
    bindData: u
  } = e, l = h || Array.from({ length: n.length }).fill(0), f = u || Array.from({ length: Object.keys(a).length }).fill(0), d = Ge(
    a,
    (y, _, w) => f[w] === 0 ? t.getRef(y) : y
  ), p = q(r, d), g = n.length === 1 ? zt(l[0] === 1, n[0], t) : n.map(
    (y, _) => zt(l[_] === 1, y, t)
  );
  return G(g, p, { immediate: s, deep: o, once: i, flush: c });
}
function zt(e, t, n) {
  return e ? () => t : n.getRef(t);
}
function fo(e, t) {
  const {
    inputs: n = [],
    outputs: r,
    slient: s,
    data: o,
    code: i,
    immediate: c = !0,
    deep: a,
    once: h,
    flush: u
  } = e, l = s || Array.from({ length: n.length }).fill(0), f = o || Array.from({ length: n.length }).fill(0), d = q(i), p = n.filter((y, _) => l[_] === 0 && f[_] === 0).map((y) => t.getRef(y));
  function g() {
    return n.map((y, _) => {
      if (f[_] === 0) {
        const w = t.getValue(y);
        return Pt(w) ? w : _n(w);
      }
      return y;
    });
  }
  G(
    p,
    () => {
      let y = d(...g());
      if (!r)
        return;
      const w = r.length === 1 ? [y] : y, k = w.map((v) => v === void 0 ? 1 : 0);
      qe(
        {
          values: w,
          types: k
        },
        r,
        t
      );
    },
    { immediate: c, deep: a, once: h, flush: u }
  );
}
function ho() {
  return Dn().__VUE_DEVTOOLS_GLOBAL_HOOK__;
}
function Dn() {
  return typeof navigator < "u" && typeof window < "u" ? window : typeof globalThis < "u" ? globalThis : {};
}
const po = typeof Proxy == "function", mo = "devtools-plugin:setup", go = "plugin:settings:set";
let _e, yt;
function yo() {
  var e;
  return _e !== void 0 || (typeof window < "u" && window.performance ? (_e = !0, yt = window.performance) : typeof globalThis < "u" && (!((e = globalThis.perf_hooks) === null || e === void 0) && e.performance) ? (_e = !0, yt = globalThis.perf_hooks.performance) : _e = !1), _e;
}
function vo() {
  return yo() ? yt.now() : Date.now();
}
class wo {
  constructor(t, n) {
    this.target = null, this.targetQueue = [], this.onQueue = [], this.plugin = t, this.hook = n;
    const r = {};
    if (t.settings)
      for (const i in t.settings) {
        const c = t.settings[i];
        r[i] = c.defaultValue;
      }
    const s = `__vue-devtools-plugin-settings__${t.id}`;
    let o = Object.assign({}, r);
    try {
      const i = localStorage.getItem(s), c = JSON.parse(i);
      Object.assign(o, c);
    } catch {
    }
    this.fallbacks = {
      getSettings() {
        return o;
      },
      setSettings(i) {
        try {
          localStorage.setItem(s, JSON.stringify(i));
        } catch {
        }
        o = i;
      },
      now() {
        return vo();
      }
    }, n && n.on(go, (i, c) => {
      i === this.plugin.id && this.fallbacks.setSettings(c);
    }), this.proxiedOn = new Proxy({}, {
      get: (i, c) => this.target ? this.target.on[c] : (...a) => {
        this.onQueue.push({
          method: c,
          args: a
        });
      }
    }), this.proxiedTarget = new Proxy({}, {
      get: (i, c) => this.target ? this.target[c] : c === "on" ? this.proxiedOn : Object.keys(this.fallbacks).includes(c) ? (...a) => (this.targetQueue.push({
        method: c,
        args: a,
        resolve: () => {
        }
      }), this.fallbacks[c](...a)) : (...a) => new Promise((h) => {
        this.targetQueue.push({
          method: c,
          args: a,
          resolve: h
        });
      })
    });
  }
  async setRealTarget(t) {
    this.target = t;
    for (const n of this.onQueue)
      this.target.on[n.method](...n.args);
    for (const n of this.targetQueue)
      n.resolve(await this.target[n.method](...n.args));
  }
}
function _o(e, t) {
  const n = e, r = Dn(), s = ho(), o = po && n.enableEarlyProxy;
  if (s && (r.__VUE_DEVTOOLS_PLUGIN_API_AVAILABLE__ || !o))
    s.emit(mo, e, t);
  else {
    const i = o ? new wo(n, s) : null;
    (r.__VUE_DEVTOOLS_PLUGINS__ = r.__VUE_DEVTOOLS_PLUGINS__ || []).push({
      pluginDescriptor: n,
      setupFn: t,
      proxy: i
    }), i && t(i.proxiedTarget);
  }
}
var O = {};
const oe = typeof document < "u";
function Mn(e) {
  return typeof e == "object" || "displayName" in e || "props" in e || "__vccOpts" in e;
}
function Eo(e) {
  return e.__esModule || e[Symbol.toStringTag] === "Module" || // support CF with dynamic imports that do not
  // add the Module string tag
  e.default && Mn(e.default);
}
const x = Object.assign;
function it(e, t) {
  const n = {};
  for (const r in t) {
    const s = t[r];
    n[r] = X(s) ? s.map(e) : e(s);
  }
  return n;
}
const xe = () => {
}, X = Array.isArray;
function N(e) {
  const t = Array.from(arguments).slice(1);
  console.warn.apply(console, ["[Vue Router warn]: " + e].concat(t));
}
const jn = /#/g, bo = /&/g, So = /\//g, ko = /=/g, Ro = /\?/g, Bn = /\+/g, Oo = /%5B/g, No = /%5D/g, Ln = /%5E/g, Po = /%60/g, Fn = /%7B/g, Vo = /%7C/g, Wn = /%7D/g, Co = /%20/g;
function xt(e) {
  return encodeURI("" + e).replace(Vo, "|").replace(Oo, "[").replace(No, "]");
}
function Ao(e) {
  return xt(e).replace(Fn, "{").replace(Wn, "}").replace(Ln, "^");
}
function vt(e) {
  return xt(e).replace(Bn, "%2B").replace(Co, "+").replace(jn, "%23").replace(bo, "%26").replace(Po, "`").replace(Fn, "{").replace(Wn, "}").replace(Ln, "^");
}
function xo(e) {
  return vt(e).replace(ko, "%3D");
}
function $o(e) {
  return xt(e).replace(jn, "%23").replace(Ro, "%3F");
}
function To(e) {
  return e == null ? "" : $o(e).replace(So, "%2F");
}
function Oe(e) {
  try {
    return decodeURIComponent("" + e);
  } catch {
    O.NODE_ENV !== "production" && N(`Error decoding "${e}". Using original value`);
  }
  return "" + e;
}
const Io = /\/$/, Do = (e) => e.replace(Io, "");
function at(e, t, n = "/") {
  let r, s = {}, o = "", i = "";
  const c = t.indexOf("#");
  let a = t.indexOf("?");
  return c < a && c >= 0 && (a = -1), a > -1 && (r = t.slice(0, a), o = t.slice(a + 1, c > -1 ? c : t.length), s = e(o)), c > -1 && (r = r || t.slice(0, c), i = t.slice(c, t.length)), r = Bo(r ?? t, n), {
    fullPath: r + (o && "?") + o + i,
    path: r,
    query: s,
    hash: Oe(i)
  };
}
function Mo(e, t) {
  const n = t.query ? e(t.query) : "";
  return t.path + (n && "?") + n + (t.hash || "");
}
function Ht(e, t) {
  return !t || !e.toLowerCase().startsWith(t.toLowerCase()) ? e : e.slice(t.length) || "/";
}
function Kt(e, t, n) {
  const r = t.matched.length - 1, s = n.matched.length - 1;
  return r > -1 && r === s && he(t.matched[r], n.matched[s]) && Un(t.params, n.params) && e(t.query) === e(n.query) && t.hash === n.hash;
}
function he(e, t) {
  return (e.aliasOf || e) === (t.aliasOf || t);
}
function Un(e, t) {
  if (Object.keys(e).length !== Object.keys(t).length)
    return !1;
  for (const n in e)
    if (!jo(e[n], t[n]))
      return !1;
  return !0;
}
function jo(e, t) {
  return X(e) ? Gt(e, t) : X(t) ? Gt(t, e) : e === t;
}
function Gt(e, t) {
  return X(t) ? e.length === t.length && e.every((n, r) => n === t[r]) : e.length === 1 && e[0] === t;
}
function Bo(e, t) {
  if (e.startsWith("/"))
    return e;
  if (O.NODE_ENV !== "production" && !t.startsWith("/"))
    return N(`Cannot resolve a relative location without an absolute path. Trying to resolve "${e}" from "${t}". It should look like "/${t}".`), e;
  if (!e)
    return t;
  const n = t.split("/"), r = e.split("/"), s = r[r.length - 1];
  (s === ".." || s === ".") && r.push("");
  let o = n.length - 1, i, c;
  for (i = 0; i < r.length; i++)
    if (c = r[i], c !== ".")
      if (c === "..")
        o > 1 && o--;
      else
        break;
  return n.slice(0, o).join("/") + "/" + r.slice(i).join("/");
}
const ce = {
  path: "/",
  // TODO: could we use a symbol in the future?
  name: void 0,
  params: {},
  query: {},
  hash: "",
  fullPath: "/",
  matched: [],
  meta: {},
  redirectedFrom: void 0
};
var Ne;
(function(e) {
  e.pop = "pop", e.push = "push";
})(Ne || (Ne = {}));
var ge;
(function(e) {
  e.back = "back", e.forward = "forward", e.unknown = "";
})(ge || (ge = {}));
const ct = "";
function zn(e) {
  if (!e)
    if (oe) {
      const t = document.querySelector("base");
      e = t && t.getAttribute("href") || "/", e = e.replace(/^\w+:\/\/[^\/]+/, "");
    } else
      e = "/";
  return e[0] !== "/" && e[0] !== "#" && (e = "/" + e), Do(e);
}
const Lo = /^[^#]+#/;
function Hn(e, t) {
  return e.replace(Lo, "#") + t;
}
function Fo(e, t) {
  const n = document.documentElement.getBoundingClientRect(), r = e.getBoundingClientRect();
  return {
    behavior: t.behavior,
    left: r.left - n.left - (t.left || 0),
    top: r.top - n.top - (t.top || 0)
  };
}
const Je = () => ({
  left: window.scrollX,
  top: window.scrollY
});
function Wo(e) {
  let t;
  if ("el" in e) {
    const n = e.el, r = typeof n == "string" && n.startsWith("#");
    if (O.NODE_ENV !== "production" && typeof e.el == "string" && (!r || !document.getElementById(e.el.slice(1))))
      try {
        const o = document.querySelector(e.el);
        if (r && o) {
          N(`The selector "${e.el}" should be passed as "el: document.querySelector('${e.el}')" because it starts with "#".`);
          return;
        }
      } catch {
        N(`The selector "${e.el}" is invalid. If you are using an id selector, make sure to escape it. You can find more information about escaping characters in selectors at https://mathiasbynens.be/notes/css-escapes or use CSS.escape (https://developer.mozilla.org/en-US/docs/Web/API/CSS/escape).`);
        return;
      }
    const s = typeof n == "string" ? r ? document.getElementById(n.slice(1)) : document.querySelector(n) : n;
    if (!s) {
      O.NODE_ENV !== "production" && N(`Couldn't find element using selector "${e.el}" returned by scrollBehavior.`);
      return;
    }
    t = Fo(s, e);
  } else
    t = e;
  "scrollBehavior" in document.documentElement.style ? window.scrollTo(t) : window.scrollTo(t.left != null ? t.left : window.scrollX, t.top != null ? t.top : window.scrollY);
}
function qt(e, t) {
  return (history.state ? history.state.position - t : -1) + e;
}
const wt = /* @__PURE__ */ new Map();
function Uo(e, t) {
  wt.set(e, t);
}
function zo(e) {
  const t = wt.get(e);
  return wt.delete(e), t;
}
let Ho = () => location.protocol + "//" + location.host;
function Kn(e, t) {
  const { pathname: n, search: r, hash: s } = t, o = e.indexOf("#");
  if (o > -1) {
    let c = s.includes(e.slice(o)) ? e.slice(o).length : 1, a = s.slice(c);
    return a[0] !== "/" && (a = "/" + a), Ht(a, "");
  }
  return Ht(n, e) + r + s;
}
function Ko(e, t, n, r) {
  let s = [], o = [], i = null;
  const c = ({ state: f }) => {
    const d = Kn(e, location), p = n.value, g = t.value;
    let y = 0;
    if (f) {
      if (n.value = d, t.value = f, i && i === p) {
        i = null;
        return;
      }
      y = g ? f.position - g.position : 0;
    } else
      r(d);
    s.forEach((_) => {
      _(n.value, p, {
        delta: y,
        type: Ne.pop,
        direction: y ? y > 0 ? ge.forward : ge.back : ge.unknown
      });
    });
  };
  function a() {
    i = n.value;
  }
  function h(f) {
    s.push(f);
    const d = () => {
      const p = s.indexOf(f);
      p > -1 && s.splice(p, 1);
    };
    return o.push(d), d;
  }
  function u() {
    const { history: f } = window;
    f.state && f.replaceState(x({}, f.state, { scroll: Je() }), "");
  }
  function l() {
    for (const f of o)
      f();
    o = [], window.removeEventListener("popstate", c), window.removeEventListener("beforeunload", u);
  }
  return window.addEventListener("popstate", c), window.addEventListener("beforeunload", u, {
    passive: !0
  }), {
    pauseListeners: a,
    listen: h,
    destroy: l
  };
}
function Jt(e, t, n, r = !1, s = !1) {
  return {
    back: e,
    current: t,
    forward: n,
    replaced: r,
    position: window.history.length,
    scroll: s ? Je() : null
  };
}
function Go(e) {
  const { history: t, location: n } = window, r = {
    value: Kn(e, n)
  }, s = { value: t.state };
  s.value || o(r.value, {
    back: null,
    current: r.value,
    forward: null,
    // the length is off by one, we need to decrease it
    position: t.length - 1,
    replaced: !0,
    // don't add a scroll as the user may have an anchor, and we want
    // scrollBehavior to be triggered without a saved position
    scroll: null
  }, !0);
  function o(a, h, u) {
    const l = e.indexOf("#"), f = l > -1 ? (n.host && document.querySelector("base") ? e : e.slice(l)) + a : Ho() + e + a;
    try {
      t[u ? "replaceState" : "pushState"](h, "", f), s.value = h;
    } catch (d) {
      O.NODE_ENV !== "production" ? N("Error with push/replace State", d) : console.error(d), n[u ? "replace" : "assign"](f);
    }
  }
  function i(a, h) {
    const u = x({}, t.state, Jt(
      s.value.back,
      // keep back and forward entries but override current position
      a,
      s.value.forward,
      !0
    ), h, { position: s.value.position });
    o(a, u, !0), r.value = a;
  }
  function c(a, h) {
    const u = x(
      {},
      // use current history state to gracefully handle a wrong call to
      // history.replaceState
      // https://github.com/vuejs/router/issues/366
      s.value,
      t.state,
      {
        forward: a,
        scroll: Je()
      }
    );
    O.NODE_ENV !== "production" && !t.state && N(`history.state seems to have been manually replaced without preserving the necessary values. Make sure to preserve existing history state if you are manually calling history.replaceState:

history.replaceState(history.state, '', url)

You can find more information at https://router.vuejs.org/guide/migration/#Usage-of-history-state`), o(u.current, u, !0);
    const l = x({}, Jt(r.value, a, null), { position: u.position + 1 }, h);
    o(a, l, !1), r.value = a;
  }
  return {
    location: r,
    state: s,
    push: c,
    replace: i
  };
}
function Gn(e) {
  e = zn(e);
  const t = Go(e), n = Ko(e, t.state, t.location, t.replace);
  function r(o, i = !0) {
    i || n.pauseListeners(), history.go(o);
  }
  const s = x({
    // it's overridden right after
    location: "",
    base: e,
    go: r,
    createHref: Hn.bind(null, e)
  }, t, n);
  return Object.defineProperty(s, "location", {
    enumerable: !0,
    get: () => t.location.value
  }), Object.defineProperty(s, "state", {
    enumerable: !0,
    get: () => t.state.value
  }), s;
}
function qo(e = "") {
  let t = [], n = [ct], r = 0;
  e = zn(e);
  function s(c) {
    r++, r !== n.length && n.splice(r), n.push(c);
  }
  function o(c, a, { direction: h, delta: u }) {
    const l = {
      direction: h,
      delta: u,
      type: Ne.pop
    };
    for (const f of t)
      f(c, a, l);
  }
  const i = {
    // rewritten by Object.defineProperty
    location: ct,
    // TODO: should be kept in queue
    state: {},
    base: e,
    createHref: Hn.bind(null, e),
    replace(c) {
      n.splice(r--, 1), s(c);
    },
    push(c, a) {
      s(c);
    },
    listen(c) {
      return t.push(c), () => {
        const a = t.indexOf(c);
        a > -1 && t.splice(a, 1);
      };
    },
    destroy() {
      t = [], n = [ct], r = 0;
    },
    go(c, a = !0) {
      const h = this.location, u = (
        // we are considering delta === 0 going forward, but in abstract mode
        // using 0 for the delta doesn't make sense like it does in html5 where
        // it reloads the page
        c < 0 ? ge.back : ge.forward
      );
      r = Math.max(0, Math.min(r + c, n.length - 1)), a && o(this.location, h, {
        direction: u,
        delta: c
      });
    }
  };
  return Object.defineProperty(i, "location", {
    enumerable: !0,
    get: () => n[r]
  }), i;
}
function Jo(e) {
  return e = location.host ? e || location.pathname + location.search : "", e.includes("#") || (e += "#"), O.NODE_ENV !== "production" && !e.endsWith("#/") && !e.endsWith("#") && N(`A hash base must end with a "#":
"${e}" should be "${e.replace(/#.*$/, "#")}".`), Gn(e);
}
function ze(e) {
  return typeof e == "string" || e && typeof e == "object";
}
function qn(e) {
  return typeof e == "string" || typeof e == "symbol";
}
const _t = Symbol(O.NODE_ENV !== "production" ? "navigation failure" : "");
var Qt;
(function(e) {
  e[e.aborted = 4] = "aborted", e[e.cancelled = 8] = "cancelled", e[e.duplicated = 16] = "duplicated";
})(Qt || (Qt = {}));
const Qo = {
  1({ location: e, currentLocation: t }) {
    return `No match for
 ${JSON.stringify(e)}${t ? `
while being at
` + JSON.stringify(t) : ""}`;
  },
  2({ from: e, to: t }) {
    return `Redirected from "${e.fullPath}" to "${Xo(t)}" via a navigation guard.`;
  },
  4({ from: e, to: t }) {
    return `Navigation aborted from "${e.fullPath}" to "${t.fullPath}" via a navigation guard.`;
  },
  8({ from: e, to: t }) {
    return `Navigation cancelled from "${e.fullPath}" to "${t.fullPath}" with a new navigation.`;
  },
  16({ from: e, to: t }) {
    return `Avoided redundant navigation to current location: "${e.fullPath}".`;
  }
};
function Pe(e, t) {
  return O.NODE_ENV !== "production" ? x(new Error(Qo[e](t)), {
    type: e,
    [_t]: !0
  }, t) : x(new Error(), {
    type: e,
    [_t]: !0
  }, t);
}
function se(e, t) {
  return e instanceof Error && _t in e && (t == null || !!(e.type & t));
}
const Yo = ["params", "query", "hash"];
function Xo(e) {
  if (typeof e == "string")
    return e;
  if (e.path != null)
    return e.path;
  const t = {};
  for (const n of Yo)
    n in e && (t[n] = e[n]);
  return JSON.stringify(t, null, 2);
}
const Yt = "[^/]+?", Zo = {
  sensitive: !1,
  strict: !1,
  start: !0,
  end: !0
}, ei = /[.+*?^${}()[\]/\\]/g;
function ti(e, t) {
  const n = x({}, Zo, t), r = [];
  let s = n.start ? "^" : "";
  const o = [];
  for (const h of e) {
    const u = h.length ? [] : [
      90
      /* PathScore.Root */
    ];
    n.strict && !h.length && (s += "/");
    for (let l = 0; l < h.length; l++) {
      const f = h[l];
      let d = 40 + (n.sensitive ? 0.25 : 0);
      if (f.type === 0)
        l || (s += "/"), s += f.value.replace(ei, "\\$&"), d += 40;
      else if (f.type === 1) {
        const { value: p, repeatable: g, optional: y, regexp: _ } = f;
        o.push({
          name: p,
          repeatable: g,
          optional: y
        });
        const w = _ || Yt;
        if (w !== Yt) {
          d += 10;
          try {
            new RegExp(`(${w})`);
          } catch (v) {
            throw new Error(`Invalid custom RegExp for param "${p}" (${w}): ` + v.message);
          }
        }
        let k = g ? `((?:${w})(?:/(?:${w}))*)` : `(${w})`;
        l || (k = // avoid an optional / if there are more segments e.g. /:p?-static
        // or /:p?-:p2
        y && h.length < 2 ? `(?:/${k})` : "/" + k), y && (k += "?"), s += k, d += 20, y && (d += -8), g && (d += -20), w === ".*" && (d += -50);
      }
      u.push(d);
    }
    r.push(u);
  }
  if (n.strict && n.end) {
    const h = r.length - 1;
    r[h][r[h].length - 1] += 0.7000000000000001;
  }
  n.strict || (s += "/?"), n.end ? s += "$" : n.strict && !s.endsWith("/") && (s += "(?:/|$)");
  const i = new RegExp(s, n.sensitive ? "" : "i");
  function c(h) {
    const u = h.match(i), l = {};
    if (!u)
      return null;
    for (let f = 1; f < u.length; f++) {
      const d = u[f] || "", p = o[f - 1];
      l[p.name] = d && p.repeatable ? d.split("/") : d;
    }
    return l;
  }
  function a(h) {
    let u = "", l = !1;
    for (const f of e) {
      (!l || !u.endsWith("/")) && (u += "/"), l = !1;
      for (const d of f)
        if (d.type === 0)
          u += d.value;
        else if (d.type === 1) {
          const { value: p, repeatable: g, optional: y } = d, _ = p in h ? h[p] : "";
          if (X(_) && !g)
            throw new Error(`Provided param "${p}" is an array but it is not repeatable (* or + modifiers)`);
          const w = X(_) ? _.join("/") : _;
          if (!w)
            if (y)
              f.length < 2 && (u.endsWith("/") ? u = u.slice(0, -1) : l = !0);
            else
              throw new Error(`Missing required param "${p}"`);
          u += w;
        }
    }
    return u || "/";
  }
  return {
    re: i,
    score: r,
    keys: o,
    parse: c,
    stringify: a
  };
}
function ni(e, t) {
  let n = 0;
  for (; n < e.length && n < t.length; ) {
    const r = t[n] - e[n];
    if (r)
      return r;
    n++;
  }
  return e.length < t.length ? e.length === 1 && e[0] === 80 ? -1 : 1 : e.length > t.length ? t.length === 1 && t[0] === 80 ? 1 : -1 : 0;
}
function Jn(e, t) {
  let n = 0;
  const r = e.score, s = t.score;
  for (; n < r.length && n < s.length; ) {
    const o = ni(r[n], s[n]);
    if (o)
      return o;
    n++;
  }
  if (Math.abs(s.length - r.length) === 1) {
    if (Xt(r))
      return 1;
    if (Xt(s))
      return -1;
  }
  return s.length - r.length;
}
function Xt(e) {
  const t = e[e.length - 1];
  return e.length > 0 && t[t.length - 1] < 0;
}
const ri = {
  type: 0,
  value: ""
}, si = /[a-zA-Z0-9_]/;
function oi(e) {
  if (!e)
    return [[]];
  if (e === "/")
    return [[ri]];
  if (!e.startsWith("/"))
    throw new Error(O.NODE_ENV !== "production" ? `Route paths should start with a "/": "${e}" should be "/${e}".` : `Invalid path "${e}"`);
  function t(d) {
    throw new Error(`ERR (${n})/"${h}": ${d}`);
  }
  let n = 0, r = n;
  const s = [];
  let o;
  function i() {
    o && s.push(o), o = [];
  }
  let c = 0, a, h = "", u = "";
  function l() {
    h && (n === 0 ? o.push({
      type: 0,
      value: h
    }) : n === 1 || n === 2 || n === 3 ? (o.length > 1 && (a === "*" || a === "+") && t(`A repeatable param (${h}) must be alone in its segment. eg: '/:ids+.`), o.push({
      type: 1,
      value: h,
      regexp: u,
      repeatable: a === "*" || a === "+",
      optional: a === "*" || a === "?"
    })) : t("Invalid state to consume buffer"), h = "");
  }
  function f() {
    h += a;
  }
  for (; c < e.length; ) {
    if (a = e[c++], a === "\\" && n !== 2) {
      r = n, n = 4;
      continue;
    }
    switch (n) {
      case 0:
        a === "/" ? (h && l(), i()) : a === ":" ? (l(), n = 1) : f();
        break;
      case 4:
        f(), n = r;
        break;
      case 1:
        a === "(" ? n = 2 : si.test(a) ? f() : (l(), n = 0, a !== "*" && a !== "?" && a !== "+" && c--);
        break;
      case 2:
        a === ")" ? u[u.length - 1] == "\\" ? u = u.slice(0, -1) + a : n = 3 : u += a;
        break;
      case 3:
        l(), n = 0, a !== "*" && a !== "?" && a !== "+" && c--, u = "";
        break;
      default:
        t("Unknown state");
        break;
    }
  }
  return n === 2 && t(`Unfinished custom RegExp for param "${h}"`), l(), i(), s;
}
function ii(e, t, n) {
  const r = ti(oi(e.path), n);
  if (O.NODE_ENV !== "production") {
    const o = /* @__PURE__ */ new Set();
    for (const i of r.keys)
      o.has(i.name) && N(`Found duplicated params with name "${i.name}" for path "${e.path}". Only the last one will be available on "$route.params".`), o.add(i.name);
  }
  const s = x(r, {
    record: e,
    parent: t,
    // these needs to be populated by the parent
    children: [],
    alias: []
  });
  return t && !s.record.aliasOf == !t.record.aliasOf && t.children.push(s), s;
}
function ai(e, t) {
  const n = [], r = /* @__PURE__ */ new Map();
  t = nn({ strict: !1, end: !0, sensitive: !1 }, t);
  function s(l) {
    return r.get(l);
  }
  function o(l, f, d) {
    const p = !d, g = en(l);
    O.NODE_ENV !== "production" && fi(g, f), g.aliasOf = d && d.record;
    const y = nn(t, l), _ = [g];
    if ("alias" in l) {
      const v = typeof l.alias == "string" ? [l.alias] : l.alias;
      for (const R of v)
        _.push(
          // we need to normalize again to ensure the `mods` property
          // being non enumerable
          en(x({}, g, {
            // this allows us to hold a copy of the `components` option
            // so that async components cache is hold on the original record
            components: d ? d.record.components : g.components,
            path: R,
            // we might be the child of an alias
            aliasOf: d ? d.record : g
            // the aliases are always of the same kind as the original since they
            // are defined on the same record
          }))
        );
    }
    let w, k;
    for (const v of _) {
      const { path: R } = v;
      if (f && R[0] !== "/") {
        const A = f.record.path, T = A[A.length - 1] === "/" ? "" : "/";
        v.path = f.record.path + (R && T + R);
      }
      if (O.NODE_ENV !== "production" && v.path === "*")
        throw new Error(`Catch all routes ("*") must now be defined using a param with a custom regexp.
See more at https://router.vuejs.org/guide/migration/#Removed-star-or-catch-all-routes.`);
      if (w = ii(v, f, y), O.NODE_ENV !== "production" && f && R[0] === "/" && hi(w, f), d ? (d.alias.push(w), O.NODE_ENV !== "production" && ui(d, w)) : (k = k || w, k !== w && k.alias.push(w), p && l.name && !tn(w) && (O.NODE_ENV !== "production" && di(l, f), i(l.name))), Qn(w) && a(w), g.children) {
        const A = g.children;
        for (let T = 0; T < A.length; T++)
          o(A[T], w, d && d.children[T]);
      }
      d = d || w;
    }
    return k ? () => {
      i(k);
    } : xe;
  }
  function i(l) {
    if (qn(l)) {
      const f = r.get(l);
      f && (r.delete(l), n.splice(n.indexOf(f), 1), f.children.forEach(i), f.alias.forEach(i));
    } else {
      const f = n.indexOf(l);
      f > -1 && (n.splice(f, 1), l.record.name && r.delete(l.record.name), l.children.forEach(i), l.alias.forEach(i));
    }
  }
  function c() {
    return n;
  }
  function a(l) {
    const f = pi(l, n);
    n.splice(f, 0, l), l.record.name && !tn(l) && r.set(l.record.name, l);
  }
  function h(l, f) {
    let d, p = {}, g, y;
    if ("name" in l && l.name) {
      if (d = r.get(l.name), !d)
        throw Pe(1, {
          location: l
        });
      if (O.NODE_ENV !== "production") {
        const k = Object.keys(l.params || {}).filter((v) => !d.keys.find((R) => R.name === v));
        k.length && N(`Discarded invalid param(s) "${k.join('", "')}" when navigating. See https://github.com/vuejs/router/blob/main/packages/router/CHANGELOG.md#414-2022-08-22 for more details.`);
      }
      y = d.record.name, p = x(
        // paramsFromLocation is a new object
        Zt(
          f.params,
          // only keep params that exist in the resolved location
          // only keep optional params coming from a parent record
          d.keys.filter((k) => !k.optional).concat(d.parent ? d.parent.keys.filter((k) => k.optional) : []).map((k) => k.name)
        ),
        // discard any existing params in the current location that do not exist here
        // #1497 this ensures better active/exact matching
        l.params && Zt(l.params, d.keys.map((k) => k.name))
      ), g = d.stringify(p);
    } else if (l.path != null)
      g = l.path, O.NODE_ENV !== "production" && !g.startsWith("/") && N(`The Matcher cannot resolve relative paths but received "${g}". Unless you directly called \`matcher.resolve("${g}")\`, this is probably a bug in vue-router. Please open an issue at https://github.com/vuejs/router/issues/new/choose.`), d = n.find((k) => k.re.test(g)), d && (p = d.parse(g), y = d.record.name);
    else {
      if (d = f.name ? r.get(f.name) : n.find((k) => k.re.test(f.path)), !d)
        throw Pe(1, {
          location: l,
          currentLocation: f
        });
      y = d.record.name, p = x({}, f.params, l.params), g = d.stringify(p);
    }
    const _ = [];
    let w = d;
    for (; w; )
      _.unshift(w.record), w = w.parent;
    return {
      name: y,
      path: g,
      params: p,
      matched: _,
      meta: li(_)
    };
  }
  e.forEach((l) => o(l));
  function u() {
    n.length = 0, r.clear();
  }
  return {
    addRoute: o,
    resolve: h,
    removeRoute: i,
    clearRoutes: u,
    getRoutes: c,
    getRecordMatcher: s
  };
}
function Zt(e, t) {
  const n = {};
  for (const r of t)
    r in e && (n[r] = e[r]);
  return n;
}
function en(e) {
  const t = {
    path: e.path,
    redirect: e.redirect,
    name: e.name,
    meta: e.meta || {},
    aliasOf: e.aliasOf,
    beforeEnter: e.beforeEnter,
    props: ci(e),
    children: e.children || [],
    instances: {},
    leaveGuards: /* @__PURE__ */ new Set(),
    updateGuards: /* @__PURE__ */ new Set(),
    enterCallbacks: {},
    // must be declared afterwards
    // mods: {},
    components: "components" in e ? e.components || null : e.component && { default: e.component }
  };
  return Object.defineProperty(t, "mods", {
    value: {}
  }), t;
}
function ci(e) {
  const t = {}, n = e.props || !1;
  if ("component" in e)
    t.default = n;
  else
    for (const r in e.components)
      t[r] = typeof n == "object" ? n[r] : n;
  return t;
}
function tn(e) {
  for (; e; ) {
    if (e.record.aliasOf)
      return !0;
    e = e.parent;
  }
  return !1;
}
function li(e) {
  return e.reduce((t, n) => x(t, n.meta), {});
}
function nn(e, t) {
  const n = {};
  for (const r in e)
    n[r] = r in t ? t[r] : e[r];
  return n;
}
function Et(e, t) {
  return e.name === t.name && e.optional === t.optional && e.repeatable === t.repeatable;
}
function ui(e, t) {
  for (const n of e.keys)
    if (!n.optional && !t.keys.find(Et.bind(null, n)))
      return N(`Alias "${t.record.path}" and the original record: "${e.record.path}" must have the exact same param named "${n.name}"`);
  for (const n of t.keys)
    if (!n.optional && !e.keys.find(Et.bind(null, n)))
      return N(`Alias "${t.record.path}" and the original record: "${e.record.path}" must have the exact same param named "${n.name}"`);
}
function fi(e, t) {
  t && t.record.name && !e.name && !e.path && N(`The route named "${String(t.record.name)}" has a child without a name and an empty path. Using that name won't render the empty path child so you probably want to move the name to the child instead. If this is intentional, add a name to the child route to remove the warning.`);
}
function di(e, t) {
  for (let n = t; n; n = n.parent)
    if (n.record.name === e.name)
      throw new Error(`A route named "${String(e.name)}" has been added as a ${t === n ? "child" : "descendant"} of a route with the same name. Route names must be unique and a nested route cannot use the same name as an ancestor.`);
}
function hi(e, t) {
  for (const n of t.keys)
    if (!e.keys.find(Et.bind(null, n)))
      return N(`Absolute path "${e.record.path}" must have the exact same param named "${n.name}" as its parent "${t.record.path}".`);
}
function pi(e, t) {
  let n = 0, r = t.length;
  for (; n !== r; ) {
    const o = n + r >> 1;
    Jn(e, t[o]) < 0 ? r = o : n = o + 1;
  }
  const s = mi(e);
  return s && (r = t.lastIndexOf(s, r - 1), O.NODE_ENV !== "production" && r < 0 && N(`Finding ancestor route "${s.record.path}" failed for "${e.record.path}"`)), r;
}
function mi(e) {
  let t = e;
  for (; t = t.parent; )
    if (Qn(t) && Jn(e, t) === 0)
      return t;
}
function Qn({ record: e }) {
  return !!(e.name || e.components && Object.keys(e.components).length || e.redirect);
}
function gi(e) {
  const t = {};
  if (e === "" || e === "?")
    return t;
  const r = (e[0] === "?" ? e.slice(1) : e).split("&");
  for (let s = 0; s < r.length; ++s) {
    const o = r[s].replace(Bn, " "), i = o.indexOf("="), c = Oe(i < 0 ? o : o.slice(0, i)), a = i < 0 ? null : Oe(o.slice(i + 1));
    if (c in t) {
      let h = t[c];
      X(h) || (h = t[c] = [h]), h.push(a);
    } else
      t[c] = a;
  }
  return t;
}
function rn(e) {
  let t = "";
  for (let n in e) {
    const r = e[n];
    if (n = xo(n), r == null) {
      r !== void 0 && (t += (t.length ? "&" : "") + n);
      continue;
    }
    (X(r) ? r.map((o) => o && vt(o)) : [r && vt(r)]).forEach((o) => {
      o !== void 0 && (t += (t.length ? "&" : "") + n, o != null && (t += "=" + o));
    });
  }
  return t;
}
function yi(e) {
  const t = {};
  for (const n in e) {
    const r = e[n];
    r !== void 0 && (t[n] = X(r) ? r.map((s) => s == null ? null : "" + s) : r == null ? r : "" + r);
  }
  return t;
}
const vi = Symbol(O.NODE_ENV !== "production" ? "router view location matched" : ""), sn = Symbol(O.NODE_ENV !== "production" ? "router view depth" : ""), Qe = Symbol(O.NODE_ENV !== "production" ? "router" : ""), $t = Symbol(O.NODE_ENV !== "production" ? "route location" : ""), bt = Symbol(O.NODE_ENV !== "production" ? "router view location" : "");
function Ve() {
  let e = [];
  function t(r) {
    return e.push(r), () => {
      const s = e.indexOf(r);
      s > -1 && e.splice(s, 1);
    };
  }
  function n() {
    e = [];
  }
  return {
    add: t,
    list: () => e.slice(),
    reset: n
  };
}
function le(e, t, n, r, s, o = (i) => i()) {
  const i = r && // name is defined if record is because of the function overload
  (r.enterCallbacks[s] = r.enterCallbacks[s] || []);
  return () => new Promise((c, a) => {
    const h = (f) => {
      f === !1 ? a(Pe(4, {
        from: n,
        to: t
      })) : f instanceof Error ? a(f) : ze(f) ? a(Pe(2, {
        from: t,
        to: f
      })) : (i && // since enterCallbackArray is truthy, both record and name also are
      r.enterCallbacks[s] === i && typeof f == "function" && i.push(f), c());
    }, u = o(() => e.call(r && r.instances[s], t, n, O.NODE_ENV !== "production" ? wi(h, t, n) : h));
    let l = Promise.resolve(u);
    if (e.length < 3 && (l = l.then(h)), O.NODE_ENV !== "production" && e.length > 2) {
      const f = `The "next" callback was never called inside of ${e.name ? '"' + e.name + '"' : ""}:
${e.toString()}
. If you are returning a value instead of calling "next", make sure to remove the "next" parameter from your function.`;
      if (typeof u == "object" && "then" in u)
        l = l.then((d) => h._called ? d : (N(f), Promise.reject(new Error("Invalid navigation guard"))));
      else if (u !== void 0 && !h._called) {
        N(f), a(new Error("Invalid navigation guard"));
        return;
      }
    }
    l.catch((f) => a(f));
  });
}
function wi(e, t, n) {
  let r = 0;
  return function() {
    r++ === 1 && N(`The "next" callback was called more than once in one navigation guard when going from "${n.fullPath}" to "${t.fullPath}". It should be called exactly one time in each navigation guard. This will fail in production.`), e._called = !0, r === 1 && e.apply(null, arguments);
  };
}
function lt(e, t, n, r, s = (o) => o()) {
  const o = [];
  for (const i of e) {
    O.NODE_ENV !== "production" && !i.components && !i.children.length && N(`Record with path "${i.path}" is either missing a "component(s)" or "children" property.`);
    for (const c in i.components) {
      let a = i.components[c];
      if (O.NODE_ENV !== "production") {
        if (!a || typeof a != "object" && typeof a != "function")
          throw N(`Component "${c}" in record with path "${i.path}" is not a valid component. Received "${String(a)}".`), new Error("Invalid route component");
        if ("then" in a) {
          N(`Component "${c}" in record with path "${i.path}" is a Promise instead of a function that returns a Promise. Did you write "import('./MyPage.vue')" instead of "() => import('./MyPage.vue')" ? This will break in production if not fixed.`);
          const h = a;
          a = () => h;
        } else a.__asyncLoader && // warn only once per component
        !a.__warnedDefineAsync && (a.__warnedDefineAsync = !0, N(`Component "${c}" in record with path "${i.path}" is defined using "defineAsyncComponent()". Write "() => import('./MyPage.vue')" instead of "defineAsyncComponent(() => import('./MyPage.vue'))".`));
      }
      if (!(t !== "beforeRouteEnter" && !i.instances[c]))
        if (Mn(a)) {
          const u = (a.__vccOpts || a)[t];
          u && o.push(le(u, n, r, i, c, s));
        } else {
          let h = a();
          O.NODE_ENV !== "production" && !("catch" in h) && (N(`Component "${c}" in record with path "${i.path}" is a function that does not return a Promise. If you were passing a functional component, make sure to add a "displayName" to the component. This will break in production if not fixed.`), h = Promise.resolve(h)), o.push(() => h.then((u) => {
            if (!u)
              throw new Error(`Couldn't resolve component "${c}" at "${i.path}"`);
            const l = Eo(u) ? u.default : u;
            i.mods[c] = u, i.components[c] = l;
            const d = (l.__vccOpts || l)[t];
            return d && le(d, n, r, i, c, s)();
          }));
        }
    }
  }
  return o;
}
function on(e) {
  const t = ae(Qe), n = ae($t);
  let r = !1, s = null;
  const o = j(() => {
    const u = H(e.to);
    return O.NODE_ENV !== "production" && (!r || u !== s) && (ze(u) || (r ? N(`Invalid value for prop "to" in useLink()
- to:`, u, `
- previous to:`, s, `
- props:`, e) : N(`Invalid value for prop "to" in useLink()
- to:`, u, `
- props:`, e)), s = u, r = !0), t.resolve(u);
  }), i = j(() => {
    const { matched: u } = o.value, { length: l } = u, f = u[l - 1], d = n.matched;
    if (!f || !d.length)
      return -1;
    const p = d.findIndex(he.bind(null, f));
    if (p > -1)
      return p;
    const g = an(u[l - 2]);
    return (
      // we are dealing with nested routes
      l > 1 && // if the parent and matched route have the same path, this link is
      // referring to the empty child. Or we currently are on a different
      // child of the same parent
      an(f) === g && // avoid comparing the child with its parent
      d[d.length - 1].path !== g ? d.findIndex(he.bind(null, u[l - 2])) : p
    );
  }), c = j(() => i.value > -1 && ki(n.params, o.value.params)), a = j(() => i.value > -1 && i.value === n.matched.length - 1 && Un(n.params, o.value.params));
  function h(u = {}) {
    if (Si(u)) {
      const l = t[H(e.replace) ? "replace" : "push"](
        H(e.to)
        // avoid uncaught errors are they are logged anyway
      ).catch(xe);
      return e.viewTransition && typeof document < "u" && "startViewTransition" in document && document.startViewTransition(() => l), l;
    }
    return Promise.resolve();
  }
  if (O.NODE_ENV !== "production" && oe) {
    const u = He();
    if (u) {
      const l = {
        route: o.value,
        isActive: c.value,
        isExactActive: a.value,
        error: null
      };
      u.__vrl_devtools = u.__vrl_devtools || [], u.__vrl_devtools.push(l), Nt(() => {
        l.route = o.value, l.isActive = c.value, l.isExactActive = a.value, l.error = ze(H(e.to)) ? null : 'Invalid "to" value';
      }, { flush: "post" });
    }
  }
  return {
    route: o,
    href: j(() => o.value.href),
    isActive: c,
    isExactActive: a,
    navigate: h
  };
}
function _i(e) {
  return e.length === 1 ? e[0] : e;
}
const Ei = /* @__PURE__ */ Z({
  name: "RouterLink",
  compatConfig: { MODE: 3 },
  props: {
    to: {
      type: [String, Object],
      required: !0
    },
    replace: Boolean,
    activeClass: String,
    // inactiveClass: String,
    exactActiveClass: String,
    custom: Boolean,
    ariaCurrentValue: {
      type: String,
      default: "page"
    }
  },
  useLink: on,
  setup(e, { slots: t }) {
    const n = Rr(on(e)), { options: r } = ae(Qe), s = j(() => ({
      [cn(e.activeClass, r.linkActiveClass, "router-link-active")]: n.isActive,
      // [getLinkClass(
      //   props.inactiveClass,
      //   options.linkInactiveClass,
      //   'router-link-inactive'
      // )]: !link.isExactActive,
      [cn(e.exactActiveClass, r.linkExactActiveClass, "router-link-exact-active")]: n.isExactActive
    }));
    return () => {
      const o = t.default && _i(t.default(n));
      return e.custom ? o : J("a", {
        "aria-current": n.isExactActive ? e.ariaCurrentValue : null,
        href: n.href,
        // this would override user added attrs but Vue will still add
        // the listener, so we end up triggering both
        onClick: n.navigate,
        class: s.value
      }, o);
    };
  }
}), bi = Ei;
function Si(e) {
  if (!(e.metaKey || e.altKey || e.ctrlKey || e.shiftKey) && !e.defaultPrevented && !(e.button !== void 0 && e.button !== 0)) {
    if (e.currentTarget && e.currentTarget.getAttribute) {
      const t = e.currentTarget.getAttribute("target");
      if (/\b_blank\b/i.test(t))
        return;
    }
    return e.preventDefault && e.preventDefault(), !0;
  }
}
function ki(e, t) {
  for (const n in t) {
    const r = t[n], s = e[n];
    if (typeof r == "string") {
      if (r !== s)
        return !1;
    } else if (!X(s) || s.length !== r.length || r.some((o, i) => o !== s[i]))
      return !1;
  }
  return !0;
}
function an(e) {
  return e ? e.aliasOf ? e.aliasOf.path : e.path : "";
}
const cn = (e, t, n) => e ?? t ?? n, Ri = /* @__PURE__ */ Z({
  name: "RouterView",
  // #674 we manually inherit them
  inheritAttrs: !1,
  props: {
    name: {
      type: String,
      default: "default"
    },
    route: Object
  },
  // Better compat for @vue/compat users
  // https://github.com/vuejs/router/issues/1315
  compatConfig: { MODE: 3 },
  setup(e, { attrs: t, slots: n }) {
    O.NODE_ENV !== "production" && Ni();
    const r = ae(bt), s = j(() => e.route || r.value), o = ae(sn, 0), i = j(() => {
      let h = H(o);
      const { matched: u } = s.value;
      let l;
      for (; (l = u[h]) && !l.components; )
        h++;
      return h;
    }), c = j(() => s.value.matched[i.value]);
    z(sn, j(() => i.value + 1)), z(vi, c), z(bt, s);
    const a = U();
    return G(() => [a.value, c.value, e.name], ([h, u, l], [f, d, p]) => {
      u && (u.instances[l] = h, d && d !== u && h && h === f && (u.leaveGuards.size || (u.leaveGuards = d.leaveGuards), u.updateGuards.size || (u.updateGuards = d.updateGuards))), h && u && // if there is no instance but to and from are the same this might be
      // the first visit
      (!d || !he(u, d) || !f) && (u.enterCallbacks[l] || []).forEach((g) => g(h));
    }, { flush: "post" }), () => {
      const h = s.value, u = e.name, l = c.value, f = l && l.components[u];
      if (!f)
        return ln(n.default, { Component: f, route: h });
      const d = l.props[u], p = d ? d === !0 ? h.params : typeof d == "function" ? d(h) : d : null, y = J(f, x({}, p, t, {
        onVnodeUnmounted: (_) => {
          _.component.isUnmounted && (l.instances[u] = null);
        },
        ref: a
      }));
      if (O.NODE_ENV !== "production" && oe && y.ref) {
        const _ = {
          depth: i.value,
          name: l.name,
          path: l.path,
          meta: l.meta
        };
        (X(y.ref) ? y.ref.map((k) => k.i) : [y.ref.i]).forEach((k) => {
          k.__vrv_devtools = _;
        });
      }
      return (
        // pass the vnode to the slot as a prop.
        // h and <component :is="..."> both accept vnodes
        ln(n.default, { Component: y, route: h }) || y
      );
    };
  }
});
function ln(e, t) {
  if (!e)
    return null;
  const n = e(t);
  return n.length === 1 ? n[0] : n;
}
const Oi = Ri;
function Ni() {
  const e = He(), t = e.parent && e.parent.type.name, n = e.parent && e.parent.subTree && e.parent.subTree.type;
  if (t && (t === "KeepAlive" || t.includes("Transition")) && typeof n == "object" && n.name === "RouterView") {
    const r = t === "KeepAlive" ? "keep-alive" : "transition";
    N(`<router-view> can no longer be used directly inside <transition> or <keep-alive>.
Use slot props instead:

<router-view v-slot="{ Component }">
  <${r}>
    <component :is="Component" />
  </${r}>
</router-view>`);
  }
}
function Ce(e, t) {
  const n = x({}, e, {
    // remove variables that can contain vue instances
    matched: e.matched.map((r) => ji(r, ["instances", "children", "aliasOf"]))
  });
  return {
    _custom: {
      type: null,
      readOnly: !0,
      display: e.fullPath,
      tooltip: t,
      value: n
    }
  };
}
function Fe(e) {
  return {
    _custom: {
      display: e
    }
  };
}
let Pi = 0;
function Vi(e, t, n) {
  if (t.__hasDevtools)
    return;
  t.__hasDevtools = !0;
  const r = Pi++;
  _o({
    id: "org.vuejs.router" + (r ? "." + r : ""),
    label: "Vue Router",
    packageName: "vue-router",
    homepage: "https://router.vuejs.org",
    logo: "https://router.vuejs.org/logo.png",
    componentStateTypes: ["Routing"],
    app: e
  }, (s) => {
    typeof s.now != "function" && console.warn("[Vue Router]: You seem to be using an outdated version of Vue Devtools. Are you still using the Beta release instead of the stable one? You can find the links at https://devtools.vuejs.org/guide/installation.html."), s.on.inspectComponent((u, l) => {
      u.instanceData && u.instanceData.state.push({
        type: "Routing",
        key: "$route",
        editable: !1,
        value: Ce(t.currentRoute.value, "Current Route")
      });
    }), s.on.visitComponentTree(({ treeNode: u, componentInstance: l }) => {
      if (l.__vrv_devtools) {
        const f = l.__vrv_devtools;
        u.tags.push({
          label: (f.name ? `${f.name.toString()}: ` : "") + f.path,
          textColor: 0,
          tooltip: "This component is rendered by &lt;router-view&gt;",
          backgroundColor: Yn
        });
      }
      X(l.__vrl_devtools) && (l.__devtoolsApi = s, l.__vrl_devtools.forEach((f) => {
        let d = f.route.path, p = er, g = "", y = 0;
        f.error ? (d = f.error, p = Ti, y = Ii) : f.isExactActive ? (p = Zn, g = "This is exactly active") : f.isActive && (p = Xn, g = "This link is active"), u.tags.push({
          label: d,
          textColor: y,
          tooltip: g,
          backgroundColor: p
        });
      }));
    }), G(t.currentRoute, () => {
      a(), s.notifyComponentUpdate(), s.sendInspectorTree(c), s.sendInspectorState(c);
    });
    const o = "router:navigations:" + r;
    s.addTimelineLayer({
      id: o,
      label: `Router${r ? " " + r : ""} Navigations`,
      color: 4237508
    }), t.onError((u, l) => {
      s.addTimelineEvent({
        layerId: o,
        event: {
          title: "Error during Navigation",
          subtitle: l.fullPath,
          logType: "error",
          time: s.now(),
          data: { error: u },
          groupId: l.meta.__navigationId
        }
      });
    });
    let i = 0;
    t.beforeEach((u, l) => {
      const f = {
        guard: Fe("beforeEach"),
        from: Ce(l, "Current Location during this navigation"),
        to: Ce(u, "Target location")
      };
      Object.defineProperty(u.meta, "__navigationId", {
        value: i++
      }), s.addTimelineEvent({
        layerId: o,
        event: {
          time: s.now(),
          title: "Start of navigation",
          subtitle: u.fullPath,
          data: f,
          groupId: u.meta.__navigationId
        }
      });
    }), t.afterEach((u, l, f) => {
      const d = {
        guard: Fe("afterEach")
      };
      f ? (d.failure = {
        _custom: {
          type: Error,
          readOnly: !0,
          display: f ? f.message : "",
          tooltip: "Navigation Failure",
          value: f
        }
      }, d.status = Fe("❌")) : d.status = Fe("✅"), d.from = Ce(l, "Current Location during this navigation"), d.to = Ce(u, "Target location"), s.addTimelineEvent({
        layerId: o,
        event: {
          title: "End of navigation",
          subtitle: u.fullPath,
          time: s.now(),
          data: d,
          logType: f ? "warning" : "default",
          groupId: u.meta.__navigationId
        }
      });
    });
    const c = "router-inspector:" + r;
    s.addInspector({
      id: c,
      label: "Routes" + (r ? " " + r : ""),
      icon: "book",
      treeFilterPlaceholder: "Search routes"
    });
    function a() {
      if (!h)
        return;
      const u = h;
      let l = n.getRoutes().filter((f) => !f.parent || // these routes have a parent with no component which will not appear in the view
      // therefore we still need to include them
      !f.parent.record.components);
      l.forEach(rr), u.filter && (l = l.filter((f) => (
        // save matches state based on the payload
        St(f, u.filter.toLowerCase())
      ))), l.forEach((f) => nr(f, t.currentRoute.value)), u.rootNodes = l.map(tr);
    }
    let h;
    s.on.getInspectorTree((u) => {
      h = u, u.app === e && u.inspectorId === c && a();
    }), s.on.getInspectorState((u) => {
      if (u.app === e && u.inspectorId === c) {
        const f = n.getRoutes().find((d) => d.record.__vd_id === u.nodeId);
        f && (u.state = {
          options: Ai(f)
        });
      }
    }), s.sendInspectorTree(c), s.sendInspectorState(c);
  });
}
function Ci(e) {
  return e.optional ? e.repeatable ? "*" : "?" : e.repeatable ? "+" : "";
}
function Ai(e) {
  const { record: t } = e, n = [
    { editable: !1, key: "path", value: t.path }
  ];
  return t.name != null && n.push({
    editable: !1,
    key: "name",
    value: t.name
  }), n.push({ editable: !1, key: "regexp", value: e.re }), e.keys.length && n.push({
    editable: !1,
    key: "keys",
    value: {
      _custom: {
        type: null,
        readOnly: !0,
        display: e.keys.map((r) => `${r.name}${Ci(r)}`).join(" "),
        tooltip: "Param keys",
        value: e.keys
      }
    }
  }), t.redirect != null && n.push({
    editable: !1,
    key: "redirect",
    value: t.redirect
  }), e.alias.length && n.push({
    editable: !1,
    key: "aliases",
    value: e.alias.map((r) => r.record.path)
  }), Object.keys(e.record.meta).length && n.push({
    editable: !1,
    key: "meta",
    value: e.record.meta
  }), n.push({
    key: "score",
    editable: !1,
    value: {
      _custom: {
        type: null,
        readOnly: !0,
        display: e.score.map((r) => r.join(", ")).join(" | "),
        tooltip: "Score used to sort routes",
        value: e.score
      }
    }
  }), n;
}
const Yn = 15485081, Xn = 2450411, Zn = 8702998, xi = 2282478, er = 16486972, $i = 6710886, Ti = 16704226, Ii = 12131356;
function tr(e) {
  const t = [], { record: n } = e;
  n.name != null && t.push({
    label: String(n.name),
    textColor: 0,
    backgroundColor: xi
  }), n.aliasOf && t.push({
    label: "alias",
    textColor: 0,
    backgroundColor: er
  }), e.__vd_match && t.push({
    label: "matches",
    textColor: 0,
    backgroundColor: Yn
  }), e.__vd_exactActive && t.push({
    label: "exact",
    textColor: 0,
    backgroundColor: Zn
  }), e.__vd_active && t.push({
    label: "active",
    textColor: 0,
    backgroundColor: Xn
  }), n.redirect && t.push({
    label: typeof n.redirect == "string" ? `redirect: ${n.redirect}` : "redirects",
    textColor: 16777215,
    backgroundColor: $i
  });
  let r = n.__vd_id;
  return r == null && (r = String(Di++), n.__vd_id = r), {
    id: r,
    label: n.path,
    tags: t,
    children: e.children.map(tr)
  };
}
let Di = 0;
const Mi = /^\/(.*)\/([a-z]*)$/;
function nr(e, t) {
  const n = t.matched.length && he(t.matched[t.matched.length - 1], e.record);
  e.__vd_exactActive = e.__vd_active = n, n || (e.__vd_active = t.matched.some((r) => he(r, e.record))), e.children.forEach((r) => nr(r, t));
}
function rr(e) {
  e.__vd_match = !1, e.children.forEach(rr);
}
function St(e, t) {
  const n = String(e.re).match(Mi);
  if (e.__vd_match = !1, !n || n.length < 3)
    return !1;
  if (new RegExp(n[1].replace(/\$$/, ""), n[2]).test(t))
    return e.children.forEach((i) => St(i, t)), e.record.path !== "/" || t === "/" ? (e.__vd_match = e.re.test(t), !0) : !1;
  const s = e.record.path.toLowerCase(), o = Oe(s);
  return !t.startsWith("/") && (o.includes(t) || s.includes(t)) || o.startsWith(t) || s.startsWith(t) || e.record.name && String(e.record.name).includes(t) ? !0 : e.children.some((i) => St(i, t));
}
function ji(e, t) {
  const n = {};
  for (const r in e)
    t.includes(r) || (n[r] = e[r]);
  return n;
}
function Bi(e) {
  const t = ai(e.routes, e), n = e.parseQuery || gi, r = e.stringifyQuery || rn, s = e.history;
  if (O.NODE_ENV !== "production" && !s)
    throw new Error('Provide the "history" option when calling "createRouter()": https://router.vuejs.org/api/interfaces/RouterOptions.html#history');
  const o = Ve(), i = Ve(), c = Ve(), a = ie(ce);
  let h = ce;
  oe && e.scrollBehavior && "scrollRestoration" in history && (history.scrollRestoration = "manual");
  const u = it.bind(null, (m) => "" + m), l = it.bind(null, To), f = (
    // @ts-expect-error: intentionally avoid the type check
    it.bind(null, Oe)
  );
  function d(m, b) {
    let E, S;
    return qn(m) ? (E = t.getRecordMatcher(m), O.NODE_ENV !== "production" && !E && N(`Parent route "${String(m)}" not found when adding child route`, b), S = b) : S = m, t.addRoute(S, E);
  }
  function p(m) {
    const b = t.getRecordMatcher(m);
    b ? t.removeRoute(b) : O.NODE_ENV !== "production" && N(`Cannot remove non-existent route "${String(m)}"`);
  }
  function g() {
    return t.getRoutes().map((m) => m.record);
  }
  function y(m) {
    return !!t.getRecordMatcher(m);
  }
  function _(m, b) {
    if (b = x({}, b || a.value), typeof m == "string") {
      const V = at(n, m, b.path), B = t.resolve({ path: V.path }, b), pe = s.createHref(V.fullPath);
      return O.NODE_ENV !== "production" && (pe.startsWith("//") ? N(`Location "${m}" resolved to "${pe}". A resolved location cannot start with multiple slashes.`) : B.matched.length || N(`No match found for location with path "${m}"`)), x(V, B, {
        params: f(B.params),
        hash: Oe(V.hash),
        redirectedFrom: void 0,
        href: pe
      });
    }
    if (O.NODE_ENV !== "production" && !ze(m))
      return N(`router.resolve() was passed an invalid location. This will fail in production.
- Location:`, m), _({});
    let E;
    if (m.path != null)
      O.NODE_ENV !== "production" && "params" in m && !("name" in m) && // @ts-expect-error: the type is never
      Object.keys(m.params).length && N(`Path "${m.path}" was passed with params but they will be ignored. Use a named route alongside params instead.`), E = x({}, m, {
        path: at(n, m.path, b.path).path
      });
    else {
      const V = x({}, m.params);
      for (const B in V)
        V[B] == null && delete V[B];
      E = x({}, m, {
        params: l(V)
      }), b.params = l(b.params);
    }
    const S = t.resolve(E, b), $ = m.hash || "";
    O.NODE_ENV !== "production" && $ && !$.startsWith("#") && N(`A \`hash\` should always start with the character "#". Replace "${$}" with "#${$}".`), S.params = u(f(S.params));
    const W = Mo(r, x({}, m, {
      hash: Ao($),
      path: S.path
    })), C = s.createHref(W);
    return O.NODE_ENV !== "production" && (C.startsWith("//") ? N(`Location "${m}" resolved to "${C}". A resolved location cannot start with multiple slashes.`) : S.matched.length || N(`No match found for location with path "${m.path != null ? m.path : m}"`)), x({
      fullPath: W,
      // keep the hash encoded so fullPath is effectively path + encodedQuery +
      // hash
      hash: $,
      query: (
        // if the user is using a custom query lib like qs, we might have
        // nested objects, so we keep the query as is, meaning it can contain
        // numbers at `$route.query`, but at the point, the user will have to
        // use their own type anyway.
        // https://github.com/vuejs/router/issues/328#issuecomment-649481567
        r === rn ? yi(m.query) : m.query || {}
      )
    }, S, {
      redirectedFrom: void 0,
      href: C
    });
  }
  function w(m) {
    return typeof m == "string" ? at(n, m, a.value.path) : x({}, m);
  }
  function k(m, b) {
    if (h !== m)
      return Pe(8, {
        from: b,
        to: m
      });
  }
  function v(m) {
    return T(m);
  }
  function R(m) {
    return v(x(w(m), { replace: !0 }));
  }
  function A(m) {
    const b = m.matched[m.matched.length - 1];
    if (b && b.redirect) {
      const { redirect: E } = b;
      let S = typeof E == "function" ? E(m) : E;
      if (typeof S == "string" && (S = S.includes("?") || S.includes("#") ? S = w(S) : (
        // force empty params
        { path: S }
      ), S.params = {}), O.NODE_ENV !== "production" && S.path == null && !("name" in S))
        throw N(`Invalid redirect found:
${JSON.stringify(S, null, 2)}
 when navigating to "${m.fullPath}". A redirect must contain a name or path. This will break in production.`), new Error("Invalid redirect");
      return x({
        query: m.query,
        hash: m.hash,
        // avoid transferring params if the redirect has a path
        params: S.path != null ? {} : m.params
      }, S);
    }
  }
  function T(m, b) {
    const E = h = _(m), S = a.value, $ = m.state, W = m.force, C = m.replace === !0, V = A(E);
    if (V)
      return T(
        x(w(V), {
          state: typeof V == "object" ? x({}, $, V.state) : $,
          force: W,
          replace: C
        }),
        // keep original redirectedFrom if it exists
        b || E
      );
    const B = E;
    B.redirectedFrom = b;
    let pe;
    return !W && Kt(r, S, E) && (pe = Pe(16, { to: B, from: S }), It(
      S,
      S,
      // this is a push, the only way for it to be triggered from a
      // history.listen is with a redirect, which makes it become a push
      !0,
      // This cannot be the first navigation because the initial location
      // cannot be manually navigated to
      !1
    )), (pe ? Promise.resolve(pe) : P(B, S)).catch((K) => se(K) ? (
      // navigation redirects still mark the router as ready
      se(
        K,
        2
        /* ErrorTypes.NAVIGATION_GUARD_REDIRECT */
      ) ? K : rt(K)
    ) : (
      // reject any unknown error
      nt(K, B, S)
    )).then((K) => {
      if (K) {
        if (se(
          K,
          2
          /* ErrorTypes.NAVIGATION_GUARD_REDIRECT */
        ))
          return O.NODE_ENV !== "production" && // we are redirecting to the same location we were already at
          Kt(r, _(K.to), B) && // and we have done it a couple of times
          b && // @ts-expect-error: added only in dev
          (b._count = b._count ? (
            // @ts-expect-error
            b._count + 1
          ) : 1) > 30 ? (N(`Detected a possibly infinite redirection in a navigation guard when going from "${S.fullPath}" to "${B.fullPath}". Aborting to avoid a Stack Overflow.
 Are you always returning a new location within a navigation guard? That would lead to this error. Only return when redirecting or aborting, that should fix this. This might break in production if not fixed.`), Promise.reject(new Error("Infinite redirect in navigation guard"))) : T(
            // keep options
            x({
              // preserve an existing replacement but allow the redirect to override it
              replace: C
            }, w(K.to), {
              state: typeof K.to == "object" ? x({}, $, K.to.state) : $,
              force: W
            }),
            // preserve the original redirectedFrom if any
            b || B
          );
      } else
        K = F(B, S, !0, C, $);
      return I(B, S, K), K;
    });
  }
  function L(m, b) {
    const E = k(m, b);
    return E ? Promise.reject(E) : Promise.resolve();
  }
  function Q(m) {
    const b = je.values().next().value;
    return b && typeof b.runWithContext == "function" ? b.runWithContext(m) : m();
  }
  function P(m, b) {
    let E;
    const [S, $, W] = Li(m, b);
    E = lt(S.reverse(), "beforeRouteLeave", m, b);
    for (const V of S)
      V.leaveGuards.forEach((B) => {
        E.push(le(B, m, b));
      });
    const C = L.bind(null, m, b);
    return E.push(C), we(E).then(() => {
      E = [];
      for (const V of o.list())
        E.push(le(V, m, b));
      return E.push(C), we(E);
    }).then(() => {
      E = lt($, "beforeRouteUpdate", m, b);
      for (const V of $)
        V.updateGuards.forEach((B) => {
          E.push(le(B, m, b));
        });
      return E.push(C), we(E);
    }).then(() => {
      E = [];
      for (const V of W)
        if (V.beforeEnter)
          if (X(V.beforeEnter))
            for (const B of V.beforeEnter)
              E.push(le(B, m, b));
          else
            E.push(le(V.beforeEnter, m, b));
      return E.push(C), we(E);
    }).then(() => (m.matched.forEach((V) => V.enterCallbacks = {}), E = lt(W, "beforeRouteEnter", m, b, Q), E.push(C), we(E))).then(() => {
      E = [];
      for (const V of i.list())
        E.push(le(V, m, b));
      return E.push(C), we(E);
    }).catch((V) => se(
      V,
      8
      /* ErrorTypes.NAVIGATION_CANCELLED */
    ) ? V : Promise.reject(V));
  }
  function I(m, b, E) {
    c.list().forEach((S) => Q(() => S(m, b, E)));
  }
  function F(m, b, E, S, $) {
    const W = k(m, b);
    if (W)
      return W;
    const C = b === ce, V = oe ? history.state : {};
    E && (S || C ? s.replace(m.fullPath, x({
      scroll: C && V && V.scroll
    }, $)) : s.push(m.fullPath, $)), a.value = m, It(m, b, E, C), rt();
  }
  let ee;
  function cr() {
    ee || (ee = s.listen((m, b, E) => {
      if (!Dt.listening)
        return;
      const S = _(m), $ = A(S);
      if ($) {
        T(x($, { replace: !0, force: !0 }), S).catch(xe);
        return;
      }
      h = S;
      const W = a.value;
      oe && Uo(qt(W.fullPath, E.delta), Je()), P(S, W).catch((C) => se(
        C,
        12
        /* ErrorTypes.NAVIGATION_CANCELLED */
      ) ? C : se(
        C,
        2
        /* ErrorTypes.NAVIGATION_GUARD_REDIRECT */
      ) ? (T(
        x(w(C.to), {
          force: !0
        }),
        S
        // avoid an uncaught rejection, let push call triggerError
      ).then((V) => {
        se(
          V,
          20
          /* ErrorTypes.NAVIGATION_DUPLICATED */
        ) && !E.delta && E.type === Ne.pop && s.go(-1, !1);
      }).catch(xe), Promise.reject()) : (E.delta && s.go(-E.delta, !1), nt(C, S, W))).then((C) => {
        C = C || F(
          // after navigation, all matched components are resolved
          S,
          W,
          !1
        ), C && (E.delta && // a new navigation has been triggered, so we do not want to revert, that will change the current history
        // entry while a different route is displayed
        !se(
          C,
          8
          /* ErrorTypes.NAVIGATION_CANCELLED */
        ) ? s.go(-E.delta, !1) : E.type === Ne.pop && se(
          C,
          20
          /* ErrorTypes.NAVIGATION_DUPLICATED */
        ) && s.go(-1, !1)), I(S, W, C);
      }).catch(xe);
    }));
  }
  let tt = Ve(), Tt = Ve(), Me;
  function nt(m, b, E) {
    rt(m);
    const S = Tt.list();
    return S.length ? S.forEach(($) => $(m, b, E)) : (O.NODE_ENV !== "production" && N("uncaught error during route navigation:"), console.error(m)), Promise.reject(m);
  }
  function lr() {
    return Me && a.value !== ce ? Promise.resolve() : new Promise((m, b) => {
      tt.add([m, b]);
    });
  }
  function rt(m) {
    return Me || (Me = !m, cr(), tt.list().forEach(([b, E]) => m ? E(m) : b()), tt.reset()), m;
  }
  function It(m, b, E, S) {
    const { scrollBehavior: $ } = e;
    if (!oe || !$)
      return Promise.resolve();
    const W = !E && zo(qt(m.fullPath, 0)) || (S || !E) && history.state && history.state.scroll || null;
    return Se().then(() => $(m, b, W)).then((C) => C && Wo(C)).catch((C) => nt(C, m, b));
  }
  const st = (m) => s.go(m);
  let ot;
  const je = /* @__PURE__ */ new Set(), Dt = {
    currentRoute: a,
    listening: !0,
    addRoute: d,
    removeRoute: p,
    clearRoutes: t.clearRoutes,
    hasRoute: y,
    getRoutes: g,
    resolve: _,
    options: e,
    push: v,
    replace: R,
    go: st,
    back: () => st(-1),
    forward: () => st(1),
    beforeEach: o.add,
    beforeResolve: i.add,
    afterEach: c.add,
    onError: Tt.add,
    isReady: lr,
    install(m) {
      const b = this;
      m.component("RouterLink", bi), m.component("RouterView", Oi), m.config.globalProperties.$router = b, Object.defineProperty(m.config.globalProperties, "$route", {
        enumerable: !0,
        get: () => H(a)
      }), oe && // used for the initial navigation client side to avoid pushing
      // multiple times when the router is used in multiple apps
      !ot && a.value === ce && (ot = !0, v(s.location).catch(($) => {
        O.NODE_ENV !== "production" && N("Unexpected error when starting the router:", $);
      }));
      const E = {};
      for (const $ in ce)
        Object.defineProperty(E, $, {
          get: () => a.value[$],
          enumerable: !0
        });
      m.provide(Qe, b), m.provide($t, kr(E)), m.provide(bt, a);
      const S = m.unmount;
      je.add(m), m.unmount = function() {
        je.delete(m), je.size < 1 && (h = ce, ee && ee(), ee = null, a.value = ce, ot = !1, Me = !1), S();
      }, O.NODE_ENV !== "production" && oe && Vi(m, b, t);
    }
  };
  function we(m) {
    return m.reduce((b, E) => b.then(() => Q(E)), Promise.resolve());
  }
  return Dt;
}
function Li(e, t) {
  const n = [], r = [], s = [], o = Math.max(t.matched.length, e.matched.length);
  for (let i = 0; i < o; i++) {
    const c = t.matched[i];
    c && (e.matched.find((h) => he(h, c)) ? r.push(c) : n.push(c));
    const a = e.matched[i];
    a && (t.matched.find((h) => he(h, a)) || s.push(a));
  }
  return [n, r, s];
}
function Fi() {
  return ae(Qe);
}
function Wi(e) {
  return ae($t);
}
const sr = Symbol("BINDING_GETTER_KEY");
function Ui(e, t) {
  const n = Gi(e, t);
  return zi(e, n, t), Or(() => {
    n._release();
  }), z(sr, n), {
    bindingGetter: n
  };
}
function zi(e, t, n) {
  var s, o, i, c, a, h, u, l, f;
  const { id: r } = e;
  if (Hi(n.vforSetting, r, t), Ki(n.slotSetting, r, t), e.routerParam) {
    const d = D(r, e.routerParam), p = Wi(), g = j(() => p.params);
    t._registerBinding(d, g), z(d, g);
  }
  if (e.routerAct) {
    const d = D(r, e.routerAct), p = Fi();
    t._registerBinding(d, p), z(d, p);
  }
  (s = e.data) == null || s.forEach((d) => {
    const p = D(r, d.id);
    t._registerBinding(p, d.value), z(p, d.value);
  }), (o = e.jsFn) == null || o.forEach((d) => {
    const p = D(r, d.id), g = qi(d);
    t._registerBinding(p, g), z(p, g);
  }), (i = e.eRefs) == null || i.forEach((d) => {
    const p = D(r, d.id), g = ie(null);
    t._registerBinding(p, g), z(p, g);
  }), (c = e.refs) == null || c.forEach((d) => {
    const { id: p, constData: g } = d, _ = g !== void 0 ? t.getValue(d.value) : d.value, w = D(r, p), k = eo({ ...d, value: _ });
    t._registerBinding(w, k), z(w, k);
  }), (a = e.web_computed) == null || a.forEach((d) => {
    const p = D(r, d.id), g = no(d);
    t._registerBinding(p, g), z(p, g);
  }), (h = e.js_computed) == null || h.forEach((d) => {
    const p = D(r, d.id), g = ro(
      d,
      t
    );
    t._registerBinding(p, g), z(p, g);
  }), (u = e.vue_computed) == null || u.forEach((d) => {
    const p = D(r, d.id), g = to(
      d,
      t
    );
    t._registerBinding(p, g), z(p, g);
  }), oo({
    watchConfigs: e.py_watch || [],
    computedConfigs: e.web_computed || [],
    bindingGetter: t,
    sid: r
  }), (l = e.js_watch) == null || l.forEach((d) => {
    fo(d, t);
  }), (f = e.vue_watch) == null || f.forEach((d) => {
    uo(d, t);
  });
}
function Hi(e, t, n) {
  if (e != null && e.item) {
    const { id: r } = e.item, s = D(t, r), o = Ji(e.item, n);
    n._registerBinding(s, o), z(s, o);
  }
  if (e != null && e.index) {
    const { id: r, value: s } = e.index, o = D(t, r), i = U(s);
    n._registerBinding(o, i), z(o, i);
  }
  if (e != null && e.key) {
    const { id: r, value: s } = e.key, o = D(t, r), i = U(s);
    n._registerBinding(o, i), z(o, i);
  }
}
function Ki(e, t, n) {
  if (!e)
    return;
  const { id: r, value: s } = e, o = D(t, r), i = ie(s);
  n._registerBinding(o, i), z(o, i);
}
function Gi(e, t) {
  const { binds: n } = e, r = /* @__PURE__ */ new Map(), s = /* @__PURE__ */ new Map();
  let o = null, i = null;
  const c = Qi(
    n,
    e.web_computed,
    e.id,
    t
  );
  c == null || c.forEach((v, R) => {
    const { sid: A, id: T } = v, L = D(A, T);
    if (A !== e.id) {
      const Q = ae(L);
      r.set(R, Q);
    } else
      s.set(L, R);
  });
  function a(v) {
    const R = h(v);
    return Gs(R, {
      paths: v.path,
      getBindableValueFn: u
    });
  }
  function h(v) {
    const R = r.get(v.r);
    if (!R)
      throw new Error(`Binding not found: ${JSON.stringify(v)}`);
    return R;
  }
  function u(v) {
    return be(a(v));
  }
  function l(v) {
    const R = r.get(v.r);
    if (!R)
      throw new Error(`Router binding not found: ${JSON.stringify(v)}`);
    return R;
  }
  function f(v, R) {
    if (kn(v)) {
      const A = h(v);
      if (v.path) {
        Tn(A.value, v.path, R, u);
        return;
      }
      A.value = R;
      return;
    }
    throw new Error(`Unsupported output binding: ${v}`);
  }
  function d(v) {
    if (v != null && v.item) {
      const { id: R, value: A, sourceInfo: T } = v.item;
      if (T) {
        const { index: P, key: I } = T;
        o && (o.value = P), i && (i.value = I);
      }
      const L = D(e.id, R), Q = a({ r: g(L) });
      Q.value = A;
    }
    if (v != null && v.index) {
      const { id: R, value: A } = v.index, T = D(e.id, R), L = a({ r: g(T) });
      L.value = A;
    }
    if (v != null && v.key) {
      const { id: R, value: A } = v.key, T = D(e.id, R), L = a({ r: g(T) });
      L.value = A;
    }
  }
  function p(v) {
    if (!v)
      return;
    const { id: R, value: A } = v, T = D(e.id, R), L = a({ r: g(T) });
    L.value = A;
  }
  function g(v) {
    return s.get(v);
  }
  function y(v, R) {
    const A = s.get(v);
    A !== void 0 && r.set(A, R);
  }
  function _() {
    r.clear(), s.clear();
  }
  function w(v) {
    return o = U(v), o;
  }
  function k(v) {
    return i = U(v), i;
  }
  return {
    getValue: u,
    getRef: a,
    updateValue: f,
    getBindIndex: g,
    updateVForInfo: d,
    updateSlotInfo: p,
    getRouter: l,
    initVForIndexRef: w,
    initVForKeyRef: k,
    _registerBinding: y,
    _release: _
  };
}
function D(e, t) {
  return `${e}-${t}`;
}
function qi(e) {
  const { immediately: t = !1, code: n } = e;
  let r = q(n);
  return t && (r = r()), ye(() => ({
    get() {
      return r;
    },
    set() {
      throw new Error("Cannot set value to js function");
    }
  }));
}
function Qa() {
  const { getRef: e, getRouter: t, getValue: n } = ae(sr);
  return {
    getRef: e,
    getRouter: t,
    getValue: n
  };
}
function Ji(e, t) {
  const { value: n, sourceInfo: r } = e;
  if (r) {
    const { source: s, type: o, index: i, key: c } = r, a = t.initVForIndexRef(i);
    return o === "array" ? ye(() => ({
      get() {
        return s.value[a.value];
      },
      set(h) {
        s.value[a.value] = h;
      }
    })) : ye(() => {
      const h = t.initVForKeyRef(c);
      return {
        get() {
          return s.value[h.value];
        },
        set(u) {
          s.value[h.value] = u;
        }
      };
    });
  }
  return U(n);
}
function Qi(e, t, n, r) {
  const s = new Set(e == null ? void 0 : e.map((a) => D(a.sid, a.id))), o = Yi(
    e,
    s,
    t,
    n
  ), i = Xi(
    o,
    s,
    n,
    r
  );
  return Zi(
    i,
    s,
    n,
    r
  );
}
function Yi(e, t, n, r) {
  if (!n)
    return e;
  const s = n.filter((o) => !t.has(D(r, o.id))).map((o) => ({ id: o.id, sid: r }));
  return [...e ?? [], ...s];
}
function Xi(e, t, n, r) {
  if (!r.vforSetting)
    return e;
  const s = [];
  return r.vforSetting.item && !t.has(D(n, r.vforSetting.item.id)) && s.push({
    id: r.vforSetting.item.id,
    sid: n
  }), r.vforSetting.index && !t.has(D(n, r.vforSetting.index.id)) && s.push({
    id: r.vforSetting.index.id,
    sid: n
  }), r.vforSetting.key && !t.has(D(n, r.vforSetting.key.id)) && s.push({
    id: r.vforSetting.key.id,
    sid: n
  }), [...e ?? [], ...s];
}
function Zi(e, t, n, r) {
  return !r.slotSetting || t.has(D(n, r.slotSetting.id)) ? e : [
    ...e ?? [],
    { id: r.slotSetting.id, sid: n }
  ];
}
const or = Z(ea, {
  props: ["config", "vforSetting", "slotSetting"]
});
function ea(e) {
  const { config: t, vforSetting: n, slotSetting: r } = e, { items: s } = t, { bindingGetter: o } = Ui(t, { vforSetting: n, slotSetting: r });
  return () => {
    if (o.updateVForInfo(e.vforSetting), o.updateSlotInfo(e.slotSetting), !s)
      return null;
    if (s.length === 1) {
      const i = s[0];
      return ve(i, { sid: t.id, bindingGetter: o });
    }
    return s == null ? void 0 : s.map(
      (i) => ve(i, { sid: t.id, bindingGetter: o })
    );
  };
}
function ta(e, t) {
  const { state: n, isReady: r, isLoading: s } = Ts(async () => {
    let o = e;
    const i = t;
    if (!o && !i)
      throw new Error("Either config or configUrl must be provided");
    if (!o && i && (o = await (await fetch(i)).json()), !o)
      throw new Error("Failed to load config");
    return o;
  }, {});
  return { config: n, isReady: r, isLoading: s };
}
function na(e) {
  const t = U(!1), n = U("");
  function r(s, o) {
    let i;
    return o.component ? i = `Error captured from component:tag: ${o.component.tag} ; id: ${o.component.id} ` : i = "Error captured from app init", console.group(i), console.error("Component:", o.component), console.error("Error:", s), console.groupEnd(), e && (t.value = !0, n.value = `${i} ${s.message}`), !1;
  }
  return Nr(r), { hasError: t, errorMessage: n };
}
let kt;
function ra(e) {
  if (e === "web" || e === "webview") {
    kt = sa;
    return;
  }
  if (e === "zero") {
    kt = oa;
    return;
  }
  throw new Error(`Unsupported mode: ${e}`);
}
function sa(e) {
  const { assetPath: t = "/assets/icons", icon: n = "" } = e, [r, s] = n.split(":");
  return {
    assetPath: t,
    svgName: `${r}.svg`
  };
}
function oa(e) {
  const { icon: t = "" } = e, [n] = t.split(":"), [r] = n.split(".");
  return {
    assetPath: "",
    svgName: r
  };
}
function ia(e, t) {
  const n = j(() => {
    const r = e.value;
    if (!r)
      return null;
    const i = new DOMParser().parseFromString(r, "image/svg+xml").querySelector("svg");
    if (!i)
      throw new Error("Invalid svg string");
    const c = {};
    for (const f of i.attributes)
      c[f.name] = f.value;
    const { size: a, color: h, attrs: u } = t;
    h.value !== null && h.value !== void 0 && (i.removeAttribute("fill"), i.querySelectorAll("*").forEach((d) => {
      d.hasAttribute("fill") && d.setAttribute("fill", "currentColor");
    }), c.color = h.value), a.value !== null && a.value !== void 0 && (c.width = a.value.toString(), c.height = a.value.toString());
    const l = i.innerHTML;
    return {
      ...c,
      ...u,
      innerHTML: l
    };
  });
  return () => {
    if (!n.value)
      return null;
    const r = n.value;
    return J("svg", r);
  };
}
const aa = {
  class: "app-box insta-theme",
  "data-scaling": "100%"
}, ca = {
  key: 0,
  style: { position: "absolute", top: "50%", left: "50%", transform: "translate(-50%, -50%)" }
}, la = {
  key: 0,
  style: { color: "red", "font-size": "1.2em", margin: "1rem", border: "1px dashed red", padding: "1rem" }
}, ua = /* @__PURE__ */ Z({
  __name: "App",
  props: {
    config: {},
    meta: {},
    configUrl: {}
  },
  setup(e) {
    const t = e, { debug: n = !1 } = t.meta, { config: r, isLoading: s } = ta(
      t.config,
      t.configUrl
    );
    G(r, (c) => {
      c.url && (Tr({
        mode: t.meta.mode,
        version: t.meta.version,
        queryPath: c.url.path,
        pathParams: c.url.params,
        webServerInfo: c.webInfo
      }), Qr(t.meta.mode)), ra(t.meta.mode);
    });
    const { hasError: o, errorMessage: i } = na(n);
    return (c, a) => (fe(), Ee("div", aa, [
      H(s) ? (fe(), Ee("div", ca, a[0] || (a[0] = [
        gn("p", { style: { margin: "auto" } }, "Loading ...", -1)
      ]))) : (fe(), Ee("div", {
        key: 1,
        class: ut(["insta-main", H(r).class])
      }, [
        Pr(H(or), {
          config: H(r).scope
        }, null, 8, ["config"]),
        H(o) ? (fe(), Ee("div", la, pn(H(i)), 1)) : ft("", !0)
      ], 2))
    ]));
  }
}), un = /* @__PURE__ */ new Map([
  [
    "size",
    {
      classes: "ist-r-size",
      handler: (e) => fa(e)
    }
  ],
  [
    "weight",
    {
      classes: "ist-r-weight",
      styleVar: "--weight",
      handler: (e) => e
    }
  ],
  [
    "text_align",
    {
      classes: "ist-r-ta",
      styleVar: "--ta",
      handler: (e) => e
    }
  ],
  [
    "trim",
    {
      classes: (e) => da("ist-r", e)
    }
  ],
  [
    "truncate",
    {
      classes: "ist-r-truncate"
    }
  ],
  [
    "text_wrap",
    {
      classes: "ist-r-tw",
      handler: (e) => ha(e)
    }
  ]
]);
function ir(e) {
  const t = {}, n = [], r = {};
  for (const [o, i] of Object.entries(e)) {
    if (i === void 0 || !un.has(o))
      continue;
    const c = typeof i == "object" ? i : { initial: i };
    for (const [a, h] of Object.entries(c)) {
      const { classes: u, styleVar: l, handler: f, propHandler: d } = un.get(o), p = a === "initial";
      if (u) {
        const g = typeof u == "function" ? u(h) : u, y = p ? g : `${a}:${g}`;
        n.push(y);
      }
      if (f) {
        const g = f(h);
        if (l) {
          const y = p ? l : `${l}-${a}`;
          t[y] = g;
        } else {
          if (!Array.isArray(g))
            throw new Error(`Invalid style value: ${g}`);
          g.forEach((y) => {
            for (const [_, w] of Object.entries(y))
              t[_] = w;
          });
        }
      }
      if (d) {
        const g = d(h);
        for (const [y, _] of Object.entries(g))
          r[y] = _;
      }
    }
  }
  return {
    classes: n.join(" "),
    style: t,
    props: r
  };
}
function fa(e) {
  const t = Number(e);
  if (isNaN(t))
    throw new Error(`Invalid font size value: ${e}`);
  return [
    { "--fs": `var(--font-size-${t})` },
    { "--lh": `var(--line-height-${t})` },
    { "--ls": `var(--letter-spacing-${t})` }
  ];
}
function da(e, t) {
  return `${e}-lt-${t}`;
}
function ha(e) {
  if (e === "wrap")
    return {
      "--ws": "normal"
    };
  if (e === "nowrap")
    return {
      "--ws": "nowrap"
    };
  if (e === "pretty")
    return [{ "--ws": "normal" }, { "--tw": "pretty" }];
  if (e === "balance")
    return [{ "--ws": "normal" }, { "--tw": "balance" }];
  throw new Error(`Invalid text wrap value: ${e}`);
}
const pa = "insta-Heading", ma = Z(ga, {
  props: [
    "as",
    "as_child",
    "size",
    "weight",
    "align",
    "trim",
    "truncate",
    "text_wrap",
    "innerText"
  ]
});
function ga(e) {
  return () => {
    const { classes: t, style: n, props: r } = ir(e), s = de(
      { class: t, style: n, ...r },
      { class: pa }
    );
    return J(e.as || "h1", s, e.innerText);
  };
}
const ya = /* @__PURE__ */ Z({
  __name: "_Teleport",
  props: {
    to: {},
    defer: { type: Boolean, default: !0 },
    disabled: { type: Boolean, default: !1 }
  },
  setup(e) {
    return (t, n) => (fe(), yn(Vr, {
      to: t.to,
      defer: t.defer,
      disabled: t.disabled
    }, [
      Cr(t.$slots, "default")
    ], 8, ["to", "defer", "disabled"]));
  }
}), va = ["width", "height", "color"], wa = ["xlink:href"], _a = /* @__PURE__ */ Z({
  __name: "Icon",
  props: {
    size: {},
    icon: {},
    color: {},
    assetPath: {},
    svgName: {},
    rawSvg: {},
    appMode: {}
  },
  setup(e) {
    const t = e, { assetPath: n, svgName: r } = kt(t), { appMode: s } = t, o = me(() => t.icon ? t.icon.split(":")[1] : ""), i = me(() => t.size || "1em"), c = me(() => t.color || "currentColor"), a = me(() => t.rawSvg || null), h = s === "zero" ? j(() => `#${r}-${o.value}`) : j(() => `${n}/${r}#${o.value}`), u = Ar(), l = ia(a, {
      size: me(() => t.size),
      color: me(() => t.color),
      attrs: u
    });
    return (f, d) => (fe(), Ee(xr, null, [
      o.value ? (fe(), Ee("svg", de({
        key: 0,
        width: i.value,
        height: i.value,
        color: c.value
      }, H(u)), [
        gn("use", { "xlink:href": H(h) }, null, 8, wa)
      ], 16, va)) : ft("", !0),
      a.value ? (fe(), yn(H(l), { key: 1 })) : ft("", !0)
    ], 64));
  }
}), $e = /* @__PURE__ */ new Map([
  [
    "p",
    {
      classes: "ist-r-p",
      styleVar: "--p",
      handler: (e) => M("space", e)
    }
  ],
  [
    "px",
    {
      classes: "ist-r-px",
      styleVar: "--px",
      handler: (e) => M("space", e)
    }
  ],
  [
    "py",
    {
      classes: "ist-r-py",
      styleVar: "--py",
      handler: (e) => M("space", e)
    }
  ],
  [
    "pt",
    {
      classes: "ist-r-pt",
      styleVar: "--pt",
      handler: (e) => M("space", e)
    }
  ],
  [
    "pb",
    {
      classes: "ist-r-pb",
      styleVar: "--pb",
      handler: (e) => M("space", e)
    }
  ],
  [
    "pl",
    {
      classes: "ist-r-pl",
      styleVar: "--pl",
      handler: (e) => M("space", e)
    }
  ],
  [
    "pr",
    {
      classes: "ist-r-pr",
      styleVar: "--pr",
      handler: (e) => M("space", e)
    }
  ],
  [
    "width",
    {
      classes: "ist-r-w",
      styleVar: "--width",
      handler: (e) => e
    }
  ],
  [
    "height",
    {
      classes: "ist-r-h",
      styleVar: "--height",
      handler: (e) => e
    }
  ],
  [
    "min_width",
    {
      classes: "ist-r-min-w",
      styleVar: "--min_width",
      handler: (e) => e
    }
  ],
  [
    "min_height",
    {
      classes: "ist-r-min-h",
      styleVar: "--min_height",
      handler: (e) => e
    }
  ],
  [
    "max_width",
    {
      classes: "ist-r-max-w",
      styleVar: "--max_width",
      handler: (e) => e
    }
  ],
  [
    "max_height",
    {
      classes: "ist-r-max-h",
      styleVar: "--max_height",
      handler: (e) => e
    }
  ],
  [
    "position",
    {
      classes: "ist-r-position",
      styleVar: "--position",
      handler: (e) => e
    }
  ],
  [
    "inset",
    {
      classes: "ist-r-inset",
      styleVar: "--inset",
      handler: (e) => M("space", e)
    }
  ],
  [
    "top",
    {
      classes: "ist-r-top",
      styleVar: "--top",
      handler: (e) => M("space", e)
    }
  ],
  [
    "right",
    {
      classes: "ist-r-right",
      styleVar: "--right",
      handler: (e) => M("space", e)
    }
  ],
  [
    "bottom",
    {
      classes: "ist-r-bottom",
      styleVar: "--bottom",
      handler: (e) => M("space", e)
    }
  ],
  [
    "left",
    {
      classes: "ist-r-left",
      styleVar: "--left",
      handler: (e) => M("space", e)
    }
  ],
  [
    "overflow",
    {
      classes: "ist-r-overflow",
      styleVar: "--overflow",
      handler: (e) => e
    }
  ],
  [
    "overflow_x",
    {
      classes: "ist-r-ox",
      styleVar: "--overflow_x",
      handler: (e) => e
    }
  ],
  [
    "overflow_y",
    {
      classes: "ist-r-oy",
      styleVar: "--overflow_y",
      handler: (e) => e
    }
  ],
  [
    "flex_basis",
    {
      classes: "ist-r-fb",
      styleVar: "--flex_basis",
      handler: (e) => e
    }
  ],
  [
    "flex_shrink",
    {
      classes: "ist-r-fs",
      styleVar: "--flex_shrink",
      handler: (e) => e
    }
  ],
  [
    "flex_grow",
    {
      classes: "ist-r-fg",
      styleVar: "--flex_grow",
      handler: (e) => e
    }
  ],
  [
    "grid_area",
    {
      classes: "ist-r-ga",
      styleVar: "--grid_area",
      handler: (e) => e
    }
  ],
  [
    "grid_column",
    {
      classes: "ist-r-gc",
      styleVar: "--grid_column",
      handler: (e) => e
    }
  ],
  [
    "grid_column_start",
    {
      classes: "ist-r-gcs",
      styleVar: "--grid_column_start",
      handler: (e) => e
    }
  ],
  [
    "grid_column_end",
    {
      classes: "ist-r-gce",
      styleVar: "--grid_column_end",
      handler: (e) => e
    }
  ],
  [
    "grid_row",
    {
      classes: "ist-r-gr",
      styleVar: "--grid_row",
      handler: (e) => e
    }
  ],
  [
    "grid_row_start",
    {
      classes: "ist-r-grs",
      styleVar: "--grid_row_start",
      handler: (e) => e
    }
  ],
  [
    "grid_row_end",
    {
      classes: "ist-r-gre",
      styleVar: "--grid_row_end",
      handler: (e) => e
    }
  ],
  [
    "m",
    {
      classes: "ist-r-m",
      styleVar: "--m",
      handler: (e) => M("space", e)
    }
  ],
  [
    "mx",
    {
      classes: "ist-r-mx",
      styleVar: "--mx",
      handler: (e) => M("space", e)
    }
  ],
  [
    "my",
    {
      classes: "ist-r-my",
      styleVar: "--my",
      handler: (e) => M("space", e)
    }
  ],
  [
    "mt",
    {
      classes: "ist-r-mt",
      styleVar: "--mt",
      handler: (e) => M("space", e)
    }
  ],
  [
    "mr",
    {
      classes: "ist-r-mr",
      styleVar: "--mr",
      handler: (e) => M("space", e)
    }
  ],
  [
    "mb",
    {
      classes: "ist-r-mb",
      styleVar: "--mb",
      handler: (e) => M("space", e)
    }
  ],
  [
    "ml",
    {
      classes: "ist-r-ml",
      styleVar: "--ml",
      handler: (e) => M("space", e)
    }
  ],
  [
    "display",
    {
      classes: "ist-r-display",
      styleVar: "--display",
      handler: (e) => e
    }
  ],
  [
    "direction",
    {
      classes: "ist-r-fd",
      styleVar: "--direction",
      handler: (e) => e
    }
  ],
  [
    "align",
    {
      classes: "ist-r-ai",
      styleVar: "--align",
      handler: (e) => e
    }
  ],
  [
    "justify",
    {
      classes: "ist-r-jc",
      styleVar: "--justify",
      handler: (e) => e
    }
  ],
  [
    "wrap",
    {
      classes: "ist-r-wrap",
      styleVar: "--wrap",
      handler: (e) => e
    }
  ],
  [
    "gap",
    {
      classes: "ist-r-gap",
      styleVar: "--gap",
      handler: (e) => M("space", e)
    }
  ],
  [
    "gap_x",
    {
      classes: "ist-r-cg",
      styleVar: "--gap_x",
      handler: (e) => M("space", e)
    }
  ],
  [
    "gap_y",
    {
      classes: "ist-r-rg",
      styleVar: "--gap_y",
      handler: (e) => M("space", e)
    }
  ],
  [
    "areas",
    {
      classes: "ist-r-gta",
      styleVar: "--areas",
      handler: (e) => e
    }
  ],
  [
    "columns",
    {
      classes: "ist-r-gtc",
      styleVar: "--columns",
      handler: (e) => fn(e)
    }
  ],
  [
    "rows",
    {
      classes: "ist-r-gtr",
      styleVar: "--rows",
      handler: (e) => fn(e)
    }
  ],
  [
    "flow",
    {
      classes: "ist-r-gaf",
      styleVar: "--flow",
      handler: (e) => e
    }
  ],
  [
    "ctn_size",
    {
      classes: "ist-r-ctn_size",
      styleVar: "--ctn_size",
      handler: (e) => M("container", e)
    }
  ]
]);
function Ye(e) {
  e.length > 1 && console.warn("Only accept one child element when as_child is true");
}
function Xe(e) {
  return Object.fromEntries(
    Object.entries(e).filter(([t, n]) => n !== void 0)
  );
}
function Ze(e, t) {
  const n = {}, r = [], s = new Set(t || []), o = {
    style: {},
    class: []
  };
  for (const [c, a] of Object.entries(e)) {
    if (!$e.has(c))
      continue;
    const h = typeof a == "object" ? a : { initial: a };
    for (const [u, l] of Object.entries(h)) {
      const { classes: f, styleVar: d, handler: p } = $e.get(c), g = u === "initial", y = g ? f : `${u}:${f}`, _ = g ? d : `${d}-${u}`, w = p(l);
      if (s.has(c)) {
        o.class.push(y), o.style[_] = w;
        continue;
      }
      r.push(y), n[_] = w;
    }
  }
  return {
    classes: r.join(" "),
    style: n,
    excludeReslut: o
  };
}
function M(e, t) {
  const n = Number(t);
  if (isNaN(n))
    return t;
  {
    const r = n < 0 ? -1 : 1;
    return `calc(var(--${e}-${n}) * ${r})`;
  }
}
function fn(e) {
  const t = Number(e);
  return isNaN(t) ? e : `repeat(${t}, 1fr)`;
}
const et = [
  "p",
  "px",
  "py",
  "pt",
  "pb",
  "pl",
  "pr",
  "width",
  "height",
  "min_width",
  "min_height",
  "max_width",
  "max_height",
  "position",
  "inset",
  "top",
  "right",
  "bottom",
  "left",
  "overflow",
  "overflow_x",
  "overflow_y",
  "flex_basis",
  "flex_shrink",
  "flex_grow",
  "grid_area",
  "grid_column",
  "grid_column_start",
  "grid_column_end",
  "grid_row",
  "grid_row_start",
  "grid_row_end",
  "m",
  "mx",
  "my",
  "mt",
  "mr",
  "mb",
  "ml"
], Ea = [
  "as",
  "as_child",
  "display",
  "align",
  "justify",
  "wrap",
  "gap",
  "gap_x",
  "gap_y"
].concat(et), ba = ["direction"].concat(Ea), Sa = [
  "as_child",
  "size",
  "display",
  "align",
  "ctn_size"
].concat(et), ka = ["as", "as_child", "display"].concat(et), Ra = [
  "as",
  "as_child",
  "display",
  "areas",
  "columns",
  "rows",
  "flow",
  "align",
  "justify",
  "gap",
  "gap_x",
  "gap_y"
].concat(et), Oa = "insta-Box", Na = Z(Pa, {
  props: ka
});
function Pa(e) {
  const t = Ke();
  return () => {
    var c;
    const n = Xe(e), { classes: r, style: s } = Ze(n), o = de(
      { class: r, style: s },
      { class: Oa }
    ), i = (c = t.default) == null ? void 0 : c.call(t);
    return e.as_child && i && i.length > 0 ? (Ye(i), re(i[0], o)) : J(e.as || "div", o, i);
  };
}
const Va = "insta-Flex", Ca = {
  gap: "2"
}, Aa = Z(xa, {
  props: ba
});
function xa(e) {
  const t = Ke();
  return () => {
    var c;
    const n = { ...Ca, ...Xe(e) }, { classes: r, style: s } = Ze(n), o = de(
      { class: r, style: s },
      { class: Va }
    ), i = (c = t.default) == null ? void 0 : c.call(t);
    return e.as_child && i && i.length > 0 ? (Ye(i), re(i[0], o)) : J(e.as || "div", o, i);
  };
}
const $a = "insta-Grid", Ta = {
  gap: "2"
}, Ia = Z(Da, {
  props: Ra
});
function Da(e) {
  const t = Ke();
  return () => {
    var a;
    const n = { ...Ta, ...Xe(e) }, r = Ze(n), [s, o] = Ma(r.classes, r.style), i = de(
      { class: s, style: o },
      { class: $a }
    ), c = (a = t.default) == null ? void 0 : a.call(t);
    return e.as_child && c && c.length > 0 ? (Ye(c), re(c[0], i)) : J(e.as || "div", i, c);
  };
}
function Ma(e, t) {
  const n = $e.get("areas").styleVar, r = $e.get("columns").styleVar, s = n in t, o = r in t;
  if (!s || o)
    return [e, t];
  const i = ja(t[n]);
  if (i) {
    const { classes: c, styleVar: a } = $e.get("columns");
    e = `${e} ${c}`, t[a] = i;
  }
  return [e, t];
}
function ja(e) {
  if (typeof e != "string") return null;
  const t = [...e.matchAll(/"([^"]+)"/g)].map((i) => i[1]);
  if (t.length === 0) return null;
  const s = t[0].trim().split(/\s+/).length;
  return t.every(
    (i) => i.trim().split(/\s+/).length === s
  ) ? `repeat(${s}, 1fr)` : null;
}
const Ba = "insta-Container", La = Z(Fa, {
  props: Sa
});
function Fa(e) {
  const t = Ke();
  return () => {
    var h;
    const n = Xe(e), { classes: r, style: s, excludeReslut: o } = Ze(n, [
      "ctn_size"
    ]), i = de(
      { class: r, style: s },
      { class: Ba }
    ), c = (h = t.default) == null ? void 0 : h.call(t);
    if (e.as_child && c && c.length > 0)
      return Ye(c), re(c[0], i);
    const a = J(
      "div",
      de({ class: "insta-ContainerInner" }, o),
      c
    );
    return J("div", i, a);
  };
}
const Wa = "insta-Text", Ua = Z(za, {
  props: [
    "as",
    "as_child",
    "size",
    "weight",
    "align",
    "trim",
    "truncate",
    "text_wrap",
    "innerText"
  ]
});
function za(e) {
  return () => {
    const { classes: t, style: n, props: r } = ir(e), s = de(
      { class: t, style: n, ...r },
      { class: Wa }
    );
    return J(e.as || "span", s, e.innerText);
  };
}
function Ha(e, t) {
  const { mode: n = "hash" } = t.router, r = n === "hash" ? Jo() : n === "memory" ? qo() : Gn();
  e.use(
    Bi({
      history: r,
      routes: Ka(t)
    })
  );
}
function Ka(e) {
  if (!e.router)
    throw new Error("Router config is not provided.");
  const { routes: t = [], kAlive: n = !1 } = e.router;
  return t.map(
    (s) => ar(s, n)
  );
}
function ar(e, t) {
  const {
    server: n = !1,
    vueItem: r,
    scope: s,
    children: o
  } = e, i = () => {
    if (n)
      throw new Error("Server-side rendering is not supported yet.");
    return Promise.resolve(Ga(e, t));
  }, c = o == null ? void 0 : o.map(
    (h) => ar(h, t)
  ), a = {
    ...r,
    children: c,
    component: i
  };
  return s || delete a.component, c || delete a.children, a;
}
function Ga(e, t) {
  const { scope: n } = e;
  if (!n)
    throw new Error("Scope is not provided.");
  const r = re(Te(n), { key: n.id });
  return t ? J($r, null, () => r) : r;
}
function Ya(e, t) {
  e.component("insta-ui", ua), e.component("teleport", ya), e.component("icon", _a), e.component("heading", ma), e.component("box", Na), e.component("flex", Aa), e.component("grid", Ia), e.component("container", La), e.component("ui-text", Ua), t.router && Ha(e, t);
}
export {
  Ue as convertDynamicProperties,
  Ya as install,
  Qa as useBindingGetter
};
