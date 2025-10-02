import { defineComponent as d, useAttrs as S, useSlots as v, createBlock as g, openBlock as _, mergeProps as y, unref as l, createSlots as D, renderList as p, withCtx as h, renderSlot as x, normalizeProps as A, guardReactiveProps as $, computed as f, ref as T, watch as I, createTextVNode as K, toDisplayString as N, resolveDynamicComponent as j } from "vue";
import * as C from "tdesign-vue-next";
function B(e) {
  const { container: t = ".insta-main" } = e;
  return t;
}
const R = /* @__PURE__ */ d({
  inheritAttrs: !1,
  __name: "Affix",
  setup(e) {
    const t = S(), r = v(), n = B(t);
    return (o, s) => (_(), g(C.Affix, y(l(t), { container: l(n) }), D({ _: 2 }, [
      p(l(r), (c, u) => ({
        name: u,
        fn: h((i) => [
          x(o.$slots, u, A($(i)))
        ])
      }))
    ]), 1040, ["container"]));
  }
}), L = {
  hover: !0,
  bordered: !0,
  tableLayout: "auto",
  showSortColumnBgColor: !0
};
function O(e) {
  return f(() => {
    const { pagination: t, data: r = [] } = e;
    let n;
    if (typeof t == "boolean") {
      if (!t)
        return;
      n = {
        defaultPageSize: 10
      };
    }
    return typeof t == "number" && t > 0 && (n = {
      defaultPageSize: t
    }), typeof t == "object" && t !== null && (n = t), {
      defaultCurrent: 1,
      total: r.length,
      ...n
    };
  });
}
function W(e) {
  let t = T(e.sort);
  const r = T([...e.data ?? []]);
  I(
    () => e.data,
    (a) => {
      r.value = [...a];
    }
  );
  const n = f(() => !e.columns && r.value.length > 0 ? H(r.value) : e.columns ?? []), {
    onSortChange: o,
    onDataChange: s,
    columns: c,
    multipleSort: u
  } = q({
    sort: t,
    tableData: r,
    columns: n
  }), i = f(() => ({
    ...L,
    ...e
  }));
  return {
    sort: t,
    tableData: r,
    onSortChange: o,
    onDataChange: s,
    columns: c,
    multipleSort: u,
    bindAttrs: i
  };
}
function H(e) {
  const t = e[0];
  return Object.keys(t).map((n) => ({
    colKey: n,
    title: n,
    sorter: !0
  }));
}
function V(e) {
  const t = e.colKey;
  return (r, n) => {
    const o = r[t], s = n[t];
    return o == null && s == null ? 0 : o == null ? 1 : s == null ? -1 : typeof o == "number" && typeof s == "number" ? o - s : o instanceof Date && s instanceof Date ? o.getTime() - s.getTime() : typeof o == "string" && typeof s == "string" ? o.localeCompare(s, void 0, { numeric: !0 }) : String(o).localeCompare(String(s), void 0, { numeric: !0 });
  };
}
function q(e) {
  const { tableData: t, sort: r, columns: n } = e, o = f(() => n.value.map((a) => (a = E(a), a.sorter === !0 ? {
    ...a,
    sorter: V(a)
  } : a))), s = f(
    () => o.value?.some((a) => a.sorter)
  ), c = f(
    () => o.value.filter((a) => a.sorter).length > 1
  );
  return {
    onSortChange: (a, m) => {
      s.value && (r.value = a, t.value = [...m.currentDataSource ?? []]);
    },
    onDataChange: (a) => {
      t.value = a;
    },
    columns: o,
    multipleSort: c
  };
}
function E(e) {
  const t = e.name ?? e.colKey, r = `header-cell-${t}`, n = `body-cell-${t}`, o = e.label ?? e.colKey;
  return {
    ...e,
    name: t,
    label: o,
    title: r,
    cell: n
  };
}
function F(e, t) {
  return f(() => {
    const r = Object.keys(e).filter(
      (n) => n.startsWith("header-cell-")
    );
    return t.value.filter((n) => !r.includes(n.title)).map((n) => ({
      slotName: `header-cell-${n.name}`,
      content: n.label ?? n.colKey
    }));
  });
}
const G = /* @__PURE__ */ d({
  inheritAttrs: !1,
  __name: "Table",
  setup(e) {
    const t = S(), r = O(t), {
      sort: n,
      onSortChange: o,
      onDataChange: s,
      columns: c,
      multipleSort: u,
      tableData: i,
      bindAttrs: a
    } = W(t), m = v(), w = F(m, c);
    return (z, X) => (_(), g(C.Table, y(l(a), {
      pagination: l(r),
      sort: l(n),
      data: l(i),
      columns: l(c),
      onSortChange: l(o),
      onDataChange: l(s),
      "multiple-sort": l(u)
    }), D({ _: 2 }, [
      p(l(w), (b) => ({
        name: b.slotName,
        fn: h(() => [
          K(N(b.content), 1)
        ])
      })),
      p(l(m), (b, P) => ({
        name: P,
        fn: h((k) => [
          x(z.$slots, P, A($(k)))
        ])
      }))
    ]), 1040, ["pagination", "sort", "data", "columns", "onSortChange", "onDataChange", "multiple-sort"]));
  }
});
function J(e) {
  const { affixProps: t = {} } = e;
  return {
    container: ".insta-main",
    ...t
  };
}
function M(e) {
  const { container: t = ".insta-main" } = e;
  return t;
}
const Q = /* @__PURE__ */ d({
  inheritAttrs: !1,
  __name: "Anchor",
  setup(e) {
    const t = S(), r = v(), n = J(t), o = M(t);
    return (s, c) => (_(), g(C.Anchor, y(l(t), {
      container: l(o),
      "affix-props": l(n)
    }), D({ _: 2 }, [
      p(l(r), (u, i) => ({
        name: i,
        fn: h((a) => [
          x(s.$slots, i, A($(a)))
        ])
      }))
    ]), 1040, ["container", "affix-props"]));
  }
}), U = /* @__PURE__ */ d({
  __name: "Icon",
  props: {
    name: {},
    size: {},
    color: {},
    prefix: {}
  },
  setup(e) {
    const t = e, r = f(() => {
      const [n, o] = t.name.split(":");
      return o ? t.name : `${t.prefix || "tdesign"}:${t.name}`;
    });
    return (n, o) => (_(), g(j("icon"), {
      class: "t-icon",
      icon: r.value,
      size: n.size,
      color: n.color
    }, null, 8, ["icon", "size", "color"]));
  }
});
function Z(e) {
  e.use(C), e.component("t-table", G), e.component("t-affix", R), e.component("t-anchor", Q), e.component("t-icon", U);
}
export {
  Z as install
};
